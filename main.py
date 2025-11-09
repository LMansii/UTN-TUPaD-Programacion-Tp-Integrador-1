# TPI - Programacion 1
# Gestion de Datos de Paises en Python
# Autores: Alejandro Daniel Maure y Lautaro Ezequiel Mansilla
# Fecha: Noviembre 2025

import os

# ============================================================================
# CONSTANTES
# ============================================================================

CONTINENTES_VALIDOS = ["America", "Europa", "Asia", "Africa", "Oceania", "Antartida"]
RUTA_CSV = "data/paises.csv"

# ============================================================================
# FUNCIONES DE UTILIDAD
# ============================================================================

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa la ejecucion hasta que el usuario presione Enter"""
    input("\nPresiona Enter para continuar...")

def es_numero_entero(texto):
    """
    Valida si un texto representa un numero entero positivo
    """
    if texto == "" or texto is None:
        return False
    
    # Verificar si todos los caracteres son digitos
    for caracter in texto:
        if caracter not in "0123456789":
            return False
    
    # Verificar que no sea solo ceros
    if int(texto) <= 0:
        return False
    
    return True

def texto_valido(texto):
    """Valida que un texto no este vacio y no contenga solo espacios"""
    if texto is None:
        return False
    texto_limpio = texto.strip()
    return len(texto_limpio) > 0

# ============================================================================
# FUNCIONES DE MANEJO DE ARCHIVOS CSV
# ============================================================================

def cargar_csv(ruta):
    """
    Carga los datos del archivo CSV y los retorna como lista de diccionarios
    Retorna una lista vacia si el archivo no existe
    """
    paises = []
    
    # Verificar si el archivo existe
    if not os.path.exists(ruta):
        print(f"ADVERTENCIA: El archivo {ruta} no existe.")
        return paises
    
    # Abrir y leer el archivo
    archivo = open(ruta, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()
    
    # Verificar que el archivo no este vacio
    if len(lineas) == 0:
        print("ADVERTENCIA: El archivo esta vacio.")
        return paises
    
    # La primera linea es el encabezado
    encabezado = lineas[0].strip().split(",")
    
    # Procesar cada linea de datos
    for i in range(1, len(lineas)):
        linea = lineas[i].strip()
        if linea == "":  # Ignorar lineas vacias
            continue
        
        valores = linea.split(",")
        
        # Crear diccionario para el pais
        pais = {
            "nombre": valores[0],
            "poblacion": int(valores[1]),
            "superficie": int(valores[2]),
            "continente": valores[3]
        }
        paises.append(pais)
    
    return paises

def guardar_csv(ruta, paises):
    """
    Guarda la lista de paises en el archivo CSV
    """
    archivo = open(ruta, "w", encoding="utf-8")
    
    # Escribir encabezado
    archivo.write("nombre,poblacion,superficie,continente\n")
    
    # Escribir cada pais
    for pais in paises:
        linea = f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n"
        archivo.write(linea)
    
    archivo.close()
    print("OK: Archivo CSV guardado correctamente.")

# ============================================================================
# FUNCIONES DE VALIDACION
# ============================================================================

def validar_nombre(nombre, paises, excluir_nombre=None):
    """
    Valida que el nombre no este vacio y no este duplicado
    excluir_nombre: nombre a excluir de la validacion de duplicados (para actualizar)
    """
    if not texto_valido(nombre):
        return False, "El nombre no puede estar vacio."
    
    # Verificar duplicados
    nombre_lower = nombre.lower()
    for pais in paises:
        if excluir_nombre and pais["nombre"].lower() == excluir_nombre.lower():
            continue
        if pais["nombre"].lower() == nombre_lower:
            return False, "Ya existe un pais con ese nombre."
    
    return True, ""

def validar_poblacion(poblacion_texto):
    """Valida que la poblacion sea un numero entero positivo"""
    if not es_numero_entero(poblacion_texto):
        return False, "La poblacion debe ser un numero entero positivo."
    return True, ""

def validar_superficie(superficie_texto):
    """Valida que la superficie sea un numero entero positivo"""
    if not es_numero_entero(superficie_texto):
        return False, "La superficie debe ser un numero entero positivo."
    return True, ""

def validar_continente(continente):
    """Valida que el continente pertenezca a la lista valida"""
    if continente not in CONTINENTES_VALIDOS:
        return False, f"El continente debe ser uno de: {', '.join(CONTINENTES_VALIDOS)}"
    return True, ""

# ============================================================================
# FUNCIONES DE BUSQUEDA Y FILTRADO
# ============================================================================

def buscar_pais_por_nombre(paises, nombre_buscar):
    """
    Busca paises por coincidencia parcial o exacta en el nombre
    Retorna lista de paises que coinciden
    """
    resultados = []
    nombre_buscar_lower = nombre_buscar.lower()
    
    for pais in paises:
        if nombre_buscar_lower in pais["nombre"].lower():
            resultados.append(pais)
    
    return resultados

def filtrar_por_continente(paises, continente):
    """Filtra paises por continente"""
    resultados = []
    
    for pais in paises:
        if pais["continente"] == continente:
            resultados.append(pais)
    
    return resultados

def filtrar_por_poblacion(paises, min_poblacion, max_poblacion):
    """Filtra paises por rango de poblacion"""
    resultados = []
    
    for pais in paises:
        if min_poblacion <= pais["poblacion"] <= max_poblacion:
            resultados.append(pais)
    
    return resultados

def filtrar_por_superficie(paises, min_superficie, max_superficie):
    """Filtra paises por rango de superficie"""
    resultados = []
    
    for pais in paises:
        if min_superficie <= pais["superficie"] <= max_superficie:
            resultados.append(pais)
    
    return resultados

# ============================================================================
# ALGORITMOS DE ORDENAMIENTO MANUAL
# ============================================================================

def ordenar_burbuja(paises, campo, ascendente=True):
    """
    Ordenamiento por metodo de burbuja
    campo: 'nombre', 'poblacion' o 'superficie'
    ascendente: True para orden ascendente, False para descendente
    """
    # Crear copia de la lista para no modificar la original
    lista_ordenada = []
    for pais in paises:
        lista_ordenada.append(pais)
    
    n = len(lista_ordenada)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparar según el campo especificado
            if campo == "nombre":
                valor1 = lista_ordenada[j][campo].lower()
                valor2 = lista_ordenada[j + 1][campo].lower()
            else:
                valor1 = lista_ordenada[j][campo]
                valor2 = lista_ordenada[j + 1][campo]
            
            # Intercambiar si es necesario
            if ascendente:
                condicion = valor1 > valor2
            else:
                condicion = valor1 < valor2
            
            if condicion:
                # Intercambiar elementos
                temp = lista_ordenada[j]
                lista_ordenada[j] = lista_ordenada[j + 1]
                lista_ordenada[j + 1] = temp
    
    return lista_ordenada

def ordenar_insercion(paises, campo, ascendente=True):
    """
    Ordenamiento por metodo de insercion
    campo: 'nombre', 'poblacion' o 'superficie'
    ascendente: True para orden ascendente, False para descendente
    """
    # Crear copia de la lista para no modificar la original
    lista_ordenada = []
    for pais in paises:
        lista_ordenada.append(pais)
    
    n = len(lista_ordenada)
    
    for i in range(1, n):
        clave = lista_ordenada[i]
        
        if campo == "nombre":
            valor_clave = clave[campo].lower()
        else:
            valor_clave = clave[campo]
        
        j = i - 1
        
        # Mover elementos mayores/menores una posición adelante
        while j >= 0:
            if campo == "nombre":
                valor_j = lista_ordenada[j][campo].lower()
            else:
                valor_j = lista_ordenada[j][campo]
            
            if ascendente:
                condicion = valor_j > valor_clave
            else:
                condicion = valor_j < valor_clave
            
            if condicion:
                lista_ordenada[j + 1] = lista_ordenada[j]
                j = j - 1
            else:
                break
        
        lista_ordenada[j + 1] = clave
    
    return lista_ordenada

# ============================================================================
# FUNCIONES DE ESTADISTICAS
# ============================================================================

def calcular_estadisticas(paises):
    """
    Calcula y muestra estadisticas de los paises
    """
    if len(paises) == 0:
        print("No hay datos para calcular estadisticas.")
        return
    
    # Pais con mayor y menor poblacion
    pais_mayor_pob = paises[0]
    pais_menor_pob = paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    
    for pais in paises:
        # Mayor y menor poblacion
        if pais["poblacion"] > pais_mayor_pob["poblacion"]:
            pais_mayor_pob = pais
        if pais["poblacion"] < pais_menor_pob["poblacion"]:
            pais_menor_pob = pais
        
        # Sumas para promedios
        suma_poblacion = suma_poblacion + pais["poblacion"]
        suma_superficie = suma_superficie + pais["superficie"]
    
    # Promedios
    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)
    
    # Cantidad de paises por continente
    continentes_count = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in continentes_count:
            continentes_count[continente] = continentes_count[continente] + 1
        else:
            continentes_count[continente] = 1
    
    # Mostrar estadisticas
    print("\n" + "="*60)
    print("ESTADISTICAS DE LOS PAISES")
    print("="*60)
    
    print(f"\nPais con MAYOR poblacion:")
    print(f"   {pais_mayor_pob['nombre']}: {pais_mayor_pob['poblacion']:,} habitantes")
    
    print(f"\nPais con MENOR poblacion:")
    print(f"   {pais_menor_pob['nombre']}: {pais_menor_pob['poblacion']:,} habitantes")
    
    print(f"\nPromedio de poblacion: {promedio_poblacion:,.0f} habitantes")
    print(f"Promedio de superficie: {promedio_superficie:,.0f} km2")
    
    print(f"\nCantidad de paises por continente:")
    for continente in continentes_count:
        print(f"   {continente}: {continentes_count[continente]} pais(es)")
    
    print("="*60)

# ============================================================================
# FUNCIONES DE VISUALIZACION
# ============================================================================

def mostrar_paises(paises, titulo="Lista de Paises"):
    """Muestra la lista de paises en formato tabla"""
    if len(paises) == 0:
        print("No hay paises para mostrar.")
        return
    
    print("\n" + "="*80)
    print(f"  {titulo}")
    print("="*80)
    print(f"{'Nombre':<20} {'Poblacion':<15} {'Superficie (km2)':<20} {'Continente':<15}")
    print("-"*80)
    
    for pais in paises:
        print(f"{pais['nombre']:<20} {pais['poblacion']:<15,} {pais['superficie']:<20,} {pais['continente']:<15}")
    
    print("-"*80)
    print(f"Total: {len(paises)} pais(es)")
    print("="*80)

# ============================================================================
# FUNCIONES DEL MENU PRINCIPAL
# ============================================================================

def menu_agregar_pais(paises):
    """Opcion 2: Agregar un pais"""
    print("\n" + "="*60)
    print("AGREGAR NUEVO PAIS")
    print("="*60)
    
    # Solicitar nombre
    nombre = input("\nNombre del pais: ").strip()
    valido, mensaje = validar_nombre(nombre, paises)
    if not valido:
        print(f"ERROR: {mensaje}")
        return
    
    # Solicitar poblacion
    poblacion_texto = input("Poblacion: ").strip()
    valido, mensaje = validar_poblacion(poblacion_texto)
    if not valido:
        print(f"ERROR: {mensaje}")
        return
    poblacion = int(poblacion_texto)
    
    # Solicitar superficie
    superficie_texto = input("Superficie (km2): ").strip()
    valido, mensaje = validar_superficie(superficie_texto)
    if not valido:
        print(f"ERROR: {mensaje}")
        return
    superficie = int(superficie_texto)
    
    # Solicitar continente
    print(f"\nContinentes validos: {', '.join(CONTINENTES_VALIDOS)}")
    continente = input("Continente: ").strip()
    valido, mensaje = validar_continente(continente)
    if not valido:
        print(f"ERROR: {mensaje}")
        return
    
    # Agregar el pais
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo_pais)
    
    print(f"\nOK: El pais '{nombre}' ha sido agregado correctamente.")
    print("ADVERTENCIA: Recuerda guardar los cambios en el CSV (opcion 8).")

def menu_actualizar_pais(paises):
    """Opcion 3: Actualizar datos de un pais"""
    print("\n" + "="*60)
    print("ACTUALIZAR DATOS DE UN PAIS")
    print("="*60)
    
    nombre = input("\nNombre del pais a actualizar: ").strip()
    
    # Buscar el pais
    pais_encontrado = None
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais_encontrado = pais
            break
    
    if pais_encontrado is None:
        print(f"ERROR: No se encontro el pais '{nombre}'.")
        return
    
    print(f"\nDatos actuales de {pais_encontrado['nombre']}:")
    print(f"  Poblacion: {pais_encontrado['poblacion']:,}")
    print(f"  Superficie: {pais_encontrado['superficie']:,} km2")
    print(f"  Continente: {pais_encontrado['continente']}")
    
    # Solicitar nueva poblacion
    print("\n(Dejar en blanco para mantener el valor actual)")
    poblacion_texto = input("Nueva poblacion: ").strip()
    
    if poblacion_texto != "":
        valido, mensaje = validar_poblacion(poblacion_texto)
        if not valido:
            print(f"ERROR: {mensaje}")
            return
        pais_encontrado["poblacion"] = int(poblacion_texto)
    
    # Solicitar nueva superficie
    superficie_texto = input("Nueva superficie (km2): ").strip()
    
    if superficie_texto != "":
        valido, mensaje = validar_superficie(superficie_texto)
        if not valido:
            print(f"ERROR: {mensaje}")
            return
        pais_encontrado["superficie"] = int(superficie_texto)
    
    print(f"\nOK: El pais '{pais_encontrado['nombre']}' ha sido actualizado correctamente.")
    print("ADVERTENCIA: Recuerda guardar los cambios en el CSV (opcion 8).")

def menu_buscar_pais(paises):
    """Opcion 4: Buscar un pais"""
    print("\n" + "="*60)
    print("BUSCAR PAIS")
    print("="*60)
    
    nombre = input("\nIngresa el nombre o parte del nombre: ").strip()
    
    if not texto_valido(nombre):
        print("ERROR: Debes ingresar un nombre valido.")
        return
    
    resultados = buscar_pais_por_nombre(paises, nombre)
    
    if len(resultados) == 0:
        print(f"\nERROR: No se encontraron paises que coincidan con '{nombre}'.")
    else:
        mostrar_paises(resultados, f"Resultados de busqueda: '{nombre}'")

def menu_filtrar_paises(paises):
    """Opcion 5: Filtrar paises"""
    print("\n" + "="*60)
    print("FILTRAR PAISES")
    print("="*60)
    print("\n1. Filtrar por continente")
    print("2. Filtrar por rango de poblacion")
    print("3. Filtrar por rango de superficie")
    print("4. Volver al menu principal")
    
    opcion = input("\nSelecciona una opcion: ").strip()
    
    if opcion == "1":
        # Filtrar por continente
        print(f"\nContinentes disponibles: {', '.join(CONTINENTES_VALIDOS)}")
        continente = input("Ingresa el continente: ").strip()
        
        valido, mensaje = validar_continente(continente)
        if not valido:
            print(f"ERROR: {mensaje}")
            return
        
        resultados = filtrar_por_continente(paises, continente)
        
        if len(resultados) == 0:
            print(f"\nERROR: No se encontraron paises en {continente}.")
        else:
            mostrar_paises(resultados, f"Paises de {continente}")
    
    elif opcion == "2":
        # Filtrar por poblacion
        min_pob = input("Poblacion minima: ").strip()
        max_pob = input("Poblacion maxima: ").strip()
        
        if not es_numero_entero(min_pob) or not es_numero_entero(max_pob):
            print("ERROR: Los valores deben ser numeros enteros positivos.")
            return
        
        min_poblacion = int(min_pob)
        max_poblacion = int(max_pob)
        
        if min_poblacion > max_poblacion:
            print("ERROR: La poblacion minima no puede ser mayor que la maxima.")
            return
        
        resultados = filtrar_por_poblacion(paises, min_poblacion, max_poblacion)
        
        if len(resultados) == 0:
            print(f"\nERROR: No se encontraron paises con poblacion entre {min_poblacion:,} y {max_poblacion:,}.")
        else:
            mostrar_paises(resultados, f"Paises con poblacion entre {min_poblacion:,} y {max_poblacion:,}")
    
    elif opcion == "3":
        # Filtrar por superficie
        min_sup = input("Superficie minima (km2): ").strip()
        max_sup = input("Superficie maxima (km2): ").strip()
        
        if not es_numero_entero(min_sup) or not es_numero_entero(max_sup):
            print("ERROR: Los valores deben ser numeros enteros positivos.")
            return
        
        min_superficie = int(min_sup)
        max_superficie = int(max_sup)
        
        if min_superficie > max_superficie:
            print("ERROR: La superficie minima no puede ser mayor que la maxima.")
            return
        
        resultados = filtrar_por_superficie(paises, min_superficie, max_superficie)
        
        if len(resultados) == 0:
            print(f"\nERROR: No se encontraron paises con superficie entre {min_superficie:,} y {max_superficie:,} km2.")
        else:
            mostrar_paises(resultados, f"Paises con superficie entre {min_superficie:,} y {max_superficie:,} km2")
    
    elif opcion == "4":
        return
    else:
        print("ERROR: Opcion invalida.")

def menu_ordenar_paises(paises):
    """Opcion 6: Ordenar paises"""
    print("\n" + "="*60)
    print("ORDENAR PAISES")
    print("="*60)
    print("\n1. Ordenar por nombre")
    print("2. Ordenar por poblacion")
    print("3. Ordenar por superficie")
    print("4. Volver al menu principal")
    
    opcion = input("\nSelecciona una opcion: ").strip()
    
    if opcion not in ["1", "2", "3", "4"]:
        print("ERROR: Opcion invalida.")
        return
    
    if opcion == "4":
        return
    
    # Determinar el campo a ordenar
    if opcion == "1":
        campo = "nombre"
    elif opcion == "2":
        campo = "poblacion"
    else:
        campo = "superficie"
    
    # Seleccionar algoritmo
    print("\nAlgoritmo de ordenamiento:")
    print("1. Metodo burbuja")
    print("2. Metodo insercion")
    
    algoritmo = input("\nSelecciona el algoritmo: ").strip()
    
    if algoritmo not in ["1", "2"]:
        print("ERROR: Opcion invalida.")
        return
    
    # Seleccionar orden
    print("\nOrden:")
    print("1. Ascendente")
    print("2. Descendente")
    
    orden = input("\nSelecciona el orden: ").strip()
    
    if orden not in ["1", "2"]:
        print("ERROR: Opcion invalida.")
        return
    
    ascendente = (orden == "1")
    
    # Ordenar
    if algoritmo == "1":
        paises_ordenados = ordenar_burbuja(paises, campo, ascendente)
        metodo = "Burbuja"
    else:
        paises_ordenados = ordenar_insercion(paises, campo, ascendente)
        metodo = "Insercion"
    
    orden_texto = "Ascendente" if ascendente else "Descendente"
    titulo = f"Paises ordenados por {campo} ({metodo}, {orden_texto})"
    
    mostrar_paises(paises_ordenados, titulo)

def mostrar_menu():
    """Muestra el menu principal"""
    print("\n" + "="*60)
    print("SISTEMA DE GESTION DE PAISES")
    print("="*60)
    print("\n1. Cargar/recargar archivo CSV")
    print("2. Agregar un pais")
    print("3. Actualizar datos de un pais")
    print("4. Buscar un pais")
    print("5. Filtrar paises")
    print("6. Ordenar paises")
    print("7. Mostrar estadisticas")
    print("8. Guardar cambios en el CSV")
    print("9. Salir del programa")
    print("\n" + "="*60)

# ============================================================================
# FUNCION PRINCIPAL
# ============================================================================

def main():
    """Funcion principal del programa"""
    paises = []
    datos_cargados = False
    
    print("\nBienvenido al Sistema de Gestion de Paises!")
    print("Por favor, carga el archivo CSV para comenzar (opcion 1).")
    
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opcion: ").strip()
        
        if opcion == "1":
            # Cargar/recargar CSV
            print("\nCargando archivo CSV...")
            paises = cargar_csv(RUTA_CSV)
            if len(paises) > 0:
                datos_cargados = True
                print(f"OK: Se cargaron {len(paises)} paises correctamente.")
                mostrar_paises(paises)
            else:
                datos_cargados = False
                print("ERROR: No se pudieron cargar los datos.")
            pausar()
        
        elif opcion == "2":
            # Agregar pais
            if not datos_cargados:
                print("ADVERTENCIA: Primero debes cargar el archivo CSV (opcion 1).")
            else:
                menu_agregar_pais(paises)
            pausar()
        
        elif opcion == "3":
            # Actualizar pais
            if not datos_cargados:
                print("ADVERTENCIA: Primero debes cargar el archivo CSV (opcion 1).")
            else:
                menu_actualizar_pais(paises)
            pausar()
        
        elif opcion == "4":
            # Buscar pais
            if not datos_cargados:
                print("ADVERTENCIA: Primero debes cargar el archivo CSV (opcion 1).")
            else:
                menu_buscar_pais(paises)
            pausar()
        
        elif opcion == "5":
            # Filtrar paises
            if not datos_cargados:
                print("ADVERTENCIA: Primero debes cargar el archivo CSV (opcion 1).")
            else:
                menu_filtrar_paises(paises)
            pausar()
        
        elif opcion == "6":
            # Ordenar paises
            if not datos_cargados:
                print("ADVERTENCIA: Primero debes cargar el archivo CSV (opcion 1).")
            else:
                menu_ordenar_paises(paises)
            pausar()
        
        elif opcion == "7":
            # Mostrar estadisticas
            if not datos_cargados:
                print("ADVERTENCIA: Primero debes cargar el archivo CSV (opcion 1).")
            else:
                calcular_estadisticas(paises)
            pausar()
        
        elif opcion == "8":
            # Guardar cambios
            if not datos_cargados:
                print("ADVERTENCIA: Primero debes cargar el archivo CSV (opcion 1).")
            else:
                confirmacion = input("\nEstas seguro de guardar los cambios? (s/n): ").strip().lower()
                if confirmacion == "s" or confirmacion == "si":
                    guardar_csv(RUTA_CSV, paises)
                else:
                    print("ERROR: No se guardaron los cambios.")
            pausar()
        
        elif opcion == "9":
            # Salir
            print("\nGracias por usar el Sistema de Gestion de Paises!")
            print("Hasta luego!\n")
            break
        
        else:
            print("ERROR: Opcion invalida. Por favor, selecciona una opcion del 1 al 9.")
            pausar()

# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    main()