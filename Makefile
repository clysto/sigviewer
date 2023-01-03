UIFILES = $(wildcard ui/*.ui)
PYFILES = $(patsubst %.ui,%.py,$(UIFILES))

ui: $(PYFILES)

%.py: %.ui
	pyside6-uic -o $@ $<
