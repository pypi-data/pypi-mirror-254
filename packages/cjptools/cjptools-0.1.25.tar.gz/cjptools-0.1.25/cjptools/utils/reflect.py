import inspect


def parseFuncParams(func, args):
    args0 = {};
    if args is None:
        return args0;
    signature = inspect.signature(func)
    parameters = signature.parameters
    for param in parameters.values():
        if param.name in args:
            args0[param.name] = args[param.name]
    return args0;
