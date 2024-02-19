class TriadeXMLException(Exception): pass


class TriadeNodeTypeError(TriadeXMLException, TypeError): pass


class TriadeNodeValueError(TriadeXMLException, ValueError): pass


class TriadeNodeKeyError(TriadeXMLException, KeyError): pass


class TriadeForbiddenChangeError(TriadeXMLException, TypeError): pass


class TriadeForbiddenWriteError(TriadeForbiddenChangeError): pass


class TriadeForbiddenDeleteError(TriadeForbiddenChangeError): pass
