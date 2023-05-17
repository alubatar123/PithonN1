Para el programa Editor de Texto se utilizaran 4 archivos:

-archivo.txt (Archivo que guarda el texto con el que se probaran las funciones del programa)
-EditorMenu.py (Programa principal que ofrece las diferentes opciones al usuario)
-EditorOper.py (Programa que establece conexion con archivo.txt y actualiza el mismo)
-ModuloConexion.py (Programa donde se ejecutan los metodos para cada accion del Menu)

Antes de ejecutar el programa, se debe cambiar la ruta del archivo "archivo.txt" de la linea 5 del
archivo "ModuloConexion.py"

ModuloConexion.py,EditorOper.py y EditorMenu.py importan metodos entre si, por lo que deben estar en la misma carpeta

Dado que el programa trabaja con diferentes tipos de indices, se recomienda cambiar los parametros en VisualEstudio antes de empezar para corregir la visualizacion:

Archivo->Preferencias->Configuracion
En la barra de busqueda escribir "wrap"
Cambiar "Diff Editor :Word Wrap" a ON
Cambiar "Editor :Word Wrap" a ON

Para iniciar el programa se debe ejecutar desde "EditorMenu.py"
