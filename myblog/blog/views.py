# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from models import *
import json
from argument.regular import *
from myblog.settings import ONE_PAGE_OF_DATA
# Create your views here.

def is_login(request):
    try:
        nickname = request.session['nickname']
    except:
        nickname = ''
    return nickname

def index(request):
    # name = register.objects.filter(email = 'jsp@qq.com')
    # print name.values()[0]['username']
    nickname = is_login(request)
    uname = "Jhon"
    welcome = "欢 迎 来 到 %s 的 博 客 论 坛, 欢 迎 大 家 来 评 论"%uname
    carousel_page_list = Carousel.objects.all()
    article_list = Article.objects.all()
    #分页
    paginator = Paginator(article_list, ONE_PAGE_OF_DATA)
    try:
        page = int(request.GET.get('page',1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    try:
        articlelist = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        articlelist = paginator.page(page.num_pages)
    content = {
        'nickname': nickname,
        'carousel_page_list': carousel_page_list,
        'welcome': welcome,
        'article_list':article_list,
        'articlelist':articlelist,

    }
    return render_to_response('index.html',content, context_instance=RequestContext(request))

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == '':
            mydict = {'errors': "用户名不能为空"}
        elif password == '':
            mydict = {'errors': "密码不能为空"}
        else:
            users = register.objects.filter(email__exact=username, password__exact=password)
            if users:
                mydict = {'errors': ""}
                nickname = register.objects.filter(email = username).values()[0]['username']
                request.session['nickname'] = nickname
            else:
                mydict = {'errors': "用户名或者密码错误"}
        return HttpResponse(
                json.dumps(mydict),
                content_type="application/json"
            )

def logout(request):
    try:
        del request.session['nickname']
        return HttpResponseRedirect("index")
    except:
        response = HttpResponse()
        response.write("<script>alert('退出失败,您已退出!!');window.location.href='index'</script>")
        return response

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if username == '':
            mydict = {'errors': "用户名不能为空"}
        elif email == '':
            mydict = {'errors': "邮箱不能为空"}
        elif password1 == '' or password2 == '':
            mydict = {'errors': "密码不能为空"}
        elif len(username)<2 or len(username)>7:
            mydict = {'errors': "用户名请控制在2-6个字符之间"}
        elif regul(re_email, email) == None:
            mydict = {'errors': "邮箱格式不正确"}
        elif regul(re_passwd, password1) == None:
            mydict = {'errors': "密码请输入6-16位字符"}
        elif password1 != password2:
            mydict = {'errors': "两次密码不一致"}
        elif register.objects.filter(username = username):
            mydict = {'errors': "用户名已存在"}
        elif register.objects.filter(email = email):
            mydict = {'errors': "该邮箱已经被注册"}
        else:
            myregist = register.objects.create(username = username, password = password1, email = email)
            myregist.save()
            request.session['nickname'] = username
            mydict = {'errors': ""}
        return HttpResponse(
                json.dumps(mydict),
                content_type="application/json"
            )

def article_detail(request):
    article_id = request.GET.get('id', '')
    nickname = is_login(request)
    articledata = Article.objects.filter(id=article_id)
    content = {
        'nickname': nickname,
        'articledata': articledata,
    }
    return render_to_response('detail/article.html', content, context_instance=RequestContext(request))
