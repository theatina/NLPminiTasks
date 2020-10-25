################################
## Christina-Theano Kylafi
################################

#Pangram checker for greek text
def isPangram(sentence):
    alphabet = set("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ")
    vowels = set("ΑΆΕΈΗΉΙΊΟΌΥΎΏΩ")
    accented_vowels = set("ΆΈΉΊΌΎΏ")

    input_txt_set = set(input_txt.upper())
    # print(input_txt_set)

    #cases of accented vowels
    input_txt_acc_vowels = accented_vowels.intersection(input_txt_set)
    # print(input_txt_acc_vowels)

    all_vowels = ( ('Α', 'Ά'), ('Ε', 'Έ'), ('Ι', 'Ί'), ('Η', 'Ή'), ('Υ', 'Ύ'), ('Ο', 'Ό'), ('Ω', 'Ώ') )
    
    #remove accents from letters in the input text set
    for vowel in input_txt_acc_vowels: 
        for tuple_index,a  in enumerate(all_vowels):
            if vowel in a:
                pos = a.index(vowel)
                # print('found %s in tuple %s at index %d' % (vowel, tuple_index, pos))
                vowel_to_add = all_vowels[tuple_index][pos-1]
                input_txt_set.remove(vowel)
                input_txt_set.update(vowel_to_add)


    print(input_txt_set)
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