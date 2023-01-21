import os
import constants as ct
import file_operations as fo


def input_parameter_check(parameter_list):
    """
    Функция предназначенная для проверки входных параметров
    :param parameter_list: список со входными параметрами
    :return: True если входные параметры верны, иначе False
    """
    # 1 проверка длинны parameter_list, если длинна равна единице вывести сообщение о ключе -h и завершить работу
    if len(parameter_list) == 1:
        os.system(ct.Errors.FEW_INPUT_ARGUMENTS)
        return False

    elif len(parameter_list) > 1:
        # 2 проверка первого параметра. Разрешенные значения -m, -r, -h, -H, -help
        if parameter_list[1] not in ["-m", "-r", "-h", "-H", "-help"]:
            os.system(ct.Errors.FIRST_INPUT_ARGUMENT.format(parameter_list[1]))
            return False

        # 3 проверка вызова меню помощи -h, -H, -help
        if parameter_list[1] in ["-h", "-H", "-help"]:
            os.system(ct.Messages.HELP_INFO)
            return False

        if len(parameter_list) > 2:
            # 4 проверка второго параметра - это должен быть файл, находящийся в данной директории
            if not fo.is_exist(parameter_list[2], os.getcwd()):
                os.system(ct.Errors.NOT_EXIST.format(parameter_list[2], os.getcwd()))
                return False

            # 5 если количество параметров больше 3, возвращаем ошибку
            if len(parameter_list) > 3:
                os.system(ct.Errors.REDUDANT_PARAMETERS.format(parameter_list[3::]))
                return False
    # в случае, если все проверки прошли успешно, возвращаем True
    return True


def ip_parameter_check(ip_rez, ip_main):
    if ip_main is not None and ip_rez is not None:
        return True
    return False

