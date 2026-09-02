print("Welcome to the Launch Console!")
name = input("What is your name? ")
print("Lovely to meet you, " + name + ".")

running = True
while running:
    print("1) About Me")
    print("2) My Goals")
    print("3) Exit")
    print("4) Fun Fact!")
    choice = input("Please pick 1, 2, 3, or 4 ")
    if choice == '1':
        print("My name is Morgan, and I am 16 years old")
    elif choice == '2':
        print("I plan to, at the least, get a Bachelors of Science of Computer Science")
    elif choice == '3':
        print("Goodbye!")
        running = False
    elif choice == '4':
        print("I love to sew, and I also weld.")
    else:
        print("Please pick 1, 2, 3, or 4.")
    
