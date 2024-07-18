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

## Ejemplos:

```bash
# Generar la hoja de personaje de rosa diaz:
python outgunned-cs-app.py -i samples/detective-rosa-diaz.yml -o samples/detective-rosa-diaz.md
# Mostrar todas las tropes
python outgunned-cs-app.py --print_tropes
# Mostrar todos los roles
python outgunned-cs-app.py --print_roles
# Mostrar el trope Vigilante
python outgunned-cs-app.py --trope=Vigilante
# Mostrar el rol Brain
python outgunned-cs-app.py --role=Brain

# Generar todos los samples
for sheet in samples/pnjs/*yml; do
    python3 outgunned-cs-app.py -i $sheet -o output/$(basename -s'.yml' $sheet).md
done

# FIXME: No funciona bien, por el simbolo de adrenalina
# # Convertir todos los output md a pdf con pandoc
# for sample in `ls output/*.md`; do
#     sample_output=`echo $sample | sed -e "s/.md/.pdf/g" -e "s,^output/,,g"`
#     # pandoc pages/til/convert-markdown-pdf-linux.md -o convert-markdown-pdf.pdf --pdf-engine=xelatex
#     pandoc $sample -o output/pdf/$sample_output.pdf --pdf-engine=xelatex
# done

```
