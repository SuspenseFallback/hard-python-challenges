is_open = input("Is wzzap market open? (y/n) ").lower()
is_open = True if is_open == "y" else False

if is_open:
    for i in range(5):
        print("Can I get a face mask please")
else:
    for i in range(100):
        print("I need to stay at home!")
