import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("Vamos a registrarte en el sistema...\n")

        nombre = input("¿Cuál es tu nombre?\n")
        apellidos = input("¿Cuáles son tus apellidos?\n")
        email = input("¿Cuá es tu dirección de correo electrónico?\n")
        password = input("Escribe tu contraseña\n")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre}, te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")

    def login(self):
        print("Identifícate en el sistema...")

        try:
            email = input("¿Cuá es tu dirección de correo electrónico?\n")
            password = input("Escribe tu contraseña\n")

            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto!! Intentalo más tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Qué quieres hacer?: \n")
        hasEl = notas.acciones.Acciones()

        if accion == "crear":
            hasEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hasEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hasEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print("Gracias por utilizar nuestro proyecto. Hasta pronto {}:".format(usuario[1]))
            exit()