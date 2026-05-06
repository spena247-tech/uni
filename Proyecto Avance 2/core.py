import json
import os
from datetime import datetime
from typing import List, Dict, Optional

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_data_path(file_name):
    return os.path.join(BASE_DIR, 'data', file_name)


class Materia:
    """Clase que representa una materia con sus atributos"""
    
    def __init__(self, nombre, codigo, creditos, nota, periodo, es_optativa=False):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.nota = nota
        self.periodo = periodo
        self.es_optativa = es_optativa
    
    def to_dict(self):
        """Convierte la materia a diccionario"""
        return {
            "nombre": self.nombre,
            "codigo": self.codigo,
            "creditos": self.creditos,
            "nota": self.nota,
            "periodo": self.periodo,
            "es_optativa": self.es_optativa
        }
    
    @staticmethod
    def from_dict(data):
        """Crea una materia desde un diccionario"""
        return Materia(
            data["nombre"],
            data["codigo"],
            data["creditos"],
            data["nota"],
            data["periodo"],
            data.get("es_optativa", False)
        )


class Usuario:
    """Clase que representa el perfil del estudiante"""
    
    def __init__(self, nombre, programa, semestre_actual, foto=None, creditos_totales=150):
        self.nombre = nombre
        self.programa = programa
        self.semestre_actual = semestre_actual
        self.modalidad = "presencial"  # Será sincronizado desde UsuarioSistema
        self.creditos_totales = creditos_totales
        self.foto = foto or "[Foto de perfil]"
        self.fecha_creacion = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "programa": self.programa,
            "semestre_actual": self.semestre_actual,
            "modalidad": self.modalidad,
            "creditos_totales": self.creditos_totales,
            "foto": self.foto,
            "fecha_creacion": self.fecha_creacion
        }
    
    @staticmethod
    def from_dict(data):
        u = Usuario(data["nombre"], data["programa"], data["semestre_actual"], data.get("foto"), data.get("creditos_totales", 150))
        if "fecha_creacion" in data:
            u.fecha_creacion = data["fecha_creacion"]
        if "modalidad" in data:
            u.modalidad = data["modalidad"]
        return u


class Evento:
    """Clase que representa eventos del calendario académico"""
    
    def __init__(self, nombre, fecha, tipo="general"):
        self.nombre = nombre
        self.fecha = fecha
        self.tipo = tipo  # parcial, entrega, matricula, otro
    
    def to_dict(self):
        return {"nombre": self.nombre, "fecha": self.fecha, "tipo": self.tipo}
    
    @staticmethod
    def from_dict(data):
        return Evento(data["nombre"], data["fecha"], data.get("tipo", "general"))


class Meta:
    """Clase que representa una meta académica personal"""
    
    def __init__(self, descripcion, promedio_objetivo=None, creditos_objetivo=None, fecha_limite=None):
        self.descripcion = descripcion
        self.promedio_objetivo = promedio_objetivo
        self.creditos_objetivo = creditos_objetivo
        self.fecha_limite = fecha_limite
        self.cumplida = False
        self.fecha_creacion = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            "descripcion": self.descripcion,
            "promedio_objetivo": self.promedio_objetivo,
            "creditos_objetivo": self.creditos_objetivo,
            "fecha_limite": self.fecha_limite,
            "cumplida": self.cumplida,
            "fecha_creacion": self.fecha_creacion
        }
    
    @staticmethod
    def from_dict(data):
        m = Meta(data["descripcion"], data.get("promedio_objetivo"), 
                data.get("creditos_objetivo"), data.get("fecha_limite"))
        m.cumplida = data.get("cumplida", False)
        if "fecha_creacion" in data:
            m.fecha_creacion = data["fecha_creacion"]
        return m


class RegistroAuditoria:
    """Clase que registra cambios en el sistema"""
    
    def __init__(self, accion, detalles, usuario="Sistema"):
        self.timestamp = datetime.now().isoformat()
        self.accion = accion  # crear, editar, eliminar
        self.detalles = detalles
        self.usuario = usuario
    
    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "accion": self.accion,
            "detalles": self.detalles,
            "usuario": self.usuario
        }
    
    @staticmethod
    def from_dict(data):
        r = RegistroAuditoria(data["accion"], data["detalles"], data.get("usuario", "Sistema"))
        r.timestamp = data["timestamp"]
        return r


