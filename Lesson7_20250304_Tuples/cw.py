a = ["a","b","c","d","e"]

#Packing a tuple using ()
sampletuple = ("Tom",6,"Soccer","English")

#unpacking a tuple
name, grade, hobby, favsub = sampletuple
print(name + str(grade) + hobby + favsub)

print(a)
print(sampletuple)

#printing indivisdual items
print(a[4])
print(sampletuple[2])

newtuple = 1,2,3,4,5,6,7,8,9
print(newtuple)

neotuple = (
    (1,2,3),
    [4,5,6],
    "apple",
    ("banana","pear")
)

#WE CANNOT ADD DATA IN TUPLEW
#Once if you made it, you can not modify(Both adding and editing) with codes

#newtuple.append(10)
#newtuple[0] = 100
#print(newtuple)