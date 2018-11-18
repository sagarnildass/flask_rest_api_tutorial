#Here we are passing another function as input
def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

#print(methodception(add_two_numbers))

#We can also pass lambda/anoynymous functions
#print(methodception(lambda: 35 + 77))

my_list = [13, 56, 77, 484]
#get rid of 13
print(list(filter(lambda x: x != 13, my_list)))

#understanding lambda functions

(lambda x: x * 3)(5)

#this is same as;

def f(x):
    return x * 3

f(5)
