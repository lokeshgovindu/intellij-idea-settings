import inspect
import sys


def callee():
    return inspect.getouterframes(inspect.currentframe())[1][1:4]


def caller():
    return inspect.getouterframes(inspect.currentframe())[2][1:4]


def getVarName(var):
    """This function returns the actual variable name"""
    import itertools
    return [tpl[0] for tpl in itertools.ifilter(lambda x: var is x[1], globals().items())]


def debug(var):
    """
    This method prints the variable value in the following format:

        <VarName> = <Value>     (Angular Brackets are for clarity)
    """
    # print inspect.getfile(var)
    varName = getVarName(var)
    print(varName)


def log(var):
    pass

def variablename(var):
    import itertools
    return [tpl[0] for tpl in itertools.ifilter(lambda x: var is x[1], globals().items())]

if __name__ == '__main__':
    name = 'My name is Lokesh!'
    print(getVarName(name))
    debug(name)
    sys.exit(0)