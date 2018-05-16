"""
    Basic neural network lifted from : (and makde into python3)
    https://iamtrask.github.io/2015/07/12/basic-python-network/

    Ordered by SPICYNESS

    Challenge 1 : Bell Pepper
        Change names of variables to more understandable ones (for you)

    Challenge 2 : Banana Pepper
        Change the test data (at the way bottom) to explore how well the
        network is trained

    Challenge 3 : Jalapeno
        Modify the number of training iterations to make the network better

    Challenge 4 : Cayenne pepper
        Add data to the network, by some pattern of your own choice, to make
        it classify that pattern

    Challenge 5 : Habanero
        Replace the nonlin function's "sigmoid" expressions with "tanh",
        which is the nonlinearity closer associated with human brain's
        activations:
                        replace sigmoid with:
                            (np.tanh(x) + 1)/2
                        the derivative is:
                            (1/2)*(1 - np.tanh(x) ** 2)

    Challenge 6 : Red Savina pepper
        Make a comparison of the sigmod and tanh activation "nonlin" functions.
        Which one works better for this kind of pattern?
        What about another pattern?

    Challenge 7 : Carolina Reaper
        Add another layer to the network (would be l2) by following the pattern
        of how l1 is connected to l0

"""
import numpy as np

# input dataset
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])

# output dataset
y = np.array([[0,0,1,1]]).T

# sigmoid "squishification" function
def nonlin(x, deriv=False):

    if (deriv == True):
        return x*(1-x)
    else:
        return 1/(1+np.exp(-x))


# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((X.shape[1],1)) - 1

# training
for iter in range(10000):

    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    # how much did we miss?
    l1_error = y - l1

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1, deriv = True)

    # update weights
    syn0 += np.dot(l0.T,l1_delta)

print("Output After Training:")
print(l1)

print("Test After Training")
# test dataset
T = np.array([  [0,0,0],
                [1,0,0],
                [1,0,1],
                [1,1,1],
                [0,0,1] ])
l0 = T
l1 = nonlin(np.dot(l0,syn0))
print(l1)
