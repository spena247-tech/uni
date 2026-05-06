"""
Módulo de interfaz de autenticación
Maneja login, registro y acceso al sistema
"""

import os
import autenticacion as auth

def limpiar_pantalla():
    """Limpia la pantalla"""
    os.system('cls')


def mostrar_bienvenida():
    """Muestra pantalla de bienvenida"""
    limpiar_pantalla()
    print("="*50)
    print("*" + " "*48 + "*")
    print("*" + "  ¡BIENVENIDO A OWLNAB CREDIT TRACKER!  ".center(48) + "*")
    print("*" + " "*48 + "*")
    print("="*50)
    print()


def menu_inicio():
    """Menú principal antes de autenticar"""
    while True:
        limpiar_pantalla()
        print("="*50)
        print("SISTEMA DE AUTENTICACIÓN")
        print("="*50)
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        print("-"*50)
        
        op = input("Seleccione opción: ").strip()
        
        if op == "1":
            user = login()
            if user:
                return user
            # Si login falla, continúa el loop para mostrar menú nuevamente
        elif op == "2":
            registrar()
        elif op == "3":
            return None
        else:
            print("Opción inválida")
            input("Presione enter...")


def login():
    """Interfaz de login"""
    limpiar_pantalla()
    print("="*50)
    print("INICIAR SESIÓN")
    print("="*50)
    
    gestor = auth.GestorUsuarios()
    
    usuario = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()
    
    exito, mensaje = gestor.login(usuario, contraseña)
    
    if exito:
        print(f"\n✓ {mensaje}")
        input("Presione enter...")
        return gestor.usuario_actual
    else:
        print(f"\n✗ {mensaje}")
        input("Presione enter...")
        return None


def registrar():
    """Interfaz de registro"""
    limpiar_pantalla()
    print("="*50)
    print("REGISTRAR NUEVO USUARIO")
    print("="*50)
    
    gestor = auth.GestorUsuarios()
    
    try:
        usuario = input("Usuario (nombre único): ").strip()
        if not usuario:
            print("✗ El usuario no puede estar vacío")
            input("Presione enter...")
            return
        
        correo = input("Correo electrónico: ").strip()
        contraseña = input("Contraseña (mín. 6 caracteres): ").strip()
        programa = input("Programa/Carrera: ").strip()
        semestre = input("Semestre actual (ej: 2025-1): ").strip()
        uid = input("UID/Código de estudiante: ").strip()
        
        try:
            creditos_totales = int(input("Créditos totales de la carrera (ej: 150): ").strip())
            if creditos_totales <= 0:
                print("✗ Los créditos deben ser un número positivo")
                input("Presione enter...")
                return
        except ValueError:
            print("✗ Créditos inválidos")
            input("Presione enter...")
            return
        
        limpiar_pantalla()
        print("="*50)
        print("MODALIDAD DE ESTUDIO")
        print("="*50)
        print("1. Presencial")
        print("2. Virtual")
        print("-"*50)
        
        op_modalidad = input("Seleccione modalidad: ").strip()
        modalidad = "virtual" if op_modalidad == "2" else "presencial"
        
        exito, mensaje = gestor.registrar_usuario(
            usuario, correo, contraseña, semestre, uid, modalidad, programa, creditos_totales
        )
        
        if exito:
            # El programa ya se guardó en registrar_usuario
            pass
        
        limpiar_pantalla()
        if exito:
            print("✓ " + mensaje)
            print("\nPuede iniciar sesión ahora")
        else:
            print("✗ " + mensaje)
        
        input("Presione enter...")
        
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        input("Presione enter...")


def menu_perfil(usuario: auth.UsuarioSistema):
    """Menú de gestión de perfil"""
    while True:
        limpiar_pantalla()
        print("="*50)
        print("MIS DATOS")
        print("="*50)
        print(f"Usuario: {usuario.usuario}")
        print(f"Correo: {usuario.correo}")
        print(f"Semestre: {usuario.semestre}")
        print(f"UID: {usuario.uid}")
        print(f"Modalidad: {usuario.modalidad}")
        print(f"Registrado: {usuario.fecha_registro}")
        print("="*50)
        print("1. Editar semestre")
        print("2. Editar modalidad")
        print("3. Cambiar contraseña")
        print("4. Volver")
        print("-"*50)
        
        op = input("Seleccione opción: ").strip()
        
        if op == "1":
            nuevo_semestre = input("Nuevo semestre: ").strip()
            if nuevo_semestre:
                gestor = auth.GestorUsuarios()
                gestor.actualizar_usuario(usuario.usuario, semestre=nuevo_semestre)
                usuario.semestre = nuevo_semestre
                print("✓ Semestre actualizado")
                input("Presione enter...")
        
        elif op == "2":
            limpiar_pantalla()
            print("Seleccione modalidad:")
            print("1. Presencial")
            print("2. Virtual")
            op_mod = input("> ").strip()
            nueva_modalidad = "virtual" if op_mod == "2" else "presencial"
            gestor = auth.GestorUsuarios()
            gestor.actualizar_usuario(usuario.usuario, modalidad=nueva_modalidad)
            usuario.modalidad = nueva_modalidad
            print("✓ Modalidad actualizada")
            input("Presione enter...")
        
        elif op == "3":
            cambiar_contraseña(usuario)
        
        elif op == "4":
            break
        
        else:
            print("Opción inválida")
            input("Presione enter...")


