type_of_flyer_to_correct = input("For \"correctivas\", type and enter \"1\".\nFor \"instalaciones\", type and enter \"2\". \nFor \"revisiones\", type and enter \"3\". \n")

if type_of_flyer_to_correct == "1":
    from Correctivas.correctivas import *
    correct_correctivas_main()

elif type_of_flyer_to_correct == "2":
    from Instalaciones.instalaciones import *
    correct_instalaciones_main()

if type_of_flyer_to_correct == "3":
    from Revisiones.revisiones import *
    correct_revisiones_main()