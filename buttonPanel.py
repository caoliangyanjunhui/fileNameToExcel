# -*- coding:UTF-8 -*-

import wx

import groupRename
import groupNum
	 
class ButtonBox(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.addOpenBox(sizer)
		#self.addRenameGroup(sizer)
		#self.addNumGroup(sizer)
		#self.addRreviewBox(sizer)
		#self.addRenameBox(sizer)
		self.addExportButton(sizer)
		self.SetSizer(sizer)


	def addOpenBox(self, sizer):
		box = wx.BoxSizer(wx.VERTICAL)
		#self.addOpenFileButton(box)
		self.addOpenFolderButton(box)
		sizer.Add(box,  0, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border=10)

	def addOpenFileButton(self, sizer):
		self.buttonOpenFile = wx.Button(self, -1, u"打开文件", size=(-1, 37))
		sizer.Add(self.buttonOpenFile, 0, flag=wx.TOP, border=0)


	def addOpenFolderButton(self, sizer):
		self.buttonOpenFolder = wx.Button(self, -1, u"打开目录", size=(-1, 37))
		sizer.Add(self.buttonOpenFolder, 0, flag=wx.TOP, border=5)


	def addRenameGroup(self, sizer):
		self.renameGroup = groupRename.RenamePanel(self)
		sizer.Add(self.renameGroup, flag=wx.LEFT, border=30)

	def addNumGroup(self, sizer):
		self.numGroup = groupNum.NumPanel(self)
		sizer.Add(self.numGroup, flag=wx.LEFT, border=1)

	def addRreviewBox(self, sizer):
		box = wx.BoxSizer(wx.VERTICAL)
		self.addPreviewButton(box)
		self.addUndoPreviewButton(box)
		self.addResetPreviewButton(box)
		sizer.Add(box,  0, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border=10)

	def addPreviewButton(self, sizer):
		self.buttonPreview = wx.Button(self, -1, u"预览")
		sizer.Add(self.buttonPreview, 0, flag=wx.TOP, border=0) 

	def addUndoPreviewButton(self, sizer):
		self.buttonUndoPreview = wx.Button(self, -1, u"撤销")
		sizer.Add(self.buttonUndoPreview, 0, flag=wx.TOP, border=3) 

	def addResetPreviewButton(self, sizer):
		self.buttonResetPreview = wx.Button(self, -1, u"清空")
		sizer.Add(self.buttonResetPreview, 0, flag=wx.TOP, border=3) 

	def addRenameBox(self, sizer):
		box = wx.BoxSizer(wx.VERTICAL)
		self.addRenameButton(box)
		self.addUndoRenameButton(box)
		sizer.Add(box,  0, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border=30)

	def addRenameButton(self, sizer):
		self.buttonRename = wx.Button(self, -1, u"执行重命名", size=(-1, 37))
		sizer.Add(self.buttonRename, 0, flag=wx.TOP, border=0)

	def addUndoRenameButton(self, sizer):
		self.buttonUndoRename = wx.Button(self, -1, u"撤销重命名", size=(-1, 37))
		sizer.Add(self.buttonUndoRename, 0, flag=wx.TOP, border=5)

	def addExportButton(self, sizer):
		self.buttonExport = wx.Button(self, -1, u"导出Excel", size=(-1, 78))
		sizer.Add(self.buttonExport, 0, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border=30)

	def reset(self):
		self.renameGroup.reset()
		self.numGroup.reset()

#---------------------------------------------------------------------------
class TestFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, u'button panel', size=(1024,120))
		self.mainPanel = wx.Panel(self, -1, style=0)
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)

		self.buttonBox = ButtonBox(self.mainPanel)

		self.mainSizer.Add(self.buttonBox, 1, wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
		self.mainPanel.SetSizer(self.mainSizer)

def test():
	app = wx.PySimpleApp()
	frame = TestFrame()
	frame.Show(True)
	app.MainLoop()

if __name__ == '__main__':
	test()