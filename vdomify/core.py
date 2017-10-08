from vdom.helpers import div, pre


def vdomify(o):
    return pre(repr(o))
