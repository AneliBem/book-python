import sys
sys.ps1 = "-->" # зміна мітки інтерактивного режиму інтерпритатору
sys.ps2 = "---" # зміна мітки інтерактивного режиму інтерпритатору

print(sys.path) # шлях пошуку модулів інтерпретатору
sys.path.append('/python/python3.13') # зміна шляху