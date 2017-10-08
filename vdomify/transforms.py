from vdom import h
from vdom.helpers import div, pre

from xml.dom import minidom


def _kabob_to_camel(s):
    parts = s.split('-')
    return parts[0] + "".join(map(lambda x: x[0].upper() + x[1:], parts[1:]))


def _style_string_to_dict(s):
    return {
        _kabob_to_camel(a[0]): a[1]
        for a in list(map(lambda x: x.strip().split(':'), s.split(';')))
        if len(a) is 2
    }


def _minidom_node_to_vdom(node):
    if (node.nodeType is node.TEXT_NODE):
        return node.data.strip()
    if (node.nodeType is node.ELEMENT_NODE):
        if (node.tagName is 'title'):
            return None

        attributes = {str(k): str(v) for (k, v) in node.attributes.items()}
        children = list(
            filter(lambda x: x is not "" and x is not None,
                   map(_minidom_node_to_vdom,
                       node.childNodes))) if node.hasChildNodes() else None

        if ('style' in attributes):
            attributes['style'] = _style_string_to_dict(attributes['style'])
        # TODO: Provide a normalizer from standard attribute names to JS / React ready names
        if ('xlink:href' in attributes):
            attributes['xlinkHref'] = attributes['xlink:href']
            del attributes['xlink:href']

        return {
            'tagName': node.tagName,
            'children': children,
            'attributes': attributes
        }


def Plain(data):
    return pre(data)


def _badHTML(data):
    # TODO: use xml.dom.minidom as dangerouslySetInnerHTML should be blocklisted in frontend
    return div(dangerouslySetInnerHTML={'__html': data})


def HTML(data):
    # TODO: This likely needs to catch parsing errors and disallow certain things...
    doc = minidom.parseString(data)
    node = doc.childNodes[0]
    v = _minidom_node_to_vdom(node)

    # make the top level a proper vdom object to allow simple display, while
    # we keep the precomputed dicts
    return h(v['tagName'], children=v['children'], attributes=v['attributes'])


def VDOM(data):
    # noop
    return data
