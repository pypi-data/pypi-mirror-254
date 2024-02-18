g++ -lm -fPIC -std=c++17 -Wextra -O3 trimstring.cc generateheader.cc -o generateheader.exe
call generateheader.exe
del /F /Q generateheader.exe

call compileobj.bat

mkdir ..\lib
g++ -lm -fPIC -std=c++17 -Wextra -O3 ..\build\*.o -shared -o ..\lib\libcon2020.dll
