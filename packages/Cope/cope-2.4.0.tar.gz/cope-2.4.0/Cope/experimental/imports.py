from typing import Union, Iterable, Literal
import importlib
from varname import nameof


def installLib(libs:Iterable):
    libs = ' '.join(libs)

    def useSubprocess():
        import subprocess
        print(subprocess.check_output(f"pip install {libs}", shell=True, text=True))

    try:
        import IPython
    except:
        useSubprocess()
    else:
        if (ipython := IPython.get_ipython()) is not None:
            ipython.run_line_magic("pip", f"install {libs}")
        else:
            useSubprocess()

def niceInstallLib(libs:Iterable):
    if input(f'Would you like to install {" ".join(libs)}? (y/n): ').lower() == 'y':
        installLib(libs)

def ensureImported(package:str, specificModules=[], as_=None,
                if_unavailable:Literal['auto', 'warn', 'error']='auto',
                _globals=globals(),
                _locals=locals(),
                level=0,
            ) -> bool:
    # Parameter handling
    if type(specificModules) is str:
        specificModules = [specificModules]
    if len(specificModules) > 1 and as_ is not None:
        raise TypeError('You cant specify both an as_ parameter and multiple specificModules')

    try:
        imported = __import__(package, _globals, _locals, specificModules, level)
    except ImportError:
        if if_unavailable == 'auto':
            print(f'It doesn\'t look like you have {package} installed. ', end='')
            niceInstallLib((package,))
            return ensureImported(package, specificModules, as_, if_unavailable, _globals, _locals, level)
        elif if_unavailable == 'warn':
            if len(specificModules):
                print(f'Can\'t import {tuple(specificModules)} from {package}. Have you installed the associated pip package? (try "pip install {pacakge}")')
            else:
                print(f'Can\'t import {package}. Have you installed the associated pip package? (try "pip install {pacakge}")')
            return False
        elif if_unavailable == 'error':
            raise ImportError(package)
            return False
        else:
            raise TypeError(f'Unknown if_unavailable value given: {if_unavailable}')
            return False
    else:
        if len(specificModules):
            # print('returning imported')
            # return imported
            for i in specificModules:
                _globals[i] = imported.__getattribute__(i)
            # globals()[as_ if as_ else specificModules[-1]] = imported.__getattribute__(specificModules[-1])
        else:
            _globals[as_ if as_ else package] = imported
    return True

# todo
def checkImport(package:str, specificModules=[], _as=None,
                fatal:bool=False, printWarning:Union[str, bool]=True,
                _globals=globals(), _locals=locals(), level=0
                ) -> "(Union[package, (packages,)], worked)":
    # todo()
    return
    if type(specificModules) is str:
        specificModules = [specificModules]
    try:
        _temp = __import__(package, _globals, _locals, specificModules, level)
    except ImportError:
        if type(printWarning) is str:
            print(printWarning)
        elif printWarning:
            if len(specificModules):
                print(f'Can\'t import {tuple(specificModules)} from {package}. Have you installed the associated pip package? (try "pip install {pacakge}")')
            else:
                print(f'Can\'t import {package}. Have you installed the associated pip package? (try "pip install {pacakge}")')
        if fatal:
            raise ImportError(package)
        return False
    else:
        if len(specificModules):
            for i in specificModules[:-1]:
                globals()[i] = _temp.__getattribute__(i)
            globals()[_as if _as else specificModules[-1]] = _temp.__getattribute__(specificModules[-1])
        else:
            globals()[_as if _as else package] = _temp
        return True

def dependsOnPackage(package:str, specificModules=[], as_=None,
                    if_unavailable:Literal['auto', 'warn', 'error']='auto',
                    _globals=globals(), _locals=locals(),
                    level=0):
    def wrap(func):
        def innerWrap(*funcArgs, **funcKwArgs):
            if ensureImported(package, specificModules, as_, if_unavailable, globals, locals, level):
                return func(*funcArgs, **funcKwArgs)
            else:
                print(f'Failed to import {package} for {nameof(func)}')
                return None
        return innerWrap
    return wrap

def importpath(path, name, moduleName):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    # This is kinda ugly and nasty, but it works. For now.
    globals()[moduleName] = importlib.import_module(
        name, moduleName).__getattribute__(moduleName)
