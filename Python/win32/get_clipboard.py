#This is a project that stores all the things i copy into my clipboard in a file
import sys
import time
import win32clipboard

def get_clipboard():
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	return data

if __name__ == '__main__':
	while True:
		u = open('file.txt', 'r')
		data = u.readlines()
		u.close()

		# print(data)
		try:
			clip = get_clipboard()
			# print(clip)
			data = [b for b in data]
			with open('file.txt', 'a') as d:
				# print(get_clipboard())
				# print(data)
				if clip in data:
					# print(' I')
					continue
				else:
					d.write(f'\n{clip}')
					# print('written')
			# print(get_clipboard()) #
		except:
			# time.sleep(10)
			print('No data in clipboard')

# Path: get_clipboard.py