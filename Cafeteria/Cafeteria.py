from abc import ABC
from enum import Enum

#--- ENUMS ---
class RolEmpleado(Enum):
    BARISTA = "BARISTA"
    MESERO = "MESERO"
    GERENTE = "GERENTE"

class TemperaturaBebida(Enum):
    FRIA = "FRIA"
    CALIENTE = "CALIENTE"

class EstadoPedido(Enum):
    PENDIENTE = "PENDIENTE"
    PREPARANDO = "PREPARANDO"
    ENTREGADO = "ENTREGADO"

#--- MODULO DE PERSONAS ---
class Persona(ABC):
    def __init__ (self, id_persona:int, nombre:str, email:str):
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email

    def login (self):
        print (f"{self.nombre} ha iniciado sesión.")

    def logout (self):
        print (f"{self.nombre} ha cerrado sesión.")

    def actualizar_perfil(self, nuevo_nombre, nuevo_email):
        self.nombre = nuevo_nombre
        self.email = nuevo_email
        print (f"Datos actualizados. Ahora te llamas {self.nombre} y tu nuevo email es {self.email}")

# --- HERENCIA DE PERSONA ---
class Cliente(Persona):
    def __init__(self, id_persona, nombre, email):
        super().__init__(id_persona, nombre, email)
        self.puntos_fidelidad = 0
        self.historial_pedidos = []

    def realizar_pedido(self, producto, costo):
        self.historial_pedidos.append(producto)
        puntos_ganados = costo // 10
        self.puntos_fidelidad += puntos_ganados
        print (f"Agregaste {producto} a tu carrito y ganaste {puntos_ganados} puntos por tu compra")

    def consultar_historial(self):
        print (f"Historial de pedidos de {self.nombre}.")
        if not self.historial_pedidos:
            print (f"No hay pedidos registrados")
        else:
            for pedido in self.historial_pedidos:
                print (f"Tu historial de compras es: {pedido}.")

    def canjear_puntos(self, puntos_a_canjear):
        if self.puntos_fidelidad >= puntos_a_canjear:
            self.puntos_fidelidad -= puntos_a_canjear
            print(f"Canje exitoso. Te quedan {self.puntos_fidelidad} puntos.")
        else:
            print(f"Puntos insuficientes. Tienes {self.puntos_fidelidad} y necesitas {puntos_a_canjear}.")

class Empleado (Persona):
    def __init__(self, id_persona, nombre, email, id_empleado, rol:RolEmpleado):
        super().__init__(id_persona, nombre, email)
        self.id_empleado = id_empleado
        self.rol = rol

    def actualizar_inventario (self):
        if self.rol == RolEmpleado.GERENTE:
            print(f"{self.nombre} esta actualizando el inventario")
            return True
        print(f"Acceso denegado para el rol {self.rol.value}.")
        return False
    
    def cambiar_estado_pedido (self, id_pedido, nuevo_estado):
        if self.rol == RolEmpleado.MESERO or self.rol == RolEmpleado.BARISTA:
            print (f"El mesero {self.nombre} cambió el pedido #{id_pedido} a: {nuevo_estado}")
            return True
        print(f"Acceso denegado para el rol {self.rol.value}.")
        return False
    
#--- MODULO DE PRODUCTOS ---
class producto_base:
    def __init__(self, id_producto:int, nombre:str, precio_base:float):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio_base = precio_base
    
class bebida(producto_base):
    def __init__(self, id_producto, nombre, precio_base, tamaño:str, temperatura:TemperaturaBebida):
        super().__init__(id_producto, nombre, precio_base)
        self.tamaño = tamaño
        self.temperatura = temperatura
        self.modificadores = []
        self.costo_extra = 0.0

    def agregar_extra(self, especificación_extra, precio_extra):
        self.modificadores.append(especificación_extra)
        if precio_extra >0:
            self.costo_extra += precio_extra
            print (f"Se agrego {especificación_extra}(+ ${precio_extra}) a tu {self.nombre}.")
        else:
            print (f"Se agrego {especificación_extra}(Gratis.).")

    def calcular_precio_final(self):
        precio_total = self.precio_base + self.costo_extra
        print(f"--- Detalle de Pedido ---")
        print(f"Producto: {self.nombre} ({self.tamaño})")
        print(f"Temperatura: {self.temperatura.value}")
        if self.modificadores:
            print("Personalización:")
            for extra in self.modificadores:
                print(f"  - {extra}") 
        print(f"Total a pagar: ${precio_total}")
        return precio_total
    
class postres(producto_base):
    def __init__(self, id_producto, nombre, precio_base, es_vegano:bool, sin_gluten:bool):
        super().__init__(id_producto, nombre, precio_base)
        self.es_vegano = es_vegano
        self.sin_gluten = sin_gluten

#--- LOGICAS Y VENTAS ---

class pedido:
    def __init__(self, id_pedido):
        self.id_pedido = id_pedido
        self.productos = []
        self.estado = EstadoPedido.PENDIENTE
        self.total = 0.0

    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)
        print(f"{nuevo_producto.nombre} añadido al pedido #{self.id_pedido}.")

    def calcular_total(self):
        cuenta_total = 0.0
        for p in self.productos:
            cuenta_total = cuenta_total + p.precio_base
        self.total = cuenta_total
        print(f"El total de su cuenta es ${self.total}")
        return self.total

    def validar_stock(self):
        if len(self.productos) > 0:
            print("Stock disponible para todos los productos.")
            return True
        else:
            print("No hay productos en el pedido.")
            return False
        
#--- MÓDULO DE INVENTARIO ---
class Inventario:
    def __init__(self):
        self.ingredientes = {
            "Café en grano (kg)": 10,
            "Leche (L)": 20,
            "Agua (L)": 50,
            "Jarabe Caramelo (ml)": 500,
            "Harina (kg)": 15
        }

    def reducir_stock(self, ingrediente, cantidad):
        if ingrediente in self.ingredientes:
            if self.ingredientes[ingrediente] >= cantidad:
                self.ingredientes[ingrediente] -= cantidad
                print(f"Stock reducido: {ingrediente}. Quedan {self.ingredientes[ingrediente]}.")
                if self.ingredientes[ingrediente] < 2:
                    self.notificar_faltante(ingrediente)
                return True
            else:
                print(f"Error: No hay suficiente {ingrediente} en stock.")
                return False
        else:
            print(f"El ingrediente {ingrediente} no existe en el inventario.")
            return False

    def notificar_faltante(self, ingrediente):
        print(f"ALERTA DE ABASTECIMIENTO: El ingrediente '{ingrediente}' se está agotando.")