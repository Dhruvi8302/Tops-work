#How will you set the starting value in generating random numbers? 
        #starting value for generating random numbers in Python by using the seed() function from the random module.

import random
random.seed(95)  # Set starting (seed) value
print(random.randint(0,100))
