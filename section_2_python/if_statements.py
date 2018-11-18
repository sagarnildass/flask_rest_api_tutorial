'''
known_people = ['sagar', 'rebecca', 'ranjan']

person = input('Enter the person you know: ')

if person in known_people:
    print("You know:{}".format(person))
else:
    print("{} is not in list!".format(person))
'''

def who_do_you_know():
    people = input("Enter the names of people you know, separated by commas: ")
    #people_list = people.split(",")
    #people_without_spaces = []

    #for person in people_list:
    #    people_without_spaces.append(person.strip())
    #return people_without_spaces

    #We could have also done this. But this makes the code ugly!
    #return [x.strip().lower() for x in input("Enter the names of people you know, separated by commas: ").split(",")]
    return [x.strip().lower() for x in people.split(",")]

def ask_user():
    person = input('Enter one person you know: ')
    if person.lower() in who_do_you_know():
        print("You know:{}".format(person.lower()))
    else:
        print("{} is not in list!".format(person.lower()))

ask_user()
