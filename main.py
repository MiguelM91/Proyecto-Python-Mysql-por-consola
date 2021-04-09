'''
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro creará un usuario en la BD
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas.
'''

from usuarios import acciones

print("""
Acciones disponibles:
    - registro
    - login
""")

hasEl = acciones.Acciones()
accion = input("¿Qué quires hacer?: ")
if accion == "registro":
    hasEl.registro()

elif accion == "login":
    hasEl.login()

