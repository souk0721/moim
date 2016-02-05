#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.
class moim_info(models.Model): #모임 정보 테이블
    BANK_NAME = ('IBK','기업은행'),('','')
    user = models.ForeignKey(User, blank=True)
    moim_name = models.CharField(unique=True, max_length=100)
    moim_deposit_date = models.CharField(max_length=100)#입금일
    moim_account_name = models.CharField(max_length=100)#계좌주인이름
    moim_account_bank = models.CharField(max_length=100)#은행선택
    moim_account_num = models.CharField(max_length=100)#계좌번호
    moim_total_money = models.IntegerField(default=0)
    moim_code = models.AutoField(primary_key=True)
    moim_symbol = models.ImageField(width_field=None,height_field=None,blank=True)
    moim_person_count = models.IntegerField(default=1)
     #def get_absolute_url(self):
     #   return reverse_lazy('view_single_photo', kwargs={'photo_id': self.id})

    def __unicode__(self):
        return self.moim_name + ' / 계좌주인: ' + self.moim_account_name

class user_info(models.Model): #사용자 정보 테이블
    moim_name = models.ForeignKey(moim_info) #모임이름
    user = models.ForeignKey(User)#사용자
    tel = models.CharField(max_length=100,null=True,blank=True)#전화번호
    manager = models.BooleanField(default=False)#총무유무
    user_name = models.CharField(max_length=100)#유저이름
    def __unicode__(self):
        return self.moim_name.moim_name + ' / 모임회원: ' + self.user_name


class deposit_info(models.Model): #예금정보 테이블
    moim_name = models.ForeignKey(moim_info)#모임이름
    user_name = models.ForeignKey(user_info)#사용자
    deposit_date = models.DateField()#입금년월
    deposit_amount=models.IntegerField(default=40000)#입금금액
    deposit_yse_no=models.BooleanField(default=False)#입금현황
    deposit_name = models.CharField(null=True,blank=True,max_length=100)

    def __unicode__(self):
        return self.moim_name.moim_name + ' / ' + self.user_name.user_name + ' / 입금일: ' + unicode(self.deposit_date)


class withdraw_info(models.Model): #출금정보 테이블

    moim_name=models.ForeignKey(moim_info)#모임이름
    withdraw_date=models.DateField()#지출년월
    withdraw_amount=models.IntegerField()#지출금액
    withdraw_title=models.CharField(max_length=100)#지출내역
    receipt_img = models.ImageField(blank=True)

    def __unicode__(self):
        return self.moim_name.moim_name + ' / 지출내역: ' + self.withdraw_title + ' / 지출일: ' + unicode(self.withdraw_date)

class outstanding_amount(models.Model): #미수금 정보 테이블
    user_name = models.ForeignKey(user_info)#유저이름
    moim_name = models.ForeignKey(moim_info)#모임이름
    out_standing_amount = models.IntegerField()#미수금

    def __unicode__(self):
        return self.moim_name.moim_name + ' / ' + self.user_name.user_name + ' / 미수금: ' + unicode(self.out_standing_amount)
