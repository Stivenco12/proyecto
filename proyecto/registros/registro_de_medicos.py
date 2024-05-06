import json
import os
import registros.globales as g
import modules.ejecuta_data_medico as e
import ui.medicos as uim
def registrar_medico(op):
        title = """
        **********************
        * REGISTRO DE MEDICO *
        **********************
        """
        g.borrar_pantalla()
        print(title)
        try:        
            cedula = int(input ("ingrese Nmr de la cedula"))
            nombre = input ("ingrese su nombre")
            apellido = input ("ingrese su apellido")
            celular = int(input ("ingrese su numero telefonico"))
            correo = input ("ingrese su correo por favor")
            edad = int(input("ingrese su edad"))
            menuhora = ("cual es su genero \n1 HOMBRE \n2 MUJER \n3 OTRO")
            if (op !=3):
                print (title)
                print (menuhora)
                try:
                    opcion = int(input(":) "))
                except ValueError:
                    print ("error en la opcion ingresada")
                    registrar_medico(0)
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
                            registrar_medico(0)
            fechanacimiento = input("ingrese la fecha de su nacimiento dia/mes/año")
        except ValueError:
            print ("error en la opccion ingresada")
            registrar_medico(0)
        menuhora = ("que tipo de medico es \n1 pediatria \n2 ginecologia \n3 dermatologia \n4 endocrinologia \n5 optometria")
        if (op !=6):
            print (title)
            print (menuhora)
            try:
                opcion = int(input(":) "))
            except ValueError:
                print ("error en la opccion ingresada")
                registrar_medico(0)
            else:
                match (opcion):
                    case 1:
                        tipo = ("pediatria")
                    case 2:
                        tipo = ("ginecologia")
                    case 3:
                        tipo = ("dermatologia")
                    case 4:
                        tipo = ("endocrinologia")
                    case 5:
                        tipo = ("optometria")
                    case _:
                        print ("opciones ingresada no pertence al menu del centro medico")
                        registrar_medico(0)
        menuhora = ("que hora de trabajo tiene disponible \n1 7a.m a 12 a.m (mañana)\n2 1p.m a 6 a.m (tarde)")
        if (op !=2):
            print (title)
            print (menuhora)
            try:
                opcion = int(input(":) "))
            except ValueError:
                print ("error en la opccion ingresada")
                registrar_medico(0)
            else:
                match (opcion):
                    case 1:
                        tipohora = ("mañana")
                    case 2:
                        tipohora = ("tarde")
                    case _:
                        print ("opciones ingresada no pertence al menu del centro medico")
                        registrar_medico(0)
            medico = {
            "cedula" : cedula,
            "nombre" : nombre,
            "apellido" : apellido,
            "correo" : correo,
            "celular" : celular,
            "genero" : genero,
            "edad" : edad,
            "fechanacimiento" : fechanacimiento,
            "tipo_de_cita" : tipo,
            "tipo_de_hora" : tipohora,
            }
            e.agregar_data("data_medico",cedula,medico)
            g.centro_medico.get("data_medico")
            if(bool(input("desea registrar otro medico S(si) o Enter(no)"))):
                registrar_medico(0)
            else:
                uim.menumedicos(0)

def buscar_data_medico():
    criterio = input("ingrese el Nro de la cedula: ")
    data = g.usuario.get("data").get(criterio)
    return data

def modificar_data_medico():
    data_medico = buscar_data_medico()
    cedula,nombre,apellido,celular,genero,edad,fechanacimiento,tipo= data_medico.values()
    for key in data_medico.keys():
        if (key != "cedula" and key != "celular"):
            if (bool(input(f"desea modificar el {key} s(si) o enter (no)"))):
                buscar_data_medico[key] = input (f"ingrese el nuevo valor para {key} : ")
    g.usuario.get("data").update({cedula:data_medico})
    e.actualizar_archivo(g.usuario)
    uim.menumedicos