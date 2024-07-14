# Outgunned Charactersheet App

## Instalacion

`pip install pyyaml`

## Manual

1. Crear el archivo con los datos especificos del personaje `samples/detective-rosa-diaz.yml`
2. Ejecutar el script en el directorio pasandole los parametros:
    * `-i <character_data.yml>` fichero con datos especificos
    * `-o <character_sheet.md>` fichero de salida para el markdown

## Acerca de los datos especificos del personaje

Lo unico que hay que poner son las cosas opcionales o que puedan cambiar, estas son:

* En Trope:
    * El punto de atributo (a elegir entre las dos opciones)
    * La feature a elegir de la lista
* En Role:
    * Dos features a elegir de la lista
    * El gear
    * Revisar que el atributo no coincide con el elegido en el trope

## Ejemplo:

```bash
python outgunned-cs-app.py -i samples/detective-rosa-diaz.yml -o samples/detective-rosa-diaz.md
```
