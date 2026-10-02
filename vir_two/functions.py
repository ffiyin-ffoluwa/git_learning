# Converts temperature
def conv_temp (temp_fah):
    temp_cel = (temp_fah - 32) * 5/9
    return temp_cel

# Converts pressure
def conv_pre(pre_pas):
    pre_nm2 = pre_pas * 1 
    return pre_nm2

# Converts Humidity
def conv_hum(hum_kg):
    hum_g = hum_kg * 1000
    return hum_g

