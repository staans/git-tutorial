def check_antwoord(antwoord):
    return antwoord == 42

LANG = "EN"

def hello_world(lang):
    if lang == "NL":
        return "Hallo wereld!"
    elif lang == "FR":
        return "Bonjour le monde!"
    else:
        return "Hello world!"

def test():
    assert hello_world("NL") == "Hallo wereld!", "Test failed"

def main():
    print(hello_world(LANG))

#test()
main()

antwoord = input("Wat is het antwoord op de ultieme vraag van het leven, het universum, en alles?")
if check_antwoord(antwoord):
    print("Correct!")
else:
    print("Mogelijk heb je een andere vraag in je hoofd?")