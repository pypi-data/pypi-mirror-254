from datetime import datetime
import chinese_calendar as cc
from datetime import timedelta

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