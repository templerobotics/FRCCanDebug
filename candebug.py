import can
from FRCsupport import FRCCanID, FRC_manufacturer, FRC_device_type
from REVsupport import REV_API_identifier


def frc_id_deconstruct(message: can.Message) -> FRCCanID:
    return FRCCanID(message.arbitration_id >> 24, message.arbitration_id >> 16 & 0xff,
                    message.arbitration_id >> 10 & 0x3f, message.arbitration_id >> 6 & 0xf,
                    message.arbitration_id & 0x1f)


if __name__ == '__main__':
    can_bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=1000000)
