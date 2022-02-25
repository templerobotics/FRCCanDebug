FRC_Device_Type = {
    0: "Broadcast Messages",
    1: "Robot Controller",
    2: "Motor Controller",
    3: "Relay Controller",
    4: "Gyro Sensor",
    5: "Accelerometer",
    6: "Ultrasonic Sensor",
    7: "Gear Tooth Sensor",
    8: "Power Distribution Model",
    9: "Pneumatics Controller",
    10: "Miscellaneous",
    11: "IO Breakout",
    31: "Firmware Update"
}


FRC_Manufacturer = {
    0: "Broadcast",
    1: "NI",
    2: "Luminary Micro",
    3: "DEKA",
    4: "CTR Electronics",
    5: "REV Robotics",
    6: "Grapple",
    7: "MindSensors",
    8: "Team Use",
    9: "Kauai Labs",
    10: "Copperforge",
    11: "Playing With Fusion",
    12: "Studica"
}


class FRCCanID:
    """Class for keeping track of the FRC CAN ID Components"""
    device_type: int
    manufacturer_code: int
    api: int
    api_class: int
    api_index: int
    device_number: int

    def __init__(self, arbitration_id: int):
        self.device_type = arbitration_id >> 24
        self.manufacturer_code = arbitration_id >> 16 & 0xff
        self.api = arbitration_id >> 6 & 0x3ff
        self.api_class = arbitration_id >> 10 & 0x3f
        self.api_index = arbitration_id >> 6 & 0xf
        self.device_number = arbitration_id & 0x1f

    def get_device_type(self) -> str:
        return FRC_Device_Type.get(self.device_type, "Reserved")

    def get_manufacturer(self) -> str:
        return FRC_Manufacturer.get(self.manufacturer_code, "Reserved")
