## Python program for discount system 

print("WELCOME TO BT21 STORE")
print("We have the following items in three size; 1. Small 2. Medium 3. Large")
print("1. BT21 Plushie. 2. BTS Stickers. 3. BTS Photocards. 4. BTS Blanket. 5. BTS Posters ")
pro= (input("Please enter the name of the desired product(in the same manner as written above):  "))
siz= (input("Please enter the name of the desired size:  "))
quan= int(input("Please enter the quantity:  "))

def order(prod,size, quant):
    print("You have ordered: ", prod)
    print("In the size: ",size)
    print("No of item: ",quant)

order(pro,siz,quan)

def bill(prod, size, quant):
    if prod=='BT21 Plushie' and size.lower() =='small':
        price= 2100
        tot_price= price*quant
        print("Your bill is: ", tot_price)
    
    elif prod=='BT21 Plushie' and size.lower()=='medium':
        price= 3300
        tot_price= price*quant
        print("Your bill is: ", tot_price)
    
    elif prod=='BT21 Plushie' and size.lower()=='large':
        price= 4200
        tot_price= price*quant
        print("Your bill is: ", tot_price)
    
    elif prod=='BTS Sticker' and size.lower()=='small':
        price= 200
        tot_price= price*quant
        print("Your bill is: ", tot_price)
    
    elif prod=='BTS Sticker' and size.lower()=='medium':
        price= 350
        tot_price= price*quant
        print("Your bill is: ", tot_price)
    
    elif prod=='BTS Sticker' and size.lower()=='large':
        price= 500
        tot_price= price*quant
        print("Your bill is: ", tot_price)

    elif prod=='BTS Photocard' and size.lower()=='small':
        price= 500
        tot_price= price*quant
        print("Your bill is: ", tot_price)

    elif prod=='BTS Photocard' and size.lower()=='medium':
        price= 700
        tot_price= price*quant
        print("Your bill is: ", tot_price)

    elif prod=='BTS Photocard' and size.lower()=='large':
        price= 900
        tot_price= price*quant
        print("Your bill is: ", tot_price)

    elif prod=='BTS Blanket' and size.lower()=='small':
        price= 2000
        tot_price= price*quant
        print("Your bill is: ", tot_price)

    elif prod=='BTS Blanket' and size.lower()=='medium':
        price= 3500
        tot_price= price*quant
        print("Your bill is: ", tot_price)
    
    elif prod=='BTS Blanket' and size.lower()=='large':
        price= 5000
        tot_price= price*quant
        print("Your bill is: ", tot_price)
    
    elif prod=='BTS Poster' and size.lower()=='small':
        price= 750
        tot_price=price*quant
        print("Your bill is: ", tot_price)
    
    elif prod=='BTS Poster' and size.lower()=='medium':
        price= 1000
        tot_price=price*quant
        print("Your bill is: ", tot_price)
    
    elif prod=='BTS Poster' and size.lower()=='large':
        price=1300
        tot_price=price*quant
        print("Your bill is: ", tot_price)

    else: 
        print("You have entered a wrong product")

bill(pro,siz,quan)

total= int(input("Please enter the total amount of bill:  "))

def dis(total_pri):
    if total_pri > 5000:
        dis=total_pri*25/100
        print("You have availed discount of:  ", dis)

    elif total_pri >= 2500:
        dis= total_pri*15/100
        print("You have availed discount of:  ", dis)

    else:
        print("No discount availed")

dis(total)

print("Thank you for shopping with us!")

