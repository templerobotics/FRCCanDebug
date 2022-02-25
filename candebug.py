import can
from FRCsupport import FRCCanID
from REVsupport import decode_rev_api


def parse_log_line(line: str) -> dict:
    split = line.split()
    timestamp = float(split[0])
    can_id = int(split[2][:-1], 16)
    data_string = ' '.join(split[6:14])
    data_hex = int(''.join(split[6:14]), 16)
    return {'timestamp': timestamp, 'can_id': can_id, 'data_string': data_string, 'data_hex': data_hex}


if __name__ == '__main__':
    # can_bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=1000000)
    # can_bus.shutdown()
    with open("2-23-430pm-drivetest.asc", 'r') as can_file:
        for i in range(0, 6):
            can_file.readline()
        for fline in can_file.readlines():
            line = parse_log_line(fline)
            can_id = FRCCanID(line['can_id'])
            if can_id.device_type == 2 and can_id.manufacturer_code == 5:
                print(f"{'{:.6f}'.format(line['timestamp'])}: {can_id.get_device_type()} | {can_id.get_manufacturer()} "
                      f"| Device {f'{can_id.device_number:02}'} | {decode_rev_api(can_id.api)} | {line['data_string']}")
            else:
                print(f"{'{:.6f}'.format(line['timestamp'])}: {can_id.get_device_type()} | {can_id.get_manufacturer()} "
                      f"| Device {f'{can_id.device_number:02}'} | {line['data_string']}")
