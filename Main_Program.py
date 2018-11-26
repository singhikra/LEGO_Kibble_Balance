import LEGOKibbleBalanceGUI
import wx
import Phidget
import LabJack_U6

class LEGOKibbleBalance(LEGOKibbleBalanceGUI.LEGOKibbleBalance):
	numChannels = 2  # Number of AIN channelgs being used
	latestAinValues = [0] * numChannels

	def __init__(self, parent):
		LEGOKibbleBalanceGUI.LEGOKibbleBalance.__init__(self, parent)
		self.KibbleLog.AppendText("Welcome to LEGO Kibble Balance!\n")
		self.CoilASupplyVoltage.SetValue("0.0")
		self.CoilBSupplyVoltage.SetValue("0.0")

	def GetCoilVoltages(self):
		global numChannels, latestAinValues
		resolutionIndex = 1
		gainIndex = 0
		settlingFactor = 0
		differential = False
		numIterations = 1000

		d = LabJack_U6.U6()
		d.getCalibrationData()

		try:
			# Configure the IOs before the test starts

			# FIOEIOAnalog = (2 ** numChannels) - 1
			# fios = FIOEIOAnalog & 0xFF
			# eios = FIOEIOAnalog // 256

			d.getFeedback(LabJack_U6.PortDirWrite(Direction=[0, 0, 0], WriteMask=[0, 0, 15]))
			feedbackArguments = []
			feedbackArguments.append(LabJack_U6.DAC0_8(Value=125))
			feedbackArguments.append(LabJack_U6.PortStateRead())

			for i in range(numChannels):
				feedbackArguments.append(LabJack_U6.AIN24(i, resolutionIndex, gainIndex, settlingFactor, differential))

			# start = datetime.now()
			# Call Feedback 1000 (default) times
			i = 0
			while i < numIterations:
				results = d.getFeedback(feedbackArguments)
				for j in range(numChannels):
					latestAinValues[j] = d.binaryToCalibratedAnalogVoltage(gainIndex, results[2 + j])
				i += 1

		finally:
			d.close()

	def DisplayCoilCurrents(self):
		global latestAinValues
		self.CurrentThroughCoilA.SetValue(str(latestAinValues[0]))
		self.CurrentThroughCoilB.SetValue(str(latestAinValues[1]))

	def SetCoilAVoltageOnButtonClick(self, event):
		self.KibbleLog.AppendText("Setting Coil A Supply Voltage to " + self.CoilASupplyVoltage.GetValue() + " V\n")
		Supply_Voltage_A = float(self.CoilASupplyVoltage.GetValue())
		Phidget.setVoltage(Supply_Voltage_A, 0)
		self.DisplayCoilCurrents()

	def SetCoilBVoltageOnButtonClick(self, event):
		self.KibbleLog.AppendText("Setting Coil B Supply Voltage to " + self.CoilBSupplyVoltage.GetValue() + " V\n")
		Supply_Voltage_B = float(self.CoilBSupplyVoltage.GetValue())
		Phidget.setVoltage(Supply_Voltage_B, 1)
		self.DisplayCoilCurrents()


# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of CalcFrame
frame = LEGOKibbleBalance(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()