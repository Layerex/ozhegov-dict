# ozhegov-dict

Словарь Ожегова в форматах [DICT](https://en.wikipedia.org/wiki/DICT#DICT_file_format) и [slob](https://github.com/itkach/slob).

## Установка

```sh
sudo make install
```

Затем добавьте следующее в файл конфигурации dictd (обычно `/etc/dict/dictd.conf`):

```
database ozhegov {
  data  /usr/local/share/dict/ozhegov.dict
  index /usr/local/share/dict/ozhegov.index
}
```

### slob

Формат для Aard2.

``` sh
make slob
```
