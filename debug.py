import logging
logging.basicConfig(level=logging.INFO,filename="ksk.log",filemode="w")
class gym:
    def __init__(self,name,training,fee,location):
        self.name = name;
        self.training = training;
        self.fee = fee;
        self.location = location;
        try:
            if (fee is not int): print(" You have entered a int value ")
            else: self.fee=fee
        except Exception as b:
            logging.error("Sorry, try again.", exc_info=True)
            print("Please enter an integer")
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
fee = input("Please enter the fee of ur gym: ")
p3 = gym("Vk", "weights", fee, "Toronto")