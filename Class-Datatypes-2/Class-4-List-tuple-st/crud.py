enames=['Rahul','Sonia','Priyanka','Modi']
#index    0      1        2             3
#-veIndex -4      -3       -2          -1
print(enames)
#how to read list elements - using indexing
#update list elements
enames[3] = 'PM Naredra Modi'
print(enames)
#delete list element
enames.pop()#['Rahul', 'Sonia', 'Priyanka', 'PM Naredra Modi']
print(enames)#['Rahul', 'Sonia', 'Priyanka']