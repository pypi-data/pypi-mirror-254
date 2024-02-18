@echo "Testing con2020 installation"
cd test
g++ testc_installed.cc -o testc_installed.exe -lcon2020
copy ..\lib\libcon2020\libcon2020.dll .
.\testc_installed.exe
del testc_installed.exe
del libcon2020.dll
cd ..