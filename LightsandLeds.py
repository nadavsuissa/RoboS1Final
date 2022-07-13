# Led ShowCase:
# Nadav David Rawan

# Basic Defines:
rotate_speed = 120 # Rotate Speed , Might Need to Change if too Fast!
l1, l2 = 0, 255 # For Easy Fill Of RGB MATRIX
seconds, milli_seconds = 1, .05 # For Timeout... Robot Must Rest

RGB1 = [
    [],  # Empty list box
    [l2, l2, l2],  # RGB White
    [l2, l1, l1],  # RGB Red
    [l2, l2, l1],  # RGB Yellow
    [l1, l1, l2],  # RGB Blue
    [l1, l2, l1],  # RGB Green
    [l2, l1, l2],  # RGB Pink
    [l1, l2, l2],  # RGB Cyan
]

RGB2 = [
    [],  # Empty list box
    [l2, l1, l1],  # RGB Red
    [l2, l2, l1],  # RGB Yellow
    [l1, l1, l2],  # RGB Blue
    [l1, l2, l1],  # RGB Green
    [l2, l1, l1],  # RGB Red
    [l2, l2, l1],  # RGB Yellow
    [l1, l1, l2],  # RGB Blue
    [l1, l2, l1],  # RGB Green
]


def start():
    # Define Basic Behaviore - Gimbal Follow
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    # Set Rotation Speed of Chassis
    chassis_ctrl.set_rotate_speed(rotate_speed)
    # Function: led_ctrl.set_flash(armor_enum, frequency) - We Will set Flash on All of the Armor - Freq is 4 times
    led_ctrl.set_flash(rm_define.armor_all, 4)
    # Function: chassis_ctrl.rotate(direction_enum)
    chassis_ctrl.rotate(rm_define.clockwise)

    for j in range(1, 8):  # By Sdk this is how the leds are indexed
        led_ctrl.gun_led_on()  # Turn on Led that's on the Gun
        # Function: led_ctrl.set_top_led(armor_enum, r, g, b, led_effect_enum) - Top All , COLOR - RGB FORMAT - effect - ALLWAYS OFF
        led_ctrl.set_top_led(rm_define.armor_top_all, RGB1[j][0], RGB1[j][1], RGB1[j][2], rm_define.effect_always_off)
        # Set Bottom Led - All - Color - Flash Effect
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, RGB1[j][0], RGB1[j][1], RGB1[j][2], rm_define.effect_flash)

        for i in range(1, 9): # BY SDK - LED SEQUENCE IS 1-8(1 Til 9 in CS)
            # Function: led_ctrl.set_single_led(armor_enum, led_index, led_effect_enum)
            led_ctrl.set_single_led(rm_define.armor_top_all, [i], rm_define.effect_always_on)
            time.sleep(milli_seconds)

        for i in range(1, 9): # Turn Every Led Off
            led_ctrl.set_single_led(rm_define.armor_top_all, [i], rm_define.effect_always_off)
            time.sleep(milli_seconds)
            led_ctrl.gun_led_off()

    for j in range(0, 2):
        led_ctrl.gun_led_on()
        for i in range(1, 9):
            led_ctrl.set_top_led(rm_define.armor_top_all, RGB2[i][0], RGB2[i][1], RGB2[i][2],
                                 rm_define.effect_always_off)

            led_ctrl.set_single_led(rm_define.armor_top_all, [i], rm_define.effect_always_on)

            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, RGB2[-i][0], RGB2[-i][1], RGB2[-i][2],
                                    rm_define.effect_breath)

            time.sleep(milli_seconds)
            led_ctrl.gun_led_off()

    for j in range(0, 3):
        led_ctrl.gun_led_on()
        for i in range(1, 5):
            led_ctrl.set_top_led(rm_define.armor_top_all,
                                 RGB2[i][0], RGB2[i][1], RGB2[i][2], rm_define.effect_always_off)
            led_ctrl.set_single_led(rm_define.armor_top_all,
                                    [i, i + 4], rm_define.effect_always_on)

            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, RGB2[-i][0], RGB2[-i][1], RGB2[-i][2],
                                    rm_define.effect_always_on)

            time.sleep(milli_seconds)
            led_ctrl.gun_led_off()

    for j in range(0, 7):
        led_ctrl.gun_led_on()
        for i in range(1, 3):
            led_ctrl.set_top_led(rm_define.armor_top_all, RGB2[i][0], RGB2[i][1], RGB2[i][2],
                                 rm_define.effect_always_off)

            led_ctrl.set_single_led(rm_define.armor_top_all, [i, i + 2, i + 4, i + 6], rm_define.effect_always_on)

            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, RGB2[-i][0], RGB2[-i][1], RGB2[-i][2],
                                    rm_define.effect_always_on)

            time.sleep(milli_seconds)
            led_ctrl.gun_led_off()

    chassis_ctrl.stop()

    for j in range(2):
        led_ctrl.gun_led_on()
        for i in range(1, 5):
            led_ctrl.set_top_led(rm_define.armor_top_all, RGB2[i][0], RGB2[i][1], RGB2[i][2],
                                 rm_define.effect_always_on)

            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, RGB2[i][0], RGB2[i][1], RGB2[i][2],
                                    rm_define.effect_always_on)

            time.sleep(milli_seconds)

        led_ctrl.gun_led_off()
        for i in range(3, 1, -1):
            led_ctrl.set_top_led(rm_define.armor_top_all, RGB2[i][0], RGB2[i][1], RGB2[i][2],
                                 rm_define.effect_always_on)

            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, RGB2[i][0], RGB2[i][1], RGB2[i][2],
                                    rm_define.effect_always_on)

            time.sleep(milli_seconds)

    chassis_ctrl.rotate(rm_define.anticlockwise)

    for j in range(0, 7):
        led_ctrl.gun_led_on()
        for i in range(2, 0, -1):
            led_ctrl.set_top_led(rm_define.armor_top_all,
                                 RGB2[i][0], RGB2[i][1], RGB2[i][2], rm_define.effect_always_off)
            led_ctrl.set_single_led(rm_define.armor_top_all,
                                    [i, i + 2, i + 4, i + 6], rm_define.effect_always_on)

            led_ctrl.set_bottom_led(rm_define.armor_bottom_all,
                                    RGB2[-i][0], RGB2[-i][1], RGB2[-i][2], rm_define.effect_always_on)
            time.sleep(milli_seconds)
            led_ctrl.gun_led_off()

    for j in range(0, 3):
        led_ctrl.gun_led_on()
        for i in range(4, 0, -1):
            led_ctrl.set_top_led(rm_define.armor_top_all, RGB2[i][0], RGB2[i][1], RGB2[i][2],
                                 rm_define.effect_always_off)

            led_ctrl.set_single_led(rm_define.armor_top_all, [i, i + 4], rm_define.effect_always_on)

            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, RGB2[-i][0], RGB2[-i][1], RGB2[-i][2],
                                    rm_define.effect_always_on)

            time.sleep(milli_seconds)
            led_ctrl.gun_led_off()

    for j in range(0, 2):
        led_ctrl.gun_led_on()
        for i in range(8, 0, -1):
            led_ctrl.set_top_led(rm_define.armor_top_all, RGB2[i][0], RGB2[i][1], RGB2[i][2],
                                 rm_define.effect_always_off)

            led_ctrl.set_single_led(rm_define.armor_top_all, [i], rm_define.effect_always_on)

            led_ctrl.set_bottom_led(rm_define.armor_bottom_all, RGB2[-i][0], RGB2[-i][1], RGB2[-i][2],
                                    rm_define.effect_always_on)

            time.sleep(milli_seconds)
            led_ctrl.gun_led_off()

    led_ctrl.set_flash(rm_define.armor_all, 4)

    for j in range(1, 8):
        led_ctrl.gun_led_on()
        led_ctrl.set_top_led(rm_define.armor_top_all, RGB1[j][0], RGB1[j][1], RGB1[j][2], rm_define.effect_always_off)

        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, RGB1[j][0], RGB1[j][1], RGB1[j][2], rm_define.effect_flash)

        for i in range(8, 0, -1):
            led_ctrl.set_single_led(rm_define.armor_top_all, [i], rm_define.effect_always_on)

            time.sleep(milli_seconds)

        for i in range(8, 0, -1):
            led_ctrl.set_single_led(rm_define.armor_top_all, [i], rm_define.effect_always_off)

            time.sleep(milli_seconds)
            led_ctrl.gun_led_off()

    time.sleep(.08)
    chassis_ctrl.stop()

    led_ctrl.set_flash(rm_define.armor_all, 6)
    led_ctrl.set_top_led(rm_define.armor_top_all, l2, l1, l1, rm_define.effect_marquee)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, l2, l1, l1, rm_define.effect_flash)
    gimbal_ctrl.rotate(rm_define.gimbal_up)
    media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate, wait_for_complete_flag=False)
    time.sleep(seconds + .5)

    led_ctrl.set_flash(rm_define.armor_all, 8)
    led_ctrl.set_top_led(rm_define.armor_top_all, l1, l2, l2, rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, l1, l2, l2, rm_define.effect_flash)

    led_ctrl.gun_led_on()
    media_ctrl.play_sound(rm_define.media_sound_shoot, wait_for_complete_flag=True)
    media_ctrl.play_sound(rm_define.media_sound_shoot, wait_for_complete_flag=True)
    led_ctrl.turn_off(rm_define.armor_all)
    led_ctrl.gun_led_off()

    led_ctrl.set_flash(rm_define.armor_all, 6)
    led_ctrl.set_top_led(rm_define.armor_top_all, l2, l1, l1, rm_define.effect_marquee)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, l2, l1, l1, rm_define.effect_flash)
    gimbal_ctrl.rotate(rm_define.gimbal_down)
    media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate, wait_for_complete_flag=False)

    chassis_ctrl.stop();
    gimbal_ctrl.recenter()
