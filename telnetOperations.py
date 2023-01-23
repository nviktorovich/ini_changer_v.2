import pexpect
import constants as ct
import time


def set_rw(ip):
    conn = pexpect.spawn(ct.Commands.TELNET_CONN.format(ip))
    conn.expect(ct.Commands.KTS_LOGIN_REQUEST)
    time.sleep(200 / 1000)
    conn.sendline(ct.Commands.KTS_USER_NAME)
    time.sleep(200 / 1000)
    conn.expect(ct.Commands.KTS_PASSWORD_REQUEST)
    time.sleep(200 / 1000)
    conn.sendline(ct.Commands.KTS_PASSWORD_ROOT)
    time.sleep(200 / 1000)
    conn.sendline(ct.Commands.KTS_SET_RW_MODE)
    time.sleep(200 / 1000)
    conn.sendline(ct.Commands.EXIT_MESS)


def set_ro(ip):
    conn = pexpect.spawn(ct.Commands.TELNET_CONN.format(ip))
    conn.expect(ct.Commands.KTS_LOGIN_REQUEST)
    time.sleep(200 / 1000)
    conn.sendline(ct.Commands.KTS_USER_NAME)
    time.sleep(200 / 1000)
    conn.expect(ct.Commands.KTS_PASSWORD_REQUEST)
    time.sleep(200 / 1000)
    conn.sendline(ct.Commands.KTS_PASSWORD_ROOT)
    time.sleep(200 / 1000)
    conn.sendline(ct.Commands.KTS_SET_RO_MODE)
    time.sleep(500 / 1000)
    conn.sendline(ct.Commands.REBOOT_MESS)
    time.sleep(200 / 1000)