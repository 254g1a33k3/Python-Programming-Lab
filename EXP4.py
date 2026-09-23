# Experement No:4A
statement = input("Enter the String you want to count it length :")


count = 0
for char in statement:
    count = count + 1


print(f"the length of give string :{count}")

# Experement No:4B

string = input("Enter the String:")

substring = input("Enter the substring:")

if substring in string:
    print("SubString is present in the string")
else:
    print("Substrting is not prisent in ther string")

# Experement No:4C
# create the list

number = [10,20,30,40,50,60,70]
print(f"Original Number:",number)

#addition into the list (adding an element to the list)
number.append(80)

print(F"List after adding:",number)

#insertion of element ot the list

number.insert(2,26)

print(F"List after insertion:",number)

print("List after slicing:",number[1:7])


# Experement No:4D
number = [1432,5671,6,5,66,11,99,23,885,285,55,4,6,565,44,26,78,457,44,1]

print("List :",number)


#len() is the function for finf=ding the length

print("Length:",len(number))

#max() gives the maximum number in the list

print("MAX:",max(number))

#min() gives the minimum nu,ber

print("MIN:",min(number))

# sort() it i will arrange in the asc order

print("Sorted List",sorted(number))

# Experement No:4E
string = input("Enter the STRING:")

for i in range(0,len(string),2):
    print(string[i])


# Experement No:4F
list1 = [10, 20, 30, 40, 50]
list2 = [60, 70, 80, 90, 100]
new_list = []
#odd index
for i in range(1,len(list1),2):
    new_list.append(list1[i])
#even index
for i in range(0,len(list2),2):
    new_list.append(list2[i])

print("List1:",list1)

print("List2:",list2)
print("New List:",new_list)
