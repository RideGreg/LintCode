#!/usr/bin/env python2.7
import argparse
import sys
import os
import os.path
import multiprocessing
import subprocess
from glob import glob
from functools import partial
import shutil
import time

if __name__ == '__main__' and sys.path[0]:
    sys.path.append(sys.path[0].rsplit('/', 1)[0])

from utils import ConfigLoader, TimeUtil, EmailUtil, OSUtil, MZTimer


def construct_aggregated_file_name(prefix, game, batch_id, job_id, start_ts):
    hour_part = TimeUtil.get_hr_str(start_ts)
    return '{hour_part}-{batch_id}-{job_id}.{prefix}.{game}.daily_snapshot.{start_ts}'.format(
        hour_part=hour_part,
        batch_id=batch_id,
        job_id=job_id,
        prefix=prefix,
        game=game,
        start_ts=int(start_ts))


def construct_daily_snapshot_temp_dir_path(archive_temp_dir, start_ts):
    hour_part = TimeUtil.get_hr_str(start_ts)
    return '{temp_dir_root}/{hour_part}.daily_snapshot_temp'.format(
        temp_dir_root=archive_temp_dir,
        hour_part=hour_part)


def construct_daily_snapshot_control_dir_path(archive_temp_dir, start_ts):
    hour_part = TimeUtil.get_hr_str(start_ts)
    return '{temp_dir_root}/{hour_part}.daily_snapshot_control'.format(
        temp_dir_root=archive_temp_dir,
        hour_part=hour_part)


def construct_success_log_file_name(job_id):
    return 'success.{}.log'.format(job_id)


def construct_cluster_temp_dir(archive_temp_dir, cluster):
    return '{archive_temp_dir}/{cluster}_temp/'.format(
        archive_temp_dir=archive_temp_dir,
        cluster=cluster)


def sort_and_compress(prefix, game='ody', batch_id=0, job_id=0, start_ts=0, sort_data=1, processing_dir=None, working_dir=None):
    file_pattern = '{}_*'.format(prefix)

    # files = glob(os.path.join(processing_dir, file_pattern))
    # if len(files) == 0:
    #     return True

    output_file_name = construct_aggregated_file_name(prefix, game, batch_id, job_id, start_ts)
    if sort_data == 1:
        cmd = 'cat {}/{} | sort > {}/{}'.format(processing_dir, file_pattern, working_dir, output_file_name)
    else:
        cmd = 'cat {}/{} > {}/{}'.format(processing_dir, file_pattern, working_dir, output_file_name)
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    error = ps.communicate()[1]

    # MMING
    if error is None:
        cmd = 'rm -rf {}/{}'.format(processing_dir, file_pattern)
        ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        error = ps.communicate()[1]

    if error is None and is_non_zero_file(os.path.join(working_dir, output_file_name)):
        cmd = 'gzip {}/{}'.format(working_dir, output_file_name)
        ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        error = ps.communicate()[1]

    return error is None


def send_files(file_path, temp_dir=None, host=None, user=None):
    exit_status = subprocess.call(['rsync', '-vte', 'ssh', file_path, '%s@%s:%s' % (user, host, temp_dir)])
    return exit_status


def clean_up_source_files(processing_dir):
    cmd = 'rm -rf {}/*'.format(processing_dir)
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    error = ps.communicate()[1]
    return error is None


def check_results(results):
    success = True
    for res in results:
        success = success and res
    return success


def exists_remote(host, user, path, file_type='f'):
    user_host = '{}@{}'.format(user, host)
    proc = subprocess.Popen(['ssh', user_host, 'test -%s %s' % (file_type, path)])
    proc.wait()
    return proc.returncode == 0


def dir_exists_remote(host, user, path):
    return exists_remote(host, user, path, 'd')


def file_exists_remote(host, user, path):
    return exists_remote(host, user, path)


def is_non_zero_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0


def is_zero_file(fpath):
    return not is_non_zero_file(fpath)


def get_date_from_compressed_file(file_name):
    fn = os.path.basename(file_name).split('.')[0]
    return '-'.join(fn.split('-')[:3])


def are_all_jobs_completed(host, user, daily_snapshot_control_dir, job_ids):
    all_completed = True
    for job_id in job_ids:
        success_log_file_name = construct_success_log_file_name(job_id)
        if not file_exists_remote(host, user, '{}/{}'.format(daily_snapshot_control_dir, success_log_file_name)):
            all_completed = False

    return all_completed


