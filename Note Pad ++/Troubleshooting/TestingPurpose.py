# import os
# for (root,dirs,files) in os.walk("D:\\Soft Tech videos\\Python",topdown =True):
#     print(root)
#     print(dir)
#     print(files)
#     print('________________________________')

# ! lambda1
# from functools import reduce
# l = [1,2,3,4]
# l = reduce(lambda x, y: x+y,l )
# print(l)

# def n_power(x):
#     return lambda num: num**x

# square = n_power(2)
# cube = n_power(3)
# print(square(5))
# print(cube(5))


# ! lambda 2
# def inc(inc_by):
#     return lambda num : num+inc_by

# add_5 = inc(5) # sends value of inc_by and lambda is yet to be called
# print(add_5(10)) # lambda in called


#! lambda 3
# def test():
#     print("In test")
#     return lambda : "In lambda function"

# call = test()
# print(call()) 
num = 100
num += num*(50/100)
print(num) 