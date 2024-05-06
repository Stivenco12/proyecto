import registros.historial_de_citas as hdc
import registros.historial_de_medicos as hdm
import registros.historial_de_usuario as hdu
def menuhistorial(op):
    title = """
    *********************
    * MENU DE HISTORIAL *
    *********************
    """
    menucitasop = "1.HISTORIAL DE CITAS \n2 HISTORIAL DE PACIENTE \n3 HISTORIAL DE MEDICO \n4 SALIR AL MENU ANTERIOS "
    if (op != 4):
        print (title)
        print (menucitasop)
        try:
            op = int(input(":) "))
        except ValueError:
            print ("error en la opccion ingresada")
            menuhistorial(0)
        else:
            match (op):
                case 1:
                    hdc.historial_cita(0)
                case 2:
                    hdu.historial_usuarios(0)
                case 3:
                    hdm.historial_medico(0)
                case 4:
                    import main
                    main.menuprincipal(0)
                case _:
                    print ("opciones ingrese no pertenece al menu de opcciones")
                    menuhistorial(op)