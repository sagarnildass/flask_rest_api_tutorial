lottery_player_dict = {
    'name':'Sagar',
    'numbers': (5, 9, 12, 3, 1, 21)
}

'''
class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer('Sagar')
player_two = LotteryPlayer('Ranjan')
player_one.numbers = (1,2,3,4,5)

print(player_one.name)
print(player_two.name)
print(player_one.numbers)
print(player_two.numbers)
print(player_one.total())
print(player_two.total())
'''
###

'''class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    #def go_to_school(self):
    #    print('I went to {}'.format(self.school))

    #If we want to make a function which does the same thing for every student, we make it a staticmethod
    @staticmethod
    def go_to_school():
        print('I am going to school.')

sagar = Student('Sagar', 'JU')
sagar.marks.append(90)
sagar.marks.append(80)
print(sagar.marks)
print(sagar.average())
#sagar.go_to_school()

#for static method, we can directly call the class
Student.go_to_school()
'''


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"

        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))


store = Store('Amazon')
store.add_item('keyboard', 160)
store.add_item('mouse', 50)
#static method
print(Store.store_details(store))
store_with_new_name = Store.franchise(store)
#class method
print(store_with_new_name.name)
