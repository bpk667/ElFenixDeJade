import os
import shutil

import yaml

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class OutgunnedData(metaclass=SingletonMeta):
    outgunned_data = None

    def __init__(self):
        with open(os.path.join(__location__, 'data.yml'), 'r') as file:
            self.outgunned_data = yaml.safe_load(file)

    def get_check_case(self, items, key):
        return items[key] if key in items else items[key.upper()]


    def get_roles(self):
        return self.outgunned_data['ROLES']

    def get_tropes(self):
        return self.outgunned_data['TROPES']

    def get_feats(self):
        return self.outgunned_data['FEATS']

    def get_attributes(self):
        return self.outgunned_data['ATTRIBUTES']

    def get_attribute(self, attribute):
        return self.get_check_case(
            self.get_attributes(), attribute
        )
    
    def get_role(self, role):
        return self.get_check_case(
            self.get_roles(), role
        )
    
    def get_role_atts(self, role):
        return self.get_role(role)['ATTRIBUTES']

    def get_role_skills(self, role):
        return self.get_role(role)['SKILL_POINTS']

    def get_trope(self, trope):
        return self.get_check_case(
            self.get_tropes(), trope
        )

    def get_trope_description(self, trope):
        return self.get_trope(trope)['DESCRIPTION']
    
    def get_trope_skills(self, trope):
        return self.get_trope(trope)['SKILL_POINTS']

    def get_feat(self, feat):
        return self.get_check_case(
            self.get_feats(), feat
        )


class OutgunnedCSGenerator:
    TEMPLATE_TAGS = {
        '<NAME>': 'get_name',
        '<ROLE>': 'get_role',
        '<JOB>': 'get_job',
        '<AGE>': 'get_age',
        '<FLAW>': 'get_flaw',
        '<CATCH_PHRASE>': 'get_catch_phrase',
        '<CHARACTER_DESCRIPTION>': 'get_character_description',
        '<TROPE>': 'get_trope',
        '<TROPE_DESCRIPTION>': 'get_trope_description',
        '<ATTRIBUTES>': 'get_attributes',
        '<FEATURES>': 'get_features',
        '<GEAR>': 'get_gear',
    }

    character_data = None
    character_sheet = None

    calculated_attributes = {}

    def __init__(self, character_data, character_sheet):
        with open(character_data, 'r') as file:
            self.character_data = yaml.safe_load(file)
        
        self.character_sheet = character_sheet

    def render(self):
        # 1. Chequeamos que no existe la hoja aun
        if os.path.isfile(self.character_sheet):
            raise Exception('El fichero %s ya existe' % self.character_sheet)

        # 2. Recorrer la copia y reemplazar
        template_file = open(os.path.join(__location__, 'character-sheet-template.md'), "r")

        new_file_content = ""

        for line in template_file:
            stripped_line = line.strip()
            new_line = stripped_line
            
            for tag in self.TEMPLATE_TAGS:
                tag_function = getattr(self, self.TEMPLATE_TAGS[tag])
                new_line = new_line.replace(tag, tag_function())
            
            new_file_content += new_line +"\n"

        template_file.close()

        print(new_file_content)

        writing_file = open(self.character_sheet, "w")
        writing_file.write(new_file_content)
        writing_file.close()
    
    def get_name(self):
        return self.character_data['personal_data']['name'] \
            if 'name' in self.character_data['personal_data'] \
            else 'John Doe'

    # Required
    def get_role(self):
        return self.character_data['personal_data']['role']

    def get_job(self):
        return self.character_data['personal_data']['job'] \
            if 'job' in self.character_data['personal_data'] \
            else 'SIN JOB!!!!'

    def get_age(self):
        return self.character_data['personal_data']['age'] \
            if 'age' in self.character_data['personal_data'] \
            else 'Adult'

    def get_flaw(self):
        return self.character_data['personal_data']['flaw'] \
            if 'flaw' in self.character_data['personal_data'] \
            else 'SIN FLAW!!!!'

    def get_catch_phrase(self):
        return self.character_data['personal_data']['catch_phrase'] \
            if 'catch_phrase' in self.character_data['personal_data'] \
            else 'SIN CATCH PHRASE!!!!'

    def get_character_description(self):
        return self.character_data['personal_data']['character_description'] \
            if 'character_description' in self.character_data['personal_data'] \
            else 'SIN CHARACTER DESCRIPTION!!!!'

    # Required
    def get_trope(self):
        return self.character_data['personal_data']['trope']
    
    def get_trope_description(self):
        return OutgunnedData().get_trope_description(
            self.get_trope()
        )

    def calculate_attributes(self):
        if self.calculated_attributes:
            return self.calculated_attributes
        
        # 1. Coger atributos de los datos del personaje
        for att in self.character_data['attributes']:
            self.add_to_calc_att(att)
        
        # 2. Coger atributos del rol
        role_atts = OutgunnedData().get_role_atts(
            self.get_role()
        )

        for att in role_atts:
            self.add_to_calc_att(att)
        
        # 3. Coger skill points del rol
        role_skills = OutgunnedData().get_role_skills(
            self.get_role()
        )

        for att in role_skills:
            self.add_to_calc_att(att)

        # 4. Coger skill points del trope
        trope_skills = OutgunnedData().get_trope_skills(
            self.get_trope()
        )

        for att in trope_skills:
            self.add_to_calc_att(att)

        # TODO: Revisar... no estoy muy seguro si mola calcular el valor total
        # aqui... (cogiendo los valores por defecto de cualquiera)
        # 5. Coger valores por defecto
        for att in self.calculated_attributes:
            if att in OutgunnedData().get_attributes():
                self.calculated_attributes[att] += 2
            else:
                self.calculated_attributes[att] += 1

        return self.calculated_attributes

    def add_to_calc_att(self, att):
        if att in self.calculated_attributes:
            self.calculated_attributes[att] += 1
        else:
            self.calculated_attributes[att] = 1

    def get_attributes(self):
        self.calculate_attributes()

        # 6. Generar lista con los resultados
        print(self.calculated_attributes)

        attributes_md = ""

        for att in self.calculated_attributes:
            attributes_md += "* **%s:** %s\n" % (
                att, self.calculated_attributes[att]
            )

        return attributes_md

    def get_features(self):
        features_md = ""

        for feat in self.character_data['feats']:
            features_md += "### %s\n\n" % feat
            features_md += "%s\n\n" % OutgunnedData().get_feat(feat)

        return features_md

    def get_gear(self):
        gear_md = ""

        for item in self.character_data['gear']:
            gear_md += "* %s\n" % item
        
        return gear_md

def outgunned_character_sheet_generate(character_data, character_sheet):
    char_generator = OutgunnedCSGenerator(
        character_data=character_data, character_sheet=character_sheet
    )

    char_generator.render()

