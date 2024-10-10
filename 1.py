caps = lambda text: [i for i, char in enumerate(text) if char.isupper()]
s = input("Введіть текст: ")
print(caps(s))
