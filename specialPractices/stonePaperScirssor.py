#Stone Paper scrissor game
import random
list = ['stone','paper','scissor']
comp = random.choice(list)
print("1 for stone, 2 for paper , 3 for scissor")
user = int(input('Enter your move:')) 

if(user == 1):
    input = 'stone'
elif(user == 2):
    input = 'paper'
else:
    input = 'scissor'
    
print('you : ',input,'\ncomp : ',comp)

def check(comp,input):
    if(comp == input):
        return print('draw')
    if(comp == 'stone' and input == 'scissor'):
        return print('lost')
    if(comp == 'paper' and input == 'stone'):
        return print('lost')
    if(comp == 'scissor' and input == 'paper'):
        return print('lost')
    return print('won')
check(comp,input)
if(comp == 'paper' and user == 'scissor'):
    print('won')
if(comp == 'scissor' and user == 'stone'):
    print('won')
if(comp == 'stone' and user == 'paper'):
    print('won')