import time
import os
"""
    este modulo tiene la finalidad de:
    crear un log de usuarios que llamaremos registro_ID.txt.
    este modulo comprueba si el archibo registro_ID.txt existe y de no existir los crea con 6 campos 
    fecha, hora, id de telegram, usuario de telegram, respuesta y el comandousado por el usuario.
    la funcion registrorecive 4 parametros que se que deveran llamar los como se explica acontinuación:
    en los comandos:
    a) message.chat.id
    b) respuesta (llameremos respuesta un codigo de terminacion el cual nos permite saber si el usuario esta utilizando de forma adecuada el bot 200 cuando el comando es el esperado y 404 cuando el comandoes cualquier cosa que no tenemos establecida)
    c) message.text 
    d) message.from_user.username
    ejemplo de uso con comando: registro(message.chat.id, "200", message.text, message.from_user.username)
    
    en los botones:
    a) call.from_user.id.
    b) registro
    c) call.data
    d) call.from_user.username
    ejemplo de uso con los botones: registro(call.from_user.id, "200", call.data, call.from_user.username)
"""


def registro(var, var_1, var_2, var_3):
    #funcion que supervisa y escribe en registro_ID.txt las acciones de los usuarios
    log = "registro_ID.txt"
    if os.path.exists(log):
        pass
    else:
        with open("registro_ID.txt", "w") as f:
            f.write("FECHA      ")
            f.write("HORA     ")
            f.write("USER_ID   ")
            f.write("USERNAME                         ")
            f.write("respuesta ")
            f.write("comando \n \n")
    if var == var:           
        cuantos_caracteres = len(var_3)
        maximoUN = 32
        espacio = maximoUN - cuantos_caracteres
        registro = []
        registro.append(str(var)),                         
        f = open("registro_ID.txt", "a", encoding="utf-8")  
    for i in registro:     
        f.write(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())+ " ")
        f.write(f"{i} ")
        f.write(f"{var_3} "+" "*espacio)
        f.write(f"{var_1}       ")
        f.write(f"{var_2}\n")
        f.close()

