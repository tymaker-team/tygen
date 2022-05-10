print("This is tygen. By GitHub/aarikpokras.")
one = input("Who are you writing to? ")
two = input("What gift did you get from " + one + "? e.g.: 'shirt' ")
three = input("What kind of party did " + one + " go to? (No connectors, just noun) ex: 'birthday' ")
four = input("What is your name? ")
five = input("What is this person to you? Friend, parent...) No connectors. ")
six = input("How would you describe this " + five + "? Include a/an. ex: 'a cool' ")
seven = input("What do you like doing with " + one + "? ex: reading books: ")
print("Here is your letter so far.")
print("Dear " + one + ", thank you so much for getting me my " + two + "! Thank you for coming to my " + three + ". I enjoy " + seven + " with you. You are " + six + " " + five + "! From, " + four)
con_one = input("If you like your letter so far, type y. If not, type n. To exit, type e. ")
if con_one == "y":
  print("Dear " + one + ", thank you so much for getting me my " + two + "! Thank you for coming to my " + three + ". I enjoy " + seven + " with you. You are " + six + " " + five + "! From, " + four)
if con_one == "n":
  print("Sorry you don't like it, but I can't do anything about it.")
if con_one == "e":
  print("Exiting.")