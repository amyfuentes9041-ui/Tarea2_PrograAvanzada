from Cafeteria import *

print("--- BIENVENIDOS A COFFEE AMY ☕ ---\n")

# 1. CREACIÓN DE PERSONAL 
gerente_1 = Empleado(1, "Carlos Ortega", "carlos@coffee.com", "E001", RolEmpleado.GERENTE)
gerente_2 = Empleado(2, "Elena Rodríguez", "elena.r@coffee.com", "E002", RolEmpleado.GERENTE)

barista_1 = Empleado(3, "Lucía Méndez", "lucia.m@coffee.com", "B001", RolEmpleado.BARISTA)
barista_2 = Empleado(4, "Marcos Ruiz", "marcos.r@coffee.com", "B002", RolEmpleado.BARISTA)
barista_3 = Empleado(5, "Sofía Alva", "sofia.a@coffee.com", "B003", RolEmpleado.BARISTA)
barista_4 = Empleado(6, "Diego Torres", "diego.t@coffee.com", "B004", RolEmpleado.BARISTA)

mesero_1 = Empleado(7, "Javier López", "javier.l@coffee.com", "M001", RolEmpleado.MESERO)
mesero_2 = Empleado(8, "Valeria Soler", "valeria.s@coffee.com", "M002", RolEmpleado.MESERO)
mesero_3 = Empleado(9, "Andrés Castro", "andres.c@coffee.com", "M003", RolEmpleado.MESERO)
mesero_4 = Empleado(10, "Paola Núñez", "paola.n@coffee.com", "M004", RolEmpleado.MESERO)

#IMPRESION DE PERSONAL
print("\n--- REGISTRO DE TRABAJADORES ---")

print(f"ID: {gerente_1.id_empleado} | Nombre: {gerente_1.nombre} | Rol: {gerente_1.rol.value} | Email: {gerente_1.email}")
print(f"ID: {gerente_2.id_empleado} | Nombre: {gerente_2.nombre} | Rol: {gerente_2.rol.value} | Email: {gerente_2.email}")

print(f"ID: {barista_1.id_empleado} | Nombre: {barista_1.nombre} | Rol: {barista_1.rol.value} | Email: {barista_1.email}")
print(f"ID: {barista_2.id_empleado} | Nombre: {barista_2.nombre} | Rol: {barista_2.rol.value} | Email: {barista_2.email}")
print(f"ID: {barista_3.id_empleado} | Nombre: {barista_3.nombre} | Rol: {barista_3.rol.value} | Email: {barista_3.email}")
print(f"ID: {barista_4.id_empleado} | Nombre: {barista_4.nombre} | Rol: {barista_4.rol.value} | Email: {barista_4.email}")

print(f"ID: {mesero_1.id_empleado} | Nombre: {mesero_1.nombre} | Rol: {mesero_1.rol.value} | Email: {mesero_1.email}")
print(f"ID: {mesero_2.id_empleado} | Nombre: {mesero_2.nombre} | Rol: {mesero_2.rol.value} | Email: {mesero_2.email}")
print(f"ID: {mesero_3.id_empleado} | Nombre: {mesero_3.nombre} | Rol: {mesero_3.rol.value} | Email: {mesero_3.email}")
print(f"ID: {mesero_4.id_empleado} | Nombre: {mesero_4.nombre} | Rol: {mesero_4.rol.value} | Email: {mesero_4.email}")

print("\n ----------------------------------------")

#2. CREACIÓN DE CLIENTES
cliente_1 = Cliente(101, "Ana García", "ana.garcia@mail.com")
cliente_2 = Cliente(102, "Luis Rodríguez", "luis.ro@mail.com")
cliente_3 = Cliente(103, "Carla Jiménez", "carla.j@mail.com")
cliente_4 = Cliente(104, "Roberto Peña", "robb.p@mail.com")
cliente_5 = Cliente(105, "Sofía Castro", "sofi.castro@mail.com")
cliente_6 = Cliente(106, "Miguel Torres", "migue.t@mail.com")
cliente_7 = Cliente(107, "Elena Méndez", "elena.m@mail.com")
cliente_8 = Cliente(108, "Fernando Soler", "fer.soler@mail.com")
cliente_9 = Cliente(109, "Lucía Valle", "lucia.v@mail.com")
cliente_10 = Cliente(110, "Ricardo Luna", "rick.luna@mail.com")

