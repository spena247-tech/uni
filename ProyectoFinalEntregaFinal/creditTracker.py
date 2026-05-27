import credit_actions
import credit_models
import academic_features
import autenticacion as auth
import auth_menu
import os

# Creadores del software
CREADORES = [
    "Sebastian Peña Arevalo",
    "Sofia Mantilla Castellanos",
    "Isabella Suarez Leon",
]


def limpiar_pantalla():
    """Limpia la pantalla"""
    os.system('cls')


def menu_principal(usuario_sistema: auth.UsuarioSistema, gestor: credit_models.GestorCreditos):
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
            credit_actions.agregar_credito(gestor)

        elif op == 2:
            credit_actions.VerData(gestor)

        elif op == 3:
            credit_actions.BuscarData(gestor)

        elif op == 4:
            credit_actions.BorrarData(gestor)

        elif op == 5:
            credit_actions.calcular_promedio(gestor)
            os.system("pause")

        # === FUNCIONALIDADES ADICIONALES ===
        elif op == 6:
            academic_features.exportar_historial(gestor)

        elif op == 7:
            academic_features.buscar_materia(gestor)

        elif op == 8:
            academic_features.mostrar_estadisticas(gestor)

        elif op == 9:
            academic_features.sistema_alertas(gestor)

        elif op == 10:
            academic_features.ver_auditoria(gestor)

        elif op == 11:
            academic_features.gestionar_periodos(gestor)

        elif op == 12:
            academic_features.editar_perfil(gestor)

        elif op == 13:
            academic_features.comparar_semestres(gestor)

        elif op == 14:
            academic_features.simulador_carga_academica(gestor)

        elif op == 15:
            academic_features.gestionar_optativas(gestor)

        elif op == 16:
            academic_features.calendario_academico(gestor)

        elif op == 17:
            academic_features.sistema_metas(gestor)

        elif op == 18:
            academic_features.generar_resumen_semestre(gestor)

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


def menu_funcionalidades_base(usuario_sistema: auth.UsuarioSistema, gestor: credit_models.GestorCreditos):
    """Submenú: funcionalidades base"""
    while True:
        limpiar_pantalla()
        print("-- FUNCIONALIDADES BASE --")
        print("1. Registrar materia")
        print("2. Ver historial de créditos")
        print("3. Buscar y editar materia")
        print("4. Eliminar materia")
        print("5. Calcular promedio")
        print("0. Volver")
        try:
            op = int(input("Seleccione una opción: "))
        except:
            print("Entrada inválida")
            os.system("pause")
            continue

        if op == 1:
            credit_actions.agregar_credito(gestor)
        elif op == 2:
            credit_actions.VerData(gestor)
        elif op == 3:
            credit_actions.BuscarData(gestor)
        elif op == 4:
            credit_actions.BorrarData(gestor)
        elif op == 5:
            credit_actions.calcular_promedio(gestor)
            os.system("pause")
        elif op == 0:
            break
        else:
            print("Opción inválida")
            os.system("pause")


def menu_funcionalidades_adicionales(usuario_sistema: auth.UsuarioSistema, gestor: credit_models.GestorCreditos, creadores):
    """Submenú: funcionalidades adicionales"""
    while True:
        limpiar_pantalla()
        print("-- FUNCIONALIDADES ADICIONALES --")
        print("1. Exportar historial (TXT/CSV)")
        print("2. Buscar materia por nombre/código")
        print("3. Ver estadísticas académicas")
        print("4. Sistema de alertas")
        print("5. Ver historial de cambios")
        print("6. Gestionar períodos académicos")
        print("7. Editar perfil del estudiante")
        print("8. Comparar rendimiento semestres")
        print("9. Simulador de carga académica")
        print("10. Gestionar optativas/obligatorias")
        print("11. Calendario académico")
        print("12. Metas académicas personales")
        print("13. Generar resumen de semestre")
        print("14. Creadores (info detallada)")
        print("0. Volver")

        op = input("Seleccione una opción: ").strip()

        if op == "1":
            academic_features.exportar_historial(gestor)
        elif op == "2":
            academic_features.buscar_materia(gestor)
        elif op == "3":
            academic_features.mostrar_estadisticas(gestor)
        elif op == "4":
            academic_features.sistema_alertas(gestor)
        elif op == "5":
            academic_features.ver_auditoria(gestor)
        elif op == "6":
            academic_features.gestionar_periodos(gestor)
        elif op == "7":
            academic_features.editar_perfil(gestor)
        elif op == "8":
            academic_features.comparar_semestres(gestor)
        elif op == "9":
            academic_features.simulador_carga_academica(gestor)
        elif op == "10":
            academic_features.gestionar_optativas(gestor)
        elif op == "11":
            academic_features.calendario_academico(gestor)
        elif op == "12":
            academic_features.sistema_metas(gestor)
        elif op == "13":
            academic_features.generar_resumen_semestre(gestor)
        elif op == "14":
            # Mostrar información detallada de los creadores
            universidad = "Universidad Autonoma de Bucaramanga (UNAB)"
            programa = "Ingeniería de Sistemas"
            semestre = "2do semestre"
            profesor = "Julian Santoyo (Programación de Computadores)"
            academic_features.mostrar_creadores_detallado(creadores, programa, universidad, semestre, profesor)
        elif op == "0":
            break
        else:
            print("Opción inválida")
            os.system("pause")


