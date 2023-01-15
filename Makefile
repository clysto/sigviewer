UIFILES = $(wildcard ui/*.ui)
PYFILES = $(patsubst %.ui,%.py,$(UIFILES))

all:
	nuitka --standalone --disable-console --plugin-enable=pyside6 --plugin-enable=numpy sigviewer.py

ui: $(PYFILES)

%.py: %.ui
	pyside6-uic -o $@ $<
