

import os
import typing
import os
import struct
import platform
import subprocess








#
# Static helper class to provide terminal width and height
#
class _TerminalSizeHelper(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	@staticmethod
	def ____tryGetTerminalSize_tput() -> typing.Union[os.terminal_size,None]:
		try:
			_data = subprocess.check_output([ "tput", "cols", "lines" ]).decode("UTF-8")
			_items = _data.split("\n")
			cols = int(_items[0])
			rows = int(_items[1])
			return os.terminal_size((cols, rows))
		except:
			pass

		return None
	#

	@staticmethod
	def ____tryGetTerminalSize_windll() -> typing.Union[os.terminal_size,None]:
		try:
			from ctypes import windll, create_string_buffer
			h = windll.kernel32.GetStdHandle(-12)
			csbi = create_string_buffer(22)
			res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
			if res:
				(_bufx, _bufy, _curx, _cury, _wattr, _left, _top, _right, _bottom, _maxx, _maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
				cols = _right - _left + 1
				rows = _bottom - _top + 1
				return os.terminal_size((cols, rows))
		except:
			pass

		return None
	#

	#
	# Main entry point for determining Windows terminal size
	#
	@staticmethod
	def __windows_getTerminalSize() -> typing.Union[os.terminal_size,None]:
		try:
			return os.get_terminal_size()
		except:
			pass

		# ----

		ret = _TerminalSizeHelper.____tryGetTerminalSize_windll()
		if ret:
			return ret

		ret = _TerminalSizeHelper.____tryGetTerminalSize_tput()
		if ret:
			return ret

		return None
	#

	################################################################################################################################

	@staticmethod
	def ____ioctl_GWINSZ(fd) -> typing.Union[os.terminal_size,None]:
		try:
			import fcntl
			import termios
			cr = struct.unpack("hh", fcntl.ioctl(fd, termios.TIOCGWINSZ, "1234"))
			return os.terminal_size((cr[0], cr[1]))
		except:
			pass

		return None
	#

	#
	# Main entry point for determining POSIX terminal size
	#
	@staticmethod
	def __posix_getTerminalSize() -> typing.Union[os.terminal_size,None]:
		try:
			return os.get_terminal_size()
		except:
			pass

		# ----

		ret = _TerminalSizeHelper.____ioctl_GWINSZ(0)
		if ret:
			return ret

		ret = _TerminalSizeHelper.____ioctl_GWINSZ(1)
		if ret:
			return ret

		ret = _TerminalSizeHelper.____ioctl_GWINSZ(2)
		if ret:
			return ret

		try:
			# NOTE: ctermid() is not available on all platforms
			with os.open(os.ctermid(), os.O_RDONLY) as fin:
				return _TerminalSizeHelper.____ioctl_GWINSZ(fin)
		except:
			pass

		return None
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	################################################################################################################################
	## Public Static Methods
	################################################################################################################################

	@staticmethod
	def getTerminalSize() -> os.terminal_size:
		ret = None
		current_os = platform.system().lower()
		if current_os == "windows":
			ret = _TerminalSizeHelper.__windows_getTerminalSize()
		elif current_os in ( "linux", "darwin" ) or current_os.startswith("cygwin"):
			ret = _TerminalSizeHelper.__posix_getTerminalSize()
		else:
			pass

		if ret:
			return ret

		return os.terminal_size((80, 25))
	#

#

















