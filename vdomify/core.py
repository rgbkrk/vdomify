from IPython.core.formatters import DisplayFormatter

from .transforms import Plain, HTML, VDOM

_default_display_order = [
    'application/vdom.v1+json',
    # TODO: Bring in minidom parsing logic
    'text/html',
    'text/plain'
]

_default_transforms = {
    'text/plain': Plain,
    'text/html': HTML,
    'application/vdom.v1+json': VDOM
}


def _acquire_formatter():
    try:
        # If the user is in ipython, get their configured display_formatter
        ip = get_ipython()  # NOQA
        return ip.display_formatter
    except NameError:
        # otherwise use the default
        return DisplayFormatter()


def _get_richest(obj, formatter, display_order, transforms):
    # TODO: Rely on disp here?
    (data, metadata) = formatter.format(obj)
    bundle = data

    supported_types = set(data.keys()).intersection(display_order)

    for mimetype in display_order:
        if mimetype in supported_types and mimetype in transforms:
            yield transforms[mimetype](bundle[mimetype])

    # We shouldn't get here, however vdom allows `null` entries, so we'll return
    # None explicitly
    return None


def vdomify(o, display_order=None, transforms=None):
    formatter = _acquire_formatter()

    if (display_order is None):
        display_order = _default_display_order

    if (transforms is None):
        transforms = _default_transforms

    return next(
        _get_richest(
            o, formatter, display_order=display_order, transforms=transforms))
