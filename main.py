# -*- coding:UTF-8 -*-

import wx
import buttonPanel
import grid
import renameFile
import csvHandler
import os

class ClientFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(
			self, None, -1, u'文件名获取工具 v0.1', size=(1000,600)
			)
		self.fileList = []
		self.showList = []
		self.files = []
		self.folderPath = ''
		self.lastOpenFolderPath = ''
		self.lastSaveFolderPath = ''
		self.addIcon()
		self.addStatusBar()
		self.splitWindow = wx.SplitterWindow(self)
		self.mainPanel = self.newMainPanel(self.splitWindow)
		self.infoPanel = self.newInfoPanel(self.splitWindow)
		self.splitWindow.SplitHorizontally(self.mainPanel, self.infoPanel, -100)
		self.splitWindow.SetMinimumPaneSize(20)
		self.bindEvents()


	def newMainPanel(self, parent):
		mainPanel = wx.Panel(parent, -1)
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		self.buttonBox = buttonPanel.ButtonBox(mainPanel)
		mainSizer.Add(self.buttonBox, proportion=0, flag= wx.TOP, border=5)

		self.grid = grid.FileTableGrid(mainPanel)
		mainSizer.Add(self.grid, proportion= 1, flag=wx.TOP | wx.EXPAND,  border=5)

		mainPanel.SetSizer(mainSizer)
		return mainPanel

	def newInfoPanel(self, parent):
		infoPanel = wx.Panel(parent)
		infoPanel.SetBackgroundColour("white")

		vbox = wx.BoxSizer(wx.VERTICAL)
		self.infoText = wx.TextCtrl(infoPanel, -1, style=wx.TE_MULTILINE)
		vbox.Add(self.infoText, proportion=1, flag=wx.EXPAND | wx.ALL)
		infoPanel.SetSizerAndFit(vbox)
		return infoPanel

	def addStatusBar(self):
		self.statusBar = wx.StatusBar(self)
		self.SetStatusBar(self.statusBar)

	def addIcon(self):
		icon = wx.Icon('ico/rename32.ico', wx.BITMAP_TYPE_ICO)
		self.SetIcon(icon)

	def bindEvents(self):
		self.buttonBox.buttonOpenFolder.Bind(wx.EVT_BUTTON, self.onFolderOpenButtonClick)
		self.buttonBox.buttonExport.Bind(wx.EVT_BUTTON, self.onExportButtonClick)

	def onFolderOpenButtonClick(self, evt):
		dlg = wx.DirDialog(self, u"选择要批处理的目录", defaultPath=self.lastOpenFolderPath, 
						  style=wx.DD_DIR_MUST_EXIST | wx.DD_CHANGE_DIR | wx.DD_DEFAULT_STYLE)
		if dlg.ShowModal() == wx.ID_OK:
			self.files = []
			self.folderPath = dlg.GetPath()
			self.lastOpenFolderPath = self.folderPath
			self.openFolder(self.folderPath)
		dlg.Destroy()


	def openFolder(self, folderPath):
		self.showStatus(u'正在扫描文件……')
		self.showList = renameFile.FileReader().readAllFrom(folderPath)
		self.grid.setData(self.showList)
		self.showInfo(folderPath)
		self.showStatus(u'打开成功')

	def onExportButtonClick(self, evt):
		if self.noShowList(): return
		
		dlg = wx.FileDialog(
			self, message=u"文件存为……", defaultDir=self.lastSaveFolderPath, 
			defaultFile=u"导出文件表格.csv", wildcard=u'逗号分隔数据表(*.CSV)|*.csv|All files (*.*)|*.*', style=wx.SAVE
			)
		if dlg.ShowModal() == wx.ID_OK:
			filePath = dlg.GetPath()
		else:
			return

		try:
			dataList = self.showList
			#dataList.insert(0, self.grid.getTitleList())
			csvHandler.CSV().write(filePath, dataList)
		except Exception, e:
			self.infoText.SetValue(str(e))
			self.showStatus(u'导出失败')
			return
		self.showInfo(filePath)
		self.showStatus(u'导出完成')

	def noShowList(self):
		if not self.showList:
			self.showInfo(u'尚未打开文件或目录')
			self.showStatus(u'操作无效')
			return True
		return False


	def showInfo(self, text):
		if not text: return
		try:
			self.infoText.SetValue(text)
		except Exception, e:
			self.infoText.SetValue(str(e))

	def showStatus(self, text):
		self.statusBar.SetStatusText(text, 0)



def main():
	app = wx.PySimpleApp()
	frame = ClientFrame()
	frame.Show(True)
	app.MainLoop()

if __name__ == '__main__':
	main()