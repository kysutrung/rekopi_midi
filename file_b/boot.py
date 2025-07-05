import board
import digitalio
import storage

button = digitalio.DigitalInOut(board.GP15)
button.switch_to_input(pull=digitalio.Pull.UP)

if button.value:
    storage.enable_usb_drive()
else:
    storage.disable_usb_drive()
