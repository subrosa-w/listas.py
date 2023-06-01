opcion1="si"
opcion2="no"
ingreso=input("ingrese si o no: ")
if ingreso.lower() == opcion1:
    print("ingreso si")
elif ingreso.lower() == opcion2:
    print("ingreso no")
else:
    print("error de ingreso")
