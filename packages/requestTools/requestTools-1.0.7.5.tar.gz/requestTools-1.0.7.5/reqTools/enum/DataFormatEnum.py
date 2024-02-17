# -*- coding:utf-8 -*-
import logging
from enum import Enum
import csv
import json
from io import StringIO

log = logging.getLogger(__name__)

class DataFormatEnum(Enum):
    """数据格式枚举类
    """

    CSV = 'CSV'

    JSON = 'JSON'

    def __init__(self, formatName):
        self.formatName = formatName


    def formatToJson(self,text_data):

        if self == DataFormatEnum.CSV:
            log.debug("text_data:%s",text_data)
            text_data = text_data.replace("\\n", "\n")
            csv_file_like_object = StringIO(text_data)
            # 使用csv模块读取数据
            csv_reader = csv.DictReader(csv_file_like_object)
            # 转换CSV读取器对象到列表中的字典
            rows = list(csv_reader)
            return rows

        elif self == DataFormatEnum.JSON:
            return json.loads(text_data)
        else:
            return json.loads(text_data)

    @staticmethod
    def getEnum(formatName):
        """
        根据枚举字符变量，找到对应枚举实例
        :param text: 数据文本
        :return: 返回对应枚举实例
        """
        for name, dataFormatEnum in DataFormatEnum.__members__.items():
            if dataFormatEnum.formatName == formatName:
                return dataFormatEnum
