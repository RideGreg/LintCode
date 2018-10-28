class Solution {
    double w_0_r_1(int w, int r) {
        double W = (double)w, R = (double)r;
        return (R / (W + R)) * (R / (W + R));
    }
    double w_1_r_0(int w, int r) {
        double W = (double)w, R = (double)r;
        return (R / (W + R)) * (W / (W + R));
    }
    double w_1_r_1(int w, int r) {
        double W = (double)w, R = (double)r;
        return (W / (W + R)) * (R / (W + R - 1));
    }
    double w_2_r_0(int w, int r) {
        double W = (double)w, R = (double)r;
        return (W / (W + R)) * ((W - 1) / (W + R - 1));
    }

    void output(vector<vector<double>> &p) {
        for(int i = 0; i < p.size(); i++) {
            for(int j = 0; j < p[i].size(); j++) 
                cout<<p[i][j]<<" ";
            cout<<endl;
        }
    }
public:
    double eatTheBeans(int w, int r) {
        if(w == 0) return 0;
        if(r == 0) return 1;

        vector<vector<double>> p(w + 1, vector<double>(r + 1, 0));
        p[w][r] = 1;

        for(int i = w; i >= 0; i--) {
            for(int j = r; j >= 0; j--) {
                if(j - 1 >= 0) {
                    p[i][j - 1] += w_0_r_1(i, j) * p[i][j];
                }
                if(i - 1 >= 0) {
                    p[i - 1][j] += w_1_r_0(i, j) * p[i][j];
                }
                if(i - 2 >= 0) {
                    p[i - 2][j] += w_2_r_0(i, j) * p[i][j];
                }
                if(i - 1>= 0 && j - 1 >= 0) {
                    p[i - 1][j - 1] += w_1_r_1(i, j) * p[i][j];
                }
            }
        }
        output(p);
        double res = 0;
        for(int i = 1; i <= w; i++) {
            if(i > 2) break;
            res += p[i][0];
        }
        return res;
    }
};
