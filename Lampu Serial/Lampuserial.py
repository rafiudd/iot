import requests
import serial
import time
import serial.tools.list_ports
import easygui as eg

runArduino = False
arduino = None

def list_available_ports():
    available_ports = list(serial.tools.list_ports.comports())
    return available_ports


def checkIfValidBoard(port):
    arduino = serial.Serial(port=port, baudrate=57600, timeout=.1)
    tipe=arduino.readline()
    print(tipe)

def select_port(available_ports):
    port_choices = [f"{port.device}: {port.description}" for port in available_ports]
    port_choices.append("Batalkan")
    msg = "Pilih port Arduino yang ingin digunakan:"
    title = "Pilih Port Arduino"
    selected_port = eg.choicebox(msg, title, port_choices)
    if selected_port:
        selected_port = selected_port.split(":")[0]
    return selected_port

available_ports = list_available_ports()
if available_ports:
    selected_port = select_port(available_ports)
    if selected_port:
        print(f"Port yang dipilih: {selected_port}")
        # checkIfValidBoard(selected_port)
        if (selected_port != 'Batalkan'):
            arduino = serial.Serial(port=selected_port, baudrate=57600, timeout=.1)
            time.sleep(5)
            runArduino = True
    else:
        print("Tidak ada port yang dipilih.")
else:
    print("Tidak ditemukan port Arduino yang tersedia.")


while runArduino:
    print(arduino)
    try:
        while True:
            r = requests.get('http://localhost/kasir/public/datalampu')
            q=r.raise_for_status()
            t=(r.text).strip()
            print("read=", t)
            arduino.write(bytes(t, 'utf-8'))
            time.sleep(0.1)
            data = arduino.readline()
            print("return=", data)
            time.sleep(5)
            
    except Exception as e:
        print(str(e))
        print("Error, repeating")
        pass

