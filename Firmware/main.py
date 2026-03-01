import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D1, board.D0, None, False),)
encoder_handler.divisor = 4

rgb = RGB(
    pixel_pin=board.D20, 
    num_pixels=3, 
    val=100, 
    rgb_order=(1, 0, 2)
)
keyboard.extensions.append(rgb)

keyboard.matrix = KeysScanner(
    pins=[
        board.D7, board.D3, board.D8, board.D4, 
        board.D9, board.D5, board.D10, board.D6
    ],
    value_when_pressed=False,
    pull=True,
)

keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3, KC.N4, 
        KC.N5, KC.N6, KC.N7, KC.RGB_TOG
    ]
]

encoder_handler.map = [((KC.VOLU, KC.VOLD),)]

if __name__ == '__main__':
    keyboard.go()