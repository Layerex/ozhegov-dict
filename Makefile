DESTDIR = /usr/local/share/dict
CONFIG_FILE = /etc/dict/dictd.conf
DICTNAME = ozhegov
DICTNAME_FULL = "Словарь Ожегова"
DICTFILE = ${DICTNAME}_dict.txt
DICTSOURCE = ${DICTNAME}.txt

DOWNLOAD_DIR = data

define CONFIG
database ${DICTNAME} {
  data  ${DESTDIR}/${DICTNAME}.dict
  index ${DESTDIR}/${DICTNAME}.index
}
endef
export CONFIG

make:
	python3 ozhegov-parse.py ${DICTSOURCE} > ${DICTFILE}
	dictfmt --utf8 --allchars -s ${DICTNAME_FULL} -j ${DICTNAME} < ${DICTFILE}

install: make
	mkdir -p ${DESTDIR}
	cp -f ${DICTNAME}.dict ${DICTNAME}.index ${DESTDIR}
	@echo "Don't forget to add following to dictd config (usually ${CONFIG_FILE}) and to restart dictd."
	@echo "$$CONFIG"

uninstall:
	rm -f ${DESTDIR}/${DICTNAME}.index ${DESTDIR}/${DICTNAME}.dict

clean:
	rm -f ${DICTFILE} ${DICTNAME}.dict ${DICTNAME}.index

# end
