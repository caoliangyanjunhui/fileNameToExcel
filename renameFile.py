#-*- coding:UTF-8 -*-

import os
from localEncode import localEncodeText, unicodeFromLocalEncode, dictToUnicode
from pathHelper import pathJoin, parentPath, rename

class FileReader(object):
	levelMax = 7
	def fileUnderPath(self, folderPath):
		children = os.listdir(localEncodeText(folderPath))
		fileList = []
		for child in children:
			parts = child.split('-')
			fileList.append(parts)
		return fileList


	def setLevelsName(self, level, folderPath, fileDict):
		pathToSplit = folderPath
		i = self.levelMax
		while i > 0:
			key = 'level' + str(i) + 'Name'
			if i > level:
				value = ''
			else:
				pathToSplit, value = os.path.split(pathToSplit)
			fileDict[key] = value
			i -= 1
		return fileDict

	def readAllFrom(self, folderPath):
		fileList = self.fileUnderPath(folderPath)
		return fileList

	def readFiles(self, files):
		fileList = []
		for filePath in files:
			fileDict = {}
			folderPath, fileName = os.path.split(filePath)
			fileList.append(fileName.split('-'))
		return fileList

class FileRename(object):
	def __init__(self, fileList, operations=None):
		self.fileList = fileList
		self.operations = operations

	def excute(self):
		for fileDict in self.fileList:
			newFileName = fileDict['newHead'] + fileDict['fileExt']
			newFilePath = pathJoin(fileDict['folderPath'], newFileName)
			fileDict['newFilePath'] = newFilePath
			rename(fileDict['filePath'], newFilePath)

	def undoExcute(self):
		for fileDict in self.fileList:
			if fileDict['newFilePath']:
				rename(fileDict['newFilePath'], fileDict['filePath'])
				fileDict['newFilePath'] = ''

	def preview(self):
		if not self.operations: 
			return self.fileList, self.listToShow(self.fileList)
		if (not self.operations['newNameOperation']) and (not self.operations['addNumOperation']):
			return self.fileList, self.listToShow(self.fileList)
		self.keepLastPreviewHistory()
		self.excuteNewName()
		self.excuteAddNum()
		return self.fileList, self.listToShow(self.fileList)

	def keepLastPreviewHistory(self):
		for fileDict in self.fileList:
			fileDict['lastNewHead'] = fileDict['newHead']

	def undoPreview(self):
		for fileDict in self.fileList:
			fileDict['newHead'] = fileDict['lastNewHead']
		return self.fileList, self.listToShow(self.fileList)

	def resetPreview(self):
		for fileDict in self.fileList:
			fileDict['newHead'] = fileDict['fileHead']
		return self.fileList, self.listToShow(self.fileList)

	def excuteNewName(self):
		newName = self.operations['newName']
		if not newName: return
		#newName = localEncodeText(newName)
		operation = self.operations['newNameOperation']
		if not operation: return
		if operation == 'replace':
			self.setNewName( newName )
		elif operation == 'prefix':
			self.addNamePrefix( newName )
		elif operation == 'postfix':
			self.addNamePostfix( newName ) 

	def setNewName(self, newHead):
		for fileDict in self.fileList:
			fileDict['newHead'] = newHead

	def addNamePrefix(self, prefix):
		for fileDict in self.fileList:
			fileDict['newHead'] = prefix + fileDict['newHead']

	def addNamePostfix(self, postfix):
		for fileDict in self.fileList:
			fileDict['newHead'] = fileDict['newHead'] + postfix

	def excuteAddNum(self):
		startNum = self.operations['startNum']
		if not startNum: return
		operation = self.operations['addNumOperation']
		if not operation: return
		if operation == 'prefix':
			self.addNumPrefix(startNum)
		elif operation == 'postfix':
			self.addNumPostfix(startNum)

	def addNumPrefix(self, startNum):
		num = int(startNum)
		for fileDict in self.fileList:
			prefix = str(num).zfill(len(startNum))
			fileDict['newHead'] = prefix + fileDict['newHead']
			num += 1

	def addNumPostfix(self, startNum):
		num = int(startNum)
		for fileDict in self.fileList:
			postfix = str(num).zfill(len(startNum))
			fileDict['newHead'] = fileDict['newHead'] + postfix
			num += 1

	def listToShow(self, fileList):
		recordList = []
		for fileDict in fileList:
			record = [	fileDict['fileHead'], 
						fileDict['newHead'], 
						fileDict['level1Name'],
						fileDict['level2Name'],
						fileDict['level3Name'],
						fileDict['level4Name'],
						fileDict['level5Name'],
						fileDict['level6Name'],
						fileDict['level7Name'],
						fileDict['filePath'],
					]
			recordList.append(record)
		return recordList

def test():
	
	folderPath = u'f:\\temp\\中文目录'
	fileList, showList = FileReader().readAllFrom(folderPath)
	print fileList
	print showList
	'''
	print FileRename(fileList, {'newNameOperation':'replace', 'newName':u'new', 
		'addNumOperation':'prefix', 'startNum':'001'}).preview()

	print FileReader().readFiles(['f:\\temp\\111.txt', u'f:\\temp\\中文目录\\中文文件.txt'])
	'''
	folderPath = 'r\\1\\2\\3\\4\\5\\6\\7'
	print FileReader().setLevelsName(7, folderPath, {})
	folderPath = 'r\\1'
	print FileReader().setLevelsName(1, folderPath, {})

if __name__ == '__main__':
	test()