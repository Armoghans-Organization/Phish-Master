import shutil

def center_print(text, width=None):
    if width is None:
        width = shutil.get_terminal_size().columns
    for line in text.split('\n'):
        print(line.center(width))