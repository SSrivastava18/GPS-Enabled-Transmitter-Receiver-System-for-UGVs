import serial
import time

BAUDRATE = 115200
LORA_PORT = '/dev/ttyS0'

def main():
    lora_serial = serial.Serial(LORA_PORT, BAUDRATE, timeout=1)
    try:
        print("LoRa Receiver started. Waiting for data...")
        while True:
            if lora_serial.in_waiting > 0:
                data = lora_serial.readline().decode('utf-8', errors='ignore').strip()
                if data:
                    print(f"Received data: {data}")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        lora_serial.close()

if __name__ == "__main__":
    main()
