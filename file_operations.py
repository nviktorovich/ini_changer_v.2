import os
import constants as ct
import re
import datetime


def is_exist(what, where):
    """
    Функция для определения существования файла по указанному пути
    :param what: название файла/папки
    :param where: абсолютный путь до файла/папки
    :return: True если файл/папка существует по указанному пути, иначе - False
    """
    if what in os.listdir(where):
        return True
    return False


def get_ip(ini_file):
    """
    Функция обрабатывает ini файл, с помощью регулярных выражений находит ip адреса основного и резервного комплекта
    КТС УК Возвращает два строковых значения
    :param ini_file: строковое значение - путь до файла
    :return: два строковых
    значения, на 1м месте ip адрес основного комлекта, на 2м - резервного
    """
    ip_main, ip_rez = None, None

    with open(ini_file, encoding=ct.Defaults.ENCODING) as file:
        data = file.read()
    checks_list = re.findall(pattern=ct.Defaults.IP_INI_PATTERN, string=data)

    for check in checks_list:
        if check[0] == ct.Defaults.REZ_NAME_HEADER:
            ip_rez = check[1]
        elif check[0] == ct.Defaults.MAIN_NAME_HEADER:
            ip_main = check[1]

    return ip_main, ip_rez


def select_device_ip(selector, ip_main, ip_rez):
    """
    Функция для выбора IP адреса устройства, на котором будет производитсья замена
    :param selector: 2 входной параметр -m, -r
    :param ip_main: значение IP основного комплекта
    :param ip_rez: значение IP резервного комплекта
    :return: строка со значением основной/резервный в зависимости от параметра
    """
    if selector == "-m":
        return ip_main
    elif selector == "-r":
        return ip_rez


def set_default():
    """
    Функция, предназначенная для того, чтобы вернуть систему хоста в исходное состояние - без папки для
    примонтирования. Проверяется наличие такой папки и наличие в ней файлов, что свидетельствует о том, что в ней уже
    что-то примонтированно. Размонтируем папку, удаляем папку. Если что-то идет не так, возвращаем False
    :return: True если удалось сбросить настройки, иначе - False
    """
    full_path = os.path.join(ct.Defaults.MOUNT_FOLDER, ct.Defaults.MOUNT_DIR_NAME)
    # если папка существует
    if is_exist(ct.Defaults.MOUNT_DIR_NAME, ct.Defaults.MOUNT_FOLDER):
        # проверяем в ней наличие файлов, что свидетельствует о том, что в ней что-то замонтировано
        list_dir = os.listdir(full_path)
        if list_dir:
            # попытка отмонтировать папку, если неудачная, возвращаем False, прекращаем работу программы
            umount_res = umount(full_path)
            if not umount_res:
                return False
        else:
            # попытка удалить папку, если неудачная, возвращаем False, прекращаем работу программы
            remove_res = os.system(ct.Commands.REMOVE_DIR.format(full_path))
            if remove_res != 0:
                return False
    return True


def create_sys_folder(path):
    os.mkdir(path, mode=0o777)


def mount(what, where):
    """
    Функция предназначенная для примонтирования устройства к операционной системе хоста
    :param what: строка типа 192.168.100.125:/mnt/sys
    :param where: строка типа /media/sys
    :return: True в случае, если операция удалась и вернулся 0 статус, в противном случае - False
    """
    make = os.system(ct.Commands.MOUNT_COMMAND.format(what, where))
    if make == 0:
        return True
    return False


def umount(where):
    """
    Функция предназначенная для отмонтирования устройства от операционной системы хоста
    :param where: строка типа /media/sys
    :return: True в случае, если операция удалась и вернулся 0 статус, в противном случае - False
    """
    make = os.system(ct.Commands.UMOUNT_COMMAND.format(where))
    if make == 0:
        return True
    return False


def get_path_to_old_ini(mount_dir_path):
    """
    Функция, предназначенная для того, чтобы определить полный путь до папки, в которой находится INI-файл для замены
    :param mount_dir_path: путь до примонтированной директории типа: /media/sys
    :return: путь до директории с INI-файлом, либо вида /media/sys/BIN, либо вида /media/sys/opt/projectDir
    """
    path_to_ini = os.path.join(mount_dir_path, ct.Defaults.BIN_INI_DIR)
    path_to_etc = os.path.join(mount_dir_path, ct.Defaults.ETC_DIR)
    if is_exist(ct.Defaults.PROJECT_CONF, path_to_etc):
        with open(os.path.join(path_to_etc, ct.Defaults.PROJECT_CONF), encoding=ct.Defaults.ENCODING) as file:
            for line in file.readlines():
                if line.startswith(ct.Defaults.PROJECT_CONF_PATTERN):
                    # path_to_ini = os.path.join(mount_dir_path, *line.split("/")[3::])
                    check_lst = re.findall(ct.Defaults.PROJECT_CONF_PATTERN_RE, line)
                    for chech in check_lst:
                        path_to_ini = os.path.join(mount_dir_path, chech[1])
    return path_to_ini


def get_timestamp():
    """
    Функция с отсуствующими аргументами, предназначена для получения строки с
    отформатированными данными по текущему времени и дате
    :return: отформатированную строку с датой и временем
    """
    now = datetime.datetime.now()
    return now.strftime(ct.Defaults.DATE_PATTERN)


