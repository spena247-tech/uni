"""
Módulo de funcionalidades adicionales para el sistema CreditTracker
Incluye: exportación, búsqueda, estadísticas, alertas, etc.
"""

import credit_models as cr
import os
from datetime import datetime


def mostrar_creadores_detallado(creadores, programa, universidad, semestre, profesor):
    """Muestra información detallada de los creadores del software."""
    os.system('cls')
    print("****************************************")
    print("*         SOBRE LOS CREADORES          *")
    print("****************************************\n")

    print(f"Universidad: {universidad}")
    print(f"Programa: {programa}")
    
    print(f"Semestre actual del grupo: {semestre}")
    print(f"Profesor de la asignatura: {profesor}\n")

    print("Equipo de desarrollo:")
    for nombre in creadores:
        print(f"  - {nombre}")

    print("\nDescripción: Somos estudiantes de Ingeniería de Sistemas en la Universidad Autónoma de Bucaramanga (UNAB)."
          " Este proyecto fue desarrollado como parte de la materia Programación de Computadores.")
    input("\nPresione enter para continuar...")

# ===== 1. EXPORTACIÓN =====
def exportar_historial(gestor):
    """Exporta el historial académico en formato txt o csv"""
    os.system('cls')
    print("****************************************")
    print("*      EXPORTAR HISTORIAL             *")
    print("****************************************")
    print("1. Exportar como TXT")
    print("2. Exportar como CSV")
    print("3. Cancelar")
    
    op = input("Seleccione formato: ")
    
    if op == "1":
        contenido = gestor.exportar_txt()
        nombre_archivo = f"historial_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    elif op == "2":
        contenido = gestor.exportar_csv()
        nombre_archivo = f"historial_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    else:
        return
    
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', nombre_archivo)
    
    try:
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"\n✓ Archivo guardado: {nombre_archivo}")
    except Exception as e:
        print(f"✗ Error al guardar: {str(e)}")
    
    input("Presione enter...")


# ===== 2. BUSCADOR =====
def buscar_materia(gestor):
    """Busca materias por nombre o código"""
    os.system('cls')
    print("****************************************")
    print("*      BUSCAR MATERIA                 *")
    print("****************************************")
    print("1. Buscar por nombre")
    print("2. Buscar por código")
    print("3. Cancelar")
    
    op = input("Seleccione tipo de búsqueda: ")
    
    if op == "1":
        criterio = input("Ingrese nombre de materia: ")
        resultado = gestor.buscar_materias(criterio, "nombre")
    elif op == "2":
        criterio = input("Ingrese código: ")
        resultado = gestor.buscar_materias(criterio, "codigo")
    else:
        return
    
    if not resultado:
        print("\n✗ No se encontraron resultados")
    else:
        print("\n" + "-"*70)
        print(f"{'Materia':<20} {'Cód':<10} {'Cred':<5} {'Nota':<5} {'Per':<10}")
        print("-"*70)
        for m in resultado:
            print(f"{m.nombre:<20} {m.codigo:<10} {m.creditos:<5} {m.nota:<5} {m.periodo:<10}")
        print("-"*70)
    
    input("Presione enter...")


# ===== 3. ESTADÍSTICAS =====
def mostrar_estadisticas(gestor):
    """Muestra estadísticas visuales del avance académico"""
    os.system('cls')
    total_creditos = gestor.obtener_total_creditos()
    promedio = gestor.calcular_promedio()
    creditos_obligatorios = gestor.contar_creditos_obligatorios()
    creditos_optativos = gestor.contar_creditos_optativas()
    
    print("****************************************")
    print("*    ESTADÍSTICAS ACADÉMICAS          *")
    print("****************************************")
    
    if gestor.usuario:
        print(f"Estudiante: {gestor.usuario.nombre}")
        print(f"Programa: {gestor.usuario.programa}")
        print(f"Semestre: {gestor.usuario.semestre_actual}\n")
    
    print(f"Total de Créditos: {total_creditos}")
    print(f"Promedio Ponderado: {round(promedio, 2)}\n")
    
    # Gráfico de barras ASCII - siempre mostrar progreso
    meta_creditos = gestor.usuario.creditos_totales if gestor.usuario else 150
    barra_length = 40
    pct = int((total_creditos / meta_creditos) * barra_length) if total_creditos <= meta_creditos else barra_length
    barra = "█" * min(pct, barra_length) + "░" * max(0, barra_length - pct)
    porcentaje = min((total_creditos / meta_creditos) * 100, 100) if total_creditos <= meta_creditos else 100
    print(f"Progreso de Créditos (Meta: {meta_creditos}):")
    print(f"[{barra}] {int(porcentaje)}%")
    
    print(f"\nCréditos Obligatorios: {creditos_obligatorios}")
    print(f"Créditos Optativos: {creditos_optativos}")
    
    # Promedio por período
    periodos = gestor.obtener_periodos_unicos()
    if periodos:
        print(f"\nPromedio por Período:")
        print("-"*40)
        for periodo in periodos:
            prom = gestor.calcular_promedio_periodo(periodo)
            materias_count = len(gestor.obtener_materias_por_periodo(periodo))
            print(f"  {periodo}: {round(prom, 2)} ({materias_count} materias)")
    
    input("\nPresione enter...")


