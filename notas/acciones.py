import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1]}!! Vamos a crear una nueva nota...\n")

        titulo = input("Introduce el titulo de tu nota: \n")
        descripcion = input("Escribe el contenido de tu nota: \n")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto, has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")

    def mostrar(self, usuario):
        print("Ok {}!! Vamos a mostrar las notas registradas...\n".format(usuario[1]))

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n************")
            print(nota[2])
            print(nota[3])
            print("************")

    def borrar(self, usuario):
        print("Ok {}!! Vamos a borrar notas...\n".format(usuario[1]))

        titulo = input("Escribe el titulo de la nota que deseas eliminar: \n")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print("La nota con título {} ha sido eliminada correctamente:".format(nota.titulo))
        else:
            print("No se ha eliminado la nota, intenta nuevamente")
