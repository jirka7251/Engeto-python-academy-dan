import sys
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    foss fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

registrovani = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

user = input("username: ")
password = input("password: ")

if registrovani.get(user) == password:
    print("-" * 40)
    print(f"Welcome to the app, {user}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print("-" * 40)
else:
    print("unregistered user, terminating the program...")
    sys.exit()

volba = input(f"Enter a number between 1 and {len(TEXTS)} to select the text: ")

if not volba.isdigit():
    print("Invalid input, please enter a digit. Terminating the program...")
    sys.exit()

index = int(volba) - 1

if not (0 <= index < len(TEXTS)):
    print("Choice out of range, terminating the program...")
    sys.exit()

vybrany_text = TEXTS[index]

slova = vybrany_text.split()
vysledky = {
    "total": 0, "title": 0, "upper": 0, 
    "lower": 0, "numeric": 0, "sum": 0
}
cetnost_delek = {}

for slovo in slova:
    ciste_slovo = slovo.strip(",.:;")
    if not ciste_slovo:
        continue
    
    vysledky["total"] += 1
    
    if ciste_slovo.isdigit():
        vysledky["numeric"] += 1
        vysledky["sum"] += int(ciste_slovo)
    elif ciste_slovo.isupper():
        vysledky["upper"] += 1
    elif ciste_slovo.istitle():
        vysledky["title"] += 1
    elif ciste_slovo.islower():
        vysledky["lower"] += 1
        
    delka = len(ciste_slovo)
    cetnost_delek[delka] = cetnost_delek.get(delka, 0) + 1

print("-" * 40)
print(f"There are {vysledky['total']} words in the selected text.")
print(f"There are {vysledky['title']} titlecase words.")
print(f"There are {vysledky['upper']} uppercase words.")
print(f"There are {vysledky['lower']} lowercase words.")
print(f"There are {vysledky['numeric']} numeric strings.")
print(f"The sum of all the numbers {vysledky['sum']}")
print("-" * 40)

print(f"{'LEN':>3}|{'OCCURRENCES':^15}|{'NR.':<3}")
print("-" * 40)

serazene_delky = sorted(cetnost_delek.keys())
for d in serazene_delky:
    hvezdy = "*" * cetnost_delek[d]
    print(f"{d:>3}|{hvezdy:<15}|{cetnost_delek[d]:<3}")