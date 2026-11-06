# la velocidad de un automovil tiene que ser menos de 90km/h


velocidad = "velocidad indefinida"
velocidad_requerida = "menor o igual a 90 km"

velocidad = int(input("ingrese velocidad: "))
velocidad_requerida = int(input("ingrese velocidad_requerida: "))
#menor_o_igual_que -> <=
menor_o_igual_que = velocidad <= velocidad_requerida
print (f"¿es {velocidad} menor o igual que {velocidad_requerida}? {menor_o_igual_que}")