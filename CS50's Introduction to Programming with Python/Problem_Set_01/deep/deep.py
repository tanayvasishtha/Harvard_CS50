answer= input("What is the answer to the great question of life, the Universe and everything? ")

if answer.strip() == "42":
    print("Yes")
elif answer.lower().strip()=="forty-two":
    print("Yes")
elif answer.lower().strip()=="forty two":
    print("Yes")
else:
    print("No")
