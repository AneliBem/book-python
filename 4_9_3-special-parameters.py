def standard_agr(agr): # аргументи і позиційні і ключові
    print(agr)

def pos_only_agr(agr, /): # тільки позиційні
    print(agr)

def kwd_only_agr(*, agr): # тільки ключові
    print(agr)

def combined_example(pos_only, /, standard, *, kwd_only): # всі три умови в одній функції
    print(pos_only, standard, kwd_only)