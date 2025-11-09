#head tail game
import random
u = 0
c = 0
while True :
    you = input("Enter one of them (h , t ) and ( e ) for end : ").lower()
    your = {"h" : 0 , "t" : 1}
    choice = ["HEAD","TAIL"]
    if you == 'e' :
        break
    if you not in your :
        you = input("Plz enter one of them (h , t ) and ( e ) for end : ").lower()
    else :
        your_choice = your[you]
        coin_drop = random.randint(0,1)
        print(f"You chose : {choice[your_choice]}")
        print(f"Coin drop  : {choice[coin_drop]}")

        if your_choice == coin_drop :
            print("YOU WON \n")
            u += 1
        else :
            print("COMPUTER WON \n")
            c += 1

print("\n--- FINAL SCORE ---\n")
print("Your score:", u)
print("Computer score:", c)

if u > c:
    print(" YOU WON THE TOURNAMENT!")
elif u < c:
    print(" COMPUTER WON THE TOURNAMENT!")
else:
    print(" IT'S A TIE!")