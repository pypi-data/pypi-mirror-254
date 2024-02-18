# meta.py
#
# Add meta features to functions of a module
#
# Copyright (c) 2022-2024 WordTM Project 
# Author: Johnny Cheng <drjohnnycheng@gmail.com>
#
# Updated: 28 January 2024
#
# URL: https://github.com/drjohnnycheng/wordtm.git
# For license information, see LICENSE.TXT

import inspect
from functools import wraps
import pkgutil
from importlib import import_module
import time


def get_module_info(modname='wordtm'):
    """Gets the function info of each sub-module of the root module.

    :param modname: The prescribed module, of which the module information is extracted,
        default to 'wordtm'
    :type modname: str, optional
    :return: The module information of the prescribed module
    :rtype: str
    """

    # modname = __name__.split('.')[0]
    module = import_module(modname)

    i = 0
    mod_info = "The list of sub-modules and their functions of Module '" + modname + "'\n"
    for _, submodname, ispkg in pkgutil.iter_modules(module.__path__):
        if not ispkg:
            i += 1
            mod_info += "%d. %s:" %(i, submodname) + "\n"
            submod = import_module(".."+submodname, modname+"."+submodname)
            for name, member in inspect.getmembers(submod):
                if inspect.isfunction(member) and name != 'files':
                    #mod_info += "\t", name, str(inspect.signature(member)) + "\n"
                    mod_info += "\t{} {}\n".format(name, inspect.signature(member))

    return mod_info


def addin(func):
    """Adds additional features to a function at runtime.

    :param func: The target function for inserting additiolnal features - 
        timing information and showing code, default to None
    :type func: function
    """

    if "code" in inspect.signature(func).parameters:
        #raise TypeError('"code" argument already defined in "' + \
        #                func.__name__ + '" function')
        return

    @wraps(func)
    def wrapper(*args, timing=False, code=False, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        if timing:
            print(f"Finished {func.__name__!r} in {run_time:.4f} secs")

        if code:
            print("\n" + inspect.getsource(func))

        return value

    sig = inspect.signature(func)
    params = list(sig.parameters.values())
    params.append(inspect.Parameter("timing",
                                    inspect.Parameter.KEYWORD_ONLY,
                                    default=False))
    params.append(inspect.Parameter("code",
                                    inspect.Parameter.KEYWORD_ONLY,
                                    default=False))
    wrapper.__signature__ = sig.replace(parameters=params)
    return wrapper


def addin_all_functions(submod):
    """Applies 'addin' function to all functions of a module at runtime.

    :param submod: The target sub-module of which all the functions are inserted
        additional features, default to None
    :type submod: module
    """

    for name, member in inspect.getmembers(submod):
        if callable(member) and \
           member.__name__ != 'files' and \
           name[0].islower():
            # print("\t", name)
            setattr(submod, name, addin(member))


def addin_all(modname='wordtm'):
    """Applies 'addin' function to all functions of all sub-modules of
    a module at runtime.

    :param modname: The target module of which all the functions are inserted
        additional features, default to 'wordtm'
    :type modname: str, optional
    """

    module = import_module(modname)

    if hasattr(module, "__path__"):
        for _, submodname, ispkg in pkgutil.iter_modules(module.__path__):
            if not ispkg and submodname != 'meta':
                # print("@", submodname)
                submod = import_module(".." + submodname, \
                                       modname + "." + submodname)
                addin_all_functions(submod)
    else:
        addin_all_functions(module)
