from abstract_classes import AbstractConfiguration, AbstractMacro

class EmptyConfiguration(AbstractConfiguration):
	# No name for this configuration
	def getName():
		return ""
	# No color
	def getColor():
		return (0, 0, 0)
	# No macros
	def getMacros():
		return []
	# Nothing
	def nothing():
		pass
	

class EmptyMacro(AbstractMacro):
	# No nanme for this macro
	def getMacroName():
		return ""
	# No actions for this macro
	def getMacro():
		pass