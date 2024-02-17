import logging

from reqTools.domain.RequestHeaders import RequestHeaders

log = logging.getLogger(__name__)

class RequestHeadersUtil:

    @staticmethod
    def loads(filePath):
        return RequestHeaders(filePath=filePath)

    @staticmethod
    def dumps(requestHeaders):
        return requestHeaders.dumpToFile();
