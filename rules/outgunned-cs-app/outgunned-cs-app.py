# La idea de este script es que a traves de un archivo minimo con los datos del
# personaje, genere un mark down bonito con la informacion relevante del mismo

# Requisitos:
# pip install pyyaml

import getopt
import os
import sys

import yaml

from outgunned import OutgunnedData, outgunned_character_sheet_generate

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main(argv):
    character_data = ''
    character_sheet = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('outgunned-cs-app.py -i <character_data.yml> -o <character_sheet.md>')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print('outgunned-cs-app.py -i <character_data.yml> -o <character_sheet.md>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            character_data = arg
        elif opt in ("-o", "--ofile"):
            character_sheet = arg

    if character_data == "" or character_sheet == "":
        print('outgunned-cs-app.py -i <character_data.yml> -o <character_sheet.md>')
        sys.exit(2)

    outgunned_data = OutgunnedData()

    # TESTS:
    # print(character_data)
    # print('Character data file is "%s"' % character_data)
    # print('Character sheet file is "%s"' % character_sheet)
    # print(outgunned_data.get_attribute('BRAWN'))
    # print(outgunned_data.get_attribute('Brawn'))
    # print(outgunned_data.get_role('Agent'))
    # print(outgunned_data.get_trope('Last boy scout / Girl Scout'))
    # print(outgunned_data.get_feat('I’LL MAKE A PHONE CALL'))

    outgunned_character_sheet_generate(
        character_data=os.path.join(__location__, character_data),
        character_sheet=os.path.join(__location__, character_sheet)
    )

    sys.exit(0)

if __name__ == "__main__":
   main(sys.argv[1:])


# print('argument list', sys.argv)
# first = int(sys.argv[1])

# # TODO: Todo

# with open('config.yml', 'r') as file:
#     prime_service = yaml.safe_load(file)

# print(prime_service['prime_numbers'][0])
# print(prime_service['rest']['url'])