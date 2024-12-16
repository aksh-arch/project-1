import random
computer = random.choice([1,-1,0])
youchoice=input('enter the choice')
youdict={'s':1, 'w':0, 'g':-1}
reversedict={1:'snake',0:'water',-1:'gun'}

you=youdict[youchoice]

print(f'you chose {reversedict[you]},\n computer chose {reversedict[computer]}')

if(computer==you):
    print('its a draw')
else:
    if(computer==1 and you==0):
        print('you win')
    elif(computer==0 and you==1):
        print('you lose')
    elif(computer==-1 and you==0):
        print('you win')
    elif(computer==0 and you==-1):
        print('you win')
    elif(computer==0 and you==1):
        print('you win')
    elif(computer==-1 and you==1):
        print('you win')

    else:
        print('something went wrong')