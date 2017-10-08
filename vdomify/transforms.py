from vdom.helpers import div, pre


def Plain(data):
    return pre(data)


def HTML(data):
    # TODO: use xml.dom.minidom as dangerouslySetInnerHTML should be blocklisted in frontends
    return div(dangerouslySetInnerHTML={'__html': data})

def VDOM(data):
    # noop
    return data
