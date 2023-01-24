#%%
#Going deep!
# Use indexing to get the string "Python" from the following dictionary: one_deep_dictionary = {'start here':1,'k1':[1,2,3,{'k2':[1,2,{'k3':['keep going',{'further':[1,2,3,4,[{'k4':'Python'}]]}]}]}]}

one_deep_dictionary = {'start here':1,'k1':[1,2,3,{'k2':[1,2,{'k3':['keep going',{'further':[1,2,3,4,[{'k4':'Python'}]]}]}]}]}

one_deep_dictionary.items()

print(one_deep_dictionary["k1"][3]["k2"][2]["k3"][1]['further'][4][0])

#%%
one_deep_dictionary = {'start here':1,'k1':[1,2,3,{'k2':[1,2,{'k3':['keep going',{'further':[1,2,3,4,[{'k4':'Python'}]]}]}]}]}
new_dict = one_deep_dictionary["k1"][3]["k2"][2]["k3"][1]['further'][4][0]
print(new_dict.values())
# %%
99>5
# %%
0==False
# %%
1==True
# %%

# Function to simulate OR Gate
def OR(A, B):
	return A | B	

OR(0,1)

x = int(input ("Enter first number"))
y = int(input ("Enter first number"))



C = OR(x, y)
print(C)

# Function to simulate AND Gate
def AND(A, B):
	return A | B	

AND(0,1)

x = int(input ("Enter first number"))
y = int(input ("Enter first number"))




D = AND(x, y)
print(D)

D_not = not(D)


print(D_not)
AND(C, D_not)
output = AND(C, D_not)
print(output)

def XOR(A, B):
	return A ^ B

XOR(1, 1)

#%%

"AAA">"aaa"
#%%
"AAB">"AAA"
#%%
"aaa">"AAA"
# unociode value of a is higher than A
# %%
"AAA" + "aaa"

# %%
x = 10
n = int(input("Please input an integer"))
if n > x:
    print(f"{n} is greater than {x}")
# %%
x = 1
while x <= 50:
    print(x)
    x += 1
# %%

for i in range(1, 51):
    print(i)
# %%
#Counting even Numbers

# Write a program that prints the numbers from 1 to 50 only if the number is even.
#Use a while loop to do so
x = 1
while x <= 50:
    if x % 2 == 0:
        print(x)
    x += 1

#%%
#Use a for loop to do so
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
# %%
#sum odd and evn numbers between 1-100
#even
sum=0
for i in range(1, 101):
    if i % 2 == 0:
        sum = sum + i
        print(sum)
     

# %%
sum=0
for i in range(1, 101):
    if i % 2 != 0:
        sum = sum + i
        print(sum)
# %%
#Write a program that prints the numbers from 1 to 100.
#For multiples of three print "Fizz" instead of the number
#For multiples of five print "Buzz"
#For numbers which are multiples of both three and five print "FizzBuzz"
#Be careful with the order of the conditions. Remember that the condition that is first met will be the one that will run, and the rest will be ignored.


def fizzbuzz():
    for i in range(1, 101):
        numbers = i
        if  i % 5 ==0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 ==0:
            print("Buzz")
        else:
            print(i)
        

fizzbuzz()

# %%
#RPS game - did in main project

#%%
# Each element is the product code, the individual price, and the quantity.
order_list = [("tom", 0.87, 4),
              ("sug", 1.09, 3),
              ("ws", 0.29, 4),
              ("juc", 1.89, 1),
              ("fo", 1.29, 2)]

# This dictionary gives the full name of each product code.
names = {"tom": "Tomatoes",
         "sug": "Sugar",
         "ws": "Washing Sponges",
         "juc": "Juice",
         "fo": "Foil"}

budget = 10.00
running_total = 0
receipt = []

while budget >= 0:
    for item, cost, amount in order_list:
        budget = budget - (cost * amount)
        if budget <= 0:
            print(f"You have exceeded your budget by {-budget}, by buying {amount} {names[item]}")
            break
        running_total = running_total + (cost * amount)
        receipt.append(f"Item Code: {names[item]}, Amount: {amount}, Individaul Price: £{cost}, Total cost: £{cost*amount}, Running Total: {running_total}")
        print(receipt)
    

