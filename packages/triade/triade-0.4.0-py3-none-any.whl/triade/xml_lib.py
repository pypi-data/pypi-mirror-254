import os
import io
import xml.dom
from xml.dom.minidom import parse as _parse

from triade.thesaurus import Thesaurus
import triade.errors as err


def check_node_lvl(node_lvl: int, strict=False):
    msg = "Invalid document. You either opened or closed one too many tags."
    if node_lvl not in [0, 1]:
        raise ValueError(msg)
    if node_lvl != 0 and strict:
        raise ValueError(msg)


def trim_xml(xmldoc: str):
    """Remove unwanted whitespace from a XML string."""
    node_lvl = 0
    index = -1
    buffers = []

    try:
        for char in xmldoc:
            index += 1

            if char == "<":
                node_lvl += 1
                check_node_lvl(node_lvl)
                buffers.append(io.StringIO())
                buffers[-1].write("<")
            elif char == ">":
                node_lvl -= 1
                check_node_lvl(node_lvl)
                buffers[-1].write(">")
                buffers.append(io.StringIO())
            else:
                buffers[-1].write(char)

        check_node_lvl(node_lvl, strict=True)

        result = "".join([buffer.getvalue().strip() for buffer in buffers])

        return result
    finally:
        for buffer in buffers:
            buffer.close()


def parse_xml(xml_document: str, parser=None, bufsize=None):
    """Parse an XML string into a DOM document node object."""
    return _parse(io.StringIO(trim_xml(xml_document)), parser, bufsize)


def document_to_dict(node):
    """Create an XML-parsable dictionary from a xml.dom node object."""
    if node.nodeType == node.DOCUMENT_NODE:
        try:
            return document_to_dict(node.documentElement)
        finally:
            node.unlink()
    elif node.nodeType == node.TEXT_NODE:
        return node.data.strip()

    node_dict = {"tagName": node.tagName}

    if node.hasAttributes():
        node_dict["attributes"] = {a.name: a.value for a in
                                   node.attributes.values()}

    if node.hasChildNodes():
        child_nodes = []
        for child_node in node.childNodes:
            if child_node.nodeType == child_node.TEXT_NODE:
                child_nodes.append(child_node.data.strip())

            elif child_node.nodeType == child_node.ELEMENT_NODE:
                child_nodes.append(document_to_dict(child_node))

        node_dict["childNodes"] = child_nodes

    return node_dict


class TriadeDocument:
    def __init__(self, data):
        data = Thesaurus(data)
        self._data = data
        tag_name = data.get(["tagName", "tag_name"])
        self._node = self._create_document(tag_name)

        self._root = TriadeElement(data, parent=self, document=self)

    def __str__(self):
        return "<?document %s ?>" % (self._node.documentElement.tagName)

    def __repr__(self):
        cls = type(self).__name__
        data = repr(self._data)
        return "%s(%s)" % (cls, data)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._node.unlink()
        return False

    @classmethod
    def fromxml(cls, xmldoc: str):
        return cls(document_to_dict(parse_xml(xmldoc)))

    @property
    def data(self):
        """The dictionary used to construct this document."""
        return self._data

    @property
    def node(self):
        """The XML DOM Document object associated with this object."""
        return self._node

    @property
    def root(self):
        """The root TriadeElement associated with this document."""
        return self._root

    @root.setter
    def root(self, element):
        self._root = element

    @property
    def parent(self):
        """None"""
        return None

    def create_element(self, tag_name):
        """Create and return a new instance of XML DOM Element"""
        return self._node.createElement(tag_name)

    def create_attribute(self, name, value):
        """Create and return a new instance of XML DOM Attr"""
        attr = self._node.createAttribute(name)
        attr.value = value
        return attr

    def create_text_node(self, text):
        """Create and return a new instance of XML DOM TextNode"""
        return self._node.createTextNode(text)

    def toxml(self, *args, **kwargs):
        return self._node.toxml(*args, **kwargs)

    def toprettyxml(self, *args, **kwargs):
        if "indent" not in kwargs:
            kwargs["indent"] = "  "

        return self._node.toprettyxml(*args, **kwargs)

    def unlink(self):
        self._node.unlink()

    def _create_document(self, name):
        impl = xml.dom.getDOMImplementation()
        return impl.createDocument(xml.dom.EMPTY_NAMESPACE, name, None)


