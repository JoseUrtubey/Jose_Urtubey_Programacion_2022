import mysql.connector

x = mysql.connector.connect(user='bdi',password='pepe1234',host='127.0.0.1',database='ejercicio1')
escribir = x.cursor()
try:
    addMedic =  ('INSERT INTO Medicos (nombre, apellido, dni) VALUES (%s, %s, %s)')
    addMeciData = (15123456,'Mario', 'Kloss')
    escribir.execute(addMedic, addMeciData)
    x.commit()
    print('Se ha insertado un nuevo medico')
except mysql.connector.Error as err:
    print('Ha ocurrido un error: {}'.format(err))
    escribir.close()
    x.close()