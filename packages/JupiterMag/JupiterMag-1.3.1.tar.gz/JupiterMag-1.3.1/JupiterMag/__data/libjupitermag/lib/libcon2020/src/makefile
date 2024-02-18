# CFLAGS for CC
CFLAGS=-lm -fPIC -std=c++17 -Wextra -O3

# Compiler
CCo=g++ -c $(CFLAGS)
CC=g++ $(CFLAGS)
CCWo=x86_64-w64-mingw32-g++-win32 -c $(CFLAGS)
CCW=x86_64-w64-mingw32-g++-win32 $(CFLAGS)

ifndef BUILDDIR 
	BUILDDIR=../build
endif

OS=$(shell uname -s)
ifeq ($(OS),Linux)
	LIBFILE=libcon2020.so
else
	LIBFILE=libcon2020.dylib
endif

all: header obj lib 

header:
	$(CC) trimstring.cc generateheader.cc -o generateheader
	./generateheader
	-rm generateheader

obj: con2020 bessel polyeval trap smoothd libcon2020 scalarpot flux lmic

con2020:
	$(CCo) con2020.cc -o $(BUILDDIR)/con2020.o 

bessel:
	$(CCo) bessel.cc -o $(BUILDDIR)/bessel.o 

polyeval:
	$(CCo) polyeval.cc -o $(BUILDDIR)/polyeval.o 

trap:
	$(CCo) trap.cc -o $(BUILDDIR)/trap.o 

smoothd:
	$(CCo) smoothd.cc -o $(BUILDDIR)/smoothd.o 

libcon2020:
	$(CCo) libcon2020.cc -o $(BUILDDIR)/libcon2020.o

scalarpot:
	$(CCo) scalarpot.cc -o $(BUILDDIR)/scalarpot.o

flux:
	$(CCo) flux.cc -o $(BUILDDIR)/flux.o

lmic:
	$(CCo) lmic.cc -o $(BUILDDIR)/lmic.o

lib:
	$(CC) $(BUILDDIR)/*.o -shared -o ../lib/$(LIBFILE)
	
winobj:
	$(CCWo) con2020.cc -o $(BUILDDIR)/con2020.o 
	$(CCWo) bessel.cc -o $(BUILDDIR)/bessel.o 
	$(CCWo) polyeval.cc -o $(BUILDDIR)/polyeval.o 
	$(CCWo) trap.cc -o $(BUILDDIR)/trap.o 
	$(CCWo) smoothd.cc -o $(BUILDDIR)/smoothd.o 
	$(CCWo) libcon2020.cc -o $(BUILDDIR)/libcon2020.o
	$(CCWo) scalarpot.cc -o $(BUILDDIR)/scalarpot.o
	$(CCWo) flux.cc -o $(BUILDDIR)/flux.o
	$(CCWo) lmic.cc -o $(BUILDDIR)/lmic.o

winlib:
	$(CCW) $(BUILDDIR)/*.o -shared -o ../lib/libcon2020.dll

test:
	$(CC) test.cc *.o -o test

