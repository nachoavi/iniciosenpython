import cx_Oracle #Importamos cx_Oracle para poder utilizar la base de datos de oracle

#Parametros para conectarnos con oracle, estos parametros serán previamente creados en sqldeveloper
usuario = "NACHO"
password = "superashe123"
dsn = "127.0.0.1/xe"

#metodo que realiza la conexion con oracle
connection = cx_Oracle.connect(user=usuario,password=password,dsn=dsn)


# el objeto de conexion tiene un metodo llamado .cursor() que nos permitira 
#interactuar con la BD de oracle
cursor = connection.cursor()

cursor.execute("select first_name,last_name,salary,department_name from employees inner join departments on employees.department_id = departments.department_id where salary = (SELECT AVG(SALARY) FROM employees INNER JOIN departments on employees.department_id = departments.department_id where departments.department_name = 'Human Resources') ")

filas = cursor.fetchall()

for i in filas:
    print(i,end="\n")


