# hello = "k" * 11
# print(hello)
# import random
# randoma = random.randint(1,200)
# print(randoma)
# complexvar = 3+6j
# print(complexvar)
# a = "{}, is the greatest fotball player of all time"
# print(a.format("Lionel Messi"))
# b = "{2}, born in {1} and moved to {0}"
# print(b.format("Toronto", "Chennai", "Kailash"))
k = [1,2,3,[],5,[],7]
result = []
for a in k:
    if(a!=[]):
        result.append(a)
print(result)

dic2 = {
    "Name": "kailash",
    "Biology": 100,
    "Maths" : 100}
dic2.update({
    "Chemistry" : 100
})
print(dic2)
print(f'key is {dic2.keys} and value is {dic2.values}')