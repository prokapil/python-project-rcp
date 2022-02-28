import random
user = input("choose rock,paper or scissor: ")
com = random.choice(['r','p','s'])

if com == "r" and  user == "r":
    print("Draw")
elif com == "r" and user == "p":
    print("user win")
elif com == "r" and user == "s":
    print("com win")
elif com == "p" and user == "r":
    print("com win")
elif com == "p" and user == "p":
    print("Draw")
elif com == "p" and user == "s":
    print("user win")
elif com == "s" and user == "r":
    print("user win")
elif com == "s" and user == "p":
    print("com win")
elif com == "s" and user == "s":
    print("Draw")
else:
    print("enter correct value")
print(com)




