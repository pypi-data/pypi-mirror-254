

ifndef BUILDDIR 
	export BUILDDIR=$(shell pwd)/build
endif

ifeq ($(OS),Windows_NT)
#windows stuff here
	MD=mkdir
else
#linux and mac here
	OS=$(shell uname -s)
	MD=mkdir -p
endif

ifeq ($(PREFIX),)
#install path
	PREFIX=/usr/local
endif


.PHONY: all lib obj clean header test install testinstall uninstall

all: 
	$(MD) $(BUILDDIR)
	$(MD) lib
	cd src; make all

windows: winobj winlib

obj:
	$(MD) $(BUILDDIR)
	cd src; make obj

lib:
	$(MD) lib
	cd src; make lib

winobj:
	$(MD) $(BUILDDIR)
	cd src; make winobj

winlib: 
	$(MD) lib
	cd src; make winlib

header:
	cd src; make header
# ifneq (,$(shell which python3))
# 	python3 generateheader.py
# else
# 	@echo "python3 command doesn't appear to exist - skipping header regeneration..."
# endif

test:
	cd test; make all

clean:
	cd test; make clean
	-rm -v lib/libcon2020.so
	-rm -v lib/libcon2020.dll
	-rm -v lib/libcon2020.dylib
	-rmdir -v lib/libcon2020
	-rm -v build/*.o
	-rmdir -v build
	-rm -v testinstall

install:
	cp -v include/con2020.h $(PREFIX)/include
	cp -v include/con2020c.h $(PREFIX)/include

ifeq ($(OS),Linux)
	cp -v lib/libcon2020.so $(PREFIX)/lib
	chmod 0775 $(PREFIX)/lib/libcon2020.so
	ldconfig
else
	cp -v lib/libcon2020.dylib $(PREFIX)/lib
	chmod 0775 $(PREFIX)/lib/libcon2020.dylib
endif


uninstall:
	rm -v $(PREFIX)/include/con2020.h
	rm -v $(PREFIX)/include/con2020c.h
ifeq ($(OS),Linux)
	rm -v $(PREFIX)/lib/libcon2020.so
	ldconfig
else
	rm -v $(PREFIX)/lib/libcon2020.dylib
endif

testinstall:
	g++ -std=c++17 test/testc_installed.cc -o testinstall -lcon2020
	./testinstall
	rm -v testinstall