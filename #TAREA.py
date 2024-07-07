"""#TAREA
#Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en
#una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de
#caracteres en un mensaje de salida por pantalla

lista_nombre=[]
nombres=""
for i in range (1,4):
    nombres=input(f"Ingresa el {i}° nombre: ")
    lista_nombre.append(nombres)
nombre_largo=max(lista_nombre, key=len)
print(f"El nombre más largo es: {nombre_largo}")
print("**********************************************")

lista_nombre=[]
nombres=""
for i in range (1,4):
    nombres=input(f"Ingresa el {i}° nombre: ")
    lista_nombre.append(nombres)
longitud_mayor=0
nombre_maslargo=None
for nombres in lista_nombre:
    if len(nombres)>longitud_mayor:
        longitud_mayor=len(nombres)
        nombre_maslargo=nombres
print(f"El nombre más largo es: {nombre_maslargo}")

#Cree 2 listas, en las cuales se guardará 3 nombres y 3 apellidos (1 lista para
#nombres y una 1 lista para apellidos), el sistema deberá mostrar de forma ordenada
#los nombres y apellidos
lista_nombre=[]
nombres=""
for i in range (1,4):
    nombres=input(f"Ingresa {i}° nombre: ")
    lista_nombre.append(nombres)
lista_apellido=[]
apellidos=""
for i in range (1,4):
    apellidos=input(f"Ingresa {i}° apellido: ")
    lista_apellido.append(apellidos)
listas=(lista_nombre+lista_apellido)
listas.sort()
print(f"Los nombres y apellidos ordenados alfabeticamente {listas}")

#Cree una lista y comience a almacenar nombres, cada vez que se agregue un
#nombre nuevo, el sistema preguntará si desea agregar otro nombre, deberá agregar
#nombres hasta que la respuesta sea “no”, “No”, “nO” o “NO” (use funciones lower()
#y upper() ) .
#Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de
#caracteres
lista_nombre = []
nombre=""
agregar = True
while agregar:
    nombre = input("Ingrese un nombre: ")
    lista_nombre.append(nombre)
    respuesta = input("¿Quiere agregar otro nombre? (si/no): ").upper().lower()
    if respuesta != 'si':
        agregar = False
print(f"Lista de nombres ingresados: {lista_nombre}")
nombre_corto=min(lista_nombre, key=len)
print(f"El nombre más corto es: {nombre_corto}")
lista_nombre.remove(nombre_corto)
print(lista_nombre)"""

#Cree un menú para registrar usuarios e iniciar sesión, también el menú tendrá la
#opción de eliminar usuarios, para ello, utilice el nombre de usuario, además para
#confirmar la eliminación, deberán escribir la contraseña correspondiente de cada
#usuario.
#1. Inicio sesión.
#2. Registrar usuario
#3. Eliminar usuario.
#4. Salir.
#La opción 1 solo mostrará un mensaje exitoso si ha iniciado correctamente,
#o un error de caso contrario

menu_principal=""
usuario_lista=[]
clave_lista=[]
usuario=""
clave=""


while menu_principal!=4:
    print ("""
    1. Inicio sesión.
    2. Registrar usuario
    3. Eliminar usuario.
    4. Salir""")
    menu_principal=int(input("Ingrese su opción: "))
    if menu_principal==1:
        usuario=input("Ingrese su usuario: ")
        clave=input("Ingrese clave: ")
        if usuario in usuario_lista and usuario_lista[usuario]==clave: 
            print("Se ha iniciado sesión correctamente")
        else:
            print("Error, debe realizar el registro o ha ingresado datos incorrectos")
    elif menu_principal==2:
        usuario=(input(f"Ingresa el usuario: "))
        usuario_lista.append(usuario)
        clave=(input(f"Ingresa la clave: "))
        clave_lista.append(clave)
        print(f'Usuario: {usuario} ,clave: {clave}')
        print("Datos guardados correctamente")
    elif menu_principal==3:
        pass
        