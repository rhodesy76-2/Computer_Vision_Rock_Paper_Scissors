#%%
from module_1 import function_1

function_1()
# %%
from module_1 import function_2

function_2()
# %%
from module_2 import function_1

function_1()

# %%
from module_1 import function_1

function_1()

from module_1 import function_2

function_2()

from module_2 import function_1

function_1()
# %%
function_1()

# %%
# Notice that you imported function_1 twice. Which one got called when you ran python main.py? Why?
''' It calls the functions in order but if I call function_1 again it calls the last import function_1 as they have the same name '''

#%%
from package_1.module_1 import function_package
function_package() 
# %%
from module_2 import x

print(x)
# %%
x = "Hello, I am in main.py"
print(x)
# %%
