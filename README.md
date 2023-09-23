# Almost a Windows Automation Tool
#### Video Demo:  <https://youtu.be/MtrDcpxBS_0>
#### Description:
This software combines Pywinauto and Pytesseract:
  - Pywinauto automates the Microsoft Windows GUI. allows to send mouse and keyboard actions to windows dialogs and controls
  - Pytesseract to give the feedback, allows to recognize and read the text embedded in images.

Having action and assertion, wrote in python tool, become in a simple automation tool.

#### Main Methods

##### General purpose
 - `def read_label():` Read the text of the selected area.
 - `def check_app_title():` verify if the title is shown in the application.
 - `def verify_character():` verify if the read character is the sent character.
 - `def read_result():` read final result of the math operation.

 `verify_character()` and ` read_result()` method use the number.png and result.png images in order to help the OCR tool, since there was difficult to process only one character.

##### Implementation purpose
 - `def init_calc():` start the application and connect to the instance.
 - `def generate_keyboard():` create a dictionary mapping each key to ( x,y ) coordinate
 - `def press_number():` press the calculator key by a mouse click.
 - `def calculator():` simulate the calculator behavior, receive the command and call each method to perform the operation.

#### Use Case: Windows Calculator application
It was planned to be used on Android applications (using Android emulator like BlueStacks). To avoid configuration several steps. The Windows calculator application was chosen to make the use case due to that this application is installed on all windows OS.\
Just for demonstration, the Windows Calculator shows the tool behavior:
1. The user is asked to insert a math expression.
2. The software sends these commands by clicking the Calculator keys.
3. Every pressed key is asserted by reading each character by the OCR tool.
4. When the operation is finished, the final result is also asserted.

These simple steps help to show how a simple automation tool works, each action can be verified: Click a calculator key and read it on the calculator screen.

#### Prerequisites
- pip install pywinauto
- pip install pytesseract
- pip install Pillow
- Be sure that the "number.png" and "result.png" are in the project folder.# Almost-Automation-Tool
