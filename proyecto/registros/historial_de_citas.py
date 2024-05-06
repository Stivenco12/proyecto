import registros.globales as g
import modules.ejecuto_data_cita as edc
import ui.historial as h
import json
import os
def historial_cita(op):
        title = """
        ******************************
        * VISUALIZACION DE HISTORIAL *
        ******************************
        """
        g.borrar_pantalla()
        print(title)
        edc.leer_archivo = "proyecto/data/data_cita.json"
        try:
                with open(edc.leer_archivo, 'r') as archivo_json:
                        datos = json.load(archivo_json)
                        print(json.dumps(datos, indent=4))
                        h.menuhistorial(0)
        except:
                print ("nose encontro el json")
                h.menuhistorial(0)

