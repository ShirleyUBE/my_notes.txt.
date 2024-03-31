# Crear y escribir en el archivo
with open("my_notes.txt", "w") as file:
    file.write("Notas personales:\n")
    file.write("1. Me gusta mucho salir de viaje.\n")
    file.write("2. todoslos dias llamo a mai mamá\n")
    file.write("3. al terminar la semana hago las compras.\n")

# Leer el archivo línea por línea y mostrar su contenido
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line.strip())  # Elimina los espacios en blanco al inicio y al final de la línea

# Cerrar el archivo después de su uso
file.close()
