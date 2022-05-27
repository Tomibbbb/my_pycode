eng = input("enter the total number of the students\n")
eng_set= set(input("enter the rool numbers of the english student subscribers \n").split())

frn = input("enter the total number of the students\n")
frn_set= set(input("enter the rool numbers of the english student subscribers \n").split())

print(len(frn_set.symmetric_difference(eng_set)))



