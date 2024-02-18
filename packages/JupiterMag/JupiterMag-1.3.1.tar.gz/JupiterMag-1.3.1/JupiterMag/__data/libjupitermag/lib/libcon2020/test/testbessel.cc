#include "testbessel.h"

double mean(int n, double *x) {

    double out = 0.0;
    int i;
    for (i=0;i<n;i++) {
        out += x[i];
    }
    return out/n;
}

double stdev(int n, double *x, double mu) {

    double out = 0.0;
    int i;
    for (i=0;i<n;i++) {
        out += pow(x[i]-mu,2.0);
    }
    return sqrt(out)/(n-1);
}

int main() {

    /* create a couple of arrays */
    int n = 100000;
    double dx = 5.0/n;
    double *x0 = new double[n];
    double *x1 = new double[n];
    double *j = new double[n];

    int i;
    srand(time(NULL)); 
    for (i=0;i<n;i++) {
        x0[i] = 5.0*((double) rand())/((double) RAND_MAX);
        x1[i] = 5.0 + 5.0*((double) rand())/((double) RAND_MAX);
    }

    /* time each section */
    
    double t0, t1, dt[5];
    double mu, std;

    for (i=0;i<5;i++) {
        t0 = clock();
        j0(n,x0,j);
        t1 = clock();
        dt[i] = (t1 - t0)/CLOCKS_PER_SEC;
    }
    mu = mean(5,dt);
    std = stdev(5,dt,mu);

    printf("j0 (0-5): %f +/- %f\n",mu,std);

    for (i=0;i<5;i++) {
        t0 = clock();
        j0(n,x1,j);
        t1 = clock();
        dt[i] = (t1 - t0)/CLOCKS_PER_SEC;
    }
    mu = mean(5,dt);
    std = stdev(5,dt,mu);

    printf("j0 (5-10): %f +/- %f\n",mu,std);

    for (i=0;i<5;i++) {
        t0 = clock();
        j1(n,x0,j);
        t1 = clock();
        dt[i] = (t1 - t0)/CLOCKS_PER_SEC;
    }
    mu = mean(5,dt);
    std = stdev(5,dt,mu);

    printf("j1 (0-5): %f +/- %f\n",mu,std);

    for (i=0;i<5;i++) {
        t0 = clock();
        j1(n,x1,j);
        t1 = clock();
        dt[i] = (t1 - t0)/CLOCKS_PER_SEC;
    }
    mu = mean(5,dt);
    std = stdev(5,dt,mu);

    printf("j1 (5-10): %f +/- %f\n",mu,std);


    delete [] x0;
    delete [] x1;
    delete [] j;

}
