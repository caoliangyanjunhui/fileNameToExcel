#-*- coding:UTF-8 -*-
from logHelper import printLog
from localEncode import localEncodeText

def saveTextFile(filePath, text):
	f = open(filePath, 'w')
	try:
		f.write( localEncodeText(text) )
	except Exception, e:
		printLog (e)
	finally:
		f.close()