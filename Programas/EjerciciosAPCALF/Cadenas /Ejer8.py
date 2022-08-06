precio=input("Cual es el precio? use 2 decimales: ")
print(precio[:precio.find(".")],"euros y", precio[precio.find(".")+1:], "centimos")