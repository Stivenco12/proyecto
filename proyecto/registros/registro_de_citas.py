import os 
import json
import registros.globales as g
import modules.ejecuto_data_cita as e
import ui.citas as uic
def registrar_cita(op):
        title = """
        ********************
        * REGISTRO DE CITA *
        ********************
        """
        g.borrar_pantalla()
        print(title)
        try:
            cedula = int(input ("ingrese Nmr de la cedula"))
            nombre = input ("ingrese su nombre")
            apellido = input ("ingrese su apellido")
            celular = int(input ("ingrese su numero telefonico"))
            edad = int(input("ingrese su edad"))
            menutipo = ("cual es su genero \n1 HOMBRE \n2 MUJER \n3 OTRO")
            if (op !=3):
                print (title)
                print (menutipo)
                try:
                    opcion = int(input(":) "))
                except ValueError:
                    print ("error en la opcion ingresada")
                    registrar_cita(0)
                else:
                    match (opcion):
                        case 1:
                            genero = ("hombre")
                        case 2: 
                            genero = ("mujer")
                        case 3:
                            genero = ("otro")
                        case _:
                            print ("opciones ingresada no pertence al menu del centro medico")
                            registrar_cita(0)
            fechanacimiento = input("ingrese la fecha de su nacimiento dia/mes/año")
            fecha = int(input("ingrese la fecha de la cita dia/mes/año"))
            menuhora = ("que hora de trabajo tiene disponible \n1 7a.m a 12 a.m (mañana)\n2 1p.m a 6 a.m (tarde)")
            if (op !=2):
                print (title)
                print (menuhora)
                try:
                    opcion = int(input(":) "))
                except ValueError:
                    print ("error en la opccion ingresada")
                    registrar_cita(0)
                else:
                    match (opcion):
                        case 1:
                            tipohora = ("mañana")
                        case 2:
                            tipohora = ("tarde")
                        case _:
                            print ("opciones ingresada no pertence al menu del centro medico")
                            registrar_cita(0)
        except ValueError:
            print ("error en la occion ingresada")
            registrar_cita(0)
        menutipo = ("que tipo de medico necesita \n1 pediatria \n2 ginecologia \n3 dermatologia \n4 endocrinologia \n5 optometria")
        if (op !=6):
            print (title)
            print (menutipo)
            try:
                opcion = int(input(":) "))
            except ValueError:
                print ("error en la opccion ingresada")
                registrar_cita(0)
            else:
                match (opcion):
                    case 1:
                        tipo_de_cita = ("pediatria")
                    case 2:
                        tipo_de_cita = ("ginecologia")
                    case 3:
                        tipo_de_cita = ("dermatologia")
                    case 4:
                        tipo_de_cita = ("endocrinologia")
                    case 5:
                        tipo_de_cita = ("optometria")
                    case _:
                        print ("opciones ingresada no pertence al menu del centro medico")
                        registrar_cita(0)
        print("ingrese a que horas quiere la cita")
        horatipo = ("1 de 7am a 8am \n2 de 8am a 9am \n3 de 9am a 10am \n4 de 10am a 11am \n5 de 11am a 12am \n6 de 1pm a 2pm \n7 de 2pm a 3pm \n8 de 3pm a 4pm n\n9 de 4pm a 5pm \n10 de 5pm a 6pm")
        if (op !=11):
            print (title)
            print (horatipo)
            try:
                opcion = int(input(":) "))
            except ValueError:
                print ("error en la opccion ingresada")
                registrar_cita(0)
            else:
                match (opcion):
                    case 1:
                        horad = ("7am")
                    case 2:
                        horad = ("8ama 9am")
                    case 3:
                        horad = ("9am a 10am")
                    case 4:
                        horad = ("10am a 11am")
                    case 5:
                        horad = ("11am a 12am")
                    case 6 :
                        horad = ("1pm a 2pm")
                    case 7: 
                        horad = ("2pm a 3pm")
                    case 8:
                        horad = ("3pm a 4pm")
                    case 9:
                        horad = ("4pm a 5pm")
                    case 10:
                        horad = ("5pm a 6pm")
                    case _:
                        registrar_cita(0)
        sintomas = input("ingrese sus sintomas, por favor ingrese al menos 3 ")
        print ("formula llenar por el medico")
        tratamiento = input ("ingrese un tratamiento medico para el paciente")
        medicina = input ("ingrese la medicina para el paciente")
        tiempo = input ("ingrese cuanto tiempo se va a demorar el paciente en recuperarse")
        cita = {
            "cedula" : cedula,
            "nombre" : nombre,
            "apellido" : apellido,
            "celular" : celular,
            "genero" : genero,
            "edad" : edad,
            "fechanacimiento" : fechanacimiento,
            "fecha" : fecha,
            "horad" : horad,
            "tipo_de_cita" : tipo_de_cita,
            "tipo_de_hora" : tipohora,
            "dignostico" : {
                "sintomas del paciente" : sintomas,
                "dignostico dado por el doctor" : {
                    "tratamiento" : tratamiento,
                    "medicina" : medicina,
                    "tiempo esperado de curar" : tiempo, 
                    }
                }
            }
        e.agregar_data("data_cita",cedula,cita)
        g.usuario.get("data_cita")
        if(bool(input("desea registrar atra cita S(si) o Enter(no)"))):
            registrar_cita(0)
        else:
            uic.menucitas(0)

def buscar_data():
    criterio = input("ingrese el Nro de la cedula: ")
    data = g.usuario.get("cita")(criterio)
    return data

def modificar_data():
        data_cita = buscar_data()
        cedula,nombre,apellido,celular,genero,edad,fechanacimiento,fecha,tipo_de_cita = data_cita.values()
        for key in data_cita.keys():
            if (key != "cedula" and key != "celular"):
                if (bool(input(f"desea modificar el {key} s(si) o enter (no)"))):
                    buscar_data[key] = input (f"ingrese el nuevo valor para {key} : ")
        g.usuario.get("data_cita").update({cedula:data_cita})
        e.actualizar_file(g.usuario)
        uic.menucitas
