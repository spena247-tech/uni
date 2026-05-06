import crud
import core
import funcionalidades
import autenticacion as auth
import auth_menu
import os


def limpiar_pantalla():
    """Limpia la pantalla"""
    os.system('cls')


def menu_principal(usuario_sistema: auth.UsuarioSistema, gestor: core.GestorCreditos):
    """Menú principal de la aplicación después de autenticar"""
    
    isMenuActivate = True
    
    while isMenuActivate:
        limpiar_pantalla()
        print("="*60)
        print(f"  OWLNAB CREDIT TRACKER - Sesión: {usuario_sistema.usuario}")
        print(f"  {usuario_sistema.programa} | Semestre: {usuario_sistema.semestre_actual} | {usuario_sistema.modalidad.upper()}")
        print("="*60)
        print("\nFUNCIONALIDADES BASE:")
        print("  1. Registrar materia")
        print("  2. Ver historial de créditos")
        print("  3. Buscar y editar materia")
        print("  4. Eliminar materia")
        print("  5. Calcular promedio")
        print("\nFUNCIONALIDADES ADICIONALES:")
        print("  6. Exportar historial (TXT/CSV)")
        print("  7. Buscar materia por nombre/código")
        print("  8. Ver estadísticas académicas")
        print("  9. Sistema de alertas")
        print("  10. Ver historial de cambios")
        print("  11. Gestionar períodos académicos")
        print("  12. Editar perfil del estudiante")
        print("  13. Comparar rendimiento semestres")
        print("  14. Simulador de carga académica")
        print("  15. Gestionar optativas/obligatorias")
        print("  16. Calendario académico")
        print("  17. Metas académicas personales")
        print("  18. Generar resumen de semestre")
        print("\nOPCIONES DE USUARIO:")
        print("  19. Mi perfil")
        print("  20. Modo administrador")
        print("  21. Cerrar sesión")
        print("  22. Salir del sistema")
        print("="*60)
        
        try:
            op = int(input("Seleccione una opción: "))
        except:
            print("Entrada inválida")
            os.system("pause")
            continue

        # === FUNCIONALIDADES BASE ===
        if op == 1:
            crud.agregar_credito(gestor)

        elif op == 2:
            crud.VerData(gestor)

        elif op == 3:
            crud.BuscarData(gestor)

        elif op == 4:
            crud.BorrarData(gestor)

        elif op == 5:
            crud.calcular_promedio(gestor)
            os.system("pause")

        # === FUNCIONALIDADES ADICIONALES ===
        elif op == 6:
            funcionalidades.exportar_historial(gestor)

        elif op == 7:
            funcionalidades.buscar_materia(gestor)

        elif op == 8:
            funcionalidades.mostrar_estadisticas(gestor)

        elif op == 9:
            funcionalidades.sistema_alertas(gestor)

        elif op == 10:
            funcionalidades.ver_auditoria(gestor)

        elif op == 11:
            funcionalidades.gestionar_periodos(gestor)

        elif op == 12:
            funcionalidades.editar_perfil(gestor)

        elif op == 13:
            funcionalidades.comparar_semestres(gestor)

        elif op == 14:
            funcionalidades.simulador_carga_academica(gestor)

        elif op == 15:
            funcionalidades.gestionar_optativas(gestor)

        elif op == 16:
            funcionalidades.calendario_academico(gestor)

        elif op == 17:
            funcionalidades.sistema_metas(gestor)

        elif op == 18:
            funcionalidades.generar_resumen_semestre(gestor)

        # === OPCIONES DE USUARIO ===
        elif op == 19:
            auth_menu.menu_perfil(usuario_sistema)

        elif op == 20:
            if usuario_sistema.es_admin:
                gestor_usuarios = auth.GestorUsuarios()
                auth_menu.menu_admin(gestor_usuarios)
            else:
                print("✗ Acceso denegado. Solo administradores pueden acceder.")
                input("Presione enter...")

        elif op == 21:
            print("\n¡Hasta luego! Cerrando sesión...")
            isMenuActivate = False
            return None  # Volver al menú de inicio

        elif op == 22:
            confirmacion = input("¿Desea salir del sistema? (S/N): ").upper()
            if confirmacion == "S":
                isMenuActivate = False
                return "SALIR"  # Señal para salir completamente

        else:
            print("Opción inválida")
            os.system("pause")


if __name__ == "__main__":
    # Mostrar bienvenida inicial
    auth_menu.mostrar_bienvenida()
    input("Presione enter para continuar...")
    
    # Loop principal de autenticación
    while True:
        # Menú de autenticación
        usuario_actual = auth_menu.menu_inicio()
        
        if usuario_actual is None:
            # Usuario eligió salir del menú de inicio
            limpiar_pantalla()
            print("¡Hasta luego! Gracias por usar OwlNab Credit Tracker")
            break
        
        # Crear gestor de créditos para el usuario autenticado
        gestor = core.GestorCreditos(usuario_actual.usuario)
        
        # Sincronizar datos del usuario con el gestor
        if not gestor.usuario:
            gestor.usuario = core.Usuario(
                usuario_actual.usuario,
                usuario_actual.programa,
                usuario_actual.semestre_actual,
                creditos_totales=usuario_actual.creditos_totales
            )
        gestor.usuario.modalidad = usuario_actual.modalidad
        gestor.usuario.creditos_totales = usuario_actual.creditos_totales
        gestor.guardar_datos()
        
        # Menú principal de la aplicación
        resultado = menu_principal(usuario_actual, gestor)
        
        if resultado == "SALIR":
            # Usuario eligió salir completamente del sistema
            limpiar_pantalla()
            print("¡Hasta luego! Gracias por usar OwlNab Credit Tracker")
            break
        # Si es None, vuelve al menú de inicio para login/registro
