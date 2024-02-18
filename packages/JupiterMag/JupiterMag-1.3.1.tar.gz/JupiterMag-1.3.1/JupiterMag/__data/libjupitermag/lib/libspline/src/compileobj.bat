mkdir ..\build
g++ -c -lm -fPIC -std=c++17 -Wextra -O3 spline.cc -o ..\build\spline.o
g++ -c -lm -fPIC -std=c++17 -Wextra -O3 libspline.cc -o ..\build\libspline.o
	
