# Ejercicio de calculo de rentabilidad:
# Se haran las siguientes consultas a la base de datos Northwind.db.
# Cual es el producto mas rentable?
# Cual es el empleado con mas Ordenes de Ventas?
# Que empleado recaudó mas?

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#----- Consulta Producto Mas Rentable -----

with sqlite3.connect("Northwind.db") as conn:
    query = '''
            SELECT ProductName, SUM(Price * Quantity) as Revenue
            FROM OrderDetails od
            JOIN Products p ON p.ProductID = od.ProductID
            GROUP BY od.ProductID
            ORDER BY Revenue DESC
            LIMIT 10
'''

top_products = pd.read_sql_query(query, conn)
top_products.plot (x="ProductName", y="Revenue", kind="bar", figsize=(10,5), legend=False)

plt.title("10 Productos Mas Rentables")
plt.xlabel("Productos")
plt.ylabel("Revenue")
plt.xticks(rotation = 45)
plt.show()

#----- Consulta Empleado con mas ordenes de ventas -----

query2 = '''
            SELECT FirstName || " " || LastName AS Employee, COUNT(*) AS Total
            FROM Orders o
            JOIN Employees e ON e.EmployeeID = o.EmployeeID
            GROUP BY o.EmployeeID
            ORDER BY Total DESC
            LIMIT 10
'''
top_employees = pd.read_sql_query(query2, conn)
top_employees.plot (x="Employee", y="Total", kind="bar", figsize=(10,5), legend=False)

plt.title("10 Empleados Mas Efectivos")
plt.xlabel("Empleados")
plt.ylabel("Total Ventas")
plt.xticks(rotation = 45)
plt.show()

#----- Que Empleado Recaudo Mas -----

query3 = '''
            SELECT FirstName || " " || LastName AS Employee, COUNT(*) AS Total
            FROM Orders o
            JOIN Employees e ON e.EmployeeID = o.EmployeeID
            GROUP BY o.EmployeeID
            ORDER BY Total DESC
            LIMIT 1
'''

best_employee = pd.read_sql_query(query3, conn)
print("El empleado del mes es:\n")
print(best_employee)
print()