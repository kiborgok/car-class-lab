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