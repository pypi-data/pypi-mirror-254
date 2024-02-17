import logging

log = logging.getLogger(__name__)

class RequestHeaders:
    """
    A class for managing HTTP request headers and cookies read from a file.

    This class provides methods to read headers and cookies from a file, dump updated headers and cookies back into the file, and update individual cookies and headers by key.

    Attributes:
        filePath (str): Path to the file containing the HTTP headers and cookies.
        cookies (dict): A dictionary of cookies loaded from the file.
        headers (dict): A dictionary of headers loaded from the file.

    Methods:
        dumpToFile(): Writes the current headers and cookies to the file.
        updateCookiesByKey(cookieKey, cookieValue): Updates the value of a cookie by its key.
        updateHeadersByKey(headerKey, headerValue): Updates the value of a header by its key.

    Usage:
        # Create a new RequestHeaders object with a given file path
        request_headers = RequestHeaders('/path/to/headers_and_cookies.txt')

        # Update a specific cookie
        request_headers.updateCookiesByKey('sessionid', 'new_session_value')

        # Update a specific header
        request_headers.updateHeadersByKey('User-Agent', 'new_user_agent_string')

        # Save changes back to the file
        request_headers.dumpToFile()
    """

    def __init__(self,filePath):
        """
        Initializes the RequestHeaders class with the path to the headers and cookies file.

        Parameters:
            filePath (str): The file path to read headers and cookies from.
        """
        self.filePath = filePath
        self.cookies = self.__private_loadCookies()
        self.headers = self.__private_loadHeaders()

    def dumpToFile(self):
        """
        Writes the current headers and cookies dictionaries to the specified file in a proper HTTP request format.
        """
        with open(self.filePath,'w') as fileObj:
            for i, (key, value) in enumerate(self.headers.items()):
                fileObj.write(key+":"+value+"\n")
            if len(self.cookies)>0:
                fileObj.write(self.__private_dumpCookies())

    def __private_loadCookies(self):
        """
        Reads the cookies from the file and loads them into a dictionary.

        Returns:
            dict: A dictionary of cookies.
        """
        cookies = {}
        with open(self.filePath, "r") as fileObj:
            for line in fileObj.readlines():
                line = line.strip('\n')
                if line.__contains__('Cookie'):
                    cookieKeyAndValues = line.replace('Cookie: ', '').replace('Cookie:', '').split("; ")
                    for cookieKeyAndValue in cookieKeyAndValues:
                        keyvalues = cookieKeyAndValue.split("=")
                        cookies[keyvalues[0]] = keyvalues[1]

        log.debug(cookies)
        return cookies

    def __private_loadHeaders(self):
        """
        Reads the headers from the file and loads them into a dictionary.

        Returns:
            dict: A dictionary of headers.
        """
        headers = {}
        with open(self.filePath, "r") as fileObj:
            for line in fileObj.readlines():
                line = line.strip('\n')
                if not line.__contains__('Cookie'):
                    cookieKeyAndValue = line.split(":")
                    headers[cookieKeyAndValue[0].strip()] = cookieKeyAndValue[1].strip()
        log.debug(headers)
        return headers

    def __private_dumpCookies(self):
        """
        Formats the cookies dictionary into a string suitable for HTTP request headers.

        Returns:
            str: A formatted string of cookies.
        """
        cookieStr = "Cookie:"
        for i, (key, value) in enumerate(self.cookies.items()):
            if i==(len(self.cookies)-1):
                cookieStr = cookieStr + key + "=" + value
            else:
                cookieStr = cookieStr + key + "=" + value + "; "
        return cookieStr

    def updateCookiesByKey(self,cookieKey,cookieValue):
        """
        Updates the value of a specific cookie in the cookies dictionary.

        Parameters:
            cookieKey (str): The key of the cookie to update.
            cookieValue (str): The new value for the cookie.
        """
        self.cookies[cookieKey] = cookieValue

    def updateHeadersByKey(self,headerKey,headerValue):
        """
        Updates the value of a specific header in the headers dictionary.

        Parameters:
            headerKey (str): The key of the header to update.
            headerValue (str): The new value for the header.
        """
        self.headers[headerKey] = headerValue