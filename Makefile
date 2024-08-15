DESTDIR = /usr/local/share/dict
CONFIG_FILE = /etc/dict/dictd.conf
DICTNAME = ozhegov
DICTNAME_FULL = "Словарь Ожегова"
DICTSOURCE = ${DICTNAME}.txt
SLOB_FILE = ${DICTNAME}.slob

define CONFIG
database ${DICTNAME} {
  data  ${DESTDIR}/${DICTNAME}.dict.dz
  index ${DESTDIR}/${DICTNAME}.index
}
endef
export CONFIG

${DICTNAME}.dict.dz: ${DICTNAME}.dict
	dictzip -f ${DICTNAME}.dict

${DICTNAME}.index ${DICTNAME}.dict: ${DICTSOURCE} convert.py
	python3 convert.py ${DICTSOURCE} | dictfmt --utf8 --allchars -s ${DICTNAME_FULL} -j ${DICTNAME}

install: ${DICTNAME}.index ${DICTNAME}.dict.dz
	mkdir -p ${DESTDIR}
	cp -f ${DICTNAME}.dict.dz ${DICTNAME}.index ${DESTDIR}
	@echo "Don't forget to add following to dictd config (usually ${CONFIG_FILE}) and to restart dictd."
	@echo "$$CONFIG"

uninstall:
	rm -f ${DESTDIR}/${DICTNAME}.index ${DESTDIR}/${DICTNAME}.dict.dz

${SLOB_FILE} slob: ${DICTSOURCE} convert.py
	rm -f ${SLOB_FILE}
	python3 convert.py ${DICTSOURCE} ${SLOB_FILE} ${DICTNAME_FULL}

clean:
	rm -f ${DICTNAME}.dict.dz ${DICTNAME}.index ${SLOB_FILE}

.PHONY: install uninstall slob clean

# end
