"""
Módulo de autenticación y gestión de usuarios
Sistema de login, registro y persistencia de usuarios
"""

import json
import os
import hashlib
from datetime import datetime
from typing import Optional, Dict, List

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_data_path(file_name):
    return os.path.join(BASE_DIR, 'data', file_name)


class UsuarioSistema:
    """Clase que representa un usuario del sistema con credenciales"""
    
    def __init__(self, usuario, correo, contraseña, semestre, uid, modalidad="presencial", programa="", creditos_totales=150):
        self.usuario = usuario
        self.correo = correo
        self.contraseña = self._hash_contraseña(contraseña)
        self.semestre = semestre
        self.semestre_actual = semestre  # Alias para compatibilidad
        self.uid = uid
        self.modalidad = modalidad  # presencial o virtual
        self.programa = programa or "Programa no especificado"
        self.creditos_totales = creditos_totales
        self.fecha_registro = datetime.now().isoformat()
        self.es_admin = False
    
    @staticmethod
    def _hash_contraseña(contraseña: str) -> str:
        """Hashea la contraseña para seguridad básica"""
        return hashlib.sha256(contraseña.encode()).hexdigest()
    
    def verificar_contraseña(self, contraseña: str) -> bool:
        """Verifica si la contraseña ingresada es correcta"""
        return self.contraseña == self._hash_contraseña(contraseña)
    
    def to_dict(self):
        return {
            "usuario": self.usuario,
            "correo": self.correo,
            "contraseña": self.contraseña,
            "semestre": self.semestre,
            "uid": self.uid,
            "modalidad": self.modalidad,
            "programa": self.programa,
            "creditos_totales": self.creditos_totales,
            "fecha_registro": self.fecha_registro,
            "es_admin": self.es_admin
        }
    
    @staticmethod
    def from_dict(data):
        u = UsuarioSistema(
            data["usuario"],
            data["correo"],
            data["contraseña"],  # Ya hasheada
            data["semestre"],
            data["uid"],
            data.get("modalidad", "presencial"),
            data.get("programa", ""),
            data.get("creditos_totales", 150)
        )
        u.contraseña = data["contraseña"]  # Usar el hash directo
        u.fecha_registro = data.get("fecha_registro", datetime.now().isoformat())
        u.es_admin = data.get("es_admin", False)
        return u


class GestorUsuarios:
    """Gestiona el registro, login y persistencia de usuarios"""
    
    def __init__(self, fileName='usuarios.json'):
        self.fileName = fileName
        self.usuarios: Dict[str, UsuarioSistema] = {}
        self.usuario_actual: Optional[UsuarioSistema] = None
        self.cargar_usuarios()
        self._crear_admin_inicial()
    
    def cargar_usuarios(self):
        """Carga todos los usuarios del archivo JSON"""
        if self.checkFile(self.fileName):
            data = self.LoadInfo(self.fileName)
            for nombre_usuario, info_usuario in data.get("usuarios", {}).items():
                self.usuarios[nombre_usuario] = UsuarioSistema.from_dict(info_usuario)
    
    def guardar_usuarios(self):
        """Guarda todos los usuarios en el archivo JSON"""
        data = {
            "usuarios": {nombre: u.to_dict() for nombre, u in self.usuarios.items()}
        }
        self.crearInfo(self.fileName, data)
    
    def _crear_admin_inicial(self):
        """Crea usuario admin inicial si no existe"""
        if "admin" not in self.usuarios:
            admin = UsuarioSistema(
                "admin",
                "admin@system.local",
                "admin123",
                "N/A",
                "ADMIN0000",
                "virtual"
            )
            admin.es_admin = True
            self.usuarios["admin"] = admin
            self.guardar_usuarios()
    
    def registrar_usuario(self, usuario: str, correo: str, contraseña: str, 
                         semestre: str, uid: str, modalidad: str, programa: str = "", creditos_totales: int = 150) -> tuple[bool, str]:
        """Registra un nuevo usuario. Retorna (éxito, mensaje)"""
        
        if usuario in self.usuarios:
            return False, "El nombre de usuario ya existe"
        
        if len(contraseña) < 6:
            return False, "La contraseña debe tener al menos 6 caracteres"
        
        if "@" not in correo:
            return False, "Correo electrónico inválido"
        
        nuevo_usuario = UsuarioSistema(usuario, correo, contraseña, semestre, uid, modalidad, programa, creditos_totales)
        self.usuarios[usuario] = nuevo_usuario
        self.guardar_usuarios()
        
        return True, f"Usuario '{usuario}' registrado exitosamente"
    
    def login(self, usuario: str, contraseña: str) -> tuple[bool, str]:
        """Intenta login de un usuario. Retorna (éxito, mensaje)"""
        
        if usuario not in self.usuarios:
            return False, "Usuario no encontrado"
        
        user_obj = self.usuarios[usuario]
        
        if not user_obj.verificar_contraseña(contraseña):
            return False, "Contraseña incorrecta"
        
        self.usuario_actual = user_obj
        return True, f"Bienvenido {usuario}"
    
    def logout(self):
        """Cierra la sesión actual"""
        self.usuario_actual = None
    
    def obtener_usuario_actual(self) -> Optional[UsuarioSistema]:
        """Retorna el usuario actual autenticado"""
        return self.usuario_actual
    
    def obtener_todos_usuarios(self) -> List[UsuarioSistema]:
        """Retorna lista de todos los usuarios (para admin)"""
        return list(self.usuarios.values())
    
    def actualizar_usuario(self, usuario: str, **kwargs) -> bool:
        """Actualiza datos de un usuario"""
        if usuario in self.usuarios:
            u = self.usuarios[usuario]
            if "semestre" in kwargs:
                u.semestre = kwargs["semestre"]
            if "modalidad" in kwargs:
                u.modalidad = kwargs["modalidad"]
            if "correo" in kwargs:
                u.correo = kwargs["correo"]
            self.guardar_usuarios()
            return True
        return False
    
    def eliminar_usuario(self, usuario: str) -> bool:
        """Elimina un usuario del sistema"""
        if usuario in self.usuarios and usuario != "admin":
            del self.usuarios[usuario]
            self.guardar_usuarios()
            return True
        return False
    
    def cambiar_contraseña(self, usuario: str, contraseña_actual: str, 
                          contraseña_nueva: str) -> tuple[bool, str]:
        """Cambia la contraseña de un usuario"""
        
        if usuario not in self.usuarios:
            return False, "Usuario no encontrado"
        
        u = self.usuarios[usuario]
        
        if not u.verificar_contraseña(contraseña_actual):
            return False, "Contraseña actual incorrecta"
        
        if len(contraseña_nueva) < 6:
            return False, "La nueva contraseña debe tener al menos 6 caracteres"
        
        u.contraseña = u._hash_contraseña(contraseña_nueva)
        self.guardar_usuarios()
        
        return True, "Contraseña actualizada exitosamente"
    
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
