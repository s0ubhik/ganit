import os, sys
import ganit as gn

version = 0.1

def interactive_mode():
	print(f"Ganit v{version} (Interactive mode)")
	while True:
		try:
			cmd = input(">>> ")
		except KeyboardInterrupt:
			print("\nExiting...")
			exit()

		gn.run(cmd)

def file_mode(filename):
	gn.origin = filename
	with open(filename) as fp:
		code = fp.read()

	gn.run(code)

if __name__ == '__main__':
	argc = len(sys.argv)
	if argc < 2:
		interactive_mode()
	else:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print(filename," no such file.")
			exit(1)
		file_mode(filename)