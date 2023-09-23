# Almost a Windows automation tool
# NNN105

from subprocess import Popen
from pywinauto import Desktop
import pytesseract
from time import sleep
from PIL import Image
import sys

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"


def main():
    # User should insert math operation
    calculus = input("Calculate: ").strip().replace(" ", "")
    # Init Calculator simulation
    dlg = init_calc()
    # Check if it is the calculation application
    if check_app_title(dlg, "Calculator"):
        # Use the calculator
        print("Result =",calculator(dlg, calculus))
    dlg.close()


def calculator(dlg, calculus):
    """Only for this implementation: Calculator test tool"""
    keyboard = generate_keyboard()
    last_digit_rect = (1470, 165, 1520, 270)
    press_number(dlg, keyboard, "CE")
    for index in range(len(calculus)):
        if calculus[index].isnumeric() or calculus[index] in ",.":
            press_number(dlg, keyboard, calculus[index])
            if verify_character(dlg, last_digit_rect, calculus[index]):
                continue
            else:
                dlg.close()
                sys.exit("Internal Error")
        elif calculus[index] in "+-*/":
            press_number(dlg, keyboard, calculus[index])
        else:
            dlg.close()
            sys.exit("Not a valid key")
    else:
        press_number(dlg, keyboard, "=")
        sleep(1)
    return read_result(dlg)


def init_calc():
    """Only for this implementation: Open the Calculator application"""
    Popen("calc.exe", shell=True)
    dlg = Desktop(backend="uia").Calculator
    dlg.wait("visible")
    dlg.maximize()
    return dlg


def generate_keyboard():
    """Only for this implementation: generate coordinates 'x' and 'y' for each key"""
    x0, y0, x1, y1 = 0, 370, 1500, 1024
    keys = [
        "sig",
        "0",
        ".",
        "=",
        "1",
        "2",
        "3",
        "+",
        "4",
        "5",
        "6",
        "-",
        "7",
        "8",
        "9",
        "*",
        "inv",
        "sqr",
        "root",
        "/",
        "%",
        "CE",
        "C",
        "BK",
    ]
    ROWS = 6
    COLUMNS = 4
    x_value = [0] * len(keys)
    y_value = [0] * len(keys)
    for val in range(len(keys)):
        x_value[val] = (x1 - x0) // COLUMNS * (val % COLUMNS) + (x1 - x0) // (
            COLUMNS * 2
        )
        y_value[val] = (
            -(y1 - y0) // ROWS * (val // COLUMNS) - (y1 - y0) // (ROWS * 2) + y1
        )

    keyboard = {
        "x": {key: value for key, value in zip(keys, x_value)},
        "y": {key: value for key, value in zip(keys, y_value)},
    }
    return keyboard


def press_number(dlg, keyb, number):
    """Only for this implementation: Call the pywinauto click method with the selected key"""
    dlg.click_input(coords=(keyb["x"][number], keyb["y"][number]))
    sleep(0.3)


def read_result(dlg):
    """Only for this implementation: return final result"""
    result_reader_rect = (700, 155, 1520, 270)
    img = cut_label(dlg, result_reader_rect)
    bwimg = img.point(lambda x: 255 if x > 180 else 0)
    # Use an assistance image to help OCR read method
    with Image.open("result.png") as im:
        im.paste(bwimg, (310, 30)) 
    read_number = pytesseract.image_to_string(im).strip().replace("\n", "")
    return read_number.replace("Number", "").strip().replace(".", "")


# Tool Library


def verify_character(dlg, last_digit_rect, character, th=180):
    """verify if the read character is the sent character
        only one number or alphabetic is checked
    :param dlg: dialog of the application
    :param label_rect: two x,y tuples in order to make a rectangle
    :param character: one alphanumeric
    :param th: threshold of the white color
    :return: True when read character is the sent character
    """
    img = cut_label(dlg, last_digit_rect).convert("L")
    # Make Black White image
    bw = img.point(lambda x: 255 if x > th else 0)
    # Use an assistance image to help OCR read method
    with Image.open("number.png") as im:
        im.paste(bw, (330, 12))
    read_number = pytesseract.image_to_string(im).strip().replace("Number", "")
    return read_number.strip() == character


def read_label(dlg, label_rect, th=180):
    """Read the text of this selected area
    :param dlg: dialog of the application
    :param label_rect: two x,y tuples in order to make a rectangle
    :param th: threshold of the white color
    :return lect: string of the read text
    """
    img = cut_label(dlg, label_rect).convert("L")
    bw = img.point(lambda x: 255 if x > th else 0)
    lect = pytesseract.image_to_string(bw).strip()
    return lect


def check_app_title(dlg, title):
    """Check if it is the calculation application
    :param dlg: dialog of the application
    :param title: string to be compared
    :raise SystemExit: If read title is not equal to string
    :return: True when read title is equal to string
    """
    if not (read_label(dlg, (55, 5, 140, 40)) in title):
        dlg.close()
        sys.exit("Incorrect application")
    else:
        return True


def cut_label(dlg, rectangle):
    """return the image in the sent rectangle
    :param dlg: dialog of the application
    :param rectangle: two x,y tuples in order to make a rectangle
    :return: A image into the rectangle
    """
    dlg.maximize()
    dlg.wait("visible")
    im = dlg.capture_as_image()
    return im.crop(rectangle)


if __name__ == "__main__":
    main()
