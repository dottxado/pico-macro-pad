class AbstractConfiguration:
	def getName():
		return ""
	def getColor():
		return (0, 0, 0)
	def getMacros():
		return []
	def nothing():
		pass

class AbstractMacro:
	def getMacroName():
		return ""
	def getMacro():
		pass