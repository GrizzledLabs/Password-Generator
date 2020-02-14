import random
import string

# Welcome message
print('Welcome to Password Generator by Grizzled Labs\nThis tool creates passwords with your choice of length and security.\n')
# Replay prepper
replay = 'Y'
while replay == 'Y':

# Security Selector
    print('Choose level of security.\nLow: i2sws86r5o\nMed: TxCzm98k4C\nHigh: t2$pz#E!*L')
    security = None
    security = input('Level of security? Low/Med/High:  ').upper()
    while security not in ('LOW', 'MED', 'HIGH'):
      security = input('Invalid choice\nLevel of security? Low/Med/High:  ').upper()

# Low Security Generator
    if security == 'LOW':
      howmanystr = input('How many characters?  ')
      howmany = int(howmanystr)
      for password in range(3):
        password = ''.join(str(random.choice(string.ascii_lowercase + string.digits)) for i in range(howmany))
        print(password)

# Med Security Generator
    elif security == 'MED':
      howmanystr = input('How many characters?  ')
      howmany = int(howmanystr)
      for password in range(3):
        password = ''.join(str(random.choice(string.ascii_letters + string.digits)) for i in range(howmany))
        print(password)

# High Security Generator
    elif security == 'HIGH':
      howmanystr = input('How many characters?  ')
      howmany = int(howmanystr)
      for password in range(3):
        password = ''.join(str(random.choice(string.ascii_letters + '####$$$$%%%%&&&&****!!!!????' + string.digits)) for i in range(howmany))
        print(password)        

# Replay Trigger
    replay = input('Try again?? Y/N  ').upper()
    while replay not in ('Y', 'N'):
      replay = input('Try again?? Y/N  ').upper()
    
# Exit Message
print('\nThanks for using Password Generator by Grizzled Labs!')