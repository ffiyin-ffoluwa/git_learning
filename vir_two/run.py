import os
import functions
import getvalues as g
from dotenv import load_dotenv

load_dotenv()
def run():
    name = os.getenv("USER")
    date =os.getenv("DATE")
    temp_fah=g.TEMP_READING
    temp_cel = functions.conv_temp(temp_fah)
    pre_pas = g.PRESSURE
    pre_nm2 = functions.conv_pre(pre_pas)
    hum_g = g.HUMIDITY
    hum_kg = functions.conv_hum(hum_g)
    print(f"Today, {date},")
    print(f" The measurement taking was:")
    print(f"{temp_cel} degree Celcus")
    print(f"{pre_nm2}N/m^2 ")
    print(f"{hum_kg}kg/m^3")
    print(name)

if __name__ == '__main__':
    run()