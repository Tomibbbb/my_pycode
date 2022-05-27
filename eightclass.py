#a={3,4,7,8,10,17}
#b={2,4,6,8,10,12}
#c = a.union(b)
#print(c)

# if you want the union of both a and b in a
#a.update(b)
#print(a)
# will give us a new set
#d = a.intersection(b)
#print(d)
#will print the resultb in a
#a.intersection_update(b)
#print(a)

#c=a.difference(b)
#print(c)
#a.difference_update(b)
#print(b)

#c=a.symmetric_difference(b)
#print(c)
#a.symmetric_difference_update(b)
#print(a)

#b={"a":5,
#"b":6,
#"c":7}
#print(b["a"])
# to change value
#b["b"]=9
#to add a new key and value
##b["d"]=8
#print(b["y"])

my_arr =[0,4,9,7,1,1,3,4,7,8,8,0,3,1,
3,2,4,8,3,2,4,6,7,8,3,6,3,7,5,6,1,0,2,
7,5,4,3,5,0,7,3,7,9,7,1,7,6,0,5,2]

freq = {}

for ele in my_arr:
    freq[str(ele)] = freq.get(str(ele),0) + 1

print(freq)    

a={}
for ele in set(my_arr):
    a[ele] = my_arr.count(ele)