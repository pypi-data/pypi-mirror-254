import csv
import json
from io import StringIO

from reqTools.enum.DataFormatEnum import DataFormatEnum


class TextFormatUtil:

    # 获取数据格式
    @staticmethod
    def getDataFormatEnum(text_data):
        if(TextFormatUtil.is_valid_json(text_data)):
            return DataFormatEnum.JSON
        elif (TextFormatUtil.is_valid_csv(text_data)):
            return DataFormatEnum.CSV

        return DataFormatEnum.JSON

    # 判断是否是json格式
    @staticmethod
    def is_valid_json(text_data):
        try:
            # 尝试将字符串解析为JSON对象
            json_object = json.loads(text_data)
        except json.JSONDecodeError as e:
            # 解析过程中出现错误，说明不是有效的JSON格式
            return False
        except TypeError as e:
            # 输入的不是字符串或字节类型，如None
            return False
        # 如果没有抛出异常，则是有效的JSON格式
        return True


    # 是否是CSV格式
    @staticmethod
    def is_valid_csv(text_data, delimiter=',', quotechar='"'):
        try:
            # 使用 StringIO，这样csv模块就可以像操作文件一样操作字符串
            f = StringIO(text_data)

            # 创建一个CSV阅读器
            reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)

            # 尝试读取第一行以获取字段数量
            first_row = next(reader)
            num_fields = len(first_row)

            # 遍历剩余的行，检查字段数量是否一致
            for row in reader:
                if len(row) != num_fields:
                    return False  # 字段数量不一致，不是有效的CSV

            return True  # 所有行的字段数量一致，是有效的CSV
        except Exception as e:
            # 如果发生任何异常，则认为文本不是有效的CSV
            return False
        finally:
            # 关闭StringIO对象
            f.close()