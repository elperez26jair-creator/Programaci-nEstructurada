
cal1 = float(input("introduce la calif1"))
cal2 = float(input("introduce la calif2"))
cal3 = float(input("introduce la calif3"))

promedio = (cal1 + cal2 +cal3) / 3

if promedio >= 7.0:
    print("aprobado")
elif promedio >=7.1 and promedio <=7.5:
    print("aprobado bajo")
elif promedio  >=7.6 and promedio <=8.7:
    print ("aprobado medio")
            

else :print("no aprobado")