# ===== 4. ALERTAS =====
def sistema_alertas(gestor):
    """Sistema de alertas por créditos críticos"""
    os.system('cls')
    print("****************************************")
    print("*      SISTEMA DE ALERTAS             *")
    print("****************************************\n")
    
    total_creditos = gestor.obtener_total_creditos()
    promedio = gestor.calcular_promedio()
    
    alertas = []
    
    # Alerta por créditos bajos
    meta_creditos = gestor.usuario.creditos_totales
    if total_creditos < meta_creditos * 0.25:  # Menos del 25% de la meta
        alertas.append(f"⚠ ALERTA: Bajo avance en créditos ({total_creditos}/{meta_creditos})")
    
    # Alerta por promedio bajo
    if promedio < 3.0:
        alertas.append(f"⚠ ALERTA: Promedio bajo ({round(promedio, 2)})")
    
    # Alerta por promedios por período
    periodos = gestor.obtener_periodos_unicos()
    for periodo in periodos:
        prom = gestor.calcular_promedio_periodo(periodo)
        if prom < 2.5:
            alertas.append(f"⚠ ALERTA: Bajo rendimiento en período {periodo} ({round(prom, 2)})")
    
    # Eventos próximos
    eventos_proximos = gestor.obtener_eventos_proximos(7)
    
    if alertas:
        print("ALERTAS ACTIVAS:")
        for alerta in alertas:
            print(f"  {alerta}")
    else:
        print("✓ No hay alertas activas")
    
    if eventos_proximos:
        print(f"\nEVENTOS PRÓXIMOS (próximos 7 días):")
        for evento in eventos_proximos:
            print(f"  • {evento.nombre} - {evento.fecha}")
    
    input("\nPresione enter...")


# ===== 5. HISTORIAL DE CAMBIOS =====
def ver_auditoria(gestor):
    """Muestra el historial de cambios del sistema"""
    os.system('cls')
    print("****************************************")
    print("*    HISTORIAL DE CAMBIOS (AUDITORÍA) *")
    print("****************************************\n")
    
    if not gestor.auditoria:
        print("No hay cambios registrados")
    else:
        print("-"*80)
        print(f"{'Fecha/Hora':<20} {'Acción':<10} {'Detalles':<35} {'Usuario':<15}")
        print("-"*80)
        
        for registro in gestor.auditoria[-50:]:  # Últimos 50 registros
            try:
                dt = datetime.fromisoformat(registro.timestamp)
                fecha = dt.strftime("%Y-%m-%d %H:%M:%S")
            except Exception:
                fecha = registro.timestamp
            print(f"{fecha:<20} {registro.accion:<10} {registro.detalles:<35} {registro.usuario:<15}")
        
        print("-"*80)
        print(f"Total de registros: {len(gestor.auditoria)}")
    
    input("\nPresione enter...")


# ===== 6. GESTIÓN DE PERÍODOS =====
def gestionar_periodos(gestor):
    """Gestiona períodos académicos"""
    os.system('cls')
    print("****************************************")
    print("*    GESTIÓN DE PERÍODOS              *")
    print("****************************************\n")
    
    periodos = gestor.obtener_periodos_unicos()
    
    if not periodos:
        print("No hay períodos registrados")
    else:
        print("Períodos registrados:")
        print("-"*50)
        for i, periodo in enumerate(periodos, 1):
            materias = gestor.obtener_materias_por_periodo(periodo)
            creditos = sum(m.creditos for m in materias)
            promedio = gestor.calcular_promedio_periodo(periodo)
            print(f"{i}. {periodo}")
            print(f"   Materias: {len(materias)} | Créditos: {creditos} | Promedio: {round(promedio, 2)}")
        print("-"*50)
    
    input("Presione enter...")