def main():
    # parsing the command line arguments
    parser = argparse.ArgumentParser(prog=sys.argv[0], add_help=True)
    parser.add_argument('-g', '--game', default='ody')
    parser.add_argument('-b', '--batch_id', default=0)
    parser.add_argument('-e', '--env', default='local')
    parser.add_argument('-a', '--async_sort_process', default=1) # MMING
    parser.add_argument('-p', '--async_push', default=0)
    parser.add_argument('-s', '--sort_data', default=0)
    parser.add_argument('-f', '--process_file', default=1)
    parser.add_argument('-t', '--process_time', default=0)
    parser.add_argument('-c', '--cleanup', default=1)
    parser.add_argument('-j', '--job_id', default=-1)
    parser.add_argument('-d', '--start_ts', default=0)

    # retrieve the arguments
    args = vars(parser.parse_args(sys.argv[1:]))
    game = args['game']
    batch_id = args['batch_id']
    env = args['env']
    async_sort_process = int(args['async_sort_process'])
    async_push = int(args['async_push'])
    sort_data = int(args['sort_data'])
    process_file = int(args['process_file'])
    process_time = int(args['process_time'])
    cleanup = int(args['cleanup'])
    job_id = int(args['job_id'])
    start_ts = int(args['start_ts'])

    # start the timer for the process
    timer = MZTimer(process_time)

    # get the config
    config = ConfigLoader(game, env, 'daily_snapshot').config

    message = "Dumped eco data from game: {}\n\n".format(time.strftime('%H:%M:%S', time.gmtime(process_time)))
    current_ts = TimeUtil.get_current_timestamp()
    if start_ts == 0:
        start_ts = current_ts
    current_time = TimeUtil.ts2str(current_ts)
    user = config['target']['user']
    processing_dir = config['source']['processing_dir']
    processed_dir = config['source']['processed_dir']
    working_dir = config['source']['working_dir']
    not_sent_dir = config['source']['not_sent_dir']
    archive_temp_dir = config['target']['archive_tmp_dir']
    target_archive_dir = config['target']['archive_dir']
    clusters = config['target']['clusters'].split(',')
    job_ids = config['target']['job_ids'].split(',')
    default_cluster = clusters[0]
    target_temp_dir = '{}/temp_{}'.format(archive_temp_dir, job_id)
    daily_snapshot_temp_dir = construct_daily_snapshot_temp_dir_path(archive_temp_dir, start_ts)
    daily_snapshot_control_dir = construct_daily_snapshot_control_dir_path(archive_temp_dir, start_ts)

    pool = multiprocessing.Pool()

    # sanity check
    if job_id < 0:
        clean_up_source_files(working_dir)
        subject = "Invalid job_id [{} UTC]".format(current_time)
        EmailUtil.send_email(config['email']['alert'], subject, message)
        sys.exit(0)

    # sort and compress the files
    if process_file == 1:
        print 'Sorting and compressing the files...'
        prefixes = config['source']['prefixes'].split(',')

        res = True
        if async_sort_process == 1:
            res = pool.map(partial(sort_and_compress, game=game, batch_id=batch_id, job_id=job_id, start_ts=start_ts, sort_data=sort_data, processing_dir=processing_dir, working_dir=working_dir), prefixes)
            res = check_results(res)
        else:
            for prefix in prefixes:
                res = sort_and_compress(prefix, game, batch_id, job_id, start_ts, sort_data, processing_dir, working_dir)

        if not res:
            clean_up_source_files(working_dir)
            subject = "Error in sorting and compressing [{} UTC]".format(current_time)
            EmailUtil.send_email(config['email']['alert'], subject, message)
            sys.exit(0)

        timer.stop()
        message += "Sorted and Compressed files: {}\n\n".format(timer.sub_process_time_str)

    # send compressed files to archive server's temp
    print 'Sending processed files to archive server...'
    timer.sub_start()

    files = glob(os.path.join(working_dir, '*.gz'))
    hosts = config['target']['hosts'].split(',')
    results = {}
    for host in hosts:
        # create target temp dir if it does not exist on the archive server
        subprocess.call(['ssh', '{}@{}'.format(user, host), 'mkdir', '-p', target_temp_dir])

        if async_push == 1:
            results[host] = pool.map(partial(send_files, temp_dir=target_temp_dir, host=host, user=user), files)
        else:
            results[host] = []
            for log_file in files:
                results[host].append(send_files(log_file, target_temp_dir, host, user))
    timer.stop()
    message += "Pushed files to archive servers: {}\n\n".format(timer.sub_process_time_str)

    # move the files to aggregated (if all exit status are 0) or not_sent (otherwise)
    timer.sub_start()
    failed = False
    for (n, log_file) in enumerate(files):
        exit_status = max([results[host][n] for host in results])
        if exit_status == 0:
            # successfully sent
            date = TimeUtil.get_date(current_ts)
            dest_dir = os.path.join(processed_dir, date)
            OSUtil.mkdir(dest_dir)
            shutil.move(log_file, dest_dir)
        else:
            # send failed; move working to not_sent directory
            failed = True
            failed_hosts = [host for host in results if results[host][n] != 0]
            for n, host in enumerate(failed_hosts):
                host_not_sent_dir = os.path.join(not_sent_dir, host)
                OSUtil.mkdir(host_not_sent_dir)
                if n == len(failed_hosts) - 1:
                    # move it
                    shutil.move(log_file, host_not_sent_dir)
                else:
                    # copy it
                    shutil.copy(log_file, host_not_sent_dir)

    if cleanup == 1:
        clean_up_source_files(processing_dir)

    if failed:
        subject = "[{}-ds] Error sending files to archive server. [{} UTC]".format(game, TimeUtil.get_current_time())
        EmailUtil.send_email(config['email']['alert'], subject, message)
        sys.exit(0)

    # move all the files to the remote archive dir
    print "Moving files to final temp direcoty on archive servers..."
    timer.sub_start()
    for host in hosts:
        user_host = '{}@{}'.format(user, host)
        # create temp and control dirs if they do not exist
        subprocess.call(['ssh', user_host, 'mkdir', '-p', daily_snapshot_temp_dir])
        subprocess.call(['ssh', user_host, 'mkdir', '-p', daily_snapshot_control_dir])

        src = os.path.join(target_temp_dir, '*')
        dest = daily_snapshot_temp_dir + '/'
        print 'ssh', user_host, 'mv', src, dest
        subprocess.call(['ssh', user_host, 'mv', src, dest])

        # mark single job success
        success_log_file_path = '{}/{}'.format(
            daily_snapshot_control_dir,
            construct_success_log_file_name(job_id))
        print(success_log_file_path)
        subprocess.call(['ssh', user_host, 'echo ' + str(TimeUtil.get_current_timestamp()) + ' > ' + success_log_file_path])

    timer.stop()
    message += "Moved files to final temp dir: {}\n\n".format(timer.sub_process_time_str)

    # move the log files from the final temp to final destinations
    last_job = False
    for host in hosts:
        if are_all_jobs_completed(host, user, daily_snapshot_control_dir, job_ids):
            last_job = True
            timer.sub_start()
            # move files from the final temp to default cluster
            src = os.path.join(daily_snapshot_temp_dir, '*')
            default_cluster_temp_dir = construct_cluster_temp_dir(archive_temp_dir, default_cluster)
            subprocess.call(['ssh', '{}@{}'.format(user, host), 'mkdir', '-p', default_cluster_temp_dir])
            print 'ssh', user_host, 'mv', src, default_cluster_temp_dir
            subprocess.call(['ssh', user_host, 'mv', src, default_cluster_temp_dir])

            # copy files from the default cluster temp to other cluster temps
            for cluster in clusters:
                if cluster != default_cluster:
                    cluster_temp_dir = construct_cluster_temp_dir(archive_temp_dir, cluster)
                    subprocess.call(['ssh', '{}@{}'.format(user, host), 'mkdir', '-p', cluster_temp_dir])

                    # copy files from first temp directory to others
                    src = os.path.join(default_cluster_temp_dir, '*')
                    print 'ssh', user_host, 'cp', src, cluster_temp_dir
                    subprocess.call(['ssh', user_host, 'cp', src, cluster_temp_dir])

            # move files from each cluster temp to the cluster final destination
            for cluster in clusters:
                cluster_target_temp_dir = construct_cluster_temp_dir(archive_temp_dir, cluster)
                src = os.path.join(cluster_target_temp_dir, '*')
                cluster_target_archive_dir = target_archive_dir.format(cluster=cluster)
                dest = cluster_target_archive_dir + '/'
                print 'ssh', user_host, 'mv', src, dest
                subprocess.call(['ssh', user_host, 'mv', src, dest])

            # clean up the success log
            subprocess.call(['ssh', user_host, 'rm -rf {}/*'.format(daily_snapshot_control_dir)])
            timer.stop()
            message += "Moved files to final destinations on {}: {}\n\n".format(host, timer.sub_process_time_str)

    message += "The whole process ran in {}.\n\n".format(timer.process_time_str)

    # send email out
    subject = "[{}] Successfully Sending Daily Snapshot Data. Job ID: {} [{} UTC]".format(game, job_id, TimeUtil.get_current_time())
    if last_job:
        recipients = config['email']['success']
    else:
        recipients = config['email']['sub_success']
    EmailUtil.send_email(recipients, subject, message)
    sys.exit(0)

if __name__ == '__main__':
    main()