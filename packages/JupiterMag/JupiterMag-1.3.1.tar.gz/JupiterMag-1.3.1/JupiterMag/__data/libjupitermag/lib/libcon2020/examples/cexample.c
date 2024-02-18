#include <stdio.h>
#include <stdbool.h>
#include <con2020.h>

int main() {

    /* we can obtain a single field vector like this,
     * using the default model parameters */
    double x = 10.0;
    double y = 20.0;
    double z = 5.0;
    double Bx, By, Bz;
    Con2020Field(x,y,z,&Bx,&By,&Bz);
    printf("B=[%5.1f,%5.1f,%5.1f] nT at [%4.1f,%4.1f,%4.1f] Rj\n",Bx,By,Bz,x,y,z);

    /* or using arrays */
    double xa[] = {10.0,20.0,30.0};
    double ya[] = {5.0,10.0,15.0};
    double za[] = {10.0,10.0,10.0};
    double Bxa[3], Bya[3], Bza[3];
    Con2020FieldArray(3,xa,ya,za,Bxa,Bya,Bza);
    int i;
    for (i=0;i<3;i++) {
        printf("B=[%5.1f,%5.1f,%5.1f] nT at [%4.1f,%4.1f,%4.1f] Rj\n",
                    Bxa[i],Bya[i],Bza[i],xa[i],ya[i],za[i]);
    }

    /* we can retrieve the current model parameters */
    double mui, irho, r0, r1, d, xt, xp, DeltaRho, DeltaZ, g, wO_open,
            wO_om, thetamm, dthetamm, thetaoc, dthetaoc;
    bool Edwards, ErrChk, CartIn, CartOut, smooth;
    char eqtype[16];
    char azfunc[16];
    GetCon2020Params(&mui,&irho,&r0,&r1,&d,&xt,&xp,eqtype,&Edwards,&ErrChk,
                    &CartIn,&CartOut,&smooth,&DeltaRho,&DeltaZ,&g,azfunc,
                    &wO_open,&wO_om,&thetamm,&dthetamm,&thetaoc,&dthetaoc);

    /* these parameters may be edited and passed aback to the model */
    irho = 0.0;
    strcpy(eqtype,"analytic");
    SetCon2020Params(mui,irho,r0,r1,d,xt,xp,eqtype,Edwards,ErrChk,
                    CartIn,CartOut,smooth,DeltaRho,DeltaZ,g,azfunc,
                    wO_open,wO_om,thetamm,dthetamm,thetaoc,dthetaoc);


}