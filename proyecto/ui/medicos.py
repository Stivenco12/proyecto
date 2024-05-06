import registros.registro_de_medicos as rdm
import modules.ejecuta_data_medico as edm
import registros.historial_de_medicos as hdm
def menumedicos(op):
        title = """
    *******************************
    * MENU DE REGISTRO DE MEDICOS *
    *******************************
    """
        menumedicosop = "1 resgistrar medicos \n2 eliminar medicos \n3 registrar citas  \n4 salir"
        if (op !=4):
                print (title)
                print (menumedicosop)
                try:
                    opcion = int(input(":) "))
                except ValueError:
                    print ("error en la opcion ingresada ")
                else:
                    match (opcion):
                        case 1:
                            rdm.registrar_medico(op)
                        case 2:
                            hdm.eliminar_datos(0)
                        case 3:
                            import ui.citas as c
                            c.menucitas(0)
                        case 4:
                            print ("regrese pronto.......")
                            import main
                            main.menuprincipal(0)
                        case _:
                            print ("opciones ingresada no pertenece al menu de opcciones")
                            menumedicos(op)
