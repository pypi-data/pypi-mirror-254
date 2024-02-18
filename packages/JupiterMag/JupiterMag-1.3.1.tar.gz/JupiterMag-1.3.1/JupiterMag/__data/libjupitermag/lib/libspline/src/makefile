# CFLAGS for CC
CFLAGS=-lm -std=c++17 -Wextra -O3

# Compiler
CCo=g++ -fPIC -c $(CFLAGS)
CC=g++ -fPIC $(CFLAGS)
CCWo=x86_64-w64-mingw32-g++-win32 -c $(CFLAGS)
CCW=x86_64-w64-mingw32-g++-win32 $(CFLAGS)

ifndef BUILDDIR 
	BUILDDIR=../build
endif

OS=$(shell uname -s)
ifeq ($(OS),Linux)
	LIBFILE=libspline.so
else
	LIBFILE=libspline.dylib
endif

all: header obj lib

header:
	$(CC) trimstring.cc generateheader.cc -o generateheader
	./generateheader
	-rm generateheader

obj:
	$(CCo) spline.cc -o $(BUILDDIR)/spline.o
	$(CCo) libspline.cc -o $(BUILDDIR)/libspline.o

winobj:
	$(CCWo) spline.cc -o $(BUILDDIR)/spline.o
	$(CCWo) libspline.cc -o $(BUILDDIR)/libspline.o

lib: 
	$(CC) -shared -o ../lib/$(LIBFILE) $(BUILDDIR)/*.o
	
winlib: 
	$(CCW) -shared -o ../lib/libspline.dll $(BUILDDIR)/*.o
	