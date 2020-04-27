#!/usr/bin/env python
# encoding: utf-8
# 日期和星期的转换  Zeller公式
import datetime


class cl:
    date_star = {'1': '星期一', '2': '星期二', '3': '星期三', '4': '星期四', '5': '星期五', '6': '星期六', '0': '星期日', }

    def caile(self):
        date = datetime.datetime.now()
        year = date.year
        month = date.month
        day = date.day
        # year,month,day = args
        month = int(month)
        day = int(day)
        year_one, year_two = int(str(year)[:2]), int(str(year)[2:])
        if month == 1 or month == 2:
            return (year_two - 1 + (year_two - 1) // 4 + year_one // 4 - 2 * year_one + 26 * (
            month + 12 + 1) // 10 + day - 1) % 7

        return (year_two + year_two // 4 + year_one // 4 - 2 * year_one + 26 * (month + 1) // 10 + day - 1) % 7


if __name__ == "__main__":
    # date = raw_input('输入年份 月份 天数，空格分隔>>>>:' )
    

    # year,month,day = date.split(' ')
    c = cl()
    a = c.caile()
    print(a)
    # print "%s\n"%date,date_star['%s'%caile(year,month,day)]
