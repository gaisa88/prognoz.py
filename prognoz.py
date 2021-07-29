from pyowm import *
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('fcb2def8228d9db2e61a145594269557', config_dict)
mgr = owm.weather_manager()
def pogoda(city):
    observation = mgr.weather_at_place(city)
    pogoda = observation.weather
    temp = pogoda.temperature('celsius')['temp']
    crednyaya = pogoda.temperature('celsius')['feels_like']
    state = pogoda.detailed_status
    veter = pogoda.wind()['speed']
    vlaga = pogoda.humidity
    print("В "+city.title()+" сейчас: "+state)
    print("Темпиратура: "+str(temp)+" градусов, ощущается как "+ str(crednyaya))
    print("Скорость ветра: "+str(veter)+" м/с")
    print("Влажность "+str(vlaga)+ "%")
pogoda(input("Введите город, в котором хотите узнать погоду: "))

k = input("Программа завершена, нажмите клавишу Enter для закрытия окна приложения")