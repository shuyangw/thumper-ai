import win32gui
import sys
import time

from PIL import ImageGrab

def rgb_to_grayscale(pixel):
	return pixel[0] * 0.299 + pixel[1] * 0.587 + pixel[2] * 0.114

def get_window_pixels(rect):
	count = 0
	pixels = ImageGrab.grab().load()
	y_range = rect[3] - rect[1]
	x_range = rect[2] - rect[0]
	export_pixels = [[0 for y in y_range] for x in x_range]
	for y in range(rect[1], rect[3]):
		for x in range(rect[0], rect[2]):
			export_pixels[x,y] = rgb_to_grayscale(pixels[x,y])
			# print(pixels[x,y])
			count += 1	
	print(count)

#Gets hwnd list
def _get_windows_by_title(title_text, exact = False):
	def _window_callback(hwnd, all_windows):
		all_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
	windows = []
	win32gui.EnumWindows(_window_callback, windows)
	if exact:
		return [hwnd for hwnd, title in windows if title_text == title]
	else:
		return [hwnd for hwnd, title in windows if title_text in title]

def get_window_rect():
	hwndList = _get_windows_by_title("THUMPER")
	try:
		hwnd = hwndList[0]
	except(IndexError):
		print("Error: Window not found. Please make sure game is launched.")
		sys.exit()

	rect = win32gui.GetWindowRect(hwnd)

	negatives = 0
	for element in rect:
		if element < 0:
			negatives += 1
	if negatives == 4:
		print("Unexpected error, please restart game retry")
		sys.exit()
	return rect