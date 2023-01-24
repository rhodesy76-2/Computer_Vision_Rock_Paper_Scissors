#%%
while True:
    try:
    
        input_1 = input('Enter a number: ')
        input_2 = input('Enter another number: ')
        int_1 = int(input_1)
        int_2 = int(input_2)
        # print(int_1 / int_2)
    except ValueError:
        print("You must enter a number")
    except ZeroDivisionError: 
        print("You cannot divide by zero")
    except KeyboardInterrupt: 
        print("You pressed Ctrl+C")

    else:
        print("No errors were raised")
        print(int_1 / int_2)
        break

# Add an exception for ValueError so when the user enters a string instead of a number, the program will not crash.
# Add an exception for ZeroDivisionError so when the user enters 0 as the second number, the program will not crash.
# Add an exception for KeyboardInterrupt so when the user presses Ctrl+C, the program will not crash.
# %%
x = '2'
print(f'The type of x is {type(x)}')
y = int(x)
print(f'The type of y is {type(y)}')
# %%
x = input('Enter your number')
print(f'The type of x is {type(x)}')
y = int(x)
print(f'The type of y is {type(y)}')
print(y ** 2)
# %%
x = 'Dog'
print(f'The type of x is {type(x)}')
y = int(x)
print(f'The type of y is {type(y)}')
# %%
ls = [1, 2, 3]
print(len(ls))

# %%
my_dict = {'Name': 'Walter White', 'Occupation': 'Cook'}
print(my_dict.keys())
# %%
