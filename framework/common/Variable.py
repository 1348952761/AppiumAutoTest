# coding:utf-8

exec ("from %s import *" % ("config",))


class Variable(object):
    def __getattr__(self, attribute_name):
        try:
            return object.__getattribute__(self, attribute_name)
        except:
            attribute_value = None
            try:
                attribute_value = project_config[attribute_name]
            except:
                try:
                    attribute_value = global_data[attribute_name]
                except:
                    pass
        self.__setattr__(attribute_name, attribute_value)
        return attribute_value

    def __setattr__(self, name, value):
       object.__setattr__(self, name, value)


def test():
    var = Variable()
    var.test = "test"
    print var.test
    print var.platformName
    print var.time
    print var.year


if __name__ == '__main__':
    test()
