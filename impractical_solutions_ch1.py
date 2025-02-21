# Author: Sneaky Celery
# Inspired by: Lee Vaughan

'''This program contains interesting ways to interact with strings and completes all of the
   challenges introduced in IMPRACTICAL PYTHON PROJECTS, Chapter 1 (the ones where no solution
   was provided). I recommend researching API key management for yourself. I chose to use a free
   version from DeepL with specific limitations. You could create a .env file and use 'dotenv'
   from the Python libraries or use a cloud-based API key manager.'''

import random
import pprint
import sys
import re
import os
from collections import defaultdict
import pandas as pd
from tabulate import tabulate
import deepl

api_key = os.getenv("DEEPL_API_KEY")  # Retrieve API key from env variable

print("\n\n")

def pseudonym():
    '''This program will generate random pseudonyms for fun.
       My favorite: Bill 'Beenie-Weenie' Jingley-Schmidt'''

    print("\nWelcome to the Silly Name Generator.\n\n")

    first = ('Andy', 'Ben', 'Bobby', "Bill", "Bob", '"Big" Bowels', 'Boxelder', "Bud", 'Butterbean',
             'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 'Chewy', "Chiggers'n", 'Cinnabuns',
             'Cleetus', 'Cornbread', 'Craven', 'Crapps', 'Danny', 'Dennis', 'Dicman', 'Elphonso',
             'Choncy', 'Figgs', 'Foncy', 'Goosy', 'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious',
             'Jimbo', 'Joe', 'Johnny', 'Lemongrass', 'Lil Debil', 'Longbranch', 'Lenny',
             'Mergatroid', '"Mr Peabody"', 'Olive', 'Oinks', 'Old Scratch', '"Time-Out"',
             'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Punkin', 'Rock Candy', 'Schlomo',
             'Scratchensniff', 'Shanky', 'Sid', 'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki',
             'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky', 'Stowaway', 'Sweet Tea', 'Trenton',
             'Wheezy Joe', 'Winston', 'Wormywarts', 'Crazy')

    middle = ('"Baby Oil"', '"Bad News"', '"Big Burps"', 'Beenie-Weenie', 'Stinkbug', 'Lite',
              'Crab-Meat', '"Dark Skies"', 'Clawhammer', '"Rainy Day"', '"Mr. Man"', 'Pottin Soil',
              '"Lunch Money"', 'Oil-Can', '"The Squirts"', '"Stoner"', 'Trendy-Purse',
              '"Jazz Hands"', '"Fancypants"', 'Rook', 'Bishop', '"Cash-out"', 'Alexander', 'Marie',
              'Lawrence', 'Deputy', 'Tink', 'Golden Showers', 'Merryweather', '"The Sprinkles"')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout',
            'Butterbaugh', 'Clovenhoof', 'Clutterbuck', 'Cocktoasten', 'Endicoot', 'Fewhairs',
            'Gooberdapple', 'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
            'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
            'Kingfisher', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Morgan', 'Nettles',
            "Ol'Maurice", 'Outerbridge', 'Outty-Inny', 'Overtime', 'Oxhandler', 'Pumm',
            'Pennywhistle', 'Peterson', 'Pienuts', 'Pinkerton', 'Porkins', 'Putney', 'Quakenfork',
            'Rainwater', 'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splurm', 'Stevens',
            'Stroganoff', 'Sugar-Mama', 'Swackhamer', 'Tamwood', 'Tippins', 'Turnipseed',
            'Walkingstick', 'Wallflower', 'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth',
            'Wimplesnatch', 'Winkertorn', 'Woolysocks', 'Jones')

    def middle_probability(chance):
        '''Satisfies the 33-50% chance of a middle name occurring.'''
        middle_name = None # Hides the middle name option chance is in range and successful.
        if 0 <= chance <= 1:
            if random.random() < chance:
                middle_name = random.choice(middle)
        return middle_name

    while True:
        first_name = random.choice(first)
        middle_name = middle_probability(0.33) # chance = (0.33)
        last_name = random.choice(last)

        print("\n\n")
        if middle_name is not None:
            print(f"Pseudonym: {first_name} {middle_name} {last_name}")
        else: print(f"Pseudonym: {first_name} {last_name}")
        print("\n\n")

        new_pseudonym = input("Re-try? (Press 'Enter', else 'n' to quit) ")
        if new_pseudonym.lower() == 'n':
            break

def piglatin():
    '''This will automatically translate your words to piglatin!'''

    print("\nWelcome to the piglatin translator!\n")
    print("Type any word or phrase (letters only) or 'n' to exit:\n\n")

    while True:
        try:
            text = input("English phrase or 'n' to exit: ")
            if text.lower() == 'n':
                break
            if re.search(r"[^a-zA-Z\s]", text):
                print("Invalid input, use only letters and spaces.")
                continue
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        words = text.lower().split()
        piglatin_words = []

        for word in words:
            if word[0] in "aeiou":
                word = word[1:] + word[0] + 'way'
                piglatin_words.append(word)
            else:
                word = word[1:] + word[0] + 'ay'
                piglatin_words.append(word)

        print("\n\nPig Latin Translation: " + " ".join(piglatin_words))
        print("\n")

def bar_chart():
    '''Map letters from a string into a dictionary and
       print a bar chart of letter frequency.'''

    def translate_text(text, source_lang="EN", target_lang="ES"):
        '''DeepL translator function from English to Spanish.'''
        translator = deepl.Translator(api_key)
        try:
            result = translator.translate_text(text, source_lang=source_lang,
                                               target_lang=target_lang)
            return result.text
        except deepl.AuthorizationException:
            return "Translation error: Invalid API key."
        except deepl.ConnectionException:
            return "Translation error: Network connection issue."
        except deepl.DeepLException as e:
            return f"Translation error: {e}"  # Generic DeepL error

    while True:
        text = input("Type any sentence to see letter frequencies or 'n' to exit:\n\n")
        if text.lower() == 'n':
            break

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        translation_choice = input("Do you want to translate this to spanish first? y/n\n")
        if translation_choice.lower() == 'y':
            text = translate_text(text)
            alphabet = 'abcdefghijklmnñopqrstuvwxyz'
        else: print("Invalid input, please type: 'y' or 'n'\n")

        # Dictionary initiated to count letter occurrences
        mapped = defaultdict(lambda: (0, []))

        for character in text:
            character = character.lower()
            if character in alphabet:
                count, occurrences = mapped[character]
                mapped[character] = (count + 1, occurrences + [character])
        pprint.pprint(dict(mapped), width=110)
        print("\n\n")

def main():
    '''This is the menu to select from various silly-string programs.'''
    def center_table(df, width):
        '''This function creates a pretty table to display the menu in.'''
        table = tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False,
                         numalign='center', stralign='center')
        table_lines = table.split('\n')
        centered_table = [line.center(width) for line in table_lines]
        return '\n'.join(centered_table)

    while True:
        print("\n")
        menu = {
                'Input':['1', '2', '3', '4'],
                'Program':['Pseudonym Generator', 'Pig Latin Translator', "Eng->Esp Bar Chart",
                           'Exit']
                }
        menu_df = pd.DataFrame(menu)
        print(center_table(menu_df, 42))
        choice = input()
        if choice == '1':
            pseudonym()
        elif choice == '2':
            piglatin()
        elif choice == '3':
            bar_chart()
        elif choice == '4':
            sys.exit()
        else: print("Invalid input.")

if __name__ == "__main__":
    main()
