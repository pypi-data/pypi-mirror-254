import os
import pickle


class Varcache:
    def __init__(self, dirpath):
        self._dirpath = dirpath
        self._name_id_mapping = {}
        self._id_name_mapping = {}

    def load(self, name, default):
        """
        Loads object from the disk if it exists.
        """
        if name in self._name_id_mapping:
            raise AlreadyLoadedError(name)

        path = self._get_object_path(name)

        if os.path.exists(path):
            with open(path, 'rb') as f:
                obj = pickle.load(f)
        else:
            obj = default()

        self.bind(obj, name)

        return obj

    def save(self, obj, name=None):
        """
        Saves the object to the disk.
        """
        if name is not None:
            self.bind(obj, name)

        obj_id = id(obj)
        name = self._id_name_mapping[obj_id]
        path = self._get_object_path(name)

        with open(path, 'wb') as f:
            pickle.dump(obj, f)

    def bind(self, obj, name):
        """
        Binds given object to its name within Varcache.
        """
        obj_id = id(obj)

        if name not in self._name_id_mapping:
            self._name_id_mapping[name] = obj_id

        if obj_id not in self._id_name_mapping:
            self._id_name_mapping[obj_id] = name

        if self._name_id_mapping[name] != obj_id:
            raise DuplicateNameError(name)

        if self._id_name_mapping[obj_id] != name:
            raise DuplicateObjectError(obj)

    def unbind(self, obj):
        """
        Unbinds the object.
        """
        obj_id = id(obj)

        if obj_id not in self._id_name_mapping:
            raise NotBoundError(obj)

        name = self._id_name_mapping[obj_id]

        del self._id_name_mapping[obj_id]
        del self._name_id_mapping[name]

    def check_name(self, name):
        """
        Checks whether the name is bound.
        """
        return name in self._name_id_mapping

    def check_object(self, obj):
        """
        Checks whether the object is bound.
        """
        return id(obj) in self._id_name_mapping

    def clear(self, name):
        """
        Remove the object saved by Varcache.
        """
        path = self._get_object_path(name)
        if os.path.exists(path):
            os.remove(path)

    def clear_all(self):
        """
        Removes all objects saved by Varcache.
        """
        for name in os.listdir(self._dirpath):
            path = self._get_object_path(name)
            os.remove(path)

        self._name_id_mapping.clear()
        self._id_name_mapping.clear()

    def _get_object_path(self, name):
        return os.path.join(self._dirpath, name)


class VarcacheError(Exception):
    pass


class DuplicateNameError(VarcacheError):
    pass


class DuplicateObjectError(VarcacheError):
    pass


class AlreadyLoadedError(VarcacheError):
    pass


class NotBoundError(VarcacheError):
    pass
