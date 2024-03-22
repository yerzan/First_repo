text = 'Today a good day i like water, i like weather in outside. Elephant running to my home.'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

char_set = set()
symbol_set = set()

for el in text:
    if el.lower() in alphabet:
        char_set.add(el)
    else:
        symbol_set.add(el)
print(f"Chars {char_set}")
print(f"Symbol {symbol_set}")