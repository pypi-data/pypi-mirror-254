from datetime import datetime, time
from zoneinfo import ZoneInfo
import time

import chinese_calendar as cc
from datetime import timedelta


class DateUtil:
    def getNow_startOfDay():
        """
        获取当前日期的开始时刻（00:00:00.000000）。

        这是一个静态方法，不依赖于类的实例。它使用`datetime.now()`来获取当前日期的
        datetime对象，并将时间设置为一天的开始（午夜）。这是通过结合当前日期和
        时间最小值`datetime.min.time()`来实现的。

        Returns:
            datetime: 当前日期的开始时刻的datetime对象。
        """
        now = datetime.now()
        start_of_day = datetime.combine(now.date(), datetime.min.time())
        return start_of_day

    @staticmethod
    def getNow_endOfDay():
        """
        获取当前日期的最后一刻时间（23:59:59.999999）。

        此函数不接受任何参数。它利用`datetime.now()`函数来获取当前的日期和时间信息，
        然后使用`datetime.combine`方法结合当前日期和一天中的最大时间值（即23:59:59.999999）
        来创建一个新的`datetime`对象，表示当天结束前的最后一刻。

        Returns:
            datetime: 当前日期的最后一刻的datetime对象。
        """
        now = datetime.now()
        end_of_day = datetime.combine(now.date(), datetime.max.time())
        return end_of_day

    @staticmethod
    def dateFromat_UTC_8T(dateTime):
        """
        将给定的datetime对象转换为UTC+8时区(亚洲/上海)的时间，并格式化为ISO 8601格式的字符串。

        此函数接受一个datetime对象作为参数，并将其转换为'Asia/Shanghai'时区的时间。
        然后，函数会计算本地时区与UTC的偏移量，将偏移量包含在格式化的字符串中，以确保输出的时间字符串
        包含正确的时区信息。最终返回的字符串格式为'YYYY-MM-DDTHH:MM:SS+0800'，假定时区为UTC+8。

        注意：此方法假设计算机的本地时间设置正确，并且考虑了夏令时(DST)的影响。

        Parameters:
            dateTime (datetime): 需要转换时区并格式化的datetime对象。

        Returns:
            str: 转换为UTC+8时区并格式化后的时间字符串，格式为'YYYY-MM-DDTHH:MM:SS+0800'。
        """
        utc_8_tz = ZoneInfo('Asia/Shanghai')
        utc_8_time = dateTime.astimezone(utc_8_tz)
        # 获取本地时区的偏移量，转化为小时
        offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
        offset_hours = -offset / 3600

        # 格式化为符合ISO 8601格式的字符串（假定时区为+0800）
        formatted_time = utc_8_time.strftime(f'%Y-%m-%dT%H:%M:%S{int(offset_hours):+03d}00')

        return formatted_time

class DateDistance:

    @staticmethod
    def getHours_no_chinese_holiday(startDatetime,endDatetime):
        """
        根据中国节假日，去除节假日时间，获取两个时间段的小时数

        :param startDatetime: 开始时间
        :param endDatetime: 结束时间

        :return: 返回小时数，精确到小数点2位
        """
        total_hours = 0

        if startDatetime.date() == endDatetime.date():
            if (cc.is_holiday(startDatetime)):
                return 0
            else:
                total_hours = (endDatetime - startDatetime).total_seconds() / 3600
                return round(total_hours, 2)

        current_datetime = datetime.combine(startDatetime.date(), datetime.min.time()) + timedelta(days=1)

        if not cc.is_holiday(startDatetime):
            total_hours = (current_datetime - startDatetime).total_seconds() / 3600

        if not cc.is_holiday(endDatetime):
            total_hours += (endDatetime - datetime.combine(endDatetime.date(), datetime.min.time()) + timedelta(
                days=0)).total_seconds() / 3600

        while current_datetime < datetime.combine(endDatetime.date(), datetime.min.time()) + timedelta(days=0):
            if not cc.is_holiday(current_datetime.date()):
                # 如果当前日期不是节假日，则算作工作时间
                total_hours += 24

            # 移动到下一天
            current_datetime = datetime.combine(current_datetime.date(), datetime.min.time()) + timedelta(days=1)

        return round(total_hours, 2)