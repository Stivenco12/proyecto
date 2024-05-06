import registros.globales as g
import modules.ejecuta_data_usuario as edu
import json
import os
def historial_usuarios(op):
        title = """
        ******************************
        * VISUALIZACION DE HISTORIAL *
        ******************************
        """
        g.borrar_pantalla()
        print(title)
        edu.leer_archivo = "proyecto/data/usuario.json"
        try:
                with open(edu.leer_archivo, 'r') as archivo_json:
                        datos = json.load(archivo_json)
                        print(json.dumps(datos, indent=4))
                        import ui.historial as h
                        h.menuhistorial(0)
        except ValueError:
                print("El archivo no se encontró.")
                h.menuhistorial(0)