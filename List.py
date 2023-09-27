#grp of data is called as collection
# list - grp of similar or disimilar dats
# list items are ordered, changeable ,allows duplicate elements
#String is imutable (Cannot modify)
l = [1,2,3,4,5]
print(l) 


#Adding elements into list
# 1.Append - Adding elemnt at the end of the list
# 2.insert - Inserting element at specific index
# 3.Extend - Addinf element at the end of another

#list elemnt can be access in 2 ways 
#i) index 
#ii) iteration

print(l[2])

for x in l:
    print(x)

#Updating list elements  
#Single update
Cap = ["Hyd","Surat","Ban","Mum"]
Cap[1] = "Gandhi Nagar" 
print(Cap)
#Multiple update
Cap[1:3] = ["Chennai", "Bhu"]
print(Cap)

#Removing list items
Cap.remove("Bhu")
print(Cap)

Cap.pop(1)
print(Cap)

Cap.pop()
print(Cap)

del Cap