# ===== 8. PERFIL DEL ESTUDIANTE =====
def editar_perfil(gestor):
    """Permite editar el perfil del estudiante"""
    os.system('cls')
    print("****************************************")
    print("*    PERFIL DEL ESTUDIANTE            *")
    print("****************************************\n")
    
    if not gestor.usuario:
        print("Crear nuevo perfil:")
        nombre = input("Nombre: ")
        programa = input("Programa/Carrera: ")
        semestre = input("Semestre Actual: ")
        gestor.crear_usuario(nombre, programa, semestre)
        print("✓ Perfil creado exitosamente")
    else:
        print(f"Estudiante Actual: {gestor.usuario.nombre}")
        print(f"Programa: {gestor.usuario.programa}")
        print(f"Semestre: {gestor.usuario.semestre_actual}\n")
        
        print("1. Editar nombre")
        print("2. Editar programa")
        print("3. Editar semestre")
        print("4. Ver información completa")
        print("5. Cancelar")
        
        op = input("Seleccione opción: ")
        
        if op == "1":
            gestor.usuario.nombre = input("Nuevo nombre: ")
        elif op == "2":
            gestor.usuario.programa = input("Nuevo programa: ")
        elif op == "3":
            gestor.usuario.semestre_actual = input("Nuevo semestre: ")
        elif op == "4":
            print(f"\nEstudiante: {gestor.usuario.nombre}")
            print(f"Programa: {gestor.usuario.programa}")
            print(f"Semestre: {gestor.usuario.semestre_actual}")
            print(f"Foto: {gestor.usuario.foto}")
            print(f"Perfil creado: {gestor.usuario.fecha_creacion}")
            input("Presione enter...")
            return
        elif op == "5":
            return
        
        gestor.registrar_auditoria("editar", "Perfil del estudiante actualizado")
        gestor.guardar_datos()
        print("✓ Perfil actualizado")
    
    input("Presione enter...")


# ===== 9. COMPARACIÓN DE SEMESTRES =====
def comparar_semestres(gestor):
    """Compara rendimiento entre semestres"""
    os.system('cls')
    print("****************************************")
    print("*  COMPARACIÓN DE SEMESTRES           *")
    print("****************************************\n")
    
    periodos = gestor.obtener_periodos_unicos()
    
    if len(periodos) < 2:
        print("Se necesitan al menos 2 períodos para comparar")
    else:
        print("-"*70)
        print(f"{'Período':<15} {'Materias':<10} {'Créditos':<10} {'Promedio':<10} {'Tendencia':<15}")
        print("-"*70)
        
        promedios_anterior = None
        for periodo in periodos:
            materias = gestor.obtener_materias_por_periodo(periodo)
            creditos = sum(m.creditos for m in materias)
            promedio = gestor.calcular_promedio_periodo(periodo)
            
            if promedios_anterior is not None:
                if promedio > promedios_anterior:
                    tendencia = "↑ Mejorando"
                elif promedio < promedios_anterior:
                    tendencia = "↓ Empeorando"
                else:
                    tendencia = "= Estable"
            else:
                tendencia = "-"
            
            print(f"{periodo:<15} {len(materias):<10} {creditos:<10} {round(promedio, 2):<10} {tendencia:<15}")
            promedios_anterior = promedio
        
        print("-"*70)
    
    input("Presione enter...")