# IMPRESIÓN MANUAL DE CLIENTES
print("\n--- REGISTRO DE CLIENTES ---")

print(f"ID: {cliente_1.id_persona} | Cliente: {cliente_1.nombre} | Email: {cliente_1.email} | Puntos: {cliente_1.puntos_fidelidad}")
print(f"ID: {cliente_2.id_persona} | Cliente: {cliente_2.nombre} | Email: {cliente_2.email} | Puntos: {cliente_2.puntos_fidelidad}")
print(f"ID: {cliente_3.id_persona} | Cliente: {cliente_3.nombre} | Email: {cliente_3.email} | Puntos: {cliente_3.puntos_fidelidad}")
print(f"ID: {cliente_4.id_persona} | Cliente: {cliente_4.nombre} | Email: {cliente_4.email} | Puntos: {cliente_4.puntos_fidelidad}")
print(f"ID: {cliente_5.id_persona} | Cliente: {cliente_5.nombre} | Email: {cliente_5.email} | Puntos: {cliente_5.puntos_fidelidad}")
print(f"ID: {cliente_6.id_persona} | Cliente: {cliente_6.nombre} | Email: {cliente_6.email} | Puntos: {cliente_6.puntos_fidelidad}")
print(f"ID: {cliente_7.id_persona} | Cliente: {cliente_7.nombre} | Email: {cliente_7.email} | Puntos: {cliente_7.puntos_fidelidad}")
print(f"ID: {cliente_8.id_persona} | Cliente: {cliente_8.nombre} | Email: {cliente_8.email} | Puntos: {cliente_8.puntos_fidelidad}")
print(f"ID: {cliente_9.id_persona} | Cliente: {cliente_9.nombre} | Email: {cliente_9.email} | Puntos: {cliente_9.puntos_fidelidad}")
print(f"ID: {cliente_10.id_persona} | Cliente: {cliente_10.nombre} | Email: {cliente_10.email} | Puntos: {cliente_10.puntos_fidelidad}")

print("\n ----------------------------------------")
   
# 3. CREACION DE PRODUCTOS
# Bebidas (id_producto, nombre, precio_base, tamaño, temperatura)
bebida_1 = bebida(201, "Americano", 35.0, "Mediano", TemperaturaBebida.CALIENTE)
bebida_2 = bebida(202, "Frappé de Oreo", 65.0, "Grande", TemperaturaBebida.FRIA)
bebida_3 = bebida(203, "Capuccino", 45.0, "Chico", TemperaturaBebida.CALIENTE)
bebida_4 = bebida(204, "Té Matcha", 55.0, "Mediano", TemperaturaBebida.CALIENTE)
bebida_5 = bebida(205, "Latte Helado", 50.0, "Grande", TemperaturaBebida.FRIA)

# Postres (id_producto, nombre, precio_base, es_vegano, sin_gluten)
postre_1 = postres(301, "Cheesecake", 45.0, False, False)
postre_2 = postres(302, "Muffin de Avena", 30.0, True, True)
postre_3 = postres(303, "Pastel de Chocolate", 55.0, False, False)
postre_4 = postres(304, "Galleta de Jengibre", 25.0, True, False)
postre_5 = postres(305, "Brownie Sin Gluten", 40.0, False, True)

# IMPRESIÓN MANUAL DE PRODUCTOS 
print("\n--- MENÚ DE CAFETERIA ---")

print("--- SECCIÓN DE BEBIDAS ---")
print(f"ID: {bebida_1.id_producto} | {bebida_1.nombre} ({bebida_1.tamaño}) - ${bebida_1.precio_base} | Temp: {bebida_1.temperatura.value}")
print(f"ID: {bebida_2.id_producto} | {bebida_2.nombre} ({bebida_2.tamaño}) - ${bebida_2.precio_base} | Temp: {bebida_2.temperatura.value}")
print(f"ID: {bebida_3.id_producto} | {bebida_3.nombre} ({bebida_3.tamaño}) - ${bebida_3.precio_base} | Temp: {bebida_3.temperatura.value}")
print(f"ID: {bebida_4.id_producto} | {bebida_4.nombre} ({bebida_4.tamaño}) - ${bebida_4.precio_base} | Temp: {bebida_4.temperatura.value}")
print(f"ID: {bebida_5.id_producto} | {bebida_5.nombre} ({bebida_5.tamaño}) - ${bebida_5.precio_base} | Temp: {bebida_5.temperatura.value}")

