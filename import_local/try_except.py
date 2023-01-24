#%%
try:
    file = open("test.txt", "r")
    print(file.read())
   
except SyntaxError:
    print("File not found")
    file = open("test.txt", "w")
    file.write("Hello, I am a file!")
    file.close()
    #print(SyntaxError)
    print("There was a syntax error")

#%%
except TypeError:
    print("There was a type error")
    
except NameError: 
    print("You used the wrong name")

finally: # executed with or without errors in the try statement
    print("This block of code is ALWAYS executed")
# %%
