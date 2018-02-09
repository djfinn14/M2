from abc import ABCMeta, abstractmethod


class ipxeServer:

	__metaclass__ = ABCMeta

    
	@abstractmethod
	def ipxeServer(self, conf_file):
	"""Set up ipxe"""
	pass



	@abstractmethod
	def generate_ipxe_file(self, node_name, target_name):
	"""Generate ipxe file"""
	pass

	