print("\n--- SECCIÓN DE POSTRES ---")
print(f"ID: {postre_1.id_producto} | {postre_1.nombre} - ${postre_1.precio_base} | Vegano: {'Sí' if postre_1.es_vegano else 'No'} | Sin Gluten: {'Sí' if postre_1.sin_gluten else 'No'}")
print(f"ID: {postre_2.id_producto} | {postre_2.nombre} - ${postre_2.precio_base} | Vegano: {'Sí' if postre_2.es_vegano else 'No'} | Sin Gluten: {'Sí' if postre_2.sin_gluten else 'No'}")
print(f"ID: {postre_3.id_producto} | {postre_3.nombre} - ${postre_3.precio_base} | Vegano: {'Sí' if postre_3.es_vegano else 'No'} | Sin Gluten: {'Sí' if postre_3.sin_gluten else 'No'}")
print(f"ID: {postre_4.id_producto} | {postre_4.nombre} - ${postre_4.precio_base} | Vegano: {'Sí' if postre_4.es_vegano else 'No'} | Sin Gluten: {'Sí' if postre_4.sin_gluten else 'No'}")
print(f"ID: {postre_5.id_producto} | {postre_5.nombre} - ${postre_5.precio_base} | Vegano: {'Sí' if postre_5.es_vegano else 'No'} | Sin Gluten: {'Sí' if postre_5.sin_gluten else 'No'}")

print("\n ----------------------------------------")

# 4. SIMULACIÓN DE LOGIN Y ACTUALIZACIÓN DE PERFIL
print("\n--- GESTIÓN DE SESIÓN Y PERFILES ---")

# Caso 1: Empleado (Gerente 2) 
print("\n[SESIÓN EMPLEADO]")
gerente_2.login()
# Elena Rodríguez decide actualizar su correo de trabajo
gerente_2.actualizar_perfil("Elena R. de Soler", "elena.soler@coffeeamy.com")
print(f"Verificación de cambio - Nombre: {gerente_2.nombre} | Email: {gerente_2.email}")
gerente_2.logout()

print("\n" + "-"*40)

# Caso 2: Cliente (Cliente 5) 
print("\n[SESIÓN CLIENTE]")
cliente_5.login()
# Sofía Castro quiere cambiar su nombre de usuario y correo
cliente_5.actualizar_perfil("Sofi Castro ", "sofi.vip@mail.com")
# Verificamos que sus puntos se mantienen intactos a pesar del cambio de nombre
print(f"Cliente: {cliente_5.nombre} | Email: {cliente_5.email} | Puntos acumulados: {cliente_5.puntos_fidelidad}")
cliente_5.logout()

print("\n ----------------------------------------")

# 5. PRUEBA DE PERMISOS (ACTUALIZAR INVENTARIO)
print("\n--- MÓDULO DE SEGURIDAD DE INVENTARIO ---")

# --- Intento con un Mesero (Debería salir Acceso Denegado) ---
print(f"[TURNO: {mesero_4.nombre}]")
mesero_4.login()
mesero_4.actualizar_inventario() 
mesero_4.logout()

print("\n" + "-"*40)

# --- Intento con un Gerente (Debería salir Acceso Autorizado) ---
print(f"[TURNO: {gerente_2.nombre}]")
gerente_2.login()
gerente_2.actualizar_inventario()
gerente_2.logout()

print("\n----------------------------------------")

# 6. PRUEBA DE CONTROL DE SUMINISTROS (Inventario)
print("\n--- CONTROL DE SUMINISTROS ---")

# Creamos el objeto inventario
mi_inventario = Inventario()

# Simulamos que el Gerente 1 revisa el stock inicial
gerente_1.login()
print(f"Ingredientes actuales: {mi_inventario.ingredientes}")

# Reducimos stock por la preparación de un pedido (Jalamos reducir_stock)
# Supongamos que un Americano gasta 1L de Agua y 0.5kg de Café
mi_inventario.reducir_stock("Agua (L)", 1)
mi_inventario.reducir_stock("Café en grano (kg)", 0.5)

# Simulamos un faltante para disparar la notificación
# Vamos a gastar casi toda la leche
mi_inventario.reducir_stock("Leche (L)", 19) 

gerente_1.logout()
print("\n----------------------------------------")

# 7. PROCESO DE VENTA: INICIO DEL PEDIDO
print("\n--- NUEVA VENTA EN MOSTRADOR ---")

