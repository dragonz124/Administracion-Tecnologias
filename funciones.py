def sumar(a,b):
    return a + b


def validar_usuario(usuario, contraseña):
    
    usuarios_registrados = {
        "admin": "admin123",
        "usuario1": "clave123",
        "invitado": "invitado123"
    }

    if usuario in usuarios_registrados and usuarios_registrados[usuario] == contraseña:
        return True  
    else:
        return False  

