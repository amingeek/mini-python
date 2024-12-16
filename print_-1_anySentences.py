def print_sentences(string):
    if len(string) == 0:
        return
    print(string)
    print_sentences(string[:-1])

string = "Shab yalda mobarak!"

print_sentences(string)