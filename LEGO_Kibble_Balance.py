'''
Program that informs the user the mass of an object placed on the LEGO Kibble Balance.
'''

import Phidget
import sys
from datetime import datetime

import LabJack_U6

def initialisePhidget():
    Phidget.initialise()

def initialiseLabJackU6():
    pass

# Performs the initialisation of Hardware Components.
def initialise():
    initialisePhidget()
    initialiseLabJackU6()

def TestLabJackU6():
    numChannels = 2 # Number of AIN channelgs being used
    resolutionIndex = 1
    gainIndex = 0
    settlingFactor = 0
    differential = False
    latestAinValues = [0] * numChannels
    numIterations = 1000

    d = LabJack_U6.U6()
    d.getCalibrationData()
    try:
    # Configure the IOs before the test starts

        FIOEIOAnalog = (2 ** numChannels) - 1
        fios = FIOEIOAnalog & 0xFF
        eios = FIOEIOAnalog // 256

        d.getFeedback(LabJack_U6.PortDirWrite(Direction=[0, 0, 0], WriteMask=[0, 0, 15]))

        feedbackArguments = []

        feedbackArguments.append(LabJack_U6.DAC0_8(Value=125))
        feedbackArguments.append(LabJack_U6.PortStateRead())

        for i in range(numChannels):
            feedbackArguments.append(LabJack_U6.AIN24(i, resolutionIndex, gainIndex, settlingFactor, differential))

        start = datetime.now()
        # Call Feedback 1000 (default) times
        i = 0
        while i < numIterations:
            results = d.getFeedback(feedbackArguments)
            for j in range(numChannels):
                latestAinValues[j] = d.binaryToCalibratedAnalogVoltage(gainIndex, results[2 + j])
            i += 1

        print("Last readings: %s" % latestAinValues)
    finally:
        d.close()

def main():
	try:
		initialise()
		while True:
			Phidget.setVoltage(1.225, 0)
	finally:
		Phidget.close()


if __name__=="__main__":
	main()