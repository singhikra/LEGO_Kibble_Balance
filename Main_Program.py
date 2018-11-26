import LEGOKibbleBalanceGUI
import wx
import Phidget

class LEGOKibbleBalance(LEGOKibbleBalanceGUI.LEGOKibbleBalance):

	def __init__(self, parent):
		LEGOKibbleBalanceGUI.LEGOKibbleBalance.__init__(self, parent)
		self.KibbleLog.AppendText("Welcome to LEGO Kibble Balance!\n")
		self.CoilASupplyVoltage.SetValue("0.0")
		self.CoilBSupplyVoltage.SetValue("0.0")

	def SetCoilAVoltageOnButtonClick(self, event):
		self.KibbleLog.AppendText("Setting Coil A Supply Voltage to " + self.CoilASupplyVoltage.GetValue() + " V\n")
		Supply_Voltage_A = float(self.CoilASupplyVoltage.GetValue())
		Phidget.setVoltage(Supply_Voltage_A, 0)

	def SetCoilBVoltageOnButtonClick(self, event):
		self.KibbleLog.AppendText("Setting Coil B Supply Voltage to " + self.CoilBSupplyVoltage.GetValue() + " V\n")
		Supply_Voltage_B = float(self.CoilBSupplyVoltage.GetValue())
		Phidget.setVoltage(Supply_Voltage_B, 1)


# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of CalcFrame
frame = LEGOKibbleBalance(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()