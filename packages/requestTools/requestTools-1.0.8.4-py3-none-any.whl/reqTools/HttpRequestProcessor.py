import re
from abc import ABC, abstractmethod


import requests
import logging

from reqTools.enum.MethodEnum import MethodEnum
from util.FileUtil import FileUtil
from util.RequestHeadersUtil import RequestHeadersUtil
from util.RequestProcessUtil import RequestProcessUtil
from util.TextFormatUtil import TextFormatUtil

log = logging.getLogger(__name__)


class NormalHttpRequestProcessor(ABC):
    """
    A common base class for data processing, suitable for performing a single POST/GET request and
    returning the result as a JSON object. This class is an abstract base class that must be extended
    by a subclass. The subclass is required to implement the abstract methods setCookieFileName,
    setUrl, setMethod, and setStaticFormValues.
    """

    def __init__(self):
        """
        Constructor method that initializes a RequestHeaders object based on the cookie file.
        """
        self.requestHeaders = RequestHeadersUtil.loads(filePath=self.getCookieFile())

    @abstractmethod
    def setCookieFileName(self):
        """
        Abstract method to set the name of the cookie file. Subclasses need to provide an implementation.

        Returns:
            None
        """
        pass

    @abstractmethod
    def setUrl(self, dynamicParams=None):
        """
        Abstract method to set the request URL. Subclasses need to provide an implementation.

        Args:
            dynamicParams (dict, optional): A dictionary of key-value pairs for dynamic URL parameters.

        Returns:
            None
        """
        pass

    @abstractmethod
    def setMethod(self):
        """
        Abstract method to set the HTTP method for the request, such as POST or GET. For specifics,
        refer to the MethodEnum enumeration implementation. Subclasses need to provide an implementation.

        Returns:
            An instance of MethodEnum representing the HTTP method.
        """
        pass

    @abstractmethod
    def setStaticFormValues(self):
        """
        Abstract method to set the static request data that does not change. Subclasses need to provide an implementation.

        Returns:
            A dictionary containing the static request data to be submitted.
        """
        pass

    def getCookieFile(self):
        """
        Retrieves the full file filePath of the cookie file.

        Returns:
            str: The full filePath to the cookie file.
        """
        return FileUtil.getProjectRootPath()+'/cookiefile/'+self.setCookieFileName()

    def getHeaders(self):
        """
        Obtains the headers object stored in the requestHeaders.

        Returns:
            dict: The current headers of the request.
        """
        return self.requestHeaders.headers

    def getCookies(self):
        """
        Gets the cookies object from the requestHeaders.

        Returns:
            dict: The cookies to be sent with the request.
        """
        return self.requestHeaders.cookies

    def getUrl(self, dynamicParams=None):
        """
        Constructs and retrieves the request URL, potentially incorporating dynamic parameters.

        Args:
            dynamicParams (dict, optional): A key-value dictionary of dynamic parameters to be
            included in the URL. Defaults to None.

        Returns:
            str: The constructed URL to be used for the request.
        """
        return self.setUrl(dynamicParams=dynamicParams)

    def getMethod(self):
        """
        Retrieves the HTTP method to be used for the request.

        Returns:
            MethodEnum: The HTTP method, such as POST or GET, as defined by the MethodEnum.
        """
        return self.setMethod()

    def getFormValues(self, dynamicParams=None):
        """
        Constructs and retrieves the form values to be submitted with the request.
        Merges any static form values set by setStaticFormValues with dynamic parameters, if provided.

        Args:
            dynamicParams (dict, optional): A key-value dictionary of dynamic parameters to be
            included in the form data. Defaults to None.

        Returns:
            dict: The complete set of form values to be submitted with the request.
        """
        formValues = self.setStaticFormValues() if self.setStaticFormValues() is not None else {};

        # Merge dynamic request parameters if any are provided
        if dynamicParams is not None:
            formValues = {**formValues, **dynamicParams}

        return formValues

    def getFileName(self,response):
        """
        Extracts the file name from the Content-Disposition header of an HTTP response.

        This method parses the Content-Disposition header to find the 'filename' parameter,
        which indicates the file name of the attachment in the response. If the file name
        is found, it is returned. Otherwise, the method returns None.

        Parameters:
        - response (requests.Response): The response object from which to extract the file name.

        Returns:
        - str: The extracted file name if the 'filename' parameter is present.
        - None: If the 'filename' parameter is not found or the header is missing.

        Usage Example:
        response = requests.get('http://example.com/path/to/resource')
        file_name = getFileName(response)
        if file_name:
            print(f'File name: {file_name}')
        else:
            print('File name could not be extracted')

        Note:
        The method assumes that the Content-Disposition header follows the format:
        'attachment; filename="filename.ext"'
        If the header uses a different format, the method might not work as expected.
        """
        content_disposition = response.headers.get('Content-Disposition', '')
        filename_match = re.search(r'filename="([^"]+)"', content_disposition)

        if filename_match:
            file_name = filename_match.group(1)  # 提取括号中匹配到的内容
            return file_name
        else:
            return None

    def getResponse(self, dynamicParams=None):
        """
        Sends the request and returns the result of the execution.

        Args:
            dynamicParams (dict, optional): A dictionary of key-value pairs for dynamic request parameters. Defaults to None.

        Returns:
            The result of the request execution as a JSON object.
        """
        session = requests.session()

        try:
            method = self.getMethod()
            datas = self.getFormValues(dynamicParams)
            url = self.getUrl()
            response = RequestProcessUtil.requestExecute(method, session, url, datas, self.getHeaders(), self.getCookies())

            log.debug("reponse text:%s" , response.text)
            return TextFormatUtil.getDataFormatEnum(response.text).formatToJson(response.text)

        finally:
            session.close()

    def downLoadFile(self, filePath, fileName=None, dynamicParams=None):
        """
        Downloads a file from a specified URL and saves it to a given filePath on the local file system.

        This method initiates a session, makes an HTTP request to retrieve the file content,
        and writes the content to a local file. It attempts to use a provided file name or
        retrieve one from the response headers. If neither is available, raises an error.

        Parameters:
        - filePath (str): The local file system filePath where the file will be saved. Must include trailing slash.
        - fileName (str, optional): The name of the file to be saved. If not provided, the method will
          attempt to obtain it from the response headers.
        - dynamicParams (dict, optional): A dictionary of dynamic parameters that might be used to modify
          the request's form data.

        Returns:
        None: The file is written to the local file system, and the method does not return a value.

        Raises:
        - HTTPError: If the HTTP request fails for any reason.
        - IOError: If there is an issue writing the file to the local file system.

        Usage Example:
        downLoadFile('/local/filePath/to/save/', fileName='myFile.xlsx', dynamicParams={'param1': 'value1'})
        """
        session = requests.session()
        try:
            method = self.getMethod()
            datas = self.getFormValues(dynamicParams)
            url = self.getUrl()
            response = RequestProcessUtil.requestExecute(method, session, url, datas, self.getHeaders(),
                                                         self.getCookies())

            fileName = fileName if fileName is not None else self.getFileName(response)

            with open(filePath + fileName, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
        finally:
            session.close()

class SimpleHttpRequestProcessor(NormalHttpRequestProcessor):
    """
    A subclass of NormalHttpRequestProcessor that provides a simplified HTTP request processor.
    This class is designed to handle basic HTTP POST requests with minimal configuration.
    It must be extended by a subclass where the abstract method setCookieFileName is implemented.
    """
    @abstractmethod
    def setCookieFileName(self):
        """
        Abstract method to set the cookie file name. This method must be implemented by subclasses
        to specify the name of the cookie file they wish to use.
        """
        pass

    def setUrl(self, dynamicParams=None):
        """
        Sets the request URL. This method can be overridden by subclasses to provide the URL.
        If not overridden, it returns None by default.

        Args:
            dynamicParams (dict, optional): A dictionary of key-value pairs that can be used
            to construct the URL dynamically. Defaults to None.

        Returns:
            The URL as a string or None if not specified.
        """
        return None

    def setMethod(self):
        """
        Sets the HTTP method for the request. This default implementation returns None, which indicates that subclasses should override
        this method to specify the desired HTTP method such as GET, POST, PUT, DELETE, etc.

        Returns:
            None, indicating that the default implementation does not specify an HTTP method. Subclasses should return an appropriate
            instance of MethodEnum or another suitable value.
        """
        return None


    def setStaticFormValues(self):
        """
        Sets the static form data for the request. By default, this method returns None, indicating that there are no static form values
        and that subclasses should provide them if needed.

        Returns:
            None, indicating that the default implementation does not provide static form values. Subclasses should return a dictionary
            containing the form data to be sent with the request.
        """
        return None


class PageDataHttpRequestProcessor(NormalHttpRequestProcessor):
    """
     An abstract base class for fetching paginated data via HTTP requests, extending the NormalHttpRequestProcessor class.
     When using this class, you should define a subclass that inherits from it and implement the following abstract methods:
     setCookieFileName, setUrl, setMethod, setStaticFormValues, getTotal, getCurrentPageDatas, parseRowValues,
     and setCurrentPageNumberKey.
     """

    @abstractmethod
    def getTotal(self,pageJsonObj):
        """
        Abstract method to extract the total number of items from the paginated data based on the JSON object of the current page.

        Args:
            pageJsonObj (dict): The JSON object representing data for the current page.

        Returns:
            int: The total number of items in the paginated data.
        """
        pass

    @abstractmethod
    def getCurrentPageDatas(self, pageJsonObj):
        """
        Abstract method to parse the data for the current page from the JSON object.

        Args:
            pageJsonObj (dict): The JSON object representing data for the current page.

        Returns:
            list: A list of JSON objects representing the data for the current page.
        """
        pass

    @abstractmethod
    def setCurrentPageNumberKey(self):
        """
        Abstract method to define the key name for the current page number used in pagination requests,
        such as "currentPage" or "pageNumber".

        Returns:
            str: The key name to be used for the current page number in the request.
        """
        pass

    def parseRowValues(self, rowJsonObj):
        """
        Method to parse and extract necessary data from each row in the paginated data.

        Args:
            rowJsonObj (dict): The JSON object representing a single row of data.

        Returns:
            dict: The parsed row data as required.
        """
        return rowJsonObj

    def getResponse(self, dynamicParams=None):
        """
        Sends the request and returns all data across pages as a result.

        Args:
            dynamicParams (dict, optional): A dictionary of key-value pairs for dynamic request parameters. Defaults to None.

        Returns:
            list: A list of dictionaries representing all the row data across pages.
        """

        session = requests.session()
        dynamicParams = {} if dynamicParams is None else dynamicParams

        try:
            allDatas = []
            pageNmuber = self.getFormValues()[self.setCurrentPageNumberKey()]
            method = self.setMethod()

            while (1):
                dynamicParams[self.setCurrentPageNumberKey()] = pageNmuber

                datas = self.getFormValues(dynamicParams)
                url = self.getUrl(dynamicParams)

                response = RequestProcessUtil.requestExecute(method, session, url, datas, self.getHeaders(),
                                                             self.getCookies())
                log.debug("reponse text:%s",response.text)

                jsonObj = TextFormatUtil.getDataFormatEnum(response.text).formatToJson(response.text)
                if (len(allDatas) >= self.getTotal(pageJsonObj=jsonObj)):
                    break

                rows = self.getCurrentPageDatas(jsonObj)
                for index, row in enumerate(rows):
                    rowDict = self.parseRowValues(rowJsonObj=row)
                    log.debug("rowDict:%s", str(rowDict))
                    allDatas.append(rowDict)

                pageNmuber = pageNmuber+1
            return allDatas

        finally:
            session.close()