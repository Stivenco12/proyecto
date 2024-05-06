import registros.globales as g
import modules.ejecuta_data_medico as edm
import json
import os
import ui.historial as h
def historial_medico(op):
        title = """
        ******************************
        * VISUALIZACION DE HISTORIAL *
        ******************************
        """
        g.borrar_pantalla()
        print(title)
        edm.leer_archivo = "proyecto/data/medico.json"
        try:
                with open(edm.leer_archivo, 'r') as archivo_json:
                        datos = json.load(archivo_json)
                        print(json.dumps(datos, indent=4))
                        import ui.historial as h
                        h.menuhistorial(0)
        except ValueError:
                print("El archivo no se encontró.")
                h.menuhistorial(0)
