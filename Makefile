##
#
# ozhegov-dict
#
# @version 0.1

DESTDIR = /usr/local/share/dict/

make:
	python3 ozhegov-parse.py > ozhegov_dict.txt
	dictfmt --utf8 --allchars -s "Словарь Ожегова" -j ozhegov < ozhegov_dict.txt

install:
	mkdir -p ${DESTDIR}
	cp -f ozhegov.dict ozhegov.index ${DESTDIR}
	@echo "Don't forget to add those files to dictd config and to restart dictd"

uninstall:
	rm -f ${DESTDIR}ozhegov.index ${DESTDIR}ozhegov.dict

clean:
	rm -f ozhegov_dict.txt ozhegov.dict ozhegov.index

# end
