g++ -lm -fPIC -std=c++17 -Wextra -O3 trimstring.cc generateheader.cc -o generateheader.exe
call generateheader.exe
del /F /Q generateheader.exe

call compileobj.bat

mkdir ..\lib\libspline
g++ -lm -fPIC -std=c++17 -Wextra -O3 -shared -o ..\lib\libspline.dll ..\build\*.o

