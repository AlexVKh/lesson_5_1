class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors:
            for i in range(int(new_floor)):
                print(i+1)
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
h3 = House('ЖК Этажи', 25)
h3.go_to(0)

