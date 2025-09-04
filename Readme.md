GPS-Enabled Transmitter-Receiver System for UGVs

Enables Unmanned Ground Vehicles (UGVs) to transmit and receive GPS signals using a ground-based setup. Ideal for extending GPS coverage in GPS-denied environments or for simulation and testing of GPS-based communication protocols.


Features

GPS Signal Forwarding: Relays GPS data from a base station to a UGV.

UGV Localization: UGV can receive GPS via RF, enabling positioning even when onboard receivers are disabled or unavailable.

Versatile Setup: Suitable for research, testing, and fallback navigation scenarios.

Open-Source: Freely reusable and modifiable under the MIT License.


Hardware Requirements

| Role               | Required Components                                     |
| ------------------ | ------------------------------------------------------- |
| **Transmitter**    | GPS module (providing NMEA or raw data), RF transmitter |
| **Receiver (UGV)** | RF receiver, onboard computing platform                 |
| **Optional**       | Antennas, RF amplifier or filter, portable power supply |


Setup Instructions

1. Clone the Repositor

   git clone https://github.com/SSrivastava18/GPS-Enabled-Transmitter-Receiver-System-for-UGVs.git
   
   cd GPS-Enabled-Transmitter-Receiver-System-for-UGVs

2. Install Dependencies

   pip install pyserial

Configure Devices

 Edit transmitter.py and receiver.py to set the correct serial ports, baud rates, and RF channel parameters.

 Place or secure antennas properly to ensure reliable transmission.

 Usage

 Transmitter (Ground Station)

 Reads GPS data (e.g., via serial NMEA stream) and forwards it over RF:

 python transmitter.py

 Receiver (On UGV)

 python receiver.py

