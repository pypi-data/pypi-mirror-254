from loomanager.errors import err
from zenyx import printf
import loomanager.files as files
import threading
import keyboard
import time
import sys

YES_NO_CHOICE: dict[str, dict[str, any]] = {
    "Yes": {"symbol": "✅", "value": "yes"},
    "No": {"symbol": "❌", "value": "no"},
}
TEST_MAIN_CHOICE: dict[str, dict[str, any]] = {
    "Test": {"symbol": "⚗️ ", "value": "test"},
    "Main": {"symbol": "📦", "value": "main"},
}


def move_cursor_up(lines):
    sys.stdout.write(f"\033[{lines}A")


can_press: bool = True


def select_from_range(nums_dict: dict[int, str]):
    def key_timeout_daemon(_time):
        global can_press
        if not can_press:
            return

        def inner():
            global can_press
            can_press = False
            time.sleep(_time)
            can_press = True

        x = threading.Thread(target=inner)
        x.daemon = True
        x.start()

    current = 0
    l_c = -2

    keyslist = list(nums_dict.keys())

    def do_print():
        for i in range(len(keyslist)):
            if current == i:
                # print(colored(f"> {}", attrs=["bold"]))
                printf(f" @!{nums_dict[keyslist[current]].title()}$&")
                continue
            printf(f" @~{nums_dict[keyslist[i]].title()}$&")
            # print(colored(f"  {nums_dict[keyslist[i]]}", attrs=["dark"]))

    do_print()

    while not keyboard.is_pressed("Enter"):
        if not can_press:
            continue

        if keyboard.is_pressed("up_arrow"):
            current -= 1
            key_timeout_daemon(0.15)
        if keyboard.is_pressed("down_arrow"):
            current += 1
            key_timeout_daemon(0.15)

        prev = current - 1
        next = current + 1
        if current == -1:
            current = len(nums_dict) - 1
        if current == len(nums_dict):
            current = 0

        if current == l_c:
            continue

        l_c = current
        move_cursor_up(len(keyslist))

        do_print()

    move_cursor_up(len(keyslist))
    for i in range(len(keyslist)):
        printf.full_line("")
    move_cursor_up(len(keyslist))

    printf(f"@?@~{nums_dict[keyslist[current]].title()}$&")

    # Only here to eat all the other chars the user typed
    x = input("\033[8m")
    print("\033[0m", end="")

    return keyslist[current]


def select_dict_key(dictionary: dict[str, dict[str, any]]):
    dict_symbols: dict[str, str] = {
        f'{value.get("symbol")} {key}': key for key, value in dictionary.items()
    }
    range_dict: dict[int, str] = {index: key for index, key in enumerate(dict_symbols)}

    return dictionary[dict_symbols[range_dict[select_from_range(range_dict)]]]


def get_input(incomplete_err: bool = False):
    res: str = input("> ")
    move_cursor_up(1)
    if res == "" and incomplete_err:
        err(
            msg="This field is required!",
            hint="\n".join(
                [
                    "This field is required to be filled, ",
                    "otherwise the program would not function.",
                    "Please fill it out next time!"
                ]
            ),
        )
    printf(f'@?@~"{res}"$&')
    return res
