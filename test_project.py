# Almost a Windows automation tool
# NNN105

import project
import pytest


def test_read_label():
    dlg = project.init_calc()
    assert project.read_label(dlg, (55, 5, 140, 40)) == "Calculator"
    assert project.read_label(dlg, (55, 55, 180, 100)) == "Standard"
    assert project.read_label(dlg, (1535, 55, 1610, 95)) == "History"
    assert project.read_label(dlg, (1615, 55, 1700, 95)) == "Memory"
    dlg.close()


def test_verify_character():
    dlg = project.init_calc()
    keyboard = project.generate_keyboard()
    last_digit_rect = (1470, 165, 1520, 270)
    # Start Test
    project.press_number(dlg, keyboard, "1")
    assert project.verify_character(dlg, last_digit_rect, "1") == True
    project.press_number(dlg, keyboard, "2")
    assert project.verify_character(dlg, last_digit_rect, "2") == True
    project.press_number(dlg, keyboard, "3")
    assert project.verify_character(dlg, last_digit_rect, "3") == True
    project.press_number(dlg, keyboard, "4")
    assert project.verify_character(dlg, last_digit_rect, "4") == True
    project.press_number(dlg, keyboard, "5")
    assert project.verify_character(dlg, last_digit_rect, "5") == True
    project.press_number(dlg, keyboard, "6")
    assert project.verify_character(dlg, last_digit_rect, "6") == True
    project.press_number(dlg, keyboard, "7")
    assert project.verify_character(dlg, last_digit_rect, "7") == True
    project.press_number(dlg, keyboard, "8")
    assert project.verify_character(dlg, last_digit_rect, "8") == True
    project.press_number(dlg, keyboard, "9")
    assert project.verify_character(dlg, last_digit_rect, "9") == True
    project.press_number(dlg, keyboard, "0")
    assert project.verify_character(dlg, last_digit_rect, "0") == True
    project.press_number(dlg, keyboard, "4")
    assert project.verify_character(dlg, last_digit_rect, "A") == False
    assert project.verify_character(dlg, last_digit_rect, "a") == False
    assert project.verify_character(dlg, last_digit_rect, "") == False
    assert project.verify_character(dlg, (0, 0, 10, 10), "4") == False
    assert project.verify_character(dlg, last_digit_rect, "4") == True
    dlg.close()


def test_calculator():
    dlg = project.init_calc()
    assert project.calculator(dlg, "20+15") == "35"
    assert project.calculator(dlg, "200+1500") == "1700"
    assert project.calculator(dlg, "55-1500") == "-1445"
    assert project.calculator(dlg, "3*1500") == "4500"
    assert project.calculator(dlg, "3000/3") == "1000"
    dlg.close()


def test_check_app_title():
    dlg = project.init_calc()
    assert project.check_app_title(dlg, "Calculator") == True
    dlg.close()


def test_calculator_exception():
    dlg = project.init_calc()
    with pytest.raises(SystemExit):
        project.calculator(dlg, "20*15A")
    dlg = project.init_calc()
    with pytest.raises(SystemExit):
        project.calculator(dlg, "Tweny")


def test_check_app_title_exception():
    dlg = project.init_calc()
    with pytest.raises(SystemExit):
        project.check_app_title(dlg, "Notepad")
