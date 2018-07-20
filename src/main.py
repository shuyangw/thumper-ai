from deepq import init
from screen import get_window_rect, get_window_pixels

if __name__ == "__main__":
    rect = get_window_rect()
    print(rect)
    get_window_pixels(rect)