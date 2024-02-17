import sys
import os
import click
import subprocess
import shlex
import platform

HERE = os.path.dirname(os.path.abspath(__file__))
OS_TYPE = platform.platform().split('-')[0]

@click.command()
def main():
    """
    Python command line tool to test espressif boards automatically. 
    \b
    Example:
    \b
    \t $ autoesp
    \t 
    """
    click.echo("")
    #click.echo("! Using Espressif Boards PyPi index ! ")
    if (OS_TYPE=='Darwin' or OS_TYPE=='macOS'):
        text_show = """echo "! Auto Testing \x1b[32;1mEspressif Boards \x1b[0m ! " """
    elif OS_TYPE=='Linux':
        text_show = """echo "! Auto Testing \e[32m\e[5mEspressif Boards \e[39m\e[25m ! " """
    elif OS_TYPE == 'Windows':
        text_show = """echo "! Auto Testing Espressif Boards ! " """
    os.system(text_show)
    click.echo("")

    
    cmd = """
    echo "----------------"
    echo "[ESP BOARD TEST]"
    echo "----------------"

    FDIR="""+HERE+"""
    echo "FDIR: ${FDIR}"

    FIRMWARE_FOLDER="${FDIR}/firmwares"


    getInfo () {
        #boardInfo=$(esptool.py read_mac | tee /dev/tty)
        # boardInfo=$(esptool.py flash_id | tee /dev/tty)
        boardInfo=$(esptool.py flash_id | tee /dev/tty)
        echo ""
        SERIAL_PORT=$(echo "${boardInfo}" | grep "Serial port " | awk -F ' ' '{print $3}')
        BOARD_CHIP=$(echo "${boardInfo}" | grep "Chip is " | awk -F ' ' '{print $3}')
    }


    eraseFlash () {
        # read -p "Enter the Serial PORT: " SERIAL_PORT
        echo ""
        echo "Erasing flash ..."
        case ${BOARD} in
            ESP8266* ) echo "  Executing on Board: [${BOARD}]" && esptool.py --chip ${CHIP} --port ${SERIAL_PORT} erase_flash;;
            ESP32* ) echo "  Executing on Board: [${BOARD}]" && esptool.py --chip ${CHIP} --port ${SERIAL_PORT} erase_flash;;
            * ) echo "[ERROR] Board type NOT recognized." && exit 1;;
        esac
        echo "... erased!"
        echo ""
    }


    writeFlash () {
        # read -p "Enter the firmware file name: " FIRMWARE_FILE
        echo ""
        echo "Writing firmware ..."
        case ${BOARD} in
            ESP8266* ) echo "  Flashign [${FIRMWARE_FILE}] to board [${BOARD}]" && esptool.py --chip ${CHIP} --port ${SERIAL_PORT} write_flash --flash_size=detect 0 ${FIRMWARE_FOLDER}/${FIRMWARE_FILE};;
            ESP32* ) echo "  Flashign [${FIRMWARE_FILE}] to board [${BOARD}]" && esptool.py --chip ${CHIP} --port ${SERIAL_PORT} write_flash -z 0x1000 ${FIRMWARE_FOLDER}/${FIRMWARE_FILE};;
            * ) echo "[ERROR] Board type NOT recognized." && exit 1;;
        esac

        echo "... written!"
        echo ""
    }


    copyCodes () {
        # read -p "Enter the config folder: " CONFIG_FOLDER
        CONFIG_FOLDER="${FDIR}/config"
        MODULE_FOLDER="${FDIR}/modules"
        echo ""
        echo "Copying codes ..."
        ampy -p ${SERIAL_PORT} mkdir config
        ampy -p ${SERIAL_PORT} put ${CONFIG_FOLDER}/wifi.conf config/wifi.conf
        ampy -p ${SERIAL_PORT} put ${CONFIG_FOLDER}/mqtt.conf config/mqtt.conf
        ampy -p ${SERIAL_PORT} put boot.py boot.py
        case ${BOARD} in
            ESP8266 ) ampy -p ${SERIAL_PORT} put main-esp8266.py main.py;;
            ESP32 ) ampy -p ${SERIAL_PORT} put main-esp32.py main.py;;
            ESP8266-01S ) ampy -p ${SERIAL_PORT} put main-esp8266-01s.py main.py && \
                          ampy -p ${SERIAL_PORT} mkdir umqtt && \
                          ampy -p ${SERIAL_PORT} put ${MODULE_FOLDER}/umqtt/simple.py /umqtt/simple.py && \
                          ampy -p ${SERIAL_PORT} put ${MODULE_FOLDER}/umqtt/__init__.py /umqtt/__init__.py ;;
            * ) echo "[ERROR] Board type NOT specified." && exit 1;;
        esac
        echo "... copied!"
        echo ""
    }


    getInfo

    if [[ "${boardInfo}" = *"A fatal error occurred: Could not connect to an Espressif device on any of"* ]]; then
        echo ""
        echo "[ERROR] NO ESP board found on any serial port."
        echo ""
        exit 1
    fi


    echo ""
    echo "Chip is: ${BOARD_CHIP}"

    while true; do
        if [[ ${SERIAL_PORT} == "" ]]; then
            echo "    [ABORT] Empty Serial Port input."
            exit 1
        elif [[ ${SERIAL_PORT} != "/dev/"* ]] && [[ ${SERIAL_PORT} != *"COM"* ]] ; then
            echo "    [WARNING] Serial Port [${SERIAL_PORT}] is unusual."
        fi
        read -p "Confirm to proceed on Serial Port [${SERIAL_PORT}]? [Y/n] " CONFIRM_PORT
        case ${CONFIRM_PORT} in
            y|Y|yes|Yes) break;;
            n|N|no|No) read -p "Enter the Serial PORT: " SERIAL_PORT;;
            *) echo "    Invalid input. (Type 'n' or 'No' if you want to change to another port)" >&2
        esac
    done


    if [[ ${SERIAL_PORT} == "" ]]; then
        echo "[ABORT] NO Serial Port provided. "
        exit 0
    else
        echo ""
        echo "Operating on Serial Port: ${SERIAL_PORT}"
    fi


    echo ""
    echo "Boards: "
    echo "    1: ESP8266 NodeMCU/D1-Mini"
    echo "    2: ESP32 WROOM/D1-Mini"
    echo "    3: ESP8266 01S"
    echo "    4: ESP32 S2-Mini"
    while true; do
        read -p "Confirm the board type: " BOARD_INDEX
        case ${BOARD_INDEX} in
            1 ) BOARD="ESP8266" && CHIP="esp8266" && FIRMWARE_FILE="ESP8266_GENERIC-20240105-v1.22.1.bin" && break;;
            2 ) BOARD="ESP32" && CHIP="esp32" && FIRMWARE_FILE="ESP32_GENERIC-20240105-v1.22.1.bin" && break;;
            3 ) BOARD="ESP8266-01S" && CHIP="esp8266" && FIRMWARE_FILE="ESP8266_GENERIC-FLASH_1M-20240105-v1.22.1.bin" && break;;
            4 ) BOARD="ESP32-S2-Mini" && CHIP="esp32s2" && FIRMWARE_FILE="LOLIN_S2_MINI-20240105-v1.22.1.uf2" && break;;
            * ) echo "    [ERROR] Bad input.";;
        esac
    done


    echo "Options: "
    echo "    0: Copy code only."
    echo "    1: Erase only."
    echo "    2: Erase and flash firmware."
    echo "    3: Erase, flash firmware, and copy code."

    while true; do
        read -p "Which option to choose: " OPTION
        case ${OPTION} in
            0 ) copyCodes && break;;
            1 ) eraseFlash && break;;
            2 ) eraseFlash && sleep 3 && writeFlash && break;;
            3 ) eraseFlash && sleep 3 && writeFlash && sleep 5 && copyCodes && break;;
            * ) echo "    [ERROR] Bad input.";;
        esac
    done

    echo "----------"
    echo "[ALL DONE]"
    echo "----------"
    """

    subprocess.call(["bash", "-c", cmd])


if __name__ == '__main__':
    print(f"HERE: {HERE}")
    main()