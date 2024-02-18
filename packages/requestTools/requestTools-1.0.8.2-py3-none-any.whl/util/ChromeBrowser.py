import base64

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


class BrowserUtil:
    """
    A utility class to interact with a web browser using Selenium for tasks such as rendering HTML content to PDF.

    This class provides static methods that leverage the Selenium WebDriver to perform browser automation tasks.
    It currently includes the `blobToPdf` method, which renders HTML content to a PDF file using a headless Chrome browser.

    Usage:
    To use the `blobToPdf` method, ensure you have the required dependencies installed and a valid filePath to the ChromeDriver executable.

    Example:
    BrowserUtil.blobToPdf("<html><body><h1>Sample PDF</h1></body></html>", "sample_pdf", "/filePath/to/chromedriver")

    Note:
    This class is designed to be used with a headless Chrome browser and requires the Selenium package and ChromeDriver to be installed and configured properly.
    """
    @staticmethod
    def blobToPdf(htmlContent, pdfName, chromedriverPath=None,optionsArgument=None):
        """
        Renders the provided HTML content in a headless Chrome browser and saves it as a PDF file.

        This static method utilizes a headless Chrome browser to render the provided HTML content and
        then uses the browser's capability to save the rendered page as a PDF file. The saved PDF file
        will have the specified name and can include a full file save filePath. The method optionally
        accepts additional Chrome options to customize the behavior of the browser instance.

        Parameters:
        - htmlContent (str): The HTML content to be rendered into a PDF. This should be a valid HTML string.
        - pdfName (str): The desired name of the saved PDF file. Can include a directory filePath if needed.
        - chromedriverPath (str): The file filePath to the ChromeDriver executable.
        - optionsArgument (list, optional): A list of strings that are additional command-line arguments
          for Chrome options. For example: ['--disable-gpu', '--no-sandbox'].

        Returns:
        None. The PDF is saved to the location specified by `pdfName`.

        Usage:
        blobToPdf("<html><body><h1>Hello, PDF!</h1></body></html>", "output", "/filePath/to/chromedriver", ["--disable-gpu"])

        Note:
        The method does not return any value or enum instance. Ensure that proper error handling is in place
        to catch any exceptions that may occur during the PDF conversion process.

        Requires:
        - selenium package installed and properly configured.
        - ChromeDriver compatible with the installed version of the Chrome browser.
        - Chrome browser installed on the system.
        """

        # 指定ChromeDriver的路径
        service = Service(chromedriverPath) if chromedriverPath is not None else Service()

        # 设置浏览器选项
        options = webdriver.ChromeOptions()
        if(optionsArgument is not None):
            for argument in optionsArgument:
                options.add_argument(argument)

        # 创建浏览器实例
        browser = webdriver.Chrome(service=service, options=options)

        # 浏览器访问空白页面
        browser.get("about:blank")

        # 使用浏览器执行JavaScript来设置页面内容
        browser.execute_script(f"document.write(`{htmlContent}`)")

        result = browser.execute_cdp_cmd("Page.printToPDF", {
            "landscape": False,  # 是否横向打印
            "printBackground": True,  # 是否打印背景
            "displayHeaderFooter": False,  # 是否显示页眉页脚
        })

        # 获取 PDF 文件的内容（base64 编码）
        pdf_content = result['data']

        # 对编码后的内容进行解码得到二进制数据
        pdf_content = base64.b64decode(pdf_content)

        # 将 PDF 内容保存到文件
        with open(pdfName + ".pdf", "wb") as f:
            f.write(pdf_content)

        # 退出浏览器
        browser.quit()