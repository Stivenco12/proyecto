from registros import registro_de_citas as rdc
import registros.historial_de_citas as hdc
import modules.ejecuto_data_cita as edc
import json

def menucitas(op):
    title = """
    *************************************
    * MENU DE REGISTRO DE CITAS MEDICAS *
    *************************************
    """
    menucitasop = "1.registrar cita \n2 cambiar datos de la cita \n3 volver al menu anterior "
    if (op != 4):
        print (title)
        print (menucitasop)
        try:
            op = int(input(":) "))
        except ValueError:
            print ("error en la opccion ingresada")
            menucitas(0)
        else:
            match (op):
                case 1:
                    rdc.registrar_cita(0)
                case 2:
                    cedula_usuario = "1234567890"
                    nueva_informacion = {
                        "nombre": "Nuevo Nombre",
                        "apellido": "Nuevo Apellido",
                        "edad": 30,
                        "email": "nuevoemail@example.com"
                    }
                    actualizar_usuario(cedula_usuario, nueva_informacion)
                case 3:
                    import main
                    main.menuprincipal(0)
                case _:
                    print ("opciones ingrese no pertenece al menu de opcciones")
                    menucitas(op)

def actualizar_usuario(cedula, nueva_informacion):
    try:
        with open("/proyecto/data/data_cita.json", "r") as archivo_json:
            datos = json.load(archivo_json)

        if cedula in datos:
            datos[cedula].update(nueva_informacion)
            print(f"Información del usuario con cédula {cedula} actualizada:")
            print(datos[cedula])
        else:
            print(f"No se encontró ningún usuario con la cédula {cedula}.")

        with open("/proyecto/data/data_cita.json", "w") as archivo_json:

            json.dump(datos, archivo_json, indent=4)

    except ValueError:
        menucitas(0)