#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Created on 2022年6月28日
@author: yuejing
'''
import random
import pymysql
from faker import Faker

def data_qury(db,sql):
    '''
    数据库查询
    '''
    cur = db.cursor()
    try:
        cur.execute(sql)
        results = cur.fetchall()
    except:
        print ("Error: unable to fetch data")
    return results

def data_alter(db,sql):
    '''
    数据库插入/修改/删除
    '''
    cur = db.cursor()
    try:
        cur.execute(sql)
        db.commit()
    except:
        db.rollback()
        print('Alter Failed')

def get_data():
    '''
    Faker制造假数据
    '''
    key_list = ["姓名","性别","年龄","详细地址","省份","城市","手机号","身份证号","出生年月","邮箱","创建时间"]
    name = fake.name()
    gender= random.choice(["男","女"])
    age=fake.random_int(min=18,max=50)
    address = fake.address()
    province = fake.province()
    city = fake.city()
    number = fake.phone_number()
    id_card = fake.ssn()
    birth_date = id_card[6:14]
    email = fake.email()
    cdate=fake.date_time_between(start_date="-2y",end_date="-1y")
    info_list = [name,gender,age,address,province,city,number,id_card,birth_date,email,cdate]
    person_info = dict(zip(key_list,info_list))
    return person_info
    
#打开数据库连接
db=pymysql.connect(host="10.10.10.71",user="root",passwd="123456",db="jimmy",port=3306,use_unicode=True, charset="utf8")
#插入测试数据
fake = Faker(locale='zh_CN')
for i in range(10):
    data=get_data()
    sql = "INSERT INTO personal_information(name,gender,age,address,province,city,phone,carid,birthday,email,cdate) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (data['姓名'],data['性别'],data['年龄'],data['详细地址'],data['省份'],data['城市'],data['手机号'],data['身份证号'],data['出生年月'],data['邮箱'],data['创建时间'])
    data_alter(db,sql)
print('插入数据完成！')
# 关闭数据库连接
db.close()
