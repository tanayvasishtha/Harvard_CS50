greeting=input("your greet: ")
new_greeting=greeting.lower().strip()

if 'hello' in new_greeting:
    print("$0")
elif new_greeting[0]=="h" :
    print("$20")
else:
    print("$100")
