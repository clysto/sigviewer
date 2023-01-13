UIFILES = $(wildcard ui/*.ui)
PYFILES = $(patsubst %.ui,%.py,$(UIFILES))

all:
	nuitka3 --standalone --disable-console --plugin-enable=pyside6 sigviewer.py

ui: $(PYFILES)

%.py: %.ui
	pyside6-uic -o $@ $<
