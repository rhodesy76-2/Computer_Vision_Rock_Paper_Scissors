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
