PY?=
PELICAN?=pelican
PELICANOPTS=

BASEDIR=../../
GITHUBDIR=$(CURDIR)
CONTENTDIR=$(GITHUBDIR)/content
OUTPUTDIR=$(GITHUBDIR)/output
CONFFILE=$(GITHUBDIR)/pelicanconf.py


DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

SERVER ?= "0.0.0.0"

PORT ?= 0
ifneq ($(PORT), 0)
	PELICANOPTS += -p $(PORT)
endif

html:
	python build.py "$(BASEDIR)" "$(CONTENTDIR)"
	"$(PELICAN)" "$(CONTENTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)
	python copy_images.py "$(BASEDIR)" "$(OUTPUTDIR)"

clean:
	[ ! -d "$(CONTENTDIR)" ] || rm -rf "$(CONTENTDIR)"
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

serve:
	"$(PELICAN)" -l "$(CONTENTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

search:
	./pagefind --site "$(OUTPUTDIR)"

.PHONY: html clean serve search
