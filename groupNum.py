# -*- coding:UTF-8 -*-
import wx

from stringHelper import isIntStr, toInt

class NumPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent, -1)
		#self.SetBackgroundColour(wx.BLUE)

		sizer = wx.BoxSizer(wx.VERTICAL)
		self.addRadioBox(sizer)
		self.addTextStartNum(sizer)
		self.SetSizer(sizer)

	def addRadioBox(self, sizer):
		options = [u'不需要', u'加前缀', u'加后缀']
		self.operations = [None, 'prefix', 'postfix']
		self.radioBox = wx.RadioBox(
				self, -1, u"编号", wx.DefaultPosition, wx.DefaultSize,
				options, 3, wx.RA_SPECIFY_COLS
				)
		sizer.Add(self.radioBox, 0, wx.ALL, 1)

	def addTextStartNum(self, sizer):
		self.startNum = wx.TextCtrl(self, -1, "001", size=(188, -1))
		sizer.Add(self.startNum, flag=wx.LEFT | wx.TOP, border=1)
		self.startNum.Bind(wx.EVT_CHAR, self.onStartNumChar)
		self.startNum.Bind(wx.EVT_TEXT, self.onStartNumText)

	def onStartNumChar(self, evt):
		inputChar = evt.GetKeyCode()
		if (inputChar >= 48 and inputChar <= 57) or (inputChar == 8) :	
			evt.Skip(True)
			return
		
		evt.Skip(False)

	def onStartNumText(self, evt):
		text = evt.GetString()
		if not isIntStr(text):
			self.startNum.SetValue('001')


	def getSelection(self):
		index = self.radioBox.GetSelection() 
		return self.operations[index]

	def getStartNum(self):
		return self.startNum.GetValue()

	def reset(self):
		self.radioBox.SetSelection(0)
		self.startNum.SetValue('')
#---------------------------------------------------------------------------
class TestFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(
			self, None, -1, u'radio box', size=(600,400)
			)
		self.mainPanel = wx.Panel(self, -1, style=0)
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)

		self.radioBox = NumPanel(self.mainPanel)

		self.mainSizer.Add(self.radioBox, 1, wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
		self.mainPanel.SetSizer(self.mainSizer)

def test():
	app = wx.PySimpleApp()
	frame = TestFrame()
	frame.Show(True)
	app.MainLoop()

if __name__ == '__main__':
	test()