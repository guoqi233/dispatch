from twisted.web import xmlrpc, server
from twisted.application import service
from twisted.internet import reactor

from aps.function import add_job, remove_job


class AddHandler(object):
    def __call__(self, *args, **kwargs):
        add_job(*args, **kwargs)
        return True


class RemoveHandler(object):
    def __call__(self, *args, **kwargs):
        remove_job(*args, **kwargs)
        return True


class DispatchProtocol(xmlrpc.XMLRPC):
    def __init__(self):
        xmlrpc.XMLRPC.__init__(self)

        self._addHandler = AddHandler()
        self._removeHandler = RemoveHandler()
        self._procedureToCallable = {
            "add": self._addHandler,
            "remove": self._removeHandler,
        }

    def lookupProcedure(self, procedurePath):
        try:
            return self._procedureToCallable.get(procedurePath)
        except KeyError as e:
            raise xmlrpc.NoSuchFunction(self.NOT_FOUND, "procedure {} not found".format(procedurePath))

    def listProcedures(self):
        return self._procedureToCallable.keys()


class DispatchService(service.Service):
    def __init__(self, port):
        service.Service.__init__(self)
        self.factory = server.Site(DispatchProtocol(), timeout=10)
        self._port = None
        self.port = port

    def startService(self):
        self._port = reactor.listenTCP(self.port, self.factory)

    def stopService(self):
        return self._port.stopListening()
