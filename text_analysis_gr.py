################################
## Christina-Theano Kylafi
################################

#Pangram checker for greek text
def isPangram(sentence):
    alphabet = set("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ")

    input_txt_set = set(input_txt.upper())

    common_letters = alphabet.intersection(input_txt_set)

    if len(common_letters) is len(alphabet):
        print("\nThe sentence: '" + input_txt + "' is a Pangram ! \n")
        return True
    else:
        print("\nThe sentence: '" + input_txt + "' is ΝΟΤ a Pangram ! \n")
        return False



# main
input_txt = input("Type a sentence to check if it is a Pangram: ")
isPangram(input_txt)