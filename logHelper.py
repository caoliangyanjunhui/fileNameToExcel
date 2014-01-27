#-*- coding:UTF-8 -*-


def printLog(obj):
	print obj
	text = str(obj)
	f = open('python_log.txt', 'a')
	f.write(text)
	f.write('\n\r')
	f.close()