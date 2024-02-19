class Thesaurus(dict):
    """A dictionary that exhaustively searches a value from a list of keys."""
    def get(self, key, default=None):
        """Retrieves a value that matches a given key, like in a regular
        dictionary, or the default value if the key is not present. If the key
        is a list, then it will iterate through all the values one by one and
        return the first match found or the default value if not. Any other
        unhashable type will simply return the default value, unlike a
        dictonary that would raise a TypeError."""
        if isinstance(key, list):
            for index in range(len(key)):
                if key[index] in self:
                    return self[key[index]]

        elif self._is_hashable(key):
            try:
                return self[key]
            except KeyError:
                return default

        return default

    def __repr__(self):
        return "%s(%s)" % (type(self).__name__, super().__repr__())

    def __contains__(self, item):
        """This method allows for the use of:
            key_list in T
        where key_list is a list and T is a Thesaurus object. It returns True
        if any of the keys found in key_list is found in T and False otherwise.
        A key of a hashable type will work as normal and any other unhashable
        types will raise a TypeError."""
        if isinstance(item, list):
            for key in item:
                if key in self.keys():
                    return True
            return False
        elif self._is_hashable(item):
            return item in self.keys()
        else:
            raise TypeError("unhashable type: '%s'" % type(item).__name__)

    def _is_hashable(self, value):
        try:
            hash(value)
            return True
        except TypeError:
            return False
