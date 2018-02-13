#!/usr/bin/python

from abc import ABCMeta, abstractmethod


class Storage(object):
    """
    Abstract class for the Storage Interface.
    Only contains the necessary functionality of
    the Storage drivers.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def copy(self, image_id, copy_name):
        """
        Make a deep copy of a given image.

        :param image_id: Id of the image to be copied
        :param copy_name: Name of the image copy
        :return: Id of the image copy
        """
        pass

    @abstractmethod
    def clone(self, instance_id, parent_image_id):
        """
        Make a clone of a given image.

        :param instance_id: Id of the instance for which
                            the clone is used to provision
        :param parent_image_id: Id of the image to clone
        :return: Id of the clone image
        """
        pass

    @abstractmethod
    def delete_clone(instance_id):
        """
        Delete a clone of a given image.

        :param instance_id: Id of the instance provisioned from the clone
        :return: None
        """
        pass

    @abstractmethod
    def get_clone_info(instance_id):
        """
        Get clone info from an instance id.

        :param instance_id: Id of the instance provisioned from the clone
        :return: Clone object (or the image id from which the clone is derived)
        """
        pass

    @abstractmethod
    def get_image_info(parent_image_id):
        """
        Get image info from image_id.

        :param parent_image_id: Image from which the clone is derived
        :return: Parent image id from the core DB
        """
        pass

    @abstractmethod
    def create_tag(self, instance_id, tag_id):
        """
        Create a tag (checkpoint) for a given
        provisoned image.

        :param instance_id: Id of instance that has been tagged
        :param tag_name: Id of tag (from core DB)
        :return: None
        """
        pass

    @abstractmethod
    def flatten(self, instance_id, tag_id):
        """
        Flatten a shallow copy (tag) into a new,
        unlinked image.

        :param instance_id: Id of instance referenced by the tag
        :param tag_id: Id of tag to flatten (from core DB)
        :return: None
        """
        pass

    @abstractmethod
    def delete_tag(self, instance_id, tag_id):
        """
        Delete an existing tag for a given
        provisioned image.

        :param instance_id: Id of instance referenced by the tag
        :param tag_id: Id of tag to delete (from core DB)
        :return: None
        """
        pass

    @abstractmethod
    def upload_image(self, image_id):
        """
        Upload an image to the datastore..

        :param image_id: Id of image in core DB
        :return: None
        """
        pass

    @abstractmethod
    def download_image(self, image_id):
        """
        Download image from storage to local disk.

        :param image_id: Id of image in core DB
        :return: The image
        """
        pass

    @abstractmethod
    def delete_image(self, image_id):
        """
        Delete a given image from storage.

        :param image_id: Id of image to delete from storage
        :return: None
        """
        pass