def menu_opciones_usuario(usuario_sistema: auth.UsuarioSistema, gestor: credit_models.GestorCreditos):
    """Submenú: opciones de usuario"""
    while True:
        limpiar_pantalla()
        print("-- OPCIONES DE USUARIO --")
        print("1. Mi perfil")
        print("2. Modo administrador")
        print("3. Cerrar sesión")
        print("0. Volver")

        op = input("Seleccione una opción: ").strip()

        if op == "1":
            auth_menu.menu_perfil(usuario_sistema)
        elif op == "2":
            if usuario_sistema.es_admin:
                gestor_usuarios = auth.GestorUsuarios()
                auth_menu.menu_admin(gestor_usuarios)
            else:
                print("✗ Acceso denegado. Solo administradores pueden acceder.")
                input("Presione enter...")
        elif op == "3":
            print("\n¡Hasta luego! Cerrando sesión...")
            return None
        elif op == "0":
            break
        else:
            print("Opción inválida")
            os.system("pause")


def menu_general(usuario_sistema: auth.UsuarioSistema, gestor: credit_models.GestorCreditos):
    """Menú general que divide la aplicación en tres submenús."""
    while True:
        limpiar_pantalla()
        print("="*60)
        print("  OWLNAB CREDIT TRACKER - Menú General")
        print("="*60)
        print("1. Funcionalidades base")
        print("2. Funcionalidades adicionales")
        print("3. Opciones de usuario")
        print("4. Cerrar sesión")
        print("5. Salir del sistema")
        print("="*60)

        try:
            op = int(input("Seleccione una opción: "))
        except:
            print("Entrada inválida")
            os.system("pause")
            continue

        if op == 1:
            menu_funcionalidades_base(usuario_sistema, gestor)
        elif op == 2:
            menu_funcionalidades_adicionales(usuario_sistema, gestor, CREADORES)
        elif op == 3:
            resultado = menu_opciones_usuario(usuario_sistema, gestor)
            if resultado is None:
                return None
        elif op == 4:
            print("\n¡Hasta luego! Cerrando sesión...")
            return None
        elif op == 5:
            confirmacion = input("¿Desea salir del sistema? (S/N): ").upper()
            if confirmacion == "S":
                return "SALIR"
        else:
            print("Opción inválida")
            os.system("pause")


if __name__ == "__main__":
    # Mostrar bienvenida inicial (incluye creadores y datos del equipo)
    auth_menu.mostrar_bienvenida(
        CREADORES,
        programa="Ingeniería de Sistemas",
        universidad="Universidad Autonoma de Bucaramanga (UNAB)",
        semestre="2do semestre",
        profesor="Julian Santoyo (Programación de Computadores)"
    )
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
        gestor = credit_models.GestorCreditos(usuario_actual.usuario)
        
        # Sincronizar datos del usuario con el gestor
        if not gestor.usuario:
            gestor.usuario = credit_models.Usuario(
                usuario_actual.usuario,
                usuario_actual.programa,
                usuario_actual.semestre_actual,
                creditos_totales=usuario_actual.creditos_totales
            )
        gestor.usuario.modalidad = usuario_actual.modalidad
        gestor.usuario.creditos_totales = usuario_actual.creditos_totales
        gestor.guardar_datos()
        
        # Menú principal de la aplicación (ahora menú general con submenús)
        resultado = menu_general(usuario_actual, gestor)
        
        if resultado == "SALIR":
            # Usuario eligió salir completamente del sistema
            limpiar_pantalla()
            print("¡Hasta luego! Gracias por usar OwlNab Credit Tracker")
            break
        # Si es None, vuelve al menú de inicio para login/registro