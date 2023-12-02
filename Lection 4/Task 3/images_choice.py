import os
images_list = sorted(os.listdir('static/images'))
current_index = 0


def image_index(button_click=None,):
    global current_index
    if button_click == 'previous':
        current_index -= 1
        if current_index < 0:
            current_index = len(images_list) - 1
    elif button_click == 'next':
        current_index += 1
        if current_index >= len(images_list):
            current_index = 0

    return current_index


