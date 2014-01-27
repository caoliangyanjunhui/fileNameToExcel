# -*- coding:UTF-8 -*-
import wx

class RenamePanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent, -1)
		#self.SetBackgroundColour(wx.BLUE)

		sizer = wx.BoxSizer(wx.VERTICAL)
		self.addRadioBox(sizer)
		self.addText(sizer)
		self.SetSizer(sizer)

	def addRadioBox(self, sizer):
		options = [u'不需要', u'替换', u'加前缀', u'加后缀']
		self.operations = [None, 'replace', 'prefix', 'postfix']
		self.radioBox = wx.RadioBox(
				self, -1, u"字符串", wx.DefaultPosition, wx.DefaultSize,
				options, 4, wx.RA_SPECIFY_COLS
				)
		sizer.Add(self.radioBox, 0, wx.ALL, 1)

	def addText(self, sizer):
		self.newName = wx.TextCtrl(self, -1, "", size=(248, -1))
		sizer.Add(self.newName, flag=wx.LEFT | wx.TOP, border=1)

	def getSelection(self):
		index = self.radioBox.GetSelection() 
		return self.operations[index]

	def getNewName(self):
		return self.newName.GetValue()

	def reset(self):
		self.radioBox.SetSelection(0)
		self.newName.SetValue('')


#---------------------------------------------------------------------------
class TestFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(
			self, None, -1, u'radio box', size=(600,400)
			)
		self.mainPanel = wx.Panel(self, -1, style=0)
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)

		self.radioBox = RenamePanel(self.mainPanel)

		self.mainSizer.Add(self.radioBox, 1, wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
		self.mainPanel.SetSizer(self.mainSizer)

def test():
	app = wx.PySimpleApp()
	frame = TestFrame()
	frame.Show(True)
	app.MainLoop()

if __name__ == '__main__':
	test()