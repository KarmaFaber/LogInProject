
import pymysql
import hashlib

from pymysql import MySQLError

global contrasenia

#----------------funciones-----------------------------

#funcion validación nickname
def nickname(nombre_usuario):
    long=len(nombre_usuario)#longitud del usuario
    y=nombre_usuario.isalnum()#comprueba que la cadena tenga valores alfanumericos

    if y==False:# la cadena contiene valores no alfanumericos
        print("el nombre de usuario puede contener solo letrasa y numeros: ")
    if long <4 or long >10:
        print("la longitud del nombre de usuario deberia ser entre 4 y 10 caractéres: ")
    if long >5 and long <10 and y==True:
        return True

#---------------------------------------------------fin funciones---------------------

#variables
print("la longitud del nombre de usuario deberia ser entre 4 y 10 caractéres")
correcto=False
while correcto==False:
    usuario = input("introduce el nombre del usuario:  ")
    if nickname(usuario)==True:
            #print("formato usuario ok")
            correcto=True
try:
    #database conection
    db=pymysql.connect("localhost","root", "", "login")

    #database query
    cursor=db.cursor()
    consulta="select nombre, contasenia from usuarios where nombre=%s"
    valor=(usuario)
    cursor.execute(consulta, valor)
    result=cursor.fetchone()#row method

    print("Recuerda que la contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")
    print("\n La contraseña deberia tener al menos 5 caractéres")
    contrasenia=input("\n Introduce tu contraseña:  ")
    cifrada=hashlib.md5(contrasenia.encode())


    correcto=False
    while correcto==False:
        if cifrada.hexdigest()!=result[1]:
            print("La contraseña no coincide :(")
            print("\n Recuerda que la contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")
            print("\n La contraseña debería tener al menos 5 caractéres. Introduce tu contraseña otra vez:  ")
        else:
            print("\nHas entrado correctamente. Wiiiii ...")
            correcto=True

    db.close()
except ConnectionRefusedError:
    print("error al conectarse a la base de datos, revise su conección al servidor y vuelva a intentarlo")
except TypeError:
    print("\nerror al introducir algún dato, vuelva a intentarlo de nuevo")
except MySQLError as e:
    print('Got error {!r}, errno is {}'.format(e, e.args[0]))
    print("error al introducir los datos en la bd :(")




