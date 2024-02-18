import abc


class APIObject(object):
    __metaclass__ = abc.ABCMeta

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, data):
        pass

    @abc.abstractmethod
    def to_dict(self):
        pass
