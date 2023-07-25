import requests
import serial
import time
arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
print("Program Started")

mejaIn = []
mejaTime = []


def check_and_remove_data(data_list, meja_value):
    for data in data_list:
        if 'meja' in data and data['meja'] == meja_value:
            endTime = time.time()
            timeDiff = endTime - data['start']
            print(
                f"Lama waktu lampu {data['meja']} menyala: {timeDiff:.2f} detik")
            data_list.remove(data)
            sendData(meja_value, timeDiff)

            break
    else:
        print(f"Data dengan meja {meja_value} tidak ditemukan.")


def sendData(mejaId, durasi):
    u = 'http://localhost/kasir/public/api/sensor/store'
    br = {'id_meja': mejaId, 'duration': round(durasi, 2)}
    r = requests.post(u, br)
    print(br)
    print(r.json())


while True:
    try:
        data = arduino.readline()
        # Menghapus karakter newline dari data
        decodeData = data.decode('utf-8').strip()

        # print(mejaTime)

        if decodeData.startswith('[') and decodeData.endswith(']'):
            # Parsing data sebagai array of integers
            if decodeData != '[]':  # data is not null
                # parse array from arduino
                newMejaIn = list(map(int, decodeData[1:-1].split(',')))
                if mejaIn != newMejaIn:
                    for data in newMejaIn:
                        if (data in mejaIn):
                            for meja in mejaIn:
                                if (meja in newMejaIn):
                                    print(meja, 'ada')
                                else:
                                    print(meja, 'hilang')
                                    check_and_remove_data(mejaTime, meja)
                        else:
                            mejaTime.append(
                                {"meja": data, "start": time.time()})
                            print(data, ' baru')
                    mejaIn = newMejaIn
                else:
                    print('pass')
            else:
                if len(mejaIn) > 0:
                    for data in mejaIn:
                        check_and_remove_data(mejaTime, data)
                    mejaIn = []

    except Exception:
        print("Error, repeating")
        pass
