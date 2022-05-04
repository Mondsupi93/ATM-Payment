from unicodedata import name

print('*** Welcome*** ')
print('This is a Payment Program')


name= ''
cardlist = []
passlist = []
phonelist = []
cardchargelist = []
phonechargelist = []

def main_menu():
    print('\n ******* Main Menu ******* : ')
    print('1. Register New Card')
    print('2. Charge Your Phone')
    print('3. Account Balance')
    print('4. Pay to other Card')
    print('5. Exit')
    print('')
    return(input('Choose one option : '))

def RegisterCard():
    cname = input('   Name :  ')
    cnum = input('   Card Number :   ' )
    cpass = input('    Password :    ')
    cphone = input('   Phone Number :     ')
    ccharge = 100000
    phcharge = 0
    return ([cname, cnum, cpass, cphone, ccharge, phcharge])

def chargephone():
    phnum = input('    Phone Number :    ')
    amount = input('   Amount of Charge :    ')
   
    if phnum not in phonelist:
        phonelist.append(phnum)
        phonechargelist.append(0)
    phindex = phonelist.index(phnum)
    cardno = input('    Your Card Number :    ')
    cardpass = input('    Your Card Password :    ')
    
    if cardno in cardlist:
        cardindex = cardlist.index(cardno)
       
        if cardpass == passlist[cardindex]:
           
            if cardchargelist[cardindex] > amount :
                cardchargelist[cardindex] -= amount
                phonechargelist[phindex] += amount
                print('Phone Number :', phnum, 'has been Charged')
                print('Charge of Phone Number : ', phnum, 'is now :', phonechargelist[phindex])
                print('Account balance for Card Number :', cardno, 'is now :', cardchargelist[cardindex])
                return True
           
            else:
                print('Your account balance is less than amount')
                print('1. Try again')
                print('2. Main Menu')
                nn = input('Choose one option :')
                
                if nn == 1 :
                    return False
               
                else:
                    return True
      
       
        else:
            print('Password is not correct')
            print('1. Try again')
            print('2. Main Menu')
            nn = input('Choose one option :')
           
            if nn == 1 :
                return False
            
            else:
                return True
    
    
    else:
        print('Card is not registered, Pleaseregister your card first')
        print('1. Try again')
        print('2. Main Menu')
        nn = input('Choose one option :')
        
        if nn == 1 :
            return False
       
        else:
            return True


def Accountbalance():
    cardno = input('Your card number : ')
    cardpass = input('Your card password : ')
    
    if cardno in cardlist:
        cardindex = cardlist.index(cardno)
        
        if cardpass == cardlist[cardindex]:
            print('Account balance for card number : ', cardno, 'is', cardchargelist[cardindex])
       
        else: print('Password is not correct!')

    else:
        print('Card is not registered, please register your card first!')

def Paytocard():
    scard = input('Main card number :')
    dcard = input('Destinition card number :')
    spass = input('Main card password :')
    amount = int(input('Amount of Money do you want to transfer :'))

    if scard in cardlist:
        index_s = cardlist.index(scard)
        if passlist[index_s] == spass:
            if dcard in cardlist:
                index_d = cardlist.index(dcard)
                if cardchargelist[index_s] > amount :
                    cardchargelist[index_s] -= amount
                    cardchargelist[index_d] += amount
                    print('Tranfer from',scard, 'to', dcard,'has been done!')
                    return True
                else:
                    print('Account balance is not enough')
                    print('1. Try again')
                    print('2. Main Menu')
                    nn = input('Choose one option')
                    if nn == '1':
                        return False
                    else:
                        return True
            
            else:
                print('Destination card is not registered!')
                print('1. Try again')
                print('2. Main Menu')
                nn = input('Choose one option')
                if nn == '1':
                    return False
                else:
                    return True
        
        else:
            print('Password is not correct')
            print('1. Try again')
            print('2. Main Menu')
            nn = input('Choose one option')
            if nn == '1':
                return False
            else:
                return True

    else:
        print('Main card is not registered!')
        print('1. Try again')
        print('2. Main Menu')
        nn = input('Choose one option')
        if nn == '1':
            return False
        else:
            return True


mm =0
mm = main_menu()
while mm != '5':
    
    if mm == '1' :
        newcard = RegisterCard()
        cardlist.append(newcard[1])
        passlist.append(newcard[2])
        phonelist.append(newcard[3])
        cardchargelist.append(newcard[4])
        phonechargelist.append(newcard[5])
        print('Card', newcard[1], 'has been registered')
        mm = main_menu()
    
    elif mm == '2':
        must_try = chargephone()
        while not must_try:
            must_try = chargephone()
        mm = main_menu()

    elif mm == '3':
        Accountbalance()
        mm = main_menu()

    elif mm == '4':
        must_try = Paytocard()
        while not must_try:
            must_try = Paytocard()
        mm = main_menu()


print('\n Thanks alot for using payment')