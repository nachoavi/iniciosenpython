list1=["Leandro","Alverto","Francisca","Camila","Jordan"]
print(list1)

list1.append("Ana")
print(list1[:])

list1.extend(["Eduardo","José","Fabian","Fabiola"])
print(list1[:])

list1.insert(0,"Alexa")
print(list1[:])

list1.pop()
print(list1[:])

print(list1.index("Ana"))

list1.remove("Ana")
print(list1[:])

print(list1[:3])