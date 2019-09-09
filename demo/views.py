from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

def about(request):
    return HttpResponse("这是一个about页面")

def demo(request,year,mon,day):
    ls = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    res = 0
    if int(year) % 4 == 0 and int(year) % 100 != 0:
        for i in range(int(mon) - 1):
            res += ls[i]
        res += int(day)
    else:
        if int(mon) == 1:
            res = int(day)
        elif int(mon) == 2:
            res = int(ls[0]) + int(day)
        else:
            for i in range(int(mon) - 1):
                res += ls[i]
            res += int(day) - 1
    return HttpResponse('这是{}年{}月{}日，第{}天'.format(year,mon,day,res))

from django.template import Template,Context
def gethtml(request):
    html="""
    <html>
        <head></head>
        <body>
            <h1>{{num}}标签</h1>
            <a href='https://baike.so.com/doc/4557198-4767897.html' target='_blank'>
                <img src='http://wx4.sinaimg.cn/large/866ceb95ly1fkt6egkj84j20sg0g0acu.jpg' title='李钟硕' alt='图片消失了'>
            </a>
        </body>
    </html>
    
    """
    # 创建一个模板
    template_obj=Template(html)
    # 渲染模板
    dic={'num':'h'}
    content_obj=Context(dic)
    # 数据渲染
    res=template_obj.render(content_obj)
    # 返回结果
    return HttpResponse(res)

    # return HttpResponse(html)

# 最常用版本
from django.shortcuts import render
def indextmp(request):
    name='柯基'
    # 有三个参数，第一个参数要加上request
    return render(request,'indextmp.html',{'name':name})


from django.shortcuts import render_to_response
def abc(request):
    # 这个可以不用写request,只有两个参数，第二个是字典
    return render_to_response('abc.html')

# from django.template.loader import get_template
# def abc(request):
#     # 先获得一个模板，将网页传进来
#     template=get_template('abc.html')
#     dic={'name':'二哈'}
#     res=template.render(dic)
#     # 返回的httpresponse
#     return HttpResponse(res)

# def test(request):
#     name='Amy'
#     age=19
#     hobby=['sing','dance','read']
#     score={'math':90,'english':92,'chinese':94}
#     return render(request,'test.html',{'name':name,'age':age,'hobby':hobby,'score':score})

class A(object):
    def hello(self):
        return 'hello'

def test(request):
    name='Amy'
    age=19
    hobby=['sing','dance','read']
    score={'math':90,'english':92,'chinese':94}
    a=A()
    return render(request,'test.html',locals())

def statictest(request):
    params=[
        {'name':'图片1','url':'1.jpg'},
        {'name': '图片2', 'url':'2.jpg'},
        {'name': '图片3', 'url':'3.jpg'},
        {'name': '图片4', 'url':'4.jpg'},
    ]
    return render(request,'statictest.html',locals())

