import curses


def main(stdscr):
    stdscr.addstr("Hello this is a test")
    stdscr.refresh()
    curses.napms(2000)
    stdscr.clear()
    stdscr.refresh()


if __name__ == '__main__':
    curses.wrapper(main)
