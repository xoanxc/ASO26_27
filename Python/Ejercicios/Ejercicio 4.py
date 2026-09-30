# 4 - Crea un progrma que solicite una cadena de texto al usuairo (como una contraseña). A continuación, vuelve a solicitar una cadena. Muestra si ambas coinciden o si son diferentes.

cadena1 = input("Introduce la contraseña: ")
cadena2 = input("Introduce de nuevo la contraseña: ")

if cadena1 != cadena2:
    print("Las contraseñas no coinciden")
else:
    print("Todo correcto")
