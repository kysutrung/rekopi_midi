import storage
import usb_cdc
import usb_midi

storage.disable_usb_drive()

usb_cdc.enable(console=True, data=True)
usb_midi.enable()
