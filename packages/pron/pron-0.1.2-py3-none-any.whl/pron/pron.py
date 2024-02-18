import ast
import pprint


def dump(obj, fp, **kwargs):
    fp.write(dumps(obj, **kwargs))


def dumps(obj, indent=None, suppress=[]):
    """
    Return pretty formatted string representation of object.
    """
    if indent is None:
        return repr(obj)
    def __format_string(obj, indent, count):
        if isinstance(obj, dict) and dict not in suppress:
            return \
                '{' + '\n' + \
                ',\n'.join(f'{indent*(count+1)}{repr(k)}: {__format_string(v, indent, count+1)}' for k,v in obj.items()) + '\n' + \
                indent*count + '}'
        elif isinstance(obj, list) and list not in suppress:
            return \
                '[' + '\n' + \
                ',\n'.join(f'{indent*(count+1)}{__format_string(v, indent, count+1)}' for v in obj) + '\n' + \
                indent*count + ']'
        elif isinstance(obj, tuple) and tuple not in suppress:
            return \
                '(' + '\n' + \
                '\n'.join(f'{indent*(count+1)}{__format_string(v, indent, count+1)},' for v in obj) + '\n' + \
                indent*count + ')'
        else:
            return repr(obj)
        
    return __format_string(obj, ' '*indent, 0)


def load(fp):
    """
    Load object from file handle
    """
    return loads(fp.read())


def loads(string):
    """
    Load object from string representation.
    """
    return ast.literal_eval(string)
