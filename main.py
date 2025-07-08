def on_forever():
    if pins.digital_read_pin(DigitalPin.P0) == 1:
        basic.show_leds("""
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            """)
    else:
        if pins.digital_read_pin(DigitalPin.P1) == 1:
            basic.show_leds("""
                . . # . .
                . . . # .
                # # # # #
                . . . # .
                . . # . .
                """)
        else:
            pass
basic.forever(on_forever)
