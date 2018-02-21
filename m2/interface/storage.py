""" Storage Interface """

from abc import ABCMeta, abstractmethod
import six


@six.add_metaclass(ABCMeta)
class Storage(object):
    """
    Abstract class for the Storage Interface.
    Only contains the necessary functionality of
    the Storage drivers.
    """

    @abstractmethod
    def copy(self, image_id, copy_image_id):
        """
        Make a deep copy of a given image.

        :param image_id: Id of the image to be copied
        :param copy_image_id: Id of the image copy
        :return: None
        :raise: Exception on failure
        """
        pass

    @abstractmethod
    def snapshot(self, instance_id, snap_image_id):
        """
        Make a deep copy of the provisioned instance's
        current state.

        :param instance_id: Id of the instance to obtain
                            the clone to be copied
        :param snap_image_id: Id of the snapshot
        :return: None
        :raise: Exception on failure
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
        :raise: Exception on failure
        """
        pass

    @abstractmethod
    def delete_clone(self, instance_id):
        """
        Delete a clone of a given image.

        :param instance_id: Id of the instance provisioned from the clone
        :return: None
        :raise: Exception on failure
        """
        pass

    @abstractmethod
    def get_clone_info(self, instance_id):
        """
        Get clone info from an instance id.

        :param instance_id: Id of the instance provisioned from the clone
        :return: Clone_info object
        :raise: Exception on failure
        """
        pass

    @abstractmethod
    def tag(self, instance_id, tag_id):
        """
        Create a tag (checkpoint) for a given
        provisoned image.

        :param instance_id: Id of instance that has been tagged
        :param tag_id: Id of tag (from core DB)
        :return: None
        :raise: Exception on failure
        """
        pass

    @abstractmethod
    def flatten_tag(self, tag_id, image_id):
        """
        Flatten a shallow copy (tag) into a new,
        unlinked image.

        :param tag_id: Id of tag to flatten (from core DB)
        :param image_id: Id of the flattened image
        :return: None
        :raise: Exception on failure
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
        :raise: Exception on failure
        """
        pass

    @abstractmethod
    def upload_image(self, image_id):
        """
        Upload an image to the datastore.

        :param image_id: Id of image in core DB
        :return: None
        :raise: Exception on failure
        """
        pass

    @abstractmethod
    def download_image(self, image_id):
        """
        Download image from storage to local disk.

        :param image_id: Id of image in core DB
        :return: The image(?)
        :raise: Exception on failure
        """
        pass

    @abstractmethod
    def delete_image(self, image_id):
        """
        Delete a given image from storage.

        :param image_id: Id of image to delete from storage
        :return: None
        :raise: Exception on failure
        """
        pass
