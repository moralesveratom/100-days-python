print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lowered = name1.lower()
name2_lowered = name2.lower()


def search_count(person_name1, person_name2):
    t = person_name1.count("t")
    r = person_name1.count("r")
    u = person_name1.count("u")
    e = person_name1.count("e")

    t2 = person_name2.count("t")
    r2 = person_name2.count("r")
    u2 = person_name2.count("u")
    e2 = person_name2.count("e")

    total_true = t + r + u + e + t2 + r2 + u2 + e2

    l = person_name1.count("l")
    o = person_name1.count("o")
    v = person_name1.count("v")
    e = person_name1.count("e")

    l2 = person_name2.count("l")
    o2 = person_name2.count("o")
    v2 = person_name2.count("v")
    e2 = person_name2.count("e")

    total_love = l + o + v + e + l2 + o2 + v2 + e2

    parsed = str(total_true) + str(total_love)
    return int(parsed)


function = search_count(name1_lowered, name2_lowered)

if function < 10 or function > 90:
    print(f"Your score is {function}, you go together like coke and mentos.")

elif function >= 40 and function <= 50:
    print(f"Your score is {function}, you are alright together.")

else:
    print(f"Your score is {function}.")
