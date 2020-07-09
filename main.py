timer = 0

def on_button_pressed_a():
    global timer
    timer = randint(5, 15)
    basic.show_icon(IconNames.CHESSBOARD)
    while timer > 0:
        timer += -1

        basic.pause(1000)
        basic.show_icon(IconNames.SKULL)
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)