def cambiar_contraseña(usuario: auth.UsuarioSistema):
    """Interfaz para cambiar contraseña"""
    limpiar_pantalla()
    print("="*50)
    print("CAMBIAR CONTRASEÑA")
    print("="*50)
    
    contraseña_actual = input("Contraseña actual: ").strip()
    contraseña_nueva = input("Nueva contraseña: ").strip()
    confirmar = input("Confirmar nueva contraseña: ").strip()
    
    if contraseña_nueva != confirmar:
        print("\n✗ Las contraseñas no coinciden")
        input("Presione enter...")
        return
    
    gestor = auth.GestorUsuarios()
    exito, mensaje = gestor.cambiar_contraseña(usuario.usuario, contraseña_actual, contraseña_nueva)
    
    print(f"\n{'✓' if exito else '✗'} {mensaje}")
    input("Presione enter...")


def menu_admin(gestor_usuarios: auth.GestorUsuarios):
    """Menú de administrador"""
    while True:
        limpiar_pantalla()
        print("="*50)
        print("PANEL DE ADMINISTRADOR")
        print("="*50)
        print("1. Ver todos los usuarios")
        print("2. Crear usuario (admin)")
        print("3. Eliminar usuario")
        print("4. Ver estadísticas generales")
        print("5. Volver")
        print("-"*50)
        
        op = input("Seleccione opción: ").strip()
        
        if op == "1":
            ver_todos_usuarios(gestor_usuarios)
        
        elif op == "2":
            crear_usuario_admin(gestor_usuarios)
        
        elif op == "3":
            eliminar_usuario_admin(gestor_usuarios)
        
        elif op == "4":
            ver_estadisticas_admin(gestor_usuarios)
        
        elif op == "5":
            break
        
        else:
            print("Opción inválida")
            input("Presione enter...")


def ver_todos_usuarios(gestor: auth.GestorUsuarios):
    """Ver lista de todos los usuarios"""
    limpiar_pantalla()
    print("="*50)
    print("LISTA DE USUARIOS")
    print("="*50)
    
    usuarios = gestor.obtener_todos_usuarios()
    
    if not usuarios:
        print("No hay usuarios registrados")
    else:
        print(f"{'Usuario':<15} {'Correo':<25} {'Semestre':<10} {'Modalidad':<12}")
        print("-"*62)
        for u in usuarios:
            modalidad_str = "Presencial" if u.modalidad == "presencial" else "Virtual"
            print(f"{u.usuario:<15} {u.correo:<25} {u.semestre:<10} {modalidad_str:<12}")
    
    print("-"*50)
    input("Presione enter...")


def crear_usuario_admin(gestor: auth.GestorUsuarios):
    """Crear usuario como administrador"""
    limpiar_pantalla()
    print("="*50)
    print("CREAR NUEVO USUARIO (ADMIN)")
    print("="*50)
    
    usuario = input("Usuario: ").strip()
    correo = input("Correo: ").strip()
    contraseña = input("Contraseña: ").strip()
    programa = input("Programa/Carrera: ").strip()
    semestre = input("Semestre: ").strip()
    uid = input("UID: ").strip()
    
    print("\nModalidad:")
    print("1. Presencial")
    print("2. Virtual")
    op = input("> ").strip()
    modalidad = "virtual" if op == "2" else "presencial"
    
    exito, mensaje = gestor.registrar_usuario(usuario, correo, contraseña, semestre, uid, modalidad, programa)
    
    print(f"\n{'✓' if exito else '✗'} {mensaje}")
    input("Presione enter...")


def eliminar_usuario_admin(gestor: auth.GestorUsuarios):
    """Eliminar usuario como administrador"""
    limpiar_pantalla()
    print("="*50)
    print("ELIMINAR USUARIO")
    print("="*50)
    
    usuario = input("Nombre de usuario a eliminar: ").strip()
    
    if usuario == "admin":
        print("✗ No se puede eliminar el usuario admin")
    else:
        confirmacion = input(f"¿Confirma eliminación de '{usuario}'? (S/N): ").upper()
        
        if confirmacion == "S":
            if gestor.eliminar_usuario(usuario):
                print("✓ Usuario eliminado")
            else:
                print("✗ No se pudo eliminar el usuario")
        else:
            print("Operación cancelada")
    
    input("Presione enter...")


def ver_estadisticas_admin(gestor: auth.GestorUsuarios):
    """Ver estadísticas generales del sistema"""
    limpiar_pantalla()
    print("="*50)
    print("ESTADÍSTICAS DEL SISTEMA")
    print("="*50)
    
    usuarios = gestor.obtener_todos_usuarios()
    total_usuarios = len(usuarios)
    usuarios_presenciales = sum(1 for u in usuarios if u.modalidad == "presencial")
    usuarios_virtuales = sum(1 for u in usuarios if u.modalidad == "virtual")
    
    print(f"Total de usuarios: {total_usuarios}")
    print(f"Usuarios presenciales: {usuarios_presenciales}")
    print(f"Usuarios virtuales: {usuarios_virtuales}")
    print("-"*50)
    
    input("Presione enter...")
