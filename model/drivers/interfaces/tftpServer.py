from abc import ABCMeta, abstractmethod


class tftpServer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def tftpServer(self, conf_file):
        """Set up TFTP server"""
    pass

    @abstractmethod
    def generate_mac_addr_file(self, img_name, node_name, mac_addr):
        """Generate mac address file"""
    pass
