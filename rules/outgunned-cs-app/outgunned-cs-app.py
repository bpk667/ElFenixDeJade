# La idea de este script es que a traves de un archivo minimo con los datos del
# personaje, genere un mark down bonito con la informacion relevante del mismo

# Requisitos:
# pip install pyyaml

import getopt
import os
import sys

from outgunned import outgunned_character_sheet_generate, \
        outgunned_print_role_details, outgunned_print_trope_details, \
        outgunned_print_roles, outgunned_print_tropes

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main(argv):
    character_data = ''
    character_sheet = ''

    trope = ''
    role = ''

    print_roles = False
    print_tropes = False

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile=","trope=","role=","print_roles","print_tropes"])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            character_data = arg
        elif opt in ("-o", "--ofile"):
            character_sheet = arg
        elif opt in "--trope":
            trope = arg
        elif opt in "--role":
            role = arg
        elif opt in "--print_tropes":
            print_tropes = True
        elif opt in "--print_roles":
            print_roles = True

    if (character_data == "" or character_sheet == "") and trope == "" and role == "" and not print_roles and not print_tropes:
        print_help()
        sys.exit(2)

    # TESTS:
    # outgunned_data = OutgunnedData()
    # print(character_data)
    # print('Character data file is "%s"' % character_data)
    # print('Character sheet file is "%s"' % character_sheet)
    # print(outgunned_data.get_attribute('BRAWN'))
    # print(outgunned_data.get_attribute('Brawn'))
    # print(outgunned_data.get_role('Agent'))
    # print(outgunned_data.get_trope('Last boy scout / Girl Scout'))
    # print(outgunned_data.get_feat('I’LL MAKE A PHONE CALL'))

    if character_data and character_sheet:
        outgunned_character_sheet_generate(
            character_data=os.path.join(__location__, character_data),
            character_sheet=os.path.join(__location__, character_sheet)
        )
    
    if role:
        outgunned_print_role_details(role)
    
    if trope:
        outgunned_print_trope_details(trope)

    if print_roles:
        outgunned_print_roles()

    if print_tropes:
        outgunned_print_tropes()

    sys.exit(0)

def print_help():
    print('outgunned-cs-app.py -i <character_data.yml> -o <character_sheet.md>')
    print('outgunned-cs-app.py [--trope=<trope>] [--role=<role>] [--print_roles] [--print_tropes]')

if __name__ == "__main__":
   main(sys.argv[1:])
