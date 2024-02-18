



import os
import typing

from .constants import *






#
# This is a stateful object that can display a spinner with descriptive text to represent activity progress.
#
class Spinner(object):

	_CHARACTERS = "|/-\\"

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, maximum:int = 0, bColor:bool = True):
		assert isinstance(maximum, int)
		assert maximum >= 0
		assert isinstance(bColor, bool)

		# ----

		self.__n = 0
		self.__counter = 0
		self.__maximum = maximum
		self.__maxCharsWritten = 1

		self.colorSpinner = FGCOLOR_LIGHT_YELLOW if bColor else ""
		self.colorProgress = FGCOLOR_LIGHT_CYAN if bColor else ""
		self.colorAction = FGCOLOR_WHITE if bColor else ""
		self.colorExtra = FGCOLOR_DARK_GRAY if bColor else ""
		self.__resetStyle = STYLE_RESET

		self.__maxWidth = os.get_terminal_size().columns - 12
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def setMaximum(self, maximum:int = 0):
		assert isinstance(maximum, int)
		assert maximum >= 0

		self.__maximum = maximum
	#

	def spin(self, action:str = None, extraText:str = None, bPrintPercent:bool = True):
		outputList = []

		if action:
			outputList.append(self.colorAction + action + self.__resetStyle)

		outputList.append(self.colorSpinner + Spinner._CHARACTERS[self.__n] + self.__resetStyle)
		self.__n = (self.__n + 1) % 4

		if (self.__maximum > 0) and bPrintPercent:
			self.__counter += 1
			pc = round(self.__counter * 100 / self.__maximum)
			outputList.append("{}{}%{}".format(self.colorProgress, pc, self.__resetStyle))

		if extraText:
			if len(extraText) > self.__maxWidth:
				extraText = extraText[:self.__maxWidth-3] + "..."
			outputList.append(self.colorExtra + ">>")
			outputList.append(extraText + self.__resetStyle)

		s = "  " + " ".join(outputList)
		if len(s) > self.__maxCharsWritten:
			self.__maxCharsWritten = len(s)
		else:
			s += " " * ((self.__maxCharsWritten) - len(s))

		print(s + "\r", end="", flush=True)
	#

	def hide(self):
		print("\r" + " " * self.__maxCharsWritten + "\r", end="", flush=True)
	#

#















