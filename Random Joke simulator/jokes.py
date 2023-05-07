import random

# Jokes and corresponding answers as strings
joke_1 = 'What’s the best thing about Switzerland?'
joke_1a = 'I don’t know, but the flag is a big plus.'

joke_2 = 'I invented a new word!'
joke_2a = 'Plagiarism!'

joke_3 = 'Did you hear about the mathematician who’s afraid of negative numbers?'
joke_3a = 'He’ll stop at nothing to avoid them.'

joke_4 = 'Hear about the new restaurant called Karma?'
joke_4a = 'There’s no menu: You get what you deserve'

joke_5 = 'Did you hear about the actor who fell through the floorboards?'
joke_5a = 'He was just going through a stage.'

joke_6 = 'Did you hear about the claustrophobic astronaut?'
joke_6a = 'He just needed a little space'

joke_7 = 'Why don’t scientists trust atoms?'
joke_7a = 'Because they make up everything'

joke_8 = 'Where are average things manufactured?'
joke_8a = 'The satisfactory'

joke_9 = 'How do you drown a hipster?'
joke_9a = 'Throw him in the mainstream.'

joke_10 = 'What sits at the bottom of the sea and twitches?'
joke_10a = 'A nervous wreck.'

joke_11 = 'What does a nosy pepper do?'
joke_11a = 'Gets jalapeño business!'

joke_12 = 'How does Moses make tea?'
joke_12a = 'He brews.'

joke_13 = 'Why can’t you explain puns to kleptomaniacs?'
joke_13a = 'They always take things literally.'

joke_14 = 'How do you keep a bagel from getting away?'
joke_14a = 'Put lox on it.'

joke_15 = 'A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”'
joke_15a = 'The doctor replies, “Sorry, I don’t follow you …'


# Dictionary for jokes corresponding to a specific key
jokes_dict = {  '1': joke_1,
                '2': joke_2,
                '3': joke_3,
                '4': joke_4,
                '5': joke_5,
                '6': joke_6,
                '7': joke_7,
                '8': joke_8,
                '9': joke_9,
                '10': joke_10,
                '11': joke_11,
                '12': joke_12,
                '13': joke_13,
                '14': joke_14,
                '15': joke_15 }

# Dictionary of answers corresponding to same key as the joke dictionary..
#..ie. Key 1 - Joke 1 in jokes dictionary corresponds with key 1 - answer 1 to joke in answers dictionary
answers_dict = {'1': joke_1a,
                '2': joke_2a,
                '3': joke_3a,
                '4': joke_4a,
                '5': joke_5a,
                '6': joke_6a,
                '7': joke_7a,
                '8': joke_8a,
                '9': joke_9a,
                '10': joke_10a,
                '11': joke_11a,
                '12': joke_12a,
                '13': joke_13a,
                '14': joke_14a,
                '15': joke_15a }


print("Please enter y or n, for yes or no!")

print(" ")

user_input = str(input("Would you like to hear a joke, y (yes) or n (no)?: ")).lower()

print(" ")

# While loop for simulating a random joke
# Loop goes through keys in jokes_dictionary and radomly selects one, printing out the joke
# loop goes to answers_dict and picks the answer matching the same key
while True:
    if user_input == 'y':
        key, value = random.choice(list(jokes_dict.items()))
        print(value)
        user_input_2 = str(input("See answer (type y)? (y): ")).lower()
        print(" ")
        if user_input_2 == 'y':

            # creates a temporary store for the random key generated
            temp_val = key

            # Uses the same random key to access the value (answer) for the same question.
            print(answers_dict.get(temp_val))

            print(" ")
    elif user_input == 'n':
            print("I guess you dont like jokes!")
            break