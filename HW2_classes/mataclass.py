class CustomMeta(type):
    def __new__(cls, class_name, parents, attributes):
        new_attributes = {}
        for name, attr in attributes.items():
            if len(name.split('__')) != 3:
                new_attributes['custom_' + name] = attributes[name]
            else:
                new_attributes[name] = attributes[name]
        return super().__new__(cls, class_name, parents, new_attributes)

    def __call__(self, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        new_dict = {}
        for name in obj.__dict__:
            new_dict['custom_' + name] = obj.__dict__[name]
        obj.__dict__ = new_dict
        return obj


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100
