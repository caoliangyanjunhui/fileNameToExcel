# -*- coding:UTF-8 -*-

import wx.grid as gridlib


#---------------------------------------------------------------------------
class FileDataTable(gridlib.PyGridTableBase):
	def __init__(self, data=[]):
		gridlib.PyGridTableBase.__init__(self)
		self.memoryOnlyList = [0,]
		self.colLabels = [	
							u'一', 
							u'二', 
							u'三',
							u'四', 
							u'五', 
							u'六', 
							u'七',  
							]
		self.initDataTypes()
		self.data = data

	def initDataTypes(self):
		self.dataTypes = [
			gridlib.GRID_VALUE_STRING, #1级文件夹
			gridlib.GRID_VALUE_STRING, #2级文件夹
			gridlib.GRID_VALUE_STRING, #3级文件夹
			gridlib.GRID_VALUE_STRING, #4级文件夹
			gridlib.GRID_VALUE_STRING, #5级文件夹
			gridlib.GRID_VALUE_STRING, #6级文件夹
			gridlib.GRID_VALUE_STRING, #7级文件夹
			]


	#--------------------------------------------------
	# required methods for the wxPyGridTableBase interface
	def GetNumberRows(self):
		return len(self.data)
	def GetNumberCols(self):
		return len(self.data[0])
	def IsEmptyCell(self, row, col):
		try:
			return not self.data[row][col]
		except IndexError:
			return True

	# Get/Set values in the table.  The Python version of these
	# methods can handle any data-type, (as long as the Editor and
	# Renderer understands the type too,) not just strings as in the
	# C++ version.
	def GetValue(self, row, col):
		try:
			return self.data[row][col]
		except IndexError:
			return ''

	def SetValue(self, row, col, value):
		try:
			self.data[row][col] = value
		except Exception, e:
			print e

	#--------------------------------------------------
	# Some optional methods
	# Called when the grid needs to display labels
	def GetColLabelValue(self, col):
		return self.colLabels[col]
	# Called to determine the kind of editor/renderer to use by
	# default, doesn't necessarily have to be the same type used
	# natively by the editor/renderer if they know how to convert.
	def GetTypeName(self, row, col):
		return self.dataTypes[col]
	# Called to determine how the data can be fetched and stored by the
	# editor and renderer.  This allows you to enforce some type-safety
	# in the grid.
	def CanGetValueAs(self, row, col, typeName):
		colType = self.dataTypes[col].split(':')[0]
		if typeName == colType:
			return True
		else:
			return False
	def CanSetValueAs(self, row, col, typeName):
		return self.CanGetValueAs(row, col, typeName)





#---------------------------------------------------------------------------
class FileTableGrid(gridlib.Grid):
	SELECT_CHOICE_INDEX = 0
	def __init__(self, parent):
		gridlib.Grid.__init__(self, parent, -1)
		data = self.getDefaultData()
		table = FileDataTable( data )
		self.SetTable(table)
		readOnlyColunms = (0, 1, 2, 3, 4, )
		self.setColumnsReadOnly(readOnlyColunms)

		self.SetRowLabelSize(30)
		self.SetMargins(0,0)
		self.AutoSizeColumns(True)

	def setColumnsReadOnly(self, columns):
		attr = gridlib.GridCellAttr()
		attr.SetReadOnly(True)
		for column in columns:
			if column >= self.GetNumberCols(): continue
			self.SetColAttr(column, attr)

	def getDefaultData(self):
		return [[],]

	def setData(self, dataList):
		if not dataList: return
		table = self.GetTable()
		table.data = None
		table.data = dataList
		self.reshow(table)

	def onLabelLeftClick(self, event):
		event.Skip(False) # 避免单击表格头部，导致所有条目被选中

	def onLabelLeftDClick(self, evt):
		evt.Skip()

	def reshow(self, table):
		self.SetTable(table)
		self.AutoSizeColumns(True)

	def getTitleList(self):
		return self.GetTable().colLabels

#---------------------------------------------------------------------------
import wx
class TestFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(
			self, parent, -1, u"grid", size=(1024,600)
			)
		p = wx.Panel(self, -1, style=0)
		self.grid = FileTableGrid(p)
		bs = wx.BoxSizer(wx.VERTICAL)
		bs.Add(self.grid, 1, wx.GROW|wx.ALL, 5)
		p.SetSizer(bs)

#---------------------------------------------------------------------------
if __name__ == '__main__':
	import sys
	app = wx.PySimpleApp()
	frame = TestFrame(None)
	frame.Show(True)
	app.MainLoop()
#---------------------------------------------------------------------------