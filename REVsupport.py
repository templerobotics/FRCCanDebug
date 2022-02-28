import struct

REV_API_identifier = {
    0x1: "Setpoint Set",
    0x2: "DC Set",
    0x12: "Speed Set",
    0x13: "Smart Velocity Set",
    0x32: "Position Set",
    0x42: "Voltage Set",
    0x43: "Current Set",
    0x52: "Smart Motion Set",
    0x60: "Status Frame 0",
    0x61: "Status Frame 1",
    0x62: "Status Frame 2",
    0x63: "Status Frame 3",
    0x6E: "Clear Faults",
    0x6A: "DRV Stat",
    0x72: "Burn Flash",
    0x73: "Set Follower",
    0x74: "Set Factory Defaults",
    0x75: "Factory Reset",
    0x80: "NACK",
    0x81: "ACK",
    0x90: "Broadcast",
    0x92: "Heartbeat",
    0x93: "Sync",
    0x94: "ID Query",
    0x95: "ID Assign",
    0x98: "Firmware",
    0x99: "Enum",
    0x9B: "Lock",
    0xB1: "Lock B",
    0xB2: "Non-Rio Heartbeat",
    0x1FF: "Software Download Bootloader",
    0x9C: "Software Download Data",
    0x9D: "Software Download Checksum",
    0x9E: "Software Download Retransmit",
    0xA0: "Mech Pos",
    0xA2: "I Accumulator",
    0x300: "Parameter Access"
}


REV_Fault_IDs = {
    0: "Brownout",
    1: "Over Current",
    2: "Over Voltage",
    3: "Motor Fault",
    4: "Sensor Fault",
    5: "Stall",
    6: "EEPPROM CRC",
    7: "CAN TX",
    8: "CAN RX",
    9: "Has Reset",
    10: "DRV Fault",
    11: "Other Fault",
    12: "Soft Limit Forward",
    13: "Soft Limit Reverse",
    14: "Hard Limit Forward",
    15: "Hard Limit Reverse"
}


def decode_rev_api(api: int) -> str:
    return REV_API_identifier.get(api, "Unknown")


def decode_rev_fault(fault: int) -> str:
    return REV_Fault_IDs.get(fault, "Unknown")


def decode_rev_data(api: int, data: bytes) -> str:
    retval = "Unknown"
    if api == 0x60:
        output, = struct.unpack('h6x', data)
        retval = f"Applied Output: {output}"
    elif api == 0x61:
        vel, temp = struct.unpack('fb3x', data)
        retval = f"Motor Velocity: {vel} | Motor Temperature: {temp}C/{(temp*1.8)+32}F"
    elif api == 0x62:
        pos, _ = struct.unpack('2f', data)
        retval = f"Motor Position: {pos}"
    return retval
