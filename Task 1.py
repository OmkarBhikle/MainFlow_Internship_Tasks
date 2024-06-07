#List(List items are ordered, changeable, and allow duplicate values)
myList = ["apple", "banana", "cherry"]
myList[0] = "jackfruit"
myList.append("orange")
myList.remove("cherry")
print(myList)

#Creating list using list constructor
list1 = list(("apple", "banana", "cherry"))
print(list1)

#Set(A set is a collection which is unordered, unchangeable, and unindexed)
mySet = {"apple", "banana", "cherry"}
mySet.add("orange")
mySet.remove("cherry")
print(mySet)

#Dictonary(A dictionary is a collection which is ordered, changeable and do not allow duplicates)
myDict = {
    "Name" : "Omkar",
    "age" : 21,
    "Domain" : "Data Science"
}

myDict["age"] = 19
myDict["Gender"] = "Male"
myDict.pop("Domain")
myDict.popitem()
print(myDict)