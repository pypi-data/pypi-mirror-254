


import os
import re





from .constants import ALL_BGCOLORS, ALL_FGCOLORS, STYLE_RESET
from ._TerminalSizeHelper import _TerminalSizeHelper








def getTerminalSize() -> os.terminal_size:
	# return tuple(os.get_terminal_size())
	return _TerminalSizeHelper.getTerminalSize()
#





def checkTerminalSupportsColors() -> bool:
	# see: https://www.gnu.org/software/gettext/manual/html_node/The-TERM-variable.html

	x = os.getenv("TERM")
	if x:
		if x.endswith("-color"):
			return True
		m = re.match("^.*-([0-9]+)color$", x)
		if m:
			n = int(m.group(1))
			if n >= 16:
				return True

	return False
#





_REPL_MAP = None

def stripColors(text:str) -> str:
	global _REPL_MAP
	if _REPL_MAP is None:
		_REPL_MAP = []
		_REPL_MAP.extend(ALL_BGCOLORS)
		_REPL_MAP.extend(ALL_FGCOLORS)
		_REPL_MAP.append(STYLE_RESET)

	for k in _REPL_MAP:
		text = text.replace(k, "")

	return text
#





