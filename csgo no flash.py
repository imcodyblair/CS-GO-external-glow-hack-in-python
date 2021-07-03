     # CS:GO no flash cheat using the python pymem library
import pymem
import pymem.process
import time               

#pointers and offsets from https://github.com/frk1/hazedumper/blob/master/csgo.hpp
dwLocalPlayer = (0xD892CC)
m_flFlashMaxAlpha = (0xA41C) 


def main():
    print(" CS:GO Coneccted...")
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
        player = pm.read_int(client + dwLocalPlayer)
        if player:
            flash_value = player + m_flFlashMaxAlpha
            if flash_value:
                pm.write_float(flash_value, float(1))
        time.sleep(1)


if __name__ == '__main__':
    main()