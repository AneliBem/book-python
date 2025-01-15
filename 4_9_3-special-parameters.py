def standard_arg(arg): # аргументи і позиційні і ключові
    print(arg)

def pos_only_arg(arg, /): # тільки позиційні
    print(arg)

def kwd_only_arg(*, arg): # тільки ключові
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only): # всі три умови в одній функції
    print(pos_only, standard, kwd_only)

standard_arg(2)

standard_arg(arg=2)


pos_only_arg(1)

# pos_only_arg(arg=1) #error


# kwd_only_arg(3) #error

kwd_only_arg(arg=3)


# combined_example(1, 2, 3) # kwd_only error
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) # pos_only error


def foo(name, /, **kwds):
    return 'name' in kwds

print(foo(1, **{'name': 2})) # return повертає значення name в словник kwds. / значить що елемент name є позиційним. функція print перевіряє чи є значення 'name' в словнику **kwds


# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2): # pos1, pos2 це позційні значення. pos_or_kwd це може бути і позиційні і ключові значення. kwd1, kwd2 це ключові значення

