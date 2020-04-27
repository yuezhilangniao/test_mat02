from django.shortcuts import render
from django.shortcuts import render

from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.http import HttpResponse
import base64
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
import matplotlib
import io
import random

import numpy as np
import pandas as pd

# Create your views here.
import time
import asyncio

import datetime
from .models import ManInfo,PartInfo

from celerytapp.models import User,FreeTime
from threading import Timer
from django.views.generic import View



def demo(request):
    #mans = ManInfo.objects.filter(id=1)
    mans = ManInfo.objects.filter(id=1)
    var = 10

    context = {
        #'lf':lf,
        'mans':mans,
        'var':var,
        'a':'white'
    }
    return render(request,'demo.html',context)

def green(id):

    mans = ManInfo.objects.filter(id=id)
    for m1 in mans:
        m1.isDelete = False
        print(m1.isDelete)
        m1.save()


def demo1(request,id):

    mans = ManInfo.objects.filter(id=id)
    for m1 in mans:
        m1.isDelete = True
        print(m1.isDelete)
        m1.save()

    print('------------------')
    print(id)
    t = Timer(1800, green,(id))
    t.daemon = True
    t.start()
    print('-----end-----')

    return render(request,'index1.html')






class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    # def get(self, request):
    #     '''显示登录页面'''
    #     # 判断是否记住了用户名
    #     if 'username' in request.COOKIES:
    #         username = request.COOKIES.get('username')
    #         checked = 'checked'
    #     else:
    #         username = ''
    #         checked = ''
    #
    #     # 使用模板
    #     return render(request, 'login.html', {'username': username, 'checked': checked})

    def post(self, request):
        '''登录校验'''
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 校验数据
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})

        # 业务处理:登录校验
        user = authenticate(username='admin', password='admin')
        if user is not None:
            # 用户名密码正确
            if user.is_active:
                # 用户已激活
                # 记录用户的登录状态
                login(request, user)

                # 获取登录后所要跳转到的地址
                # 默认跳转到首页
                next_url = request.GET.get('next', reverse('index'))

                # 跳转到next_url
                response = redirect(next_url)  # HttpResponseRedirect

                # 判断是否需要记住用户名
                remember = request.POST.get('remember')

                if remember == 'on':
                    # 记住用户名
                    response.set_cookie('username', username, max_age=7 * 24 * 3600)
                else:
                    response.delete_cookie('username')

                # 返回response
                return response
            else:
                # 用户未激活
                return render(request, 'login.html', {'errmsg': '账户未激活'})
        else:
            # 用户名或密码错误
            return render(request, 'login.html', {'errmsg': '用户名或密码错误'})


# /user/logout
class LogoutView(View):
    '''退出登录'''
    def get(self, request):
        '''退出登录'''
        # 清除用户的session信息
        logout(request)

        # 跳转到首页
        return redirect(reverse('index'))


class UserCenterView(View):
    pass





from celerytapp.models import User,FreeTime



def func():
    mans = ManInfo.objects.filter(id=1)
    for m1 in mans:
        m1.isDelete = False
        m2 = m1.isDelete
        m1.save()
    #return m2



# def index(request):
#     return render(request, 'index1.html')
def doc(reqeust):
    a = ManInfo.objects.all()

    list1 = [b.yeji for b in a]
    total = 0.00
    ele = 0

    #list1 = [11, 5, 17, 18, 23]

    while (ele < len(list1)):
        total = total + list1[ele]
        ele += 1
    #total = round(total,3)
    total = ("%.2f" % total)
    context = {'a': a,'list1':list1,'total':total}
    return render(reqeust, 'doc.html',context)


def index3(reqeust):

    return render(reqeust, 'index3.html')

def index2(reqeust):
    import numpy as np
    import matplotlib.pyplot as plt

    # t = np.arange(0, 88, 1)
    # plt.plot(t, t, 'r', t, t ** 2, 'b')
    # label = ['t', 't**2']
    # plt.legend(label, loc='upper left')
    # plt.savefig('static/pic/test3.png')
    # #plt.show()
    # plt.clf()
    # plt.close()
    #设置matplotlib正常显示中文和负号
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    # 随机生成（10000,）服从正态分布的数据
    data = np.random.randn(10000)
    """
    绘制直方图
    data:必选参数，绘图数据
    bins:直方图的长条形数目，可选项，默认为10
    normed:是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率。
    facecolor:长条形的颜色
    edgecolor:长条形边框的颜色
    alpha:透明度
    """

    plt.hist(data, bins=40, facecolor="blue", edgecolor="black", alpha=0.9)
    # 显示横轴标签
    plt.xlabel("2020年月度业绩")
    # 显示纵轴标签
    plt.ylabel("业绩/月份")
    # 显示图标题
    plt.title("2020年月度业绩直方图")
    plt.savefig('static/pic/test4.png')
    plt.clf()
    plt.close()
    return render(reqeust, 'index2.html')



def index(request):
    import matplotlib.pyplot as plt
    import matplotlib
    # 设置中文字体和负号正常显示
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False

    label_list = ['2014', '2015', '2016', '2017']  # 横坐标刻度显示值
    num_list1 = [20, 30, 15, 35]  # 纵坐标值1
    num_list2 = [15, 30, 40, 20]  # 纵坐标值2
    x = range(len(num_list1))
    """
    绘制条形图
    left:长条形中点横坐标
    height:长条形高度
    width:长条形宽度，默认值0.8
    label:为后面设置legend准备
    """
    rects1 = plt.bar(x=x, height=num_list1, width=0.4, alpha=0.8, color='red', label="一部门")
    rects2 = plt.bar(x=[i + 0.4 for i in x], height=num_list2, width=0.4, color='green', label="二部门")
    plt.ylim(0, 50)  # y轴取值范围
    plt.ylabel("业绩/千万")
    """
    设置x轴刻度显示值
    参数一：中点坐标
    参数二：显示值
    """
    plt.xticks([index + 0.2 for index in x], label_list)
    plt.xlabel("年份")
    plt.title("百卓网络")
    plt.legend()  # 设置题注
    # 编辑文本
    # for rect in rects1:
    #     height = rect.get_height()
    #     plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
    # for rect in rects2:
    #     height = rect.get_height()
    #     plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
    # plt.show()








    f = matplotlib.figure.Figure()

    # Code that sets up figure goes here; in the question, that's ...
    FigureCanvasAgg(f)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(f)
    plt.clf()
    #plt.close()
    image = base64.encodebytes(buf.getvalue()).decode()
    # plt.show()

    a = ManInfo.objects.all()

    list1 = [b.yeji for b in a]
    total = 0.00
    ele = 0

    # list1 = [11, 5, 17, 18, 23]

    while (ele < len(list1)):
        total = total + list1[ele]
        ele += 1
    # total = round(total,3)
    total = ("%.2f" % total)

    #取合同的 list 和综合
    list2 = [c.hetong for c in a]
    total2 = 0
    ele2 = 0

    # list1 = [11, 5, 17, 18, 23]
    print(list2)
    while (ele2 < len(list2)):
        total2 = total2 + list2[ele2]
        ele2 += 1
    # total = round(total,3)
    #total2 = ("%.2f" % total2)
    total2 = int(total2)
    context = {'a': a, 'list1': list1, 'total': total,'total2':total2,'image':image}
    return render(request, 'index1.html', context)

    #return render(request, 'index1.html', {'image': image})
