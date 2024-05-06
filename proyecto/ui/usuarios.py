import registros.registro_de_usuarios as rdu
import modules.ejecuta_data_usuario as edu

def menuusuarios(op):
    title = """
    ********************************
    * MENU DE REGISTRO DE USUARIOS *
    ********************************
    """
    menuusuariosop = "1.registrar usuario \n2 cambiar datos registrados \n3 historial \n4 salir"
    if (op != 4):
        print (title)
        print (menuusuariosop)
        try:
            opcion = int(input(":) "))
        except ValueError:
            print ("error en la opccion ingresada")
        else:
            match (opcion):
                case 1:
                    rdu.registrar_usuario(0)
                case 2:
                    rdu.modificar_data_usuarios()
                case 3:
                    import ui.historial as h
                    h.menuhistorial(0)
                case 4:
                    import main
                    main.menuprincipal(0)
                case _:
                    print ("opciones ingrese no pertenece al menu de opcciones")
                    menuusuarios(op)