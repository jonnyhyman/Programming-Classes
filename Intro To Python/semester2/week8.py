"""
    SOME CORE CONCEPTS IN PYTHON worth going over

    - Lists, Tuples
    - Dictionaries
    - "Iterables"
    - Iterable manipulation tools:
        ''.join()
        += 's' or []
        dictionary['key'] = blah
        .append, .extend

    - Writing functions from scratch:
        Arguments
        Keyword / Optional Arguments
        Return values
        Multiple return values
        Capturing ALL inputs
        Capturing ALL keyword inputss
"""
Ateam = ['this', 'list', 0, 1343.21341234,]
Bteam = ('between','these','two')

MerriamWebster = {  'lamp' : ['A lamp is a bright object that I love'],
                    'beef' : ["A beef is when you don't like someone"]}

MerriamWebster['amp'] = 'Not a lamp'

name = 'jonny'

#for letter in name:
#    print(letter)

for thing, otherthing in MerriamWebster.items():
    print(thing, otherthing)

"""
''.join()
+= 's' or []
dictionary['key'] = blah
.append, .extend
"""
listofstring = [letter for letter in name]
#print(listofstring)
#print("".join(listofstring))

name += ' hyman'
#name = name + ' hyman'


imageformats = ['.png', '.jpg']
imageformats.append('.psd')
imageformats.extend(['.jpeg','.pixar'])

#print(imageformats + ['.tiff'])
""""
    - Writing functions from scratch:
        Arguments
        Keyword / Optional Arguments
        Return values
        Multiple return values
        Capturing ALL inputs
        Capturing ALL keyword inputss
"""
#---------------------------------------

x, y = 0,0

def direction(input_key, a, b, speed = 5):
    """ Update position by arrow key

        input: input_key(str)
        output: x,y (float)
    """

    if input_key == 'w':
        b -= speed

    elif input_key == 's':
        b += speed

    elif input_key == 'd':
        a += speed

    elif input_key == 'a':
        a -= speed

    return a, b

def function(*args, **kwargs):

    args[0]
    args[1]

    kwargs['IDONTKNOW']

    print('ALL ARGS:', args)
    print('ALL KWARGS:', kwargs)

print(direction('w', x, y, speed=100))
print(type(direction('w', x, y, speed=100)))

function('a whole bunch', 'of random stuff', IDONTKNOW='Yeah, right?')

#timer = Timer(timeout=1/60)
#timer.connect(direction)