# %%
#Create a list comprehension that squares even arguments, and squares odd arguments after adding one to them
#Test it on the following list my_list = [1, 5, 8, 6, 21]
#The output should be:
#[4, 36, 64, 36, 484]
my_list = [1, 5, 8, 6, 21]
new_list = []

for i in my_list:
    if i % 2 == 0:
        i= i**2
        new_list.append(i)
    else:
       i = (i+1)**2
       new_list.append(i)
print(new_list)
# %%
# Dictionairies and List Comprehension
# Create two dictionaries, each one with 2 keys
# name: a string of your name
# skills: a list of strings
#Put both of them in a list
#Now index that list of dictionaries to find the last letter of the first skill of the last dictionary
#Create a list comprehension which maps that list to a list of the length of names
#Add that list together to get the total number of characters in all of the names
#WTF?
my_list = [{'name':'James', "skills":["Python", "Java"]}, {"name": "Rhodes", "skills": ["Lisp", "Prolog"]}]

my_list[1]
#%%
my_list[1]["skills"]
#%%
my_list[1]["skills"][0][-1]
#%%
my_list = [{'name':'James', "skills":["Python", "Java"]}, {"name": "Rhodes", "skills": ["Lisp", "Prolog"]}]
my_list[0]['name']
len(my_list[0]['name'])

#%%
name_length = []

for i in range(0,2):
    name_length.append(len(my_list[i]['name']))
print(name_length)
print(sum(name_length))


#%%
# Shop Item Filter
# Filter shop_dict using list comprehension to find only items with values of over 1.00
#Assign them to a list called filtered_shop by their full names, not their codes, using names_dict.
#shop_dict = {"tom":0.87, "sug":1.09, "ws":0.29, "cc":1.89, "ccz":1.29}
# names_dict = {"tom":"Tomatoes", "sug":"Sugar", "ws":"Washing Sponges", "cc":"Coca-Cola", "ccz":"Coca-Cola Zero"}

filtered_shop =[]
shop_dict = {"tom":0.87, "sug":1.09, "ws":0.29, "cc":1.89, "ccz":1.29}
names_dict = {"tom":"Tomatoes", "sug":"Sugar", "ws":"Washing Sponges", "cc":"Coca-Cola", "ccz":"Coca-Cola Zero"}



for key, value in shop_dict.items():
    if value > 1.00:
        filtered_shop.append(names_dict[key])
print(filtered_shop)
    


# %%
# Write a program to produce the following pattern.
# Here's a clue: Use nested for loops, using one nested loop to increase in size and another to decrease.*
#Start with n=5
#Example:
#?
#? ?
#? ? ?
#? ? ? ?
#? ? ? ? ?
#? ? ? ?
#? ? ?
#? ?
#?
n = 5
for i in range(n+1):
    for j in range(i):
        print("?",end=" ")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('?', end=" ")
    print('')
  
    
# %%
#Write a program to check whether each number from 10 to 50 is prime
#Your answer should take the following format:
#"x is a prime number." for primes
#"x is not a prime number because y is a factor of x." for non-primes
#Here's a clue: This is possible using a while loop nested in a for loop or using a nested for loop; if you can, try to find both

for num in range (10, 51):
    count = 0
    for i in range(2, (num//2 + 1)):
        if(num % i == 0):
            print(num,"is not a prime number")
            count = count + 1
            print(i,"times",num//i,"is",num)
            break

    if (count == 0 and num != 1):
        print(num,"is a prime number")

# %%
#10 imports

import sys
sys.path
# %%
import sys

print(sys.path)
# %%
my_list = [1, 2, 3, 4, 5]
1 in my_list

# %%
6 in my_list
# %%
7 not in my_list
# %%
my_number_1 = 1
my_number_2 = 2
my_number_1 == my_number_2 
# %%
my_number_1 is my_number_2 
# %%
# same as 1 & 2 different
# %%
my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [1, 2, 3, 4, 5]
my_list_1 == my_list_2 

# %%
my_list_1 is my_list_2 
# %%
# different as lists go into seperate parts of memory. If we set my_list_1 = my_list_2 then would be true
# %%
my_dict = {}
# my_dict.items()
# %%
bool(my_dict)
# %%
not my_dict
# %%
my_dict_2 = {"key_1": 1, "key_2": 2}
bool(my_dict)
# %%
not my_dict_2
# %%
