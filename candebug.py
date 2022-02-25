import can
import pandas as pd
import curses

from FRCsupport import FRCCanID
from REVsupport import decode_rev_api


class TableListener(can.Listener):

    def __init__(self, df: pd.DataFrame, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.df = df

    def on_message_received(self, msg: can.Message) -> None:
        can_data = ' '.join([format(x, '02x') for x in msg.data])
        if hex(msg.arbitration_id) not in self.df.index:
            frc_can_id = FRCCanID(msg.arbitration_id)
            self.df.loc[hex(msg.arbitration_id)] = [frc_can_id.get_device_type(), frc_can_id.get_manufacturer(),
                                                    frc_can_id.device_number, decode_rev_api(frc_can_id.api), can_data]
        else:
            self.df.at[hex(msg.arbitration_id), "Data"] = can_data

    def on_error(self, exc: Exception) -> None:
        pass


def main(stdscr):
    with can.interface.Bus(bustype='socketcan', channel='can0', bitrate=1000000) as can_bus:
        stdscr.addstr("Program started. Waiting 1 second")
        stdscr.refresh()
        curses.napms(1000)
        df = pd.DataFrame(columns=["Device Type", "Manufacturer", "Device Number", "REV API", "Data"])
        can_notifier = can.Notifier(can_bus, [TableListener(df)])
        while True:
            df.sort_values(['Device Number', "REV API"], inplace=True)
            stdscr.erase()
            stdscr.addstr(df.to_string())
            stdscr.refresh()
            curses.napms(25)


if __name__ == '__main__':
    curses.wrapper(main)
