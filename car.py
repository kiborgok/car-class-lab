class Car:
    def __init__(self, name='General', model='GM', type='Benz', speed=0):
        self.name = name
        self.model = model
        self.type = type
        self.speed = speed

    def num_of_doors(self, doors = 2):
        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            result = doors
        else:
            result = doors + 2
        return result

    def num_of_wheels(self, wheels=4):
        if self.type == 'trailer':
            result = wheels + 4
        else:
            result = wheels
        return result

    def is_saloon(self):
        if self.type == 'trailer':
            return True
        else:
            self.type = 'saloon'
            return self.type

    def drive(self, m_speed):
        return m_speed

    def car_speed(self):
        moving_speed = self.drive(7)
        return moving_speed
    

if __name__ == '__main__':
    honda = Car()
    truck = Car('Truck', 'Isuzu', 'trailer')
    toyota = Car('Toyota', 'Cruiser')
    koenigsegg = Car('Koenigsegg', 'model 65')
    porshe = Car('Porshe', '911 Turbo')
    man = Car('MAN', 'Truck', 'trailer')

    print('######Wheels######')
    print(truck.num_of_wheels())
    print(toyota.num_of_wheels())

    print('######Doors######')
    print(truck.num_of_doors())
    print(porshe.num_of_doors())
    print(koenigsegg.num_of_doors())

    print('######saloon or trailer')
    print(porshe.is_saloon())
    print(man.speed)