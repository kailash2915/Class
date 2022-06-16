# #Timer function
# import threading;
# def func1(k):
#     print('Start',k);
# def func2():
#     print("Stop");
# print("Hello from function1");
# o1="Kailash";
# timer = threading.Timer(3,func1,args=(o1,));
# timer.start();
# timer2 = threading.Timer(5,func2);
# timer2.start();
# print("Hello from function2");
# o2 = "John";
# func1(o2);


# #try and except
# i = 0;
# while i!=2:
#     value = int(input("Enter a number: "))
#     try:
#         answer = value / 2;
#         print(answer)
#     except:
#         print("Enter a number and not any other datatype");
#     else:
#         print("Thanks for entering the correct value");
#     finally:
#         print("U have completed it");
class gym:
    def __init__(self,name,training,fee,location):
        self.name = name;
        self.training = training;
        self.fee = fee;
        self.location = location;
    def GetGymDetails(self):
        return ('name {} training: {}, fee: {}, location: {}'. format(self.name,self.training,self.fee,self.location))
p1 = gym("Fit4less", "weights", 56.5, "Toronto")
p1.GetGymDetails()
print(p1.GetGymDetails())
class member(gym):
    def __init__(self, name1, id, membership, time,name,training,fee,location):
        super().__init__(name, training, fee,location)
        self.name1 = name1;
        self.id = id;
        self.membership = membership;
        self.time = time;
    def GetMemberDetails(self):
        print('Name1: {}, id: {}, membership: {}, time: {}, name of ur gym: {}, training: {}, fee: {}, location: {}'. format(self.name1,self.id,self.membership,self.time,self.name,self.training,self.fee,self.location))
p2 = member("Kailash", 1634997, "Yearly", "24*7", "Fit4less", "weights", 56.5, "Toronto")
p2.GetMemberDetails()