# El empleado inicia sesión para registrar la venta
mesero_3.login() 

print(f"\nAtendiendo a: {cliente_3.nombre}")

# Definimos los productos que Carla va a comprar
p1 = bebida_2  # Frappé de Oreo
p2 = postre_2  # Muffin de Avena
# Creamos el objeto pedido para centralizar todo
ticket_carla = pedido(id_pedido=1050)
ticket_carla.agregar_producto(p1)
ticket_carla.agregar_producto(p2)

# El cliente realiza el pedido (suma puntos iniciales sobre el precio base)
total_inicial = p1.precio_base + p2.precio_base
cliente_3.realizar_pedido(p1.nombre, total_inicial)
cliente_3.realizar_pedido(p2.nombre, total_inicial)

# PASO 1: El mesero deja el pedido como PENDIENTE
mesero_3.cambiar_estado_pedido(ticket_carla.id_pedido, EstadoPedido.PENDIENTE)

print(f"\nResumen: {cliente_3.nombre} ha iniciado su pedido #{ticket_carla.id_pedido}.")
mesero_3.logout()

print("\n----------------------------------------")

# 8. PREPARACIÓN Y DETALLES (EXTRAS Y ESPECIFICACIONES)
print("\n--- ÁREA DE PREPARACIÓN (BARISTA) ---")

# Seleccionamos a Barista 1 para preparar el pedido de Carla
barista_1.login()

print(f"\nPreparando pedido #{ticket_carla.id_pedido} para {cliente_3.nombre}:")

# Jalamos el método agregar_extra (Esto modifica el objeto bebida_2 que está en el ticket)
bebida_2.agregar_extra("Crema Batida", 12.0)
bebida_2.agregar_extra("Jarabe de Chocolate", 5.0)

# Revisamos las especificaciones del postre antes de servir
print(f"\nRevisando etiquetas de: {postre_2.nombre}")
print(f"¿Es Vegano?: {'Sí' if postre_2.es_vegano else 'No'}")
print(f"¿Es Sin Gluten?: {'Sí' if postre_2.sin_gluten else 'No'}")

# PASO 2: La barista cambia el estado a PREPARANDO
barista_1.cambiar_estado_pedido(ticket_carla.id_pedido, EstadoPedido.PREPARANDO)
barista_1.logout()

print("\n----------------------------------------")

# 10. CONSOLIDACIÓN DE VENTA Y TICKET FINAL (DETALLADO)
print("\n--- GENERANDO RECIBO DE PAGO FINAL ---")

# El mesero 2 se encarga de la entrega final y el cobro
mesero_2.login()

# Validamos que el ticket tenga productos (Jalamos de la clase pedido)
ticket_carla.validar_stock()

print(f"\n" + "="*40)
print(f"        TICKET DE VENTA: #{ticket_carla.id_pedido}")
print(f"        CLIENTE: {cliente_3.nombre}")
print(f"="*40)

# --- DETALLE DE BEBIDA (Jalamos método programado) ---
bebida_2.calcular_precio_final() 

# --- DETALLE DE POSTRE (Jalamos atributos manualmente) ---
print(f"\nDETALLE DE POSTRE:")
print(f"Producto: {postre_2.nombre}")
print(f"Opciones: {'Vegano' if postre_2.es_vegano else 'Tradicional'} | {'Sin Gluten' if postre_2.sin_gluten else 'Con Gluten'}")
# AQUÍ JALAMOS EL PRECIO DEL POSTRE QUE FALTABA:
print(f"Precio Unitario: ${postre_2.precio_base}") 

# --- CÁLCULO FINAL ---
print("\n" + "-"*30)
# Jalamos calcular_total para obtener la suma de precios base
total_base = ticket_carla.calcular_total() 
# Sumamos el costo_extra que la barista añadió en el paso anterior
total_con_extras = total_base + bebida_2.costo_extra

print(f"SUBTOTAL (Precios Base): ${total_base}")
print(f"EXTRAS BEBIDA:           ${bebida_2.costo_extra}")
print(f"TOTAL FINAL A PAGAR:     ${total_con_extras}")
print("-" * 30)

# PASO FINAL: Cambiamos el estado a ENTREGADO
mesero_2.cambiar_estado_pedido(ticket_carla.id_pedido, EstadoPedido.ENTREGADO)
mesero_2.logout()

print("\n--- GRACIAS POR SU COMPRA EN COFFEE AMY ---")