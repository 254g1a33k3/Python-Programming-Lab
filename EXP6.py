#Exprement : 6D
my_tuple = (10,20,30,20,40,10,50,30)
repeated = set()

for item in my_tuple:
    if my_tuple.count(item)>1:
        repeated.add(item)
print("Repeated Items :",repeated)
"""
#Exprement : 6E
my_list = [(1,"Akhil"),(2,"Bhavana"),(3,"Charan")]
number,names = zip(*my_list)
number = list(number)
names = list(names)
print("First List:",number)
print("Second List:",names)

#EXPREMENT : 6F

my_list = [10, 20, 30, 40, (50, 60), 70, 80]
count = 0
for item in my_list:
    if isinstance(item, tuple):
        break


    count = count + 1
# Display the count
print("Number of elements before the tuple:", count)


#Exprement :6G
my_tuple = (1,2,3,4,5,6,7,8,9,10)
product = 1

for num in my_tuple:
    product = product * num

print("Product of all elements:",product)
"""