class TriadeElement:
    def __init__(self, data, *, parent=None, document=None):
        self._validate(data)
        data = Thesaurus(data)
        self._data = data
        self._doc = self._get_document(document)
        self._parent = self._get_parent(parent)

        self._tag_name = data.get(["tagName", "tag_name"])
        for char in self._tag_name:
            if char.isspace():
                msg = "The tagName parameter cannot have any whitespace characters"
                raise err.TriadeNodeValueError(msg)

        child_nodes = data.get(["childNodes", "child_nodes"], [])
        if child_nodes is None:
            child_nodes = []

        self._children = TriadeNodeList(child_nodes, parent=self,
                                        document=self._doc)

        if isinstance(self._parent, TriadeDocument):
            self._node = self._parent.node.documentElement
        else:
            self._node = self._doc.create_element(self._tag_name)

        if document is not None:
            for child_node in self._children:
                self._node.appendChild(child_node.node)

        attributes = data.get("attributes", {})
        self._attrs = TriadeNamedNodeMap(attributes, element=self)

    def __str__(self):
        size = len(self)
        if size == 0:
            return "<?element %s ?>" % (self.tag_name)
        return '<?element %s childNodes="%d" ?>' % (self.tag_name, size)

    def __repr__(self):
        cls = type(self).__name__
        data = dict(self._data)
        return "%s(%s)" % (cls, repr(data))

    def __len__(self):
        try:
            return len(self._children)
        except AttributeError:
            return 0

    def __iter__(self):
        return iter(self._children)

    def __getitem__(self, key):
        if key in ["tagName", "tag_name"]:
            return self._tag_name
        elif key in ["childNodes", "child_nodes"]:
            return self._children
        elif key == "attributes":
            return self._attrs
        elif isinstance(key, str):
            cls = type(self).__name__
            msg = '"%s" key is not present in objects of type %s.' % (key, cls)
            raise TriadeNodeKeyError(msg)
        else:
            return self._children[key]

    def __setitem__(self, key, value):
        if key in ["tagName", "tag_name"]:
            msg = "Tag name reassignment is not allowed"
            raise err.TriadeForbiddenWriteError(msg)

    def __delitem__(self, key):
        pass

    @property
    def data(self):
        """The dictionary used to construct this element."""
        return self._data

    @property
    def node(self):
        """The XML DOM Element object associated with this object."""
        return self._node

    @property
    def parent(self):
        """This object's parent node."""
        return self._parent

    @property
    def document(self):
        """The document containing this element."""
        return self._doc

    @property
    def tagName(self):
        """The element's tag name."""
        return self._tag_name

    @tagName.setter
    def tagName(self, value):
        if not isinstance(value, str):
            raise err.TriadeNodeTypeError('"tagName" value must be a string.')
        self._tag_name = value

    @tagName.deleter
    def tagName(self):
        raise err.TriadeForbiddenDeleteError("Deleting tagName is not allowed.")

    tag_name = property(tagName.fget, tagName.fset, tagName.fdel)

    @property
    def childNodes(self):
        """The element's child nodes as a list."""
        return self._children

    @childNodes.setter
    def childNodes(self, _):
        msg = "Reassignment of child nodes list is not allowed."
        raise err.TriadeForbiddenWriteError(msg)

    @childNodes.deleter
    def childNodes(self):
        self._children = []

    child_nodes = property(childNodes.fget, childNodes.fset, childNodes.fdel)

    @property
    def attributes(self):
        """The element's attributes as a dictionary."""
        return self._attrs

    @attributes.setter
    def attributes(self, _):
        msg = "Reassignment of attributes list is not allowed"
        raise err.TriadeForbiddenWriteError(msg)

    @attributes.deleter
    def attributes(self):
        self._attrs = {}

    def append(self, obj, /):
        self._children.append(obj)

    def toxml(self, *args, **kwargs):
        return self._node.toxml(*args, **kwargs)

    def toprettyxml(self, *args, **kwargs):
        if "indent" not in kwargs:
            kwargs["indent"] = "  "

        return self._node.toprettyxml(*args, **kwargs)

    def _validate(self, data):
        if not isinstance(data, dict):
            raise err.TriadeNodeTypeError('"data" should be a dictionary.')

        if ["tagName", "tag_name"] not in Thesaurus(data):
            raise err.TriadeNodeValueError('"tagName" not found in "data".')

    def _get_document(self, document):
        if document is not None:
            return document

        document = TriadeDocument(self._data)
        document.root = self
        return document

    def _get_parent(self, parent):
        if parent is not None:
            return parent

        return self._doc


