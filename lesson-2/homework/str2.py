#Extract car names from this text: txt = 'LMaasleitbtui'
# ushbu matndan mashina nomini chiqarib oling
# slicing or indexing  #begin:end:step
 


      #01234567890123
txt = 'LMaasleitbtui'
car_1 = txt[0]+txt[3:5]+txt[6]+txt[8]+  txt[8]+txt[12]
car_2 = txt[1]+txt[2]+txt[5]+txt[7]+txt[9]+txt[11]
print(f"{car_1} and {car_2}")
print(len(txt))