class GestorCreditos:
    """Clase que gestiona la colección de materias y persistencia por usuario"""
    
    def __init__(self, usuario_nombre: str, fileName='creditos_usuarios.json'):
        self.usuario_nombre = usuario_nombre
        self.fileName = fileName
        self.materias = []
        self.usuario = None
        self.eventos = []
        self.metas = []
        self.auditoria = []
        self.cargar_datos()
    
    def cargar_datos(self):
        """Carga las materias desde el archivo JSON para el usuario específico"""
        if self.checkFile(self.fileName):
            data_completa = self.LoadInfo(self.fileName)
            data = data_completa.get("usuarios", {}).get(self.usuario_nombre, {})
            
            self.materias = [Materia.from_dict(m) for m in data.get("creditos", [])]
            
            if "usuario" in data:
                self.usuario = Usuario.from_dict(data["usuario"])
            
            if "eventos" in data:
                self.eventos = [Evento.from_dict(e) for e in data["eventos"]]
            
            if "metas" in data:
                self.metas = [Meta.from_dict(m) for m in data["metas"]]
            
            if "auditoria" in data:
                self.auditoria = [RegistroAuditoria.from_dict(r) for r in data["auditoria"]]
    
    def guardar_datos(self):
        """Guarda todas las materias y datos en el archivo JSON para el usuario actual"""
        # Cargar datos existentes para no perder otros usuarios
        if self.checkFile(self.fileName):
            data_completa = self.LoadInfo(self.fileName)
        else:
            data_completa = {"usuarios": {}}
        
        # Actualizar datos del usuario actual
        data_completa["usuarios"][self.usuario_nombre] = {
            "creditos": [m.to_dict() for m in self.materias],
            "usuario": self.usuario.to_dict() if self.usuario else None,
            "eventos": [e.to_dict() for e in self.eventos],
            "metas": [m.to_dict() for m in self.metas],
            "auditoria": [a.to_dict() for a in self.auditoria]
        }
        
        self.crearInfo(self.fileName, data_completa)
    
    def registrar_auditoria(self, accion, detalles, usuario="Sistema"):
        """Registra una acción en el historial de auditoría"""
        registro = RegistroAuditoria(accion, detalles, usuario)
        self.auditoria.append(registro)
        self.guardar_datos()
    
    def agregar_materia(self, materia):
        """Añade una materia a la colección"""
        self.materias.append(materia)
        self.registrar_auditoria("crear", f"Materia agregada: {materia.nombre}")
        self.guardar_datos()
    
    def eliminar_materia(self, indice):
        """Elimina una materia por índice"""
        if 0 <= indice < len(self.materias):
            materia = self.materias[indice]
            del self.materias[indice]
            self.registrar_auditoria("eliminar", f"Materia eliminada: {materia.nombre}")
            self.guardar_datos()
            return True
        return False
    
    def obtener_materia(self, indice):
        """Obtiene una materia por índice"""
        if 0 <= indice < len(self.materias):
            return self.materias[indice]
        return None
    
    def obtener_todas(self):
        """Retorna todas las materias"""
        return self.materias
    
    def calcular_promedio(self):
        """Calcula el promedio ponderado de todas las materias"""
        if not self.materias:
            return 0
        
        total_creditos = sum(m.creditos for m in self.materias)
        suma_ponderada = sum(m.nota * m.creditos for m in self.materias)
        
        if total_creditos == 0:
            return 0
        
        return suma_ponderada / total_creditos
    
    def buscar_materias(self, criterio: str, tipo="nombre") -> List[Materia]:
        """Busca materias por nombre o código"""
        resultado = []
        criterio_lower = criterio.lower()
        
        for materia in self.materias:
            if tipo == "nombre" and criterio_lower in materia.nombre.lower():
                resultado.append(materia)
            elif tipo == "codigo" and criterio_lower in materia.codigo.lower():
                resultado.append(materia)
        
        return resultado
    
    def obtener_materias_por_periodo(self, periodo: str) -> List[Materia]:
        """Obtiene materias de un período específico"""
        return [m for m in self.materias if m.periodo == periodo]
    
    def obtener_periodos_unicos(self) -> List[str]:
        """Obtiene todos los períodos únicos registrados"""
        return sorted(list(set(m.periodo for m in self.materias)))
    
    def contar_creditos_optativas(self) -> int:
        """Cuenta el total de créditos en optativas"""
        return sum(m.creditos for m in self.materias if m.es_optativa)
    
    def contar_creditos_obligatorios(self) -> int:
        """Cuenta el total de créditos en obligatorias"""
        return sum(m.creditos for m in self.materias if not m.es_optativa)
    
    def calcular_promedio_periodo(self, periodo: str) -> float:
        """Calcula el promedio de un período específico"""
        materias_periodo = self.obtener_materias_por_periodo(periodo)
        if not materias_periodo:
            return 0
        
        total_creditos = sum(m.creditos for m in materias_periodo)
        suma_ponderada = sum(m.nota * m.creditos for m in materias_periodo)
        
        return suma_ponderada / total_creditos if total_creditos > 0 else 0
    
    def obtener_total_creditos(self) -> int:
        """Obtiene el total de créditos cursados"""
        return sum(m.creditos for m in self.materias)
    
    def crear_usuario(self, nombre, programa, semestre):
        """Crea o actualiza el perfil del usuario"""
        self.usuario = Usuario(nombre, programa, semestre)
        self.registrar_auditoria("crear", "Perfil de usuario creado")
        self.guardar_datos()
    
    def agregar_evento(self, evento: Evento):
        """Añade un evento al calendario"""
        self.eventos.append(evento)
        self.guardar_datos()
    
    def obtener_eventos_proximos(self, dias=7) -> List[Evento]:
        """Obtiene eventos dentro de los próximos N días"""
        hoy = datetime.now()
        proximos = []
        for e in self.eventos:
            try:
                fecha_evento = datetime.fromisoformat(e.fecha)
                delta = (fecha_evento - hoy).days
                if 0 <= delta <= dias:
                    proximos.append(e)
            except:
                pass
        return sorted(proximos, key=lambda x: x.fecha)
    
    def agregar_meta(self, meta: Meta):
        """Añade una meta académica"""
        self.metas.append(meta)
        self.registrar_auditoria("crear", f"Meta creada: {meta.descripcion}")
        self.guardar_datos()
    
    def marcar_meta_cumplida(self, indice):
        """Marca una meta como cumplida"""
        if 0 <= indice < len(self.metas):
            self.metas[indice].cumplida = True
            self.registrar_auditoria("editar", f"Meta cumplida: {self.metas[indice].descripcion}")
            self.guardar_datos()
            return True
        return False
    
    def exportar_csv(self) -> str:
        """Genera un string en formato CSV del historial"""
        lineas = ["Nombre,Código,Créditos,Nota,Período,Tipo"]
        for m in self.materias:
            tipo = "Optativa" if m.es_optativa else "Obligatoria"
            lineas.append(f'"{m.nombre}","{m.codigo}",{m.creditos},{m.nota},"{m.periodo}","{tipo}"')
        return "\n".join(lineas)
    
    def exportar_txt(self) -> str:
        """Genera un string en formato TXT del historial"""
        lineas = []
        lineas.append("="*70)
        lineas.append("HISTORIAL ACADÉMICO".center(70))
        lineas.append("="*70)
        
        if self.usuario:
            lineas.append(f"\nEstudiante: {self.usuario.nombre}")
            lineas.append(f"Programa: {self.usuario.programa}")
            lineas.append(f"Semestre Actual: {self.usuario.semestre_actual}")
        
        lineas.append(f"\nTotal de Créditos: {self.obtener_total_creditos()}")
        lineas.append(f"Promedio Ponderado: {round(self.calcular_promedio(), 2)}")
        lineas.append(f"Créditos Obligatorios: {self.contar_creditos_obligatorios()}")
        lineas.append(f"Créditos Optativos: {self.contar_creditos_optativas()}")
        
        lineas.append("\n" + "-"*70)
        lineas.append(f"{'Item':<5} {'Materia':<20} {'Cred':<5} {'Nota':<5} {'Período':<10} {'Tipo':<10}")
        lineas.append("-"*70)
        
        for i, m in enumerate(self.materias, 1):
            tipo = "Optativa" if m.es_optativa else "Obligatoria"
            lineas.append(f"{i:<5} {m.nombre:<20} {m.creditos:<5} {m.nota:<5} {m.periodo:<10} {tipo:<10}")
        
        lineas.append("-"*70)
        lineas.append("\nGenerado: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        return "\n".join(lineas)
    
    # Métodos auxiliares de persistencia
    def checkFile(self, filePath):
        archivo = get_data_path(filePath)
        try:
            with open(archivo, 'r', encoding='utf-8'):
                return True
        except FileNotFoundError:
            return False
        except OSError:
            return False

    def crearInfo(self, fileName, data):
        archivo = get_data_path(fileName)
        os.makedirs(os.path.dirname(archivo), exist_ok=True)
        with open(archivo, "w", encoding='utf-8') as write_file:
            json.dump(data, write_file, indent=4, ensure_ascii=False)

    def LoadInfo(self, fileName):
        archivo = get_data_path(fileName)
        with open(archivo, "r", encoding='utf-8') as read_file:
            dicc = json.load(read_file)
        return dicc


# Funciones heredadas para compatibilidad
def checkFile(filePath):
    archivo = get_data_path(filePath)
    try:
        with open(archivo, 'r', encoding='utf-8'):
            return True
    except FileNotFoundError:
        return False
    except OSError:
        return False


def crearInfo(fileName, data):
    archivo = get_data_path(fileName)
    os.makedirs(os.path.dirname(archivo), exist_ok=True)
    with open(archivo, "w", encoding='utf-8') as write_file:
        json.dump(data, write_file, indent=4, ensure_ascii=False)


def editarInfo(fileName, data):
    archivo = get_data_path(fileName)
    with open(archivo, "w", encoding='utf-8') as write_file:
        json.dump(data, write_file, indent=4, ensure_ascii=False)


def delInfo(fileName, data, index):
    archivo = get_data_path(fileName)
    rta = input("¿Desea eliminar la materia seleccionada? S/N: ").strip().upper()

    if rta == "S":
        try:
            del data["creditos"][index]
            with open(archivo, "w", encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("Materia eliminada exitosamente.")
        except Exception:
            print("Error al eliminar.")
    elif rta == "N":
        print("Operación cancelada.")
    else:
        print("Entrada no válida.")

    input("Presione enter para continuar...")


def LoadInfo(fileName):
    archivo = get_data_path(fileName)
    with open(archivo, "r", encoding='utf-8') as read_file:
        dicc = json.load(read_file)
    return dicc
