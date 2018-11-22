'''
Program that informs the user the mass of an object placed on the LEGO Kibble Balance.
'''
import Phidget

def initialisePhidget():
    Phidget.initialise()

def initialiseLabJackU6():
    pass

# Performs the initialisation of Hardware Components.
def initialise():
    initialisePhidget()
    initialiseLabJackU6()

def main():
	try:
		initialise()
		while True:
			Phidget.setVoltage(1.225, 0)
	finally:
		Phidget.close()


if __name__=="__main__":
	main()