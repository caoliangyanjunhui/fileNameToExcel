# -*- coding: UTF-8 -*-
import os
import shutil
from localEncode import localEncodeText, unicodeFromLocalEncode



def pathJoin(parentPath, childNmae):
	return os.path.abspath(os.path.join( localEncodeText(parentPath), localEncodeText(childNmae) ))

def rename(sourcePath, destinationPath):
	try:
		if os.path.isdir(sourcePath): return
		os.rename( localEncodeText(sourcePath), localEncodeText(destinationPath))
	except Exception, e:
		print e

def copyToPath(sourcePath, destinationPath):
	try:
		if os.path.isdir(sourcePath):
			shutil.copytree(sourcePath, destinationPath)
		else:
			shutil.copy(sourcePath, destinationPath)
	except Exception, e:
		print e

def moveToPath(sourcePath, destinationPath):
	try:
		shutil.move(sourcePath, destinationPath)
	except Exception, e:
		print e

def removePath(path):
	if not os.path.exists(path): return
	try:
		if os.path.isfile(path):
			os.remove(path)
		else:
			os.system('rd/s/q %s' % path)
	except Exception, e:
		print e

def copyToPathWithOverWrite(sourcePath, destinationPath):
	removePath(destinationPath)
	try:
		copyToPath(sourcePath, destinationPath)
	except Exception, e:
		print e

def moveToPathWithOverWrite(sourcePath, destinationPath):
	removePath(destinationPath)
	try:
		shutil.move(sourcePath, destinationPath)
	except Exception, e:
		print e

def parentPath(path):
	return os.path.abspath(pathJoin(path, os.path.pardir))

def createFolder(path):
	try:
		if os.path.exists(path):
		 	if os.path.isdir(path): 
		 		return
		 	else:
		 		removePath(path)
		os.mkdir(path)
		return True
	except Exception, e:
		print e
		return False

def exists(path):
	return os.path.exists( localEncodeText(path) )

def childFolderList(folderPath):
	folderPathDict = {}
	folderPath = localEncodeText(folderPath)
	if not exists(folderPath): return folderPathDict
	dirList = os.listdir(folderPath)
	for item in dirList:
		itemPath = pathJoin(folderPath, item)
		if os.path.isdir(itemPath):
			folderPathDict[item] = itemPath
	return folderPathDict

def readText(filePath):
	text = ''
	filePath = localEncodeText(filePath)
	if not exists(filePath): return text
	f = open(filePath, 'r')
	try:
		text = f.read()
	except Exception, e:
		print e
	finally:
		f.close()
	return unicodeFromLocalEncode(text)

def fileNameWithoutExtention(fileName):
	name, ext = os.path.splitext(fileName)
	return name

def __test():
	print fileNameWithoutExtention('123.txt')

if __name__ == '__main__':
	__test()