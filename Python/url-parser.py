'''
Parse a html page, extract the Urls in it.

Example: input
<html>
  <body>
    <div>
      <a  HREF =    "http://www.google.com" class="text-lg">Google</a>
      <a  HREF = "www.facebook.com" style="display:none">Facebook</a>
      <a href >www.baidu.com</a>
    </div>
    <div>
      <a href="https://www.linkedin.com">Linkedin</a>
      <a href = "http://github.io">LintCode</a>
    </div>
  </body>
</html>

Output
["http://github.io","http://www.google.com","https://www.linkedin.com","www.facebook.com"]
'''

class HtmlParser:
    # @param {string} content source code
    # @return {string[]} a list of links
    def parseUrls(self, content):
        import re
        # The pattern has one group, so return result is what in the group, not what is matched.
        # The pattern is: space, case-insensitive href, space, =, space, quote, anything until one from "'>\s (complement).
        ans = re.findall(r"\s*(?i)href\s*=\s*['|\"]([^'\">\s]*)", content)
        return [a for a in ans if len(a) and not a.startswith('#')]