# -*- coding:UTF-8 -*-

def isIntStr(text):
	try:
		value = int(text)
		return type(value) is type(1)
	except:
		return False

def toInt(text):
	value = None
	try:
		value = int(text)
	except:
		pass
	finally:
		return value


def __test():
	print isIntStr('123')
	print isIntStr('123.4')
	print isIntStr('123a')

if __name__ == '__main__':
	__test()