
// hacker rank matrix[2n][2n] => top [n][n] max by reverse row or col ;-)

void reverse_hline(int R, int C, int **mat, int r)
{
    for(int i = 0; i<C/2;i++) {
        int t = mat[r][i];
        mat[r][i] = mat[r][C-1-i];
        mat[r][C-1-i] = t;
    }
}

void reverse_vline(int R, int C, int **mat, int c)
{
    for(int j = 0; j<R/2;j++) {
        int t = mat[j][c];
        mat[j][c] = mat[R-1-j][c];
        mat[R-1-j][c] = t;
    }
}

// Check [r][c] vs other 3.
int max4(int a, int b, int c, int d)
{
    int m1 = 0;
    if (a>b) m1 = a;
    else m1 = b;

    int m2 = 0;
    if (c>d) m2 = c;
    else m2 = d;

    if (m1>m2) return m1;
    else return m2;
}

void check_one(int R, int C, int **mat, int r, int c)
{
    int v00 = mat[r][c], v01 = mat[r][C-1-c];
    int v10 = mat[R-1-r][c], v11 = mat[R-1-r][C-1-c];
    int vmax = max4(v00, v01, v10, v11);

    if (vmax==v00) {
        // do nothing
    }
    else if (vmax==v01) {
        // flip h
        reverse_hline(R, C, mat, r);
    }
    else if (vmax==v10) {
        // flip v
        reverse_vline(R, C, mat, c);
    }
    else {
        // flip both h and v
        reverse_hline(R, C, mat, r);
        reverse_vline(R, C, mat, c);
    }
}

void check_all(int R, int C, int **mat)
{
    for(int j = 0; j<R/2;j++) for(int i = 0; i<C/2;i++) check_one(R, C, mat, j, i);
}

int sum_nxn(int R, int C, int **mat)
{
    int sum = 0;
    for(int j = 0; j<R/2;j++) for(int i = 0; i<C/2;i++) sum += mat[j][i];
    return sum;
}
