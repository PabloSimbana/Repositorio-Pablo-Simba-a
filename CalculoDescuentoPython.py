# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje al monto total.
    Retorna el valor del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
# Primera llamada: solo se pasa el monto total (usa el 10% por defecto)
monto1 = 1000
descuento1 = calcular_descuento(monto1)
print(f"El descuento para una compra de ${monto1} con 10% es: ${descuento1}")

# Segunda llamada: se pasa el monto total y el porcentaje de descuento
monto2 = 2000
descuento2 = calcular_descuento(monto2, 15)
print(f"El descuento para una compra de ${monto2} con 15% es: ${descuento2}")
