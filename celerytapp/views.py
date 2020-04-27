from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from .models import User,FreeTime
import datetime
from threading import Timer
from utils.caile import cl
def celery(request):

    c = cl()
    w = c.caile()

    user = User.objects.all()
    alltime = FreeTime.objects.filter(fhour=datetime.datetime.now().hour).filter(fweek=w)

    for u in user:
        try:
            # get拿不到数据会报错 所以使用try
            t = alltime.get(who_id=u.id).fstate
            #做判断 默认7×24里面除了1就是4
            if t > u.status:
                u.status = t
                u.save()
        except:
            print('meiyou fstate')

    context = {
        'users':user,
        'alltime':alltime
    }
    return render(request,'celery.html',context)


def green(id):

    mans = User.objects.filter(id=id)
    for m1 in mans:
        m1.status = 1
        print(m1.status)
        m1.save()


def red(request,id):

    mans = User.objects.filter(id=id)
    for m1 in mans:
        m1.status = 2
        print(m1.status)
        m1.save()

    print('------------------')
    print(id)
    # 8是时间 green是 异步线程函数  id传参
    t = Timer(8, green,(id))
    t.daemon = True
    t.start()
    print('-----end-----')

    # index的url 配置了name=‘index’属性  重定向依稀啊到首页
    return redirect(reverse('index'))
    #return render(request,'/index1/')



'''celery '''










#coding:utf-8
# from celery.task.schedules import crontab
# from celery.decorators import periodic_task
#
# @periodic_task(run_every=crontab())
# def some_task():
#     print('periodic task test!!!!!')
#     time.sleep(5)
#     print('success')
#     return True