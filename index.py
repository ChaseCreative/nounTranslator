import random
import  time
#from the file Nouns, import class of Nouns,Verb 1, and Verbs
from Nouns import Nouns1

def nounFormTester():
    
    user_noun_input = input("Give the nominative, genitive, gender, and singlular and plural meaning of a word: ")
    
#    print(user_noun_input) this prints the user's input
    #this replaces the comma with a space
    x = user_noun_input.replace(","," ")
    #this replaces the period with a space and then splits the string into a list
    uni = x.replace("."," ").split()
    #uni = [for z in y.split()]
    
    #uni = [x.replace(","," ") and x.replace("."," ") for x in user_noun_input.split()]
#    print(uni) this prints a list of the string
#    print(uni[4]) this prints the index 4

    while True:
        
        case = ["nominative", "genitive", "dative", "accusative", "ablative", "vocative"]
        number = ["_singular", "_plural"]
        userNoun = Nouns1(uni[0],uni[1],uni[2],uni[3],uni[4])

        
        
        #this creates a random index of a range from 0 through the length of list -1.
        ranCaseIndx = random.randint(0, len(case)-1)
        ranNumberIndx = random.randint(0, len(number)-1)
        #rnf signifies random noun form
        rnf = case[ranCaseIndx] + number[ranNumberIndx]
        #print(random_noun)
        #rui signifies random user input
        #rui = ("userNoun." + random_noun)

        #print(userNoun.nominative_singular())



        user_response = input("What is the " + rnf.replace("_", " ") + " of " + uni[0] + "?")
        noun_form = userNoun.__getattribute__(rnf)()
#        print(userNoun.__getattribute__(rnf))
        if user_response == noun_form:
            print("Nice!")
        else:
            print("Oops! The " + rnf.replace("_", " ") + " of " + uni[0] + " is " + noun_form)

        play_again = input("Do you want to play again?")
        if play_again.lower().startswith("y"):
            continue
        if play_again.lower().startswith("n"):
            time.sleep(1)
            another_noun = input("Do you want to pick another noun?")
            if another_noun.lower().startswith("y"):
                nounFormTester()

            else:
                print("Okay! See you later!")
                exit()


nounFormTester()
#print(noun_form)


