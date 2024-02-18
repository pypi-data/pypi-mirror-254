# CFLAGS for CC
CFLAGS=-lm -std=c++17 -Wextra -O3

# Compiler
CCo=g++ -fPIC -c $(CFLAGS)
CC=g++ -fPIC $(CFLAGS)
CCc=gcc -fPIC -ldl -lm -Wextra -O3
CCWo=x86_64-w64-mingw32-g++-win32 -c $(CFLAGS)
CCW=x86_64-w64-mingw32-g++-win32 $(CFLAGS)

OS=$(shell uname -s)
ifeq ($(OS),Linux) 
	LDFLAGS=-Wl,-rpath='$$ORIGIN/../lib' -L ../lib -lspline
else 
	LDFLAGS=-L ../lib -lspline
endif

all:
	$(CC) cpptest.cc -o cpptest	$(LDFLAGS) 
	./cpptest
	$(CCc) ctest.c -o ctest	$(LDFLAGS) -lm
	./ctest
	python3 testspline.py

clean:
	-rm -v cpptest
	-rm -v ctest