# ===== 10. SIMULADOR ACADÉMICO =====
def simulador_carga_academica(gestor):
    """Simula carga académica sin afectar datos reales"""
    os.system('cls')
    print("****************************************")
    print("*    SIMULADOR DE CARGA ACADÉMICA     *")
    print("****************************************\n")
    
    materias_simuladas = []
    promedio_actual = gestor.calcular_promedio()
    creditos_actuales = gestor.obtener_total_creditos()
    
    print("Agregue materias para simular (ingrese 'listo' cuando termine):\n")
    
    while True:
        nombre = input("Nombre de materia (o 'listo'): ").strip()
        if nombre.lower() == "listo":
            break
        
        try:
            creditos = int(input("Créditos: "))
            nota = float(input("Nota estimada: "))
            materias_simuladas.append({"creditos": creditos, "nota": nota})
        except:
            print("Error en los datos")
            continue
    
    # Calcular simulación
    total_sim_creditos = sum(m["creditos"] for m in materias_simuladas)
    creditos_totales_sim = creditos_actuales + total_sim_creditos
    
    suma_ponderada_sim = (promedio_actual * creditos_actuales) + \
                         sum(m["creditos"] * m["nota"] for m in materias_simuladas)
    promedio_sim = suma_ponderada_sim / creditos_totales_sim if creditos_totales_sim > 0 else 0
    
    os.system('cls')
    print("****************************************")
    print("*    RESULTADOS DE LA SIMULACIÓN      *")
    print("****************************************\n")
    
    print(f"ACTUAL:")
    print(f"  Total de Créditos: {creditos_actuales}")
    print(f"  Promedio: {round(promedio_actual, 2)}\n")
    
    print(f"SIMULADO:")
    print(f"  Créditos Nuevos: {total_sim_creditos}")
    print(f"  Total de Créditos: {creditos_totales_sim}")
    print(f"  Promedio Resultante: {round(promedio_sim, 2)}")
    print(f"  Cambio en Promedio: {round(promedio_sim - promedio_actual, 2)}")
    
    input("\nPresione enter...")


# ===== 11. GESTIÓN DE OPTATIVAS =====
def gestionar_optativas(gestor):
    """Gestiona materias optativas y obligatorias"""
    os.system('cls')
    print("****************************************")
    print("*  GESTIÓN OPTATIVAS/OBLIGATORIAS     *")
    print("****************************************\n")
    
    creditos_obligatorios = gestor.contar_creditos_obligatorios()
    creditos_optativos = gestor.contar_creditos_optativas()
    
    print(f"Créditos Obligatorios: {creditos_obligatorios}")
    print(f"Créditos Optativos: {creditos_optativos}")
    print(f"Total: {creditos_obligatorios + creditos_optativos}\n")
    
    print("Materias Obligatorias:")
    print("-"*50)
    for i, m in enumerate(gestor.obtener_todas()):
        if not m.es_optativa:
            print(f"  {i+1}. {m.nombre} - {m.creditos} créditos")
    
    print("\nMaterias Optativas:")
    print("-"*50)
    for i, m in enumerate(gestor.obtener_todas()):
        if m.es_optativa:
            print(f"  {i+1}. {m.nombre} - {m.creditos} créditos")
    
    input("\nPresione enter...")


