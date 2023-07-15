import csv
import sys


def read_glossary(csv_file):
    glossary_content = {}
    with open(csv_file, newline="") as glossary_file:
        glossary = csv.reader(glossary_file)
        for row in glossary:
            translations = []
            for translation in row[1:]:
                translations.append(translation)
            glossary_content[row[0]] = translations

    return glossary_content


class Glossary:
    def __init__(self, glossary_content):
        self.glossary_content = glossary_content

    # TODO
    # def search_source_term(self):
    #     pass

    # def search_target_term(self):
    #     pass

    # def add_source_term(self):
    #     pass

    # def add_target_term(self):
    #     pass

    # def edit_term(self):
    #     pass

    # def delete_source_term(self):
    #     pass

    # def delete_target_term(self):
    #     pass

    # def delete_glossary_unit(self):
    #     pass


print(read_glossary(sys.argv[1]))
