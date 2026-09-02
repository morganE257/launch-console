print("Welcome to the Launch Console!")

name = 'Morgan'
print("Hi, " + name + "!")

menu = ["About me", "My goals", "Exit"]
print(len(menu))

def about_me(name):
    return "My name is " + name + "."
    pass

print(about_me("Ada"))

choice = "3"
if choice == "3":
    print("Goodbye!")

running = True
while running:
    print("running...")
    running = False

def mystery(words):
    out = ""
    for w in words:
        out = out + w[0]
    return out
print(mystery(["Grit", "Impact", "Trust"]))