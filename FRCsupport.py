from dataclasses import dataclass


FRC_device_type = {
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


FRC_manufacturer = {
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


@dataclass
class FRCCanID:
    """Class for keeping track of the FRC CAN ID Components"""
    device_type: int
    manufacturer_code: int
    api_class: int
    api_index: int
    device_number: int
