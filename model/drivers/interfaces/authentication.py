from abc import ABCMeta, abstractmethod

class authentication:

	__metaclass__ = ABCMeta


	@abstractmethod
	def isAdmin(self):
	"""verify admin's authority"""
	pass

	@abstractmethod
	def isLegit(self, entityId):
	"""verify user's authority"""
	pass
	


