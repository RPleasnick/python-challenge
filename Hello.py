# This program says hello and asks for my name

print('Hello world!')

print('What is your name?') # ask for their name
myName=input()
print('It is good to meet you, '+myName)
print('The length of yur name is:')
print(len(myName))

print('What is your age?') # ask for their age
myAge=input()
print('You will be ' + str(int(myAge)+1)+' in a year.')

myrange=list(range(0,10,2))
type (myrange)
print ("range=",myrange)
print ("starting")
for i in ["a",4,68]:
    print ("I=",i)