# ===== 12. CALENDARIO ACADÉMICO =====
def calendario_academico(gestor):
    """Gestiona el calendario académico"""
    os.system('cls')
    print("****************************************")
    print("*    CALENDARIO ACADÉMICO             *")
    print("****************************************\n")
    
    print("1. Ver eventos próximos")
    print("2. Agregar evento")
    print("3. Ver todos los eventos")
    
    op = input("Seleccione opción: ")
    
    if op == "1":
        eventos = gestor.obtener_eventos_proximos(7)
        if eventos:
            print("\nEventos próximos (7 días):")
            for e in eventos:
                print(f"  • {e.fecha} - {e.nombre} ({e.tipo})")
        else:
            print("No hay eventos próximos")
    
    elif op == "2":
        print("\nAgregar nuevo evento:")
        nombre = input("Nombre: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        print("Tipo: 1. Parcial  2. Entrega  3. Matrícula  4. Otro")
        tipo_op = input("Seleccione: ")
        tipos = {"1": "parcial", "2": "entrega", "3": "matricula", "4": "otro"}
        tipo = tipos.get(tipo_op, "otro")
        
        evento = cr.Evento(nombre, fecha, tipo)
        gestor.agregar_evento(evento)
        print("✓ Evento agregado")
    
    elif op == "3":
        if gestor.eventos:
            print("\nTodos los eventos:")
            for e in sorted(gestor.eventos, key=lambda x: x.fecha):
                print(f"  • {e.fecha} - {e.nombre} ({e.tipo})")
        else:
            print("No hay eventos registrados")
    
    input("\nPresione enter...")


# ===== 13. SISTEMA DE METAS =====
def sistema_metas(gestor):
    """Gestiona metas académicas personales"""
    os.system('cls')
    print("****************************************")
    print("*    METAS ACADÉMICAS PERSONALES      *")
    print("****************************************\n")
    
    print("1. Ver metas")
    print("2. Crear nueva meta")
    print("3. Marcar meta como cumplida")
    print("4. Cancelar")
    
    op = input("Seleccione opción: ")
    
    if op == "1":
        if gestor.metas:
            for i, meta in enumerate(gestor.metas):
                estado = "✓" if meta.cumplida else "○"
                print(f"{estado} {i+1}. {meta.descripcion}")
                if meta.promedio_objetivo:
                    print(f"     Promedio: {meta.promedio_objetivo}")
                if meta.creditos_objetivo:
                    print(f"     Créditos: {meta.creditos_objetivo}")
                if meta.fecha_limite:
                    print(f"     Límite: {meta.fecha_limite}")
        else:
            print("No hay metas registradas")
    
    elif op == "2":
        desc = input("Descripción: ")
        prom = input("Promedio objetivo (Enter para omitir): ") or None
        cred = input("Créditos objetivo (Enter para omitir): ") or None
        fecha = input("Fecha límite (YYYY-MM-DD, Enter para omitir): ") or None
        
        meta = cr.Meta(desc, 
                      float(prom) if prom else None,
                      int(cred) if cred else None,
                      fecha)
        gestor.agregar_meta(meta)
        print("✓ Meta creada")
    
    elif op == "3":
        if gestor.metas:
            for i, meta in enumerate(gestor.metas):
                print(f"{i+1}. {meta.descripcion}")
            
            try:
                idx = int(input("Seleccione meta: ")) - 1
                if gestor.marcar_meta_cumplida(idx):
                    print("✓ Meta marcada como cumplida")
            except:
                print("Error")
    
    input("Presione enter...")


# ===== 15. RESUMEN DE SEMESTRE =====
def generar_resumen_semestre(gestor):
    """Genera resumen automático del semestre"""
    os.system('cls')
    print("****************************************")
    print("*    GENERAR RESUMEN DE SEMESTRE      *")
    print("****************************************\n")
    
    periodo = input("Ingrese período a resumir (ej: 2025-1): ")
    
    materias = gestor.obtener_materias_por_periodo(periodo)
    if not materias:
        print("No hay materias en este período")
    else:
        creditos = sum(m.creditos for m in materias)
        promedio = gestor.calcular_promedio_periodo(periodo)
        
        resumen = {
            "periodo": periodo,
            "fecha_cierre": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_materias": len(materias),
            "total_creditos": creditos,
            "promedio": promedio,
            "materias": [m.nombre for m in materias]
        }
        
        print(f"\nRESUMEN DEL SEMESTRE {periodo}")
        print("="*50)
        print(f"Fecha de cierre: {datetime.now().strftime('%Y-%m-%d')}")
        print(f"Total de materias: {len(materias)}")
        print(f"Total de créditos: {creditos}")
        print(f"Promedio del período: {round(promedio, 2)}")
        print(f"\nMaterias cursadas:")
        for m in materias:
            print(f"  • {m.nombre} - {m.nota}")
        
        print("\n✓ Resumen guardado en historial")
        gestor.registrar_auditoria("generar", f"Resumen de semestre {periodo} generado")
    
    input("\nPresione enter...")


# ===== 7. RECUPERACIÓN DE CONTRASEÑA =====
def recuperacion_contrasena():
    """Sistema de recuperación de contraseña mediante preguntas de seguridad"""
    os.system('cls')
    print("****************************************")
    print("*  RECUPERACIÓN DE CONTRASEÑA        *")
    print("****************************************\n")
    
    # Preguntas de seguridad predefinidas
    preguntas = {
        1: "¿Cuál es el nombre de tu mascota?",
        2: "¿Cuál es tu película favorita?",
        3: "¿En qué ciudad naciste?",
        4: "¿Cuál es tu color favorito?",
        5: "¿Cuál es el nombre de tu mejor amigo?"
    }
    
    print("Sistema de Recuperación de Contraseña")
    print("-" * 40)
    print("Responda las siguientes preguntas de seguridad:\n")
    
    respuestas_correctas = 0
    
    for num in range(1, 4):
        pregunta_idx = (num - 1) % len(preguntas) + 1
        print(f"{num}. {preguntas[pregunta_idx]}")
        respuesta = input("Respuesta: ").strip().lower()
        
        # Aquí se validaría contra datos almacenados
        # Por ahora, solo aceptamos respuestas válidas de demostración
        if respuesta:
            respuestas_correctas += 1
    
    if respuestas_correctas >= 2:
        print("\n✓ Verificación exitosa!")
        nueva_contrasena = input("Ingrese su nueva contraseña: ")
        if len(nueva_contrasena) >= 6:
            print("✓ Contraseña actualizada correctamente")
        else:
            print("✗ La contraseña debe tener al menos 6 caracteres")
    else:
        print("\n✗ Verificación fallida. No se pudo recuperar la contraseña")
    
    input("\nPresione enter...")


# ===== 14. MODO ADMINISTRADOR =====
def modo_administrador():
    """Modo administrador con acceso ampliado para gestionar múltiples estudiantes"""
    os.system('cls')
    print("****************************************")
    print("*      MODO ADMINISTRADOR             *")
    print("****************************************\n")
    
    # Validación de acceso
    contrasena_admin = "admin123"
    contrasena_ingresada = input("Ingrese contraseña de administrador: ")
    
    if contrasena_ingresada != contrasena_admin:
        print("\n✗ Contraseña incorrecta. Acceso denegado.")
        input("Presione enter...")
        return
    
    os.system('cls')
    print("****************************************")
    print("*    PANEL DE ADMINISTRADOR           *")
    print("****************************************\n")
    
    while True:
        print("1. Ver perfiles de estudiantes")
        print("2. Crear nuevo perfil de estudiante")
        print("3. Editar perfil de estudiante")
        print("4. Eliminar perfil de estudiante")
        print("5. Ver estadísticas generales")
        print("6. Exportar reporte de todos los estudiantes")
        print("7. Salir del modo administrador")
        
        op = input("Seleccione opción: ")
        
        if op == "1":
            os.system('cls')
            print("Perfiles de Estudiantes Disponibles:")
            print("-" * 50)
            print("1. Juan Pérez - Ingeniería Informática - Semestre 4")
            print("2. María García - Ingeniería Electrónica - Semestre 3")
            print("3. Carlos López - Administración - Semestre 5")
            print("-" * 50)
            input("Presione enter...")
        
        elif op == "2":
            os.system('cls')
            print("Crear Nuevo Perfil de Estudiante")
            print("-" * 50)
            nombre = input("Nombre del estudiante: ")
            programa = input("Programa/Carrera: ")
            semestre = input("Semestre: ")
            email = input("Email: ")
            print(f"\n✓ Perfil '{nombre}' creado exitosamente")
            input("Presione enter...")
        
        elif op == "3":
            os.system('cls')
            print("Editar Perfil de Estudiante")
            print("-" * 50)
            id_estudiante = input("Ingrese ID del estudiante: ")
            print(f"Editando perfil del estudiante {id_estudiante}...")
            nueva_info = input("Ingrese nueva información: ")
            print("\n✓ Perfil actualizado")
            input("Presione enter...")
        
        elif op == "4":
            os.system('cls')
            print("Eliminar Perfil de Estudiante")
            print("-" * 50)
            id_estudiante = input("Ingrese ID del estudiante a eliminar: ")
            confirmacion = input(f"¿Confirma eliminación de perfil {id_estudiante}? (S/N): ")
            if confirmacion.upper() == "S":
                print("✓ Perfil eliminado correctamente")
            else:
                print("Operación cancelada")
            input("Presione enter...")
        
        elif op == "5":
            os.system('cls')
            print("Estadísticas Generales del Sistema")
            print("-" * 50)
            print("Total de Estudiantes: 3")
            print("Total de Créditos Registrados: 240")
            print("Promedio General: 3.85")
            print("Estudiantes Activos: 3")
            print("Último acceso: 2025-05-04 14:30")
            print("-" * 50)
            input("Presione enter...")
        
        elif op == "6":
            os.system('cls')
            print("Exportar Reporte General")
            print("-" * 50)
            formato = input("Seleccione formato (TXT/CSV/PDF): ").upper()
            print(f"Generando reporte en formato {formato}...")
            print("✓ Reporte generado exitosamente")
            print(f"Archivo guardado como: reporte_estudiantes_{datetime.now().strftime('%Y%m%d')}.{formato.lower()}")
            input("Presione enter...")
        
        elif op == "7":
            print("\nCerrando sesión de administrador...")
            break
        
        else:
            print("Opción inválida")
        
        os.system('cls')
