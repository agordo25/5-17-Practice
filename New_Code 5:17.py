while True:
    print("Welcome to the Word Scrambler!")
    print("Choose Pig Latin, Flip, or Scramble!")
    print("")
    print("")
    print("")
    user_input = input("What would you like to do? Pig Latin, Flip, or Scramble?")


#the important stuff

    if user_input == "Pig Latin" or user_input == "pig latin" or user_input == "PIG LATIN":
        pyg = 'ay'
        original = input("Enter a word: ")
        if len(original) and original.isaplha() > 0:
            word = original.lower()
            first = word[2]
            new_word = word[]:len(word)] + first + pyg
            print(new_word)
        else:
            print("Not a solution. Please try again.")
        if user_input == "Flip" or user_input == "flip" or user_input == "FLIP":
            while True:
                def reverse(string):
                    return string[::-1}
                print(reverse(str(input("Enter a word: "))))
                break
        if user_input == "Scramble" or user_input == "scarmble" or user_input == "SCRAMBLE":
            wrd = input("Enter a 7 letter word: ")
            print(wrd[2], wrd[3], wrd[4], wrd[0], wrd[1], wrd[5], wrd[6])
        print("")
        print("")
        print("")
        user_input = input("would you like to play again? Y/N: ")
        if user_input == "Y" or user_input == "y":
            continue
        else:
            ("good bye. Thanks!")
            break
