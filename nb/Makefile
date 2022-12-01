BIN ?= nb
BIN_BOOKMARK ?= bookmark
PREFIX ?= /usr

install:
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	$(INSTALL) $(BIN) $(DESTDIR)$(PREFIX)/bin/$(BIN)
	$(INSTALL) bin/$(BIN_BOOKMARK) $(DESTDIR)$(PREFIX)/bin/$(BIN_BOOKMARK)
