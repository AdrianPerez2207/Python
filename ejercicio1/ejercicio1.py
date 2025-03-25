

def calcular_precio(modelo, color):
    precio_base = {"M1": 8000, "M2": 10000, "M3": 12000, "M4": 14000}
    suplementos = {"amarillo": 1.03, "rojo": 1.05}
    precio = precio_base[modelo] * suplementos.get(color, 1)
    return precio


def organizar_stock(lista_coches):
    stock = []
    for modelo, color in lista_coches:
        precio = calcular_precio(modelo, color)
        stock.append((modelo, color, precio))

    #Ordenar por precio ascendente, el precio se encuentra en la posición 2 de la lista.
    stock.sort(key=lambda x: x[2])
    return stock

#El stock es una lista de coches.
def resolver_peticion(stock, modelo_solicitado, color_solicitado):
    stock_organizado = organizar_stock(stock)
    #Encontrar el modelo solicitado en el stock.
    for modelo in stock_organizado:
        #Recorremos el stock para encontrar el modelo solicitado y el color solicitado.
        for color in stock_organizado[modelo_solicitado]:
            if color == color_solicitado:
                return modelo_solicitado, color
        
        #Volvemos a recorrer el stock para encontrar el modelo solicitado de diferente color, buscamos el modelo y sacamos el índice.
        for modelo, index in stock_organizado:
            if modelo in modelo_solicitado:
                return stock_organizado[index]
            
        for modelo, color, index in stock_organizado:
            if modelo not in modelo_solicitado and color == color_solicitado:
                return stock_organizado[index]
            
        for modelo, color, index in stock_organizado:
            if modelo not in modelo_solicitado and color not in color_solicitado:
                return stock_organizado[index]

    


lista_vehiculos = [("M1", "amarillo"), ("M2", "rojo"), ("M3", "rojo"), ("M4", "amarillo")]

print(resolver_peticion(lista_vehiculos, "M1", "amarillo"))