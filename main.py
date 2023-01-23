#!/usr/bin/python3

import os
import shutil
import sys
import constants as ct
import checkParameters as cp
import fileOperations as fo
import netOperations as nop
import telnetOperations as tnet


def main():
    if cp.input_parameter_check(sys.argv, os.geteuid()):
        # создание переменной active_ini_file для того, чтобы хранить в ней абсолютный путь к файлу, который надо
        # записать
        active_ini_file = os.path.join(os.getcwd(), sys.argv[2])
        # получение информации об IP адрессах
        ip_main, ip_rez = fo.get_ip(active_ini_file)
        if cp.ip_parameter_check(ip_main, ip_rez):
            # записываем в переменную ip адрес в зависимости от входных параметров
            ip = fo.select_device_ip(sys.argv[1], ip_main, ip_rez)
            # 1 пингуем устройство
            if nop.pinger(ip):
                # 2 подготавливаем систему для монтирования
                if fo.set_default():
                    # 3 подключаемся по telnet и устанавливаем режим
                    tnet.set_rw(ip)
                    # 4 создаем временную папку sys в папке /media
                    temp_path = os.path.join(ct.Defaults.MOUNT_FOLDER, ct.Defaults.MOUNT_DIR_NAME)
                    fo.create_sys_folder(temp_path)
                    if fo.is_exist(ct.Defaults.MOUNT_DIR_NAME, ct.Defaults.MOUNT_FOLDER):
                        # 5 монтируем устройство
                        fo.mount(ct.Commands.DEVICE_MNT_SYS.format(ip), temp_path)
                        # 6 выясняем тип структуры
                        old_ini_path = fo.get_path_to_old_ini(temp_path)
                        # 7 проверяем наличие INI в папке, которую получили
                        if fo.is_exist(sys.argv[2], old_ini_path):
                            # 8 переименовываем старый INI
                            old_ini = os.path.join(old_ini_path, sys.argv[2])
                            os.rename(old_ini, old_ini+".{}".format(fo.get_timestamp()))
                            # 9 копируем новый INI в рабочую директорию
                            shutil.copy(active_ini_file, old_ini)
                            # 10 отмонтируем устройство
                            fo.umount(temp_path)
                            # 11 подключаемся по telnet и устанавливаем режим
                            tnet.set_ro(ip)
                            if fo.set_default():
                                os.system(ct.Messages.OK_MESS.format(sys.argv[2], ip))
                                send_exit_and_close()
                            else:
                                os.system(ct.Errors.FINAL_ERR)
                                os.system(ct.Errors.NO_SET_DEFAULT.format(temp_path))
                                send_exit_and_close()
                        else:
                            os.system(ct.Errors.NO_EXIST_INI.format(sys.argv[2], old_ini_path))
                            send_exit_and_close()
                    else:
                        os.system(ct.Errors.NO_EXIST_TMP_FOLDER.format(ct.Defaults.MOUNT_DIR_NAME,
                                                                       ct.Defaults.MOUNT_FOLDER))
                        send_exit_and_close()
                else:
                    os.system(ct.Errors.NO_SET_DEFAULT.format(os.path.join(
                        ct.Defaults.MOUNT_FOLDER,
                        ct.Defaults.MOUNT_DIR_NAME))
                    )
                    send_exit_and_close()
            else:
                os.system(ct.Errors.NO_DEVICE_IN_NET.format(ip))
                send_exit_and_close()
        else:
            os.system(ct.Errors.NOT_IP.format(ip_main, ip_rez))
            send_exit_and_close()
    else:
        send_exit_and_close()


def send_exit_and_close():
    """
    Функция для завершения работы приложения. Отправляет сообщение о завершени работы и выполняет команду sys.exit(1)
    :return:
    """
    os.system(ct.Messages.EXIT_MESS)
    sys.exit(1)


if __name__ == "__main__":
    main()