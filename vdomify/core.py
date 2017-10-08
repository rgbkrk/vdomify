from IPython.core.formatters import DisplayFormatter

from .transforms import Plain

_default_display_order = [
    'application/vdom.v1+json',
    # TODO: Bring in minidom parsing logic
    # 'text/html',
    'text/plain'
]

_default_transforms = {
    'text/plain': Plain
}

def _acquire_formatter():
    try:
        # If the user is in ipython, get their configured display_formatter
        ip = get_ipython()  # NOQA
        return ip.display_formatter
    except NameError:
        # otherwise use the default
        return DisplayFormatter()

def _get_richest(obj, formatter, display_order):
    (data, metadata) = formatter.format(obj)
    bundle = data

    supported_types = set(data.keys()).intersection(display_order)

    for mimetype in display_order:
        if mimetype in supported_types:
            yield { "type": mimetype, "payload": bundle[mimetype] }
            return

    # should not get here, we'll do a default 'text/plain' using repr for now...
    yield { "type": 'text/plain', "payload": repr(obj)}

def vdomify(o, display_order=None, transforms=None):
    formatter = _acquire_formatter()

    if(display_order is None):
        display_order = _default_display_order

    if(transforms is None):
        transforms = _default_transforms

    richest = next(_get_richest(o, formatter, display_order=display_order))

    return transforms[richest['type']](richest['payload'])
