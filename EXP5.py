
#EXPREMENT : 5A

string = input("Enter a string: ")

vowels = "aeiouAEIOU"

count_a = string.count('a')
count_e = string.count('e')
count_i = string.count('i')
count_o = string.count('o')
count_u = string.count('u')

count_A = string.count('A')
count_E = string.count('E')
count_I = string.count('I')
count_O = string.count('O')
count_U = string.count('U')

count = count_a +count_e +count_i +count_o +count_u +count_A +count_E +count_I +count_O +count_U

print("Number of viowels : ",count)


#EXPERMENT :5B
employee = {
    "Name" : "C G Govardhan Reddy",
    "Age":19,
    "Department": "CSM"

    }
key = input("Enter the key to search:")

print(key in employee)



#EXPREMENT : 5C


employee = {
    "Name":"C G Govardhan Reddy",
    "Age" : "19",
    "Department":"CSM"
    }
employee["Salary"]= 30000

print("Updated Dictonary:",employee)




#EXPREMENT :5D

marks = {
    "Maths":80,
    "Science":75,
    "English":85
    }
total = sum(marks.values())
print("Sum of all items : ",total)



#EXPREMENT : 5E

numbers = [1,2,3,2,4,1,2,3,46,76,9,43,67,9,3,3,3,3,2]
count = {}
for num in numbers :
    count[num] = count.get(num,0) + 1

print("Occurance of each elements:",count)



#EXPREMENT : 5F

numbers = [10,20,30,40,50]
data = {
    "a":10,
    "b" : 30,
    "c" : 50
    }
for num in numbers[:]:
    if num not in data.values():
        numbers.remove(num)


print("Updated list:",numbers)
