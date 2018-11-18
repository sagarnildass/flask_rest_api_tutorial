#list comprehension is building a modified list by iterating over the older list

multiply_list = [x * 3 for x in range(5)]
print(multiply_list)

#print even numbers
print([n for n in range(10) if n % 2 == 0])

#string
people_you_know = ['RANJAN', 'Rebecca', ' sagar']
normalised_people = [person.strip().lower() for person in people_you_know]
print(normalised_people)
