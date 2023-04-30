# python input output
int_var= 17
float_var= 4.5
string_var= 'Vinay'
bool_var= True
print ('Value of int_var=', int_var)
print ('Value of float_var=', float_var)
print ('Value of str_var=', string_var)
print ('Value of bool_var=', bool_var)



#how to check data type in any variable 
#print(" Type of float_var ? ", (float_var))


#how to do type casting in python
int_var = int_var + 10
casted_int_var = float(int_var)
casted_float_var = int(float_var)
print("int to float type casting int_var = ", casted_int_var)
print("float to int type casting int_var = ", casted_float_var)
numeric_str = '450'
numeric_str= int(numeric_str) + 150
print ('value of numeric_str',numeric_str)


#how to use input() function in python
name= input()
age = input()
print('user name',name)
print("user age",age)

*numerical operators
x=5
y=2
print('addition of x+y=',x+y)
print('Substraction of x-y=',x-y)
print('Multiplication of x*y=',x*y)
print('Float division of x/y=',x/y)
print('interger division of x//y=',x//y)
print('modulus of x%y=',x%y)
print('power of x**y=',x**y)


#some operations of string
str_data="vinay"

#concat operations in str
full_name= str_data+ " "+ "HUndalekar"
print ('full name=',full_name)
mul_name= "vinay"*5
print("mul name=",mul_name)
