amountdue= 50
changeowed= 0

while amountdue > 0:
    print("Amount Due:",amountdue)

    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5 :
        amountdue = amountdue - coin

    if amountdue <= 0:
        changeowed -= amountdue
        print("Change Owed:",changeowed)

