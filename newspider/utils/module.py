import inspect
from importlib import import_module
from pkgutil import iter_modules


def walk_modules(path):
    """Loads a module and all its submodules from the given module path and
    returns them. If *any* module throws an exception while importing, that
    exception is thrown back.

    For example: walk_modules('scrapy.utils')
    """

    mods = []
    mod = import_module(path)

    mods.append(mod)
    if hasattr(mod, '__path__'):
        for _, subpath, ispkg in iter_modules(mod.__path__):
            fullpath = path + '.' + subpath
            if ispkg:
                mods += walk_modules(fullpath)
            else:
                submod = import_module(fullpath)
                mods.append(submod)
    return mods


def _iter_command_classes(module_name):
    # TODO: add `name` attribute to commands and and merge this function with
    # scrapy.utils.spider.iter_spider_classes
    for module in walk_modules(module_name):
        for obj in vars(module).values():
            if inspect.isclass(obj) and issubclass(obj, object) and obj.__module__ == module.__name__:
                yield obj


def _get_commands_from_module(module):
    d = {}
    for cmd in _iter_command_classes(module):
        cmdname = cmd.__module__.split('.')[-1]
        d[cmdname] = cmd
    return d

if __name__ == '__main__':
    print _get_commands_from_module("scrapy.commands")