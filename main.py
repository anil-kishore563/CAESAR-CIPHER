from replit import clear
clear
import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

looping=True
while looping:
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    print()
    while not direction=='encode' and not direction =='decode':
          print("What the heck you just typed,It's invalid.Type again")
          direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    print()
    shift = int(input("Type the shift number:\n"))
    print()
    def ceasar(direction,text,shift):
        new_list=[]
        text_list=[]
        new_alphabet=[]
        shift=shift % 26
        if direction=='encode':         
          new_alphabet+=(alphabet[shift:])
          new_alphabet+=(alphabet[:shift])
        else: 
          new_alphabet+=(alphabet[-shift:])
          new_alphabet+=(alphabet[:26-shift]) 

        for i in text:
          text_list.append(i)
        for i in text_list:  
            if i in alphabet :
                index=alphabet.index(i)     
                new_list.append(new_alphabet[index])
            else:
                new_list.append(i)   
        print(f"Your {direction}d message is {''.join(new_list)}")
        print()

    ceasar(direction,text,shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    while not restart=='yes' and not restart=='no':
        print("What the heck you just typed,It's invalid.Type again")
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        print()

    if restart=='yes':
        looping=True
        clear()
    else:
        clear()
        looping=False
        print('Good Bye')
                
    


        