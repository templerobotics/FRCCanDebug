REV_API_identifier = {
    0x1: "Setpoint Set",
    0x2: "DC Set",
    0x12: "Speed Set",
    0x13: "Smart Velocity Set",
    0x32: "Position Set",
    0x42: "Voltage Set",
    0x43: "Current Set"
}


def decode_rev_api(api: int) -> str:
    return REV_API_identifier.get(api, "Unknown")

