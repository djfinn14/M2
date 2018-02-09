from abc import ABCMeta, abstractmethod

class autherization:

	__metaclass__ = ABCMeta


	@abstractmethod
	def autherize_access_node(self, nodeId):
	"""Autherize entity's access to a specific node"""
	pass

	@abstractmethod
	def autherize_access_image(self, imageId):
	"""Autherize entity's access to a specific image"""
	pass

	@abstractmethod
	def autherize_access_tag(self, tagId):
	"""Autherize entity's access to a specific tag"""
	pass