class TriadeNodeList:
    def __init__(self, data, *, parent=None, document=None):
        self._validate(data)
        self._data = data

        self._parent = parent
        self._document = document

        self._nodes = []
        for elem in data:
            if elem is None:
                continue
            if isinstance(elem, dict):
                child_node = TriadeElement(elem, parent=parent, document=document)
            elif isinstance(elem, (str, int, float)):
                child_node = TriadeTextNode(str(elem), parent=parent,
                                            document=document)

            self._nodes.append(child_node)

    def __len__(self):
        return len(self._nodes)

    def __iter__(self):
        return iter(self._nodes)

    def __getitem__(self, index):
        return self._nodes[index]

    @property
    def data(self):
        """The list of child nodes as dictionaries."""
        return self._data

    @property
    def parent(self):
        """This object's parent node."""
        return self._parent

    @property
    def document(self):
        """The document containing this element."""
        return self._document

    def append(self, obj, /):
        if not isinstance(obj, (dict, str)):
            msg = "The appended value should be a dict or str."
            raise err.TriadeNodeTypeError(msg)

        if isinstance(obj, dict):
            node = TriadeElement(obj, parent=self.parent, document=self.document)
        elif isinstance(obj, str):
            node = TriadeTextNode(obj, parent=self.parent, document=self.document)

        self._nodes.append(node)
        self.parent.node.appendChild(node.node)

    def _validate(self, data):
        if not isinstance(data, list):
            raise err.TriadeNodeTypeError("Input data should be a list.")

        for node in data:
            if node is None:
                continue
            if not isinstance(node, (dict, str, int, float)):
                msg = "Every value in the input list should be a dict, str, int or float."
                raise err.TriadeNodeValueError(msg)


class TriadeAttribute:
    def __init__(self, name, value, *, element=None):
        self._name = name
        self._value = value

        if name.count(":") > 1:
            msg = "Attribute name should contain at most one colon."
            raise err.TriadeNodeValueError(msg)

        self._element = element
        if element is not None:
            self._node = self._element.document.create_attribute(name, value)
            self.element.node.setAttribute(name, value)

    def __str__(self):
        return '<?attr %s="%s" ?>' % (self._name, self._value)

    def __repr__(self):
        cls = type(self).__name__
        return "%s(%s, %s)" % (cls, repr(self._name), repr(self._value))

    def __getitem__(self, key):
        if key not in ["name", "value"]:
            msg = "The key %s is not present in TriadeAttribute." % (key,)
            raise err.TriadeNodeKeyError(msg)

        if key == "name":
            return self._node.name
        elif key == "value":
            return self._node.value

    def __setitem__(self, key, value):
        if key not in ["name", "value"]:
            msg = 'The only keys allowed for TriadeAttribute are "name" and "value".'
            raise err.TriadeNodeKeyError(msg)

        if key == "name":
            self._node.name = value
        elif key == "value":
            self._node.value = value

    def __delitem__(self, key):
        raise err.TriadeForbiddenDeleteError("Deletion not allowed")

    @property
    def data(self):
        """A tuple containing the attribute's name and value."""
        return self._name, self._value

    @property
    def element(self):
        return self._element

    @property
    def document(self):
        try:
            return self._element.document
        except AttributeError:
            return None

    @property
    def node(self):
        return self._node

    @property
    def name(self):
        """The attribute's name."""
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
        try:
            self._node.name = new_name
        except AttributeError:
            pass

    @name.deleter
    def name(self):
        raise err.TriadeForbiddenDeleteError("Deletion not allowed")

    @property
    def value(self):
        """The attribute's value."""
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        try:
            self._node.value = new_value
        except AttributeError:
            pass

    @value.deleter
    def value(self):
        raise err.TriadeForbiddenDeleteError("Deletion not allowed")

    @property
    def node(self):
        """The XML DOM Attr object associated with this object."""
        try:
            return self._node
        except AttributeError:
            return None

    @property
    def localName(self):
        parts = self.name.split(":")
        return parts[1] if len(parts) > 1 else self.name

    @property
    def prefix(self):
        parts = self.name.split(":")
        return parts[0] if len(parts) > 1 else ""

    @property
    def namespaceURI(self):
        return self._node.namespaceURI

    nodeName = property(name.fget, name.fset, name.fdel)
    nodeValue = property(value.fget, value.fset, value.fdel)


