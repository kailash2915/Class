#import threading, random, time
#def threadex():pass
#for i in range(5):

# class student:
#     def __init__(self,name,birthyear):
#         self.nme=name
#         self.byear=birthyear
#     def prininfo(self):
#         print('Name: {}, Birthyear: {}'. format(self.nme,self.byear))
# p1=student("kailash",1996)
# print(p1)
# p1.birthyear=1996
# p1.name="Kailash"
from datetime import date
class movie:
    def __init__(self,name,yearreleased,director,rating):
        self.nme=name
        self.year=yearreleased
        self.dir=director
        self.rate=rating
    def print1(self):
        print("The name of the movie is {} and the year of release is {} and the director is {} and the rating will be {}". format(self.nme,self.year,self.dir,self.rate))
    def rating(self):
        if self.rate==5:
            print("The movie is great")
        else: print("Average")
    def compare(self):
        ks=date.today().year-self.year
        if ks>20 and self.rate>5: print("Old is good movie")
    @classmethod
    def movieLanguage(cls):
        lang = "Tamil"
        return cls(lang)
p1=movie("Baahubali",2019,"Rajmouli",5)
p1.print1()
p2=movie("Billa",1987,"Rajamouli",7)
p2.print1()
p2.compare()
movie.movieLanguage()
print(p2)