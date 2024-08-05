"""
Script para buscar y crear una lista de forma recursiva con los md
que encuentre en el directorio actual de ejecucion
"""
import os
from glob import glob

DOC_FILES_DIR = os.path.join(os.getcwd())

MD_FILE_LIST = (
    y for x in os.walk(DOC_FILES_DIR)
    for y in glob(os.path.join(x[0], '*.md'))
)

text = []

text.append("* Index")

for m_file in MD_FILE_LIST:
    levels = m_file.replace(DOC_FILES_DIR, '').count(os.sep)
    text.append(
        '%s* [%s](./%s)' % (
        ' ' * levels * 4,
        m_file.split(os.sep)[-1].replace('.md', ''),
        m_file.replace(DOC_FILES_DIR, '').replace(os.sep,'/'))
    )

for line in text:
    print(line)