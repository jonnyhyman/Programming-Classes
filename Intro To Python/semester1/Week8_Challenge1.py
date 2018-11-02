''' This is a first name / last name dictionary & retrieval system

    Try this:

    1. Add your name
    2. Use the difflib tricks in Challenge0 to match SIMILAR names
                    (instead of exact names)
'''


database = {
    'Luke':'Skywalker',
    'Leia':'Skywalker',
    'Han':'Solo',
    'Chewie':'Chewbacca',
    'Finn':'FN-2187',
}

# in case you forgot to type the keys (prompts) as all lower case

for key in dict(database):
    if key != key.lower():  # if some upper case characters

        # Add an extra entry with all lower case characters in prompt
        database[key.lower()] = database[key]

def sorry():
    print('Sorry, no records found matching that name!')

while True:

    typ = input('Search By First Name or Last Name? (type "first" or "last") >> ')

    if typ.lower() == 'first':

        name = input('First Name? >> ')
        name = name.lower()

        if name in database.keys():
            print('Last Name Is', database[name])
        else:
            sorry()

    elif typ.lower() == 'last':

        name = input('Last Name? >> ')
        name = name.lower()

        if name in database.values():

            for first, last in database.items():
                if last == name:
                    print('First Name Is', first)
                    break # quit this for loop
        else:
            sorry()
