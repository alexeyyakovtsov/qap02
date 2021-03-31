my_list = [88,66,33,55,77]


for i, j in enumerate(my_list):
    
    if j < my_list[i + 1]:
        print('False')
    elif i + 1 == len(my_list):
        break
    elif j > my_list[i + 1]:
        print('True')
