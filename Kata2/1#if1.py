password = "contraseña"

password_del_usuario = input("Introduzca la contraseña: ")
password_del_usuario = password_del_usuario.lower()

if password == password_del_usuario:
    print("El password es correcto")
else:
    print("El password no coincide")

print("Fin del programa")
