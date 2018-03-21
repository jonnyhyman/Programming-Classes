''' This is a reliable*** chatbot in a dense amount of code

    HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!

        YOUR CHALLENGES...

        IF YOU CHOOSE TO ACCEPT THEM:


            1. Make 3 more scripted responses and test that they work

            2. Make a special set of responses for when there is very
                little similarity. Things like "What?", "Uhh, riiiight..."

                HINTS: Make a new list, and use random.choice() on it
                        if best_similarity < some smallish number (like 0.5)

'''

responses = {

        # user typed : reponse string
        # LOWER CASE  :  ANY CASE
        'your name'   : 'My name is Python, duh! Yours?',
        'how are you' : 'Great, how are you?',
        'stupid'      : 'Stupid is as stupid does.',
        'smart'       : 'Intelligence is in the eye of the beholder',
        'weird'       : 'Yeah.. Weird things are weird. You know?',
        'i know'      : "I thought so",
        'stop'        : "Why?",
        'Haha'        : "Haha I know right?",

}

# in case you forgot to type the keys (prompts) as all lower case

for key in dict(responses):
    if key != key.lower():  # if some upper case characters

        # Add an extra entry with all lower case characters in prompt
        responses[key.lower()] = responses[key]


'''-------------------------------- SIDE NOTE -------------------------------'''

''' *** In order to be reliable (allow typos), we can use "difflib" ! '''


import difflib

a = 'jonny is a cool dude'  # make a string
b = 'j;nmy is a cewl dood'  # make another, similar-ish

# Calculate the percent similarity between them!
similarity = difflib.SequenceMatcher(None, a, b).ratio()
print(similarity)  # will be 0.7 or 70 % similar

'''-------------------------------- ANYWAY --------------------------------'''

say_next = "Hi! How are you?  >> "

while True: # FOREVER (until we quit)

    text = input(say_next)
    text = text.lower()  # make lowercase

    # Now go through the response dictionary and get the most similar input

    best_prompt = ''  # I don't know yet, so make empty
    best_similarity = 0  # I don't know yet, so make 0

    for prompt, response in responses.items():

        similarity = difflib.SequenceMatcher(None, text, prompt).ratio()

        if similarity > best_similarity:
            best_similarity = similarity
            best_prompt = prompt

    # Once we're done checking the entire responses list, SPEAK!!

    say_next = responses[best_prompt] + '  >> '  # arrows to make clean print
