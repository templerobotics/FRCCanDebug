import can
from FRCsupport import FRCCanID
from REVsupport import REV_API_identifier


if __name__ == '__main__':
    can_bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=1000000)
    can_bus.shutdown()
