import os
import random
from support import *
import time

org_words = file_to_list('google-10000-english.txt')
learned_words = file_to_list('learned_words.txt')

word_count = len(org_words)
correct, wrong, total = 0, 0, 0
lastspell = ""
total += 1

while True:
    current_random = random.randint(0, word_count)
    word = org_words[current_random]

    if word in learned_words:
        continue

    correct_in_first_try = True

    while True:
        os.system('clear')
        if lastspell:
            print("Last Spell:", lastspell)
        print("""
Total Spellings Learned: %s
correct: %s, wrong: %s
score: %s
Actions:
    1) say slowly
    2) Answer
    9) Exit
""" % (len(learned_words), correct, wrong, (correct)/(wrong + 1)))
        os.system("""say 'Spell, %s'""" % word)
        response = input("=> ")

        if response == "":
            continue
        elif response == "1":
            os.system("""say --rate=90  '%s'""" % word)
            continue
        elif response == "2":
            print("""
Answer: %s
Next (Enter), Retry (else)
----------------------------------
            """ % word)
            os.system("""say '%s'""" % word)
            option_response = input()
            if option_response:
                continue
            wrong += 1
            lastspell = False
            break
        elif response == "9":
            list_to_file(learned_words, 'learned_words.txt')
            os.system("""say 'Good bye, come again'""")
            exit("Saved and Exited")
        else:
            error = lev_distance(word, response)
            if error == 0:
                lastspell = ""
                if correct_in_first_try:
                    learned_words.append(word)
                print("""
Correct!
----------------------------------
                """)
                os.system("""say 'thats Correct'""")
                correct += 1
                lastspell = False
            else:
                correct_in_first_try = False
                os.system("""say 'you wrote, %s'""" % response)
                lastspell = "%s, Error:%s" % (response, error)
                continue
        break



