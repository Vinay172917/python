#declare empty list
#L1=[]
#print(type(L1))

#insert value in list
#L1.append(9)
#L1.append(0)
#L1.append(5)
#print(L1)

#using for loop print L1

#L1=[]
#for int in range (1,10):
    #L1.append(int)
    #print(L1)

#how to calculate length of list
    
#len_of_list=len(L1)
#print("length of list=",len_of_list)

#how to check list are equal to each other
#L2=["vinay",17,4.5,"im"]
#L3=["vinay",17,4.5,"im"]
#L4=["vinay",17,4.5,"im"]
#print("list are equals to each other",L2==L3==L4)

#list adding or concenate
#result=L2 + L3 + L4
#print(result)

#how to access list value
#L5=[32,45,56,33,35,56]

#how to print all elements (option 1)
#for int in L5:
    #print(int)

#how to print 4th element from all elements (option 2)
#syntax= list_name[index]
#print(L5[1])

#what will happened 
#list index will out of range
#print(L5[100])


list7=[5,"vinay",15]
#how to update the value of list index?
#update vinay to rahul

list7[1]="rahul"
print(list7)

#how to print list element using lenght?
for index in range(0,len(list7)):
    print(list7[index])

list8=[1,34,"vinay",45,"hund",45,[5,45,4]]#what will be the Output/
print(len(list8))

#differnce between append() and Extend()
list9=[2,4,5]
list10=["vinay","python","v"]
list9.append(list10)
print(list9)

list11=[2,4,5]
list12=["vinay","python","v"]
list11.extend(list12)
print(list11)


#list Slicing
#syntex-> list_name[start index:end index]
#end index always exclusive
list13=[34,56,34,34,35,5,63]
print(list13[0 : 5])
print(list13[0 : ])
print(list13[2 : 8])
#how to take jump of 2 steps 3step etc.
print(list13[0 : : 2]) #3rd value is for step increment

#how to print the last value of list
print(list13[len(list13)- 1])
print(list13[-1])#negative index -1 is represent last element of list

#print second last element in list
print(list13[-2])

#print input list in reverse direction using list slicing
print(list13[-1: :-1])

