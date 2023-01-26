class Commands:
    DEVICE_MNT_SYS = "{}:/mnt/sys"
    MOUNT_PATH = "/media/sys"
    MOUNT_COMMAND = "mount {} {}"
    UMOUNT_COMMAND = "umount -f {}"
    REMOVE_DIR = "rm -r {}"


class Errors:
    WEAK_USER = "echo ошибка запуска программы. Необходиы привелегии суперпользователя. Используйте sudo."
    FEW_INPUT_ARGUMENTS = "echo 'ошибка вводных аргументов. Необходимо запускать программу с аргументами: -h HELP'"
    FIRST_INPUT_ARGUMENT = "echo ошибка вводных аргументов. Значение первого аргумента недопустимо: {}"
    NOT_EXIST = "echo ошибка вводных аргументов. Отсутствует файл {} в директории {}"
    REDUDANT_PARAMETERS = "echo ошибка введенных аргументов. Присуствуют избыточные параметры {}"
    NOT_IP = "echo ошибка распознования файла. Не удалось получить информацию об IP-адрессах main: {}, rez: {}"
    NO_DEVICE_IN_NET = "echo ошибка работы с сетью. Не удалось установить соединение с устройством {}"
    NO_SET_DEFAULT = "echo ошибка работы с файловой системой хоста. Не удалось установить исходное состояние системы. Проверьте папку {}"
    NO_EXIST_TMP_FOLDER = "echo ошибка работы с файловой системой хоста. Не удалось создать папку {} в директории {}"
    NO_EXIST_INI = "echo ошибка работы с файловой системой МПК. Не удалось обнаружить файл {} в директории {}"
    FINAL_ERR = "echo после успешного проведения всех операций возникла ошибка с восстановлением исходного состояния"
    TNET_FAIL = "echo ошибка установки режима. Модуль telnet_driver вернул ошибку."


class Messages:
    EXIT_MESS = "echo работа приложения завершена."
    OK_MESS = "echo успешное выполнение всех операций. INI - {} заменен на устройстве ip - {}"
    HELP_INFO = "echo 'Использование:\nktschange <комплект: -m(основной)/-r(резервный)> <INI-файл>\nktschange <HELP: " \
                "-h/-help/-H>'"


class Defaults:
    ENCODING = "koi8-r"
    IP_INI_PATTERN = r" *отправитель(Резервный|Основной) *{ *[ \t]*[ \n]*[ \t]*адрес:([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})"
    MAIN_NAME_HEADER = "Основной"
    REZ_NAME_HEADER = "Резервный"
    MOUNT_DIR_NAME = "sys"
    MOUNT_FOLDER = "/media"
    BIN_INI_DIR = "BIN"
    ETC_DIR = "etc"
    PROJECT_CONF = "project.conf"
    PROJECT_CONF_PATTERN = "PROJECT_DIR"
    PROJECT_CONF_PATTERN_RE = "(^PROJECT_DIR=\/mnt\/sys\/)(\S*)"
    DATE_PATTERN = "%Y-%m-%d %H:%M "
    PATH_TO_EXECUTABLE_FILE = "/bin/ktschange-files/telnet_driver"
    RO = "ro"
    RW = "rw"

