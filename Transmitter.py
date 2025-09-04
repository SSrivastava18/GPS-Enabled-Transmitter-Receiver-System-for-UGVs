import serial
import time
from MicropyGPS import MicropyGPS

BAUDRATE = 115200
LORA_PORT = '/dev/ttyS0'
GPS_PORT = '/dev/ttyUSB0'

lora_serial = serial.Serial(LORA_PORT, BAUDRATE, timeout=1)
gps_serial = serial.Serial(GPS_PORT, 9600, timeout=1)

gps = MicropyGPS()

def send_lora(data, address):
    """Send data to LoRa module."""
    command = f"AT+SEND={address},{len(data)},{data}\r\n"
    lora_serial.write(command.encode('utf-8'))

def display_info():
    """Process and send GPS data."""
    if gps.latitude[0] and gps.longitude[0]:
        lat = f"{gps.latitude[0]:.6f}"
        lng = f"{gps.longitude[0]:.6f}"
        data = f"{lat},{lng}"
        send_lora(data, 2)
        print(f"Sent data: {data}")
        time.sleep(3)

def main():
    start_time = time.time()
    try:
        print("LoRa Transmitter started. Waiting for GPS data...")
        while True:
            if gps_serial.in_waiting > 0:
                data = gps_serial.read(gps_serial.in_waiting).decode('utf-8')
                for char in data:
                    gps.update(char)
                display_info()

            if time.time() - start_time > 5:
                if gps.satellite_data['used_satellites'] < 1:
                    print("No GPS detected: Check wiring.")
                    break
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        lora_serial.close()
        gps_serial.close()

if __name__ == "__main__":
    main()
