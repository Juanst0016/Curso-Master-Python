
Inyecciones = int(input("Cantidad de inyecciones :"))
NPH = int(input("Introduce lo NPH por día :"))
Rapida_dia = int(input("Introduce la Inyección rapida por día :"))

print(f"Tienes {Inyecciones} inyecciones")
print("Pinchazos por día :" + str(NPH + Rapida_dia))
pinchazo_mes = (NPH + Rapida_dia * 30)
pinchazo_dia = (NPH + Rapida_dia)
print("Pinchazos por aguja :" + str(pinchazo_mes / pinchazo_dia))






    