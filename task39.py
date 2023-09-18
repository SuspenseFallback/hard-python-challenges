console = input("Do you play games on your console? (y/n) ").lower()
pc = input("Do you play games on your PC? (y/n) ").lower()

if pc == "y" and console == "y":
    print("Game master")
elif pc == "y":
    print("PC master")
elif console == "y":
    print("Console master")
else:
    print("Error")