class TriadeNamedNodeMap:
    def __init__(self, attributes, *, element=None):
        self._attrs = {}
        self._len = 0
        self._element = element

        if attributes is None:
            attributes = {}

        self._validate(attributes)

        for name, value in attributes.items():
            self._attrs[name] = TriadeAttribute(name, str(value),
                                                element=element)
            self._len += 1

    def __str__(self):
        values = self._attrs.values()

        if len(values) == 0:
            return "<?attributeList ?>"

        text = " ".join('%s="%s"' % (attr.name, attr.value) for attr in values)
        return "<?attributeList %s ?>" % (text)

    def __repr__(self):
        cls = type(self).__name__
        data = self.data
        if self._element is None:
            return "%s(%s)" % (cls, repr(data))

        element = self._element
        return "%s(%s, element=%s)" %(cls, repr(data), repr(element))

    def __iter__(self):
        return iter(self._attrs.values())

    def __contains__(self, name):
        return name in self._attrs

    def __getitem__(self, name):
        return self._attrs[name]

    def __setitem__(self, name, value):
        if name in self._attrs:
            self._change_value(name, value)
        else:
            self._add_value(name, value)

    def __delitem__(self, name):
        del self._attrs[name]
        self._len -= 1

    def __len__(self):
        return self._len

    @property
    def data(self):
        return {a.name: a.value for a in self.values()}

    def get(self, name, default=None):
        return self._attrs.get(name, default)

    def item(self, index):
        try:
            return list(self._attrs.values())[index]
        except IndexError:
            return None

    def items(self):
        return [(a.name, a.value) for a in self._attrs.values()]

    def keys(self):
        return self._attrs.keys()

    def values(self):
        return self._attrs.values()

    def _add_value(self, name, value):
        if isinstance(value, (list, tuple)):
            new_name  = value[0]
            new_value = value[1]
        elif isinstance(value, dict):
            new_name  = value["name"]
            new_value = value["value"]
        elif isinstance(value, str):
            new_name  = name
            new_value = value
        else:
            msg = ("You can't assign a value of type %s to the \"%s\" attribute" %
                   (type(value).__name__, name))
            raise err.TriadeNodeTypeError(msg)

        self._attrs[name] = TriadeAttribute(new_name, new_value)
        self._len += 1

    def _change_value(self, name, value):
        if isinstance(value, (list, tuple)):
            new_name  = value[0]
            new_value = value[1]

            self._attrs[name].name  = new_name
            self._attrs[name].value = new_value

            self._attrs[new_name] = self._attrs[name]
            del self._attrs[name]
        elif isinstance(value, dict):
            new_name  = value["name"]
            new_value = value["value"]

            self._attrs[name].name  = new_name
            self._attrs[name].value = new_value

            self._attrs[new_name] = self._attrs[name]
            del self._attrs[name]
        elif isinstance(value, str):
            self._attrs[name].value = value
        else:
            msg = ("You can't assign a value of type %s to the \"%s\" key." %
                   (type(value).__name__, name))
            raise err.TriadeNodeTypeError(msg)

    def _validate(self, attributes):
        if not isinstance(attributes, dict):
            msg = "Input for TriadeNamedNodeMap should be a dictionary."
            raise TriadeNodeTypeError(msg)


class TriadeTextNode:
    def __init__(self, data, *, parent=None, document=None):
        self._data = data
        self._parent = parent
        self._document = document
        self._node = self._document.create_text_node(data)

    def __str__(self):
        return self._node.data

    def __repr__(self):
        cls = type(self).__name__
        return "%s(%s)" % (cls, repr(self._node.data))

    @property
    def node(self):
        """The XML DOM TextNode object associated with this object."""
        return self._node

    @property
    def parent(self):
        """This object's parent node."""
        return self._parent

    @property
    def document(self):
        """The document containing this element."""
        return self._document

    @property
    def data(self):
        """The content of the text node as a string."""
        return self._data

    @data.setter
    def data(self, value):
        self._node.data = value

    @data.deleter
    def data(self):
        raise err.TriadeForbiddenDeleteError("Deletion not allowed")

    def toxml(self, *args, **kwargs):
        return self._node.toxml(*args, **kwargs)

    def toprettyxml(self, *args, **kwargs):
        return self._node.toprettyxml(*args, **kwargs)
