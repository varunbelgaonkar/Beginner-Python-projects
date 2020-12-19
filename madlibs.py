#string concatenation -- joining two or more string together
#name = "varun" # some string variable
# a few ways to do this
#print("hello my name is "+ name)
#print("hello my name is {}".format(name))
#print(f"hello my name is {name}")

animal = input("animal: ")
food = input("food: ")
noun1 = input("noun1: ")
verb1 = input("verb1: ")
verb2 = input("verb2: ")
verb3 = input("verb3: ")
verb4 = input("verb4: ")
noun2 = input("noun2: ")
location = input("location: ")
noun3 = input("noun3: ")
noun4 = input("noun4: ")


madlib = f"If you give {animal} a {food}, he/she is going to ask for a {noun1}.\
    When you give him/her the {noun1}, he/she will want to {verb1}.\
        When he/she is finished, he/she will {verb2}.\
            Then he/she will {verb3} and {verb4} to the {noun2}.\
                Since that doesn't work out, he/she will want to go to {location}.\
                    On the way, he/she will see a {noun3} and will want {noun4}.\"

print(madlib)
    
    
    
    