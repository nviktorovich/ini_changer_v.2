import os


def pinger(ip):
    """
    Функция для проверки соединения с устройством, принимает на вход строку, возвращает булево значение
    :param ip: строковый параметр - адресс устройства МПК
    :return: булево значение, если устройтсво по сети отвечает - True, если нет - False
    """
    response = os.system("ping -c 1 {}".format(ip))
    if response == 0:
        return True
    return False
