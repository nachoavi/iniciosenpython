listf=["Juan","Pablo","Lorena","Ignacio","Sebastían"]
print(listf)

listf.append("Ana")
print(listf[:])

listf.extend(["Alverto","Luis","Ivan","José"])
print(listf[:])

listf.insert(0, "Xímena")
print(listf[:])

listf.remove("José")
print(listf[:])

print(listf.index("Ana"))

listf.remove("Ana")
print(listf[:])

print(listf[1:4])