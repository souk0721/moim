
#-*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .models import *
User = get_user_model()

@login_required()
def moim_list(request):
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    if request.method == "GET":
       user = get_object_or_404(User, username=request.user)

       try:
           Moim_info_all = moim_info.objects.all()
           User_info_all = user_info.objects.all()
           User_info = user_info.objects.filter(user = request.user)

       except:
           print("nono")

        #Moim_list = User_info.moim_name.filter(user=request.user)
        #moim_list = Moim_list.get().moim_name
    return render(
        request,
        'moim_list.html',
        {
            #'form': edit_form,
            'user_info_all': User_info_all,
            'user_name': user,
            'user_info': User_info,
            #'moim_name' :Moim_list,
        }
    )

def moim_detail(request,moim_name):
    manager = ""
    user = ""
    notuser =""



    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    if request.method == "GET":
        try:
            moim_info.objects.get(moim_name=moim_name) #잘못된 모임이름이 들어왔을 때 오류
            User_info = user_info.objects.filter(moim_name__moim_name=moim_name) #모임이름으로 필터링
            User_info_user = user_info.objects.filter(user=request.user)
            for user_Info_for in User_info:
                    if user_Info_for.manager == True and user_Info_for.user == request.user:
                        manager = 'True'

                    elif user_Info_for.user == request.user:
                         user = 'True'

                    elif user_Info_for.user != request.user:
                        notuser = 'True'
        except:
            return render(
                request,
                'error.html',
                {
                    'error':'잘못된 모임 이름입니다.'
                }

            )



        #Moim_list = User_info.moim_name.filter(user=request.user)
        #moim_list = Moim_list.get().moim_name
    return render(
        request,
        'moim_detail.html',
              {
            #'form': edit_form,
            'Manager' : manager,
            'User' : user,
            'NotUser' : notuser,
            'moim_name': moim_name,
            'user_info': User_info,
            #'moim_name' :Moim_list,
             }
        )


from but_moim.forms import Moim_join_Form
def moim_join(request): #모임등록
     if not request.user.is_authenticated():
       return redirect(settings.LOGIN_URL)

     if request.method == "GET":
        currunt_user = request.user
        edit_form = Moim_join_Form()


     elif request.method =="POST":
        edit_form = Moim_join_Form(request.POST, request.FILES)

        if edit_form.is_valid():
            User_info = user_info.objects.filter(user = request.user)
            new_moim = edit_form.save(commit=False)
            new_moim.user = request.user
            new_moim.save()

            user = get_object_or_404(User, username=request.user)
            #tel = user_info.objects.get(user=request.user)
            Moim_Name = moim_info.objects.get(moim_name=new_moim.moim_name) # 중요 fk의경우 상위모델의 인스턴스를 만들고 그 변수를 사용한다.
            userinfo = user_info(moim_name = Moim_Name,user_name=user.get_full_name(),tel='',user=request.user,manager=True)
            userinfo.save()


            return redirect('/moim_list')
     return render(
        request,
        'moim_join.html',
        {
            'form': edit_form,
            #'moim_name': moim_name,
            #'user_info': User_info,
            #'moim_name' :Moim_list,
        }
    )


from but_moim.forms import MoimSearchForm
def moim_search(request): #모임검색
     if not request.user.is_authenticated():
       return redirect(settings.LOGIN_URL)

     if request.method == "GET":
        edit_form = MoimSearchForm()

     elif request.method =="POST":
        edit_form = MoimSearchForm(request.POST)

        if edit_form.is_valid():
           search_form = edit_form.cleaned_data['search_name']
           search = moim_info.objects.filter(moim_name=search_form)

           return render(
               request,
               'moim_search.html',
                {
                    'search': search,
                     #'moim_name': moim_name,
                     #'user_info': User_info,
                     #'moim_name' :Moim_list,
        }
    )
     return render(
        request,
        'moim_search.html',
        {
            'form': edit_form,
            #'moim_name': moim_name,
            #'user_info': User_info,
            #'moim_name' :Moim_list,
        }
    )

def moim_search_join(request,moim_name): #모임검색 등록

    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    if request.method == "GET":
        Moim_info = moim_info.objects.get(moim_name=moim_name)
        User_info = user_info.objects.filter(moim_name__moim_name=moim_name)

        for user in User_info:

          if user.user == request.user:
              return render(
                  request,
                  'error.html',
                      {
                      #'form': edit_form,
                      'error' : '이미 가입되어 있습니다.',
                      #'moim_name' :Moim_list,
                       }
                  )
        user = get_object_or_404(User, username=request.user)
        Moim_Name = moim_info.objects.get(moim_name=moim_name)
        userinfo = user_info(moim_name = Moim_Name,user_name=user.get_full_name(),tel='',user=request.user)
        a = moim_info.objects.get(moim_name = moim_name)
        b = a.moim_person_count
        moim_info.objects.filter(moim_name=moim_name).update(moim_person_count = b + 1)
        print(b)
        #moiminfo.save()
        userinfo.save()


        #Moim_list = User_info.moim_name.filter(user=request.user)
        #moim_list = Moim_list.get().moim_name
    return render(
        request,
        'welcome.html',
        {
            #'form': edit_form,
            'welcome': '가입완료',

            #'moim_name' :Moim_list,
        }
    )







