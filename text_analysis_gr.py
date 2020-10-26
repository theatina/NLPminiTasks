################################
## Christina-Theano Kylafi
################################

#Pangram checker for greek text
def isPangram(sentence):
    #Set of all the capital greek letters
    alphabet = set("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ")
    vowels = set("ΑΆΕΈΗΉΙΊΟΌΥΎΏΩ")
    #Set of the accented vowels
    accented_vowels = set("ΆΈΉΊΌΎΏ")

    #In both cases of 'ς' and 'σ', the upper letter will be the same('Σ'), merging the two different lower symbols into one capital
    input_txt_set = set(input_txt.upper())

    #cases of accented vowels
    input_txt_acc_vowels = accented_vowels.intersection(input_txt_set)

    #create a tuple with pairs of non-accented and accented vowels
    all_vowels = ( ('Α', 'Ά'), ('Ε', 'Έ'), ('Η', 'Ή'), ('Ι', 'Ί'), ('Υ', 'Ύ'), ('Ο', 'Ό'), ('Ω', 'Ώ') )
    
    acc_vowels_to_remove = []
    vowels_to_add = []
    #remove accents from the accented vowels in the input text set - update the character set of the sentense
    for vowel in input_txt_acc_vowels: 
        for tuple_index,a  in enumerate(all_vowels):
            #if an accented vowel is found, it is replaced by the non accented upper case one
            if vowel in a:
                pos = a.index(vowel)
                acc_vowels_to_remove.append(vowel)
                vowel_to_add = all_vowels[tuple_index][pos-1]
                vowels_to_add.append(vowel_to_add)



    #remove accented vowels
    input_txt_set.difference_update(acc_vowels_to_remove)
    #add - if not in set - the non accented versions of the vowels above
    input_txt_set.update(vowels_to_add)
    
    #Creation of the sets 'input_txt_set' and 'alphabet' intersection set - common letters between the alphabet and the sentence set of characters
    #which is the set of the letters that the sentence includes
    common_letters = alphabet.intersection(input_txt_set)
    #Find the letters of the alphabet that are not included in the sentence set
    non_common_letters = alphabet - common_letters

    line = ["_" for i in range(100)]
    line = "".join(line)

    print("\n"+str(line)+"\n")

    if len(common_letters) is len(alphabet):
        print("\nThe sentence: '" + input_txt + "' is a Pangram ! \n")
        # return True
    else:
        print("\nThe sentence: '" + input_txt + "' is ΝΟΤ a Pangram ! \n\n( set of missing letters -> " + str(non_common_letters)+" )\n")
        # return False

    print(str(line)+"\n")


# main
input_txt = input("Type a sentence to check if it is a Pangram: ")
isPangram(input_txt)