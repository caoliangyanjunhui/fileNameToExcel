# -*- coding: UTF-8 -*-

LOCAL_ENCODE = 'gbk'

def localEncodeText(text):
	if isinstance(text, unicode):
		return text.encode( LOCAL_ENCODE )
	else:
		return text

def unicodeFromLocalEncode(text):
	if isinstance(text, unicode):
		return text
	else:
		return text.decode( LOCAL_ENCODE )

def utf8(text):
	if isinstance(text, unicode):
		return text.encode('UTF-8')
	else:
		return text


def dictToUnicode(dictionary):
	for key, value in dictionary.items():
		if type(value) == type(u'中文'.encode(LOCAL_ENCODE)):
			dictionary[key] = unicodeFromLocalEncode(value)
	return dictionary


def __test():
	localTxt = localEncodeText(u'unicode中文')
	print localTxt, type(localTxt)
	unicodeTxt = unicodeFromLocalEncode(u'gbk中文'.encode('gbk'))
	print unicodeTxt, type(unicodeTxt)
	print dictToUnicode({'a':u'UTF-8中文'.encode('gbk'), 'b':u'UTF-8汉字'.encode('gbk')})

if __name__ == '__main__':
	__test()