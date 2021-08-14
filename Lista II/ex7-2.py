area = float(input("Área a ser pintada (em m²): "))
if area % 54 == 0:
   print(f"{area/54} latas")    
else:
   print(f"{int(area/54+1)} latas")
