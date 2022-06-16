import datetime
class Person:
    def __init__(self,name,byear,gender):
        self.name = name;
        self.byear = byear;
        self.gender = gender;
    def GetAge(self):
        self.age=datetime.datetime.now().year - self.byear;
        return self.age;
    def __str__(self):
        return 'Name: {}/ Age: {}/ Gender: {}'.format(self.name,self.age,self.gender);
p1 = Person('Kailash', 1996, 'M')
p1.GetAge()
print(p1)
