import LEGOKibbleBalanceGUI
import wx

class LEGOKibbleBalance(LEGOKibbleBalanceGUI.LEGOKibbleBalance):

	def __init__(self, parent):
		LEGOKibbleBalanceGUI.LEGOKibbleBalance.__init__(self, parent)


# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of CalcFrame
frame = LEGOKibbleBalance(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()