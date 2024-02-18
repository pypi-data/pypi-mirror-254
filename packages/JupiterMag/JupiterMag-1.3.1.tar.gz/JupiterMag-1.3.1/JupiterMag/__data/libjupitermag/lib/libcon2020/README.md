# libcon2020

C++ implementation of the Connerney et al., 1981 and Connerney et al., 2020 Jovian magnetodisc model. This model provides the magnetic field due to a "washer-shaped" current disc near to Jupiter's magnetic equator. The model uses the analytical equations from Edwards et al., 2001 or Connerney et al., 1981; or the numerical integration of the Connerney et al., 1981 equations to provide the magnetic field vectors due to the azimuthal current. This code also implements the Connerney et al., 2020 radial current and the Leicester magnetosphere-ionosphere coupling (L-MIC, Cowley et al., 2005, 2008) models which provide the azimuthal component of the mangetic field.

This is part of [libjupitermag](https://github.com/mattkjames7/libjupitermag.git), which is part of a greater effort to provide community code for the Jovian magnetosphere:

[Magnetospheres of the Outer Planets Group Community Code](https://lasp.colorado.edu/home/mop/missions/juno/community-code/)

## Building libcon2020

To build this library in Linux or Mac OS:

```bash
#clone this repo
git clone https://github.com/mattkjames7/libcon2020.git
cd libcon2020

#build
make 

#optionally install it system wide
sudo make install
```

In Windows:

```powershell
git clone https://github.com/mattkjames7/libcon2020.git
cd libcon2020

.\compile.bat
```

With a system wide installation, the compiler and linker will be able to locate the library and its header, otherwise absolute paths must be provided for linking and including. In Windows there is an experimental script ```install.bat``` which will copy the DLL and headers to folders within the `C:\TDM-GCC-64\` directory. This is experimental, instead it might be better to copy the headers and the DLL to the root directory of the executable linked to it.

Uninstallation can be acheived in Linux and Mac using ```sudo make uninstall```.

## Usage

### Linking to and Including libcon2020

If a system-wide installation is successful then the library may be linked to simply by including the ```-lcon2020``` flag while compiling/linking. Otherwise the path to the library must also be included, e.g. ```-L /path/to/lib/directory -lcon2020```. In Windows, the DLL should be placed in the root directory of the executable linked to it.

This library includes a header file `include/con2020.h` which is compatible with both C and C++. This header contains the full set of function and class prototypes for use with C++, it also includes C-compaitble wrapper functions. The wrapper functions in the header file would also provide the easiest ways to link other languages to the library such as Python, IDL and Fortran.

If the library was installed system-wide, then the headers may be included using ```#include <con2020.h>```. Otherwise, a relative or absolute path to the headers must be used, e.g. ```#include "path/to/con2020.h"```.

### C++ usage

This section briefly describes some C++ specific examples for using the `libcon2020` library, while the following section is also somewhat applicable.

Access the model using the `Con2020` class:

```cpp
/* contents of cppexample.cc */
#include <stdio.h>
#include <con2020.h>

int main () {
	/* create an instance of the model */
	Con2020 model;

	/* set coordinate system to be Cartesian SIII (default) */
	model.SetCartIn(true);
	model.SetCartOut(true);

	/* create some variables to stor a field vector in,
	 * note that positions are in units of Rj */
	double x = 11.0;
	double y = 5.0;
	double z = -10.0;
	double Bx, By, Bz;

	/* call the model */
	model.Field(x,y,z,&Bx,&By,&Bz);
	printf("B=[%5.1f,%5.1f,%5.1f] nT at [%4.1f,%4.1f,%4.1f] Rj\n",Bx,By,Bz,x,y,z);

	/* alternatively obtain an array of field vectors in spherical polar coords */
	model.SetCartIn(false);
	model.SetCartOut(false);
	double r[] = {5.0,10.0,15.0};
	double theta[] = {1.0,1.5,2.0};
	double phi[] = {0.0,0.1,0.2};
	double Br[3], Bt[3], Bp[3];

	model.Field(3,r,theta,phi,Br,Bt,Bp);
	int i;
	for (i=0;i<3;i++) {
		printf("B=[%5.1f,%5.1f,%5.1f] nT at r = %4.1f Rj, theta = %4.1f rad, phi = %4.1f rad\n",Br[i],Bt[i],Bp[i],r[i],theta[i],phi[i]);
	}
	
	return 0;
}
```

In the example above, the model can be configured by using class member functions (e.g. `Con2020::SetCartIn()`), see the table below for a full list of configurable parameters. The `Con2020::Field()` function is overloaded, so can either accept a single input position in order to provide a single field vector, or can accept an array of positions in order to provide an array of field vectors. Compile and run the above example using

```bash
g++ cppexample.cc -o cppexample -lcon2020
./cppexample
```



### Other Languages

In other languages, it is easier to run the model code by using the wrapper functions listed in both `con2020.h`. For example in C:

```c
/* contents of cexample.c */
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
```

Compile and run using:

```bash
gcc cexample.c -o cexample -lcon2020
./cexample
```

## Model Parameters

This table lists all of the configurable parameters currently included in the code.

| Parameter  | Default             | `Con2020` Member Functions                                   | Description                                                                                                                                                                                                                                          |
| ---------- | ------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mui`      | `139.6`             | `SetAzCurrentParameter()` <br /> `GetAzCurrentParameter()`   | Azimuthal current sheet parameter, nT.                                                                                                                                                                                                               |
| `irho`     | `16.7`              | `SetRadCurrentParameter()` <br /> `GetRadCurrentParameter()` | *Radial current intensity, MA                                                                                                                                                                                                                        |
| `r0`       | `7.8`               | `SetR0()` <br /> `GetR0()`                                   | Inner edge of the current sheet, R<sub>J<sub/>.                                                                                                                                                                                                      |
| `r1`       | `51.4`              | `SetR1()` <br /> `GetR1()`                                   | Outer edge of the current sheet, R<sub>J<sub/>.                                                                                                                                                                                                      |
| `d`        | `3.6`               | `SetCSHalfThickness()` <br /> `GetSCHalfThickness()`         | Half thickness of the current sheet, R<sub>J<sub/>.                                                                                                                                                                                                  |
| `xt`       | `9.3`               | `SetCSTilt()` <br /> `GetCSTilt()`                           | Tilt angle of the current sheet away from the SIII $z$-axis, °.                                                                                                                                                                                      |
| `xp`       | `155.8`             | `SetCSTiltAzimuth()` <br /> `GetCSTiltAzimuth()`             | Right-handed longitude towards which the current sheet is tilted, °.                                                                                                                                                                                 |
| `eqtype`   | `"hybrid"`          | `SetEqType()` <br /> `GetEqType()`                           | Set what method to use: <br /> `"analytic"`- use analytic equations <br /> `"integral"` - use full integral equations <br /> `"hybrid"` - use a combination of both                                                                                  |
| `Edwards`  | `true`              | `SetEdwardsEqs()` <br /> `GetEdwardsEqs()`                   | Switch between the Edwards et al., 2001 and Connerney et al., 1981 analytical equations                                                                                                                                                              |
| `ErrChk`   | `true`              | `SetErrCheck()` <br /> `GetErrChk()`                         | Check for errors on the inputs to `Con2020::Field()`, set to `false` for and every so slightly risky speedup.                                                                                                                                        |
| `CartIn`   | `true`              | `SetCartIn()` <br /> `GetCartIn()`                           | If `true` then input coordinates will be assumed to be SIII Cartesian (in units of R<sub>J</sub>), otherwise spherical polar coordinates (_r_ in units of R<sub>J</sub>; $\theta$ and $\phi$ in radians).                                            |
| `CartOut`  | `true`              | `SetCartOut()` <br /> `GetCartOut()`                         | If `true` then output field vectors will be in Cartesian SIII coordinates, otherwise they will be oriented such that the three components are radial, meridional and azimuthal.                                                                      |
| `smooth`   | `true`              | `SetSmooth()` <br /> `GetSmooth()`                           | Use Stan's $\tanh$ based functions to smooth over the $r_0$ and $r_1$ boundaries in the $\rho$ direction and across $\pm d$ in the $z$ direction.                                                                                                    |
| `DeltaRho` | `1.0`               | `SetDeltaRho()` <br /> `GetDeltaRho()`                       | Scale length over which smoothing is done in the $\rho$ direction R<sub>J</sub>.                                                                                                                                                                     |
| `DeltaZ`   | `0.1`               | `SetDeltaZ()` <br /> `GetDeltaZ()`                           | Scale length over which smoothing is done in the $z$ direction.                                                                                                                                                                                      |
| `g`        | `417659.3836476442` | `SetG()` <br /> `GetG()`                                     | **Magnetic dipole parameter, nT                                                                                                                                                                                                                      |
| `azfunc`   | `"connerney"`       | `SetAzimuthalFunc()` <br /> `GetAzimuthalFunc()`             | Set the method to use to calculate the azimuthal field due to the radial component of the current: <br /> `"connerney"` - use the Connerney et al., 2020 azimuthal field model <br /> `"lmic"` - use the L-MIC model (Connerney et al., 2005, 2008). |
| `wO_open`  | `0.1`               | `SetOmegaOpen()` <br /> `GetOmegaOpen()`                     | **Ratio of plasma to Jupiter's angular velocity on open field lines.                                                                                                                                                                                 |
| `wO_om`    | `0.35`              | `SetOmegaOM()` <br /> `GetOmegaOM()`                         | **Ratio of plasma to Jupiter's angular velocity in the outer magnetosphere.                                                                                                                                                                          |
| `thetamm`  | `16.1`              | `SetThetaMM()` <br /> `GetThetaMM()`                         | **Colatitude of the centre of the middle magnetosphere, where the plasma transitions from corotating to sub-corotating, °.                                                                                                                           |
| `dthetamm` | `0.5`               | `SetdThetaMM()` <br /> `GetdThetaMM()`                       | **Colatitude range over which the transition from inner to outer magnetosphere occurs, °.                                                                                                                                                            |
| `thetaoc`  | `10.716`            | `SetThetaOC()` <br /> `GetThetaOC()`                         | **Colatitude of the centre of the open-closed field line boundary, °.                                                                                                                                                                                |
| `dthetaoc` | `0.125`             | `SetdThetaOC()` <br /> `GetdThetaOC())`                      | **Colatitude range of the open-closed field line boundary, °.                                                                                                                                                                                        |

\* Applicable to the Connerney et al., 2020 model of $B_{\phi}$.

** Applicable to L-MIC model for $B_{\phi}$.

## References

- Connerney, J. E. P., Timmins, S., Herceg, M., & Joergensen, J. L. (2020). A Jovian magnetodisc model for the Juno era. *Journal of Geophysical Research: Space Physics*, 125, e2020JA028138. https://doi.org/10.1029/2020JA028138
- Connerney, J. E. P., Acuña, M. H., and Ness, N. F. (1981), Modeling the Jovian current sheet and inner magnetosphere, *J. Geophys. Res.*, 86( A10), 8370– 8384, doi:[10.1029/JA086iA10p08370](https://doi.org/10.1029/JA086iA10p08370)
- Cowley, S. W. H., Alexeev, I. I., Belenkaya, E. S., Bunce, E. J., Cottis, C. E., Kalegaev, V. V., Nichols, J. D., Prangé, R., and Wilson, F. J. (2005), A simple axisymmetric model of magnetosphere-ionosphere coupling currents in Jupiter's polar ionosphere, *J. Geophys. Res.*, 110, A11209, doi:[10.1029/2005JA011237](https://doi.org/10.1029/2005JA011237 "Link to external resource: 10.1029/2005JA011237").
- Cowley, S. W. H., Deason, A. J., and Bunce, E. J.: Axi-symmetric models of auroral current systems in Jupiter's magnetosphere with predictions for the Juno mission, Ann. Geophys., 26, 4051–4074, https://doi.org/10.5194/angeo-26-4051-2008, 2008.
- Edwards T.M., Bunce E.J., Cowley S.W.H. (2001), A note on the vector potential of Connerney et al.'s model of the equatorial current sheet in Jupiter's magnetosphere, *Planetary and Space Science,*49, 1115-1123,[10.1016/S0032-0633(00)00164-1](https://doi.org/10.1016/S0032-0633(00)00164-1).
  
  


