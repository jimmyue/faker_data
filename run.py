#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Created on 2022年6月28日
@author: yuejing
'''
import random
import pymysql
from faker import Faker

# CREATE TABLE `tb_personal_information` (
#   `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
#   `name` varchar(50) DEFAULT NULL COMMENT '姓名',
#   `gender` varchar(10) DEFAULT NULL COMMENT '性别',
#   `age` varchar(10) DEFAULT NULL COMMENT '年龄',
#   `address` varchar(100) DEFAULT NULL COMMENT '详细地址',
#   `province` varchar(10) DEFAULT NULL COMMENT '省份',
#   `city` varchar(10) DEFAULT NULL COMMENT '城市',
#   `phone` varchar(50) DEFAULT NULL COMMENT '手机号',
#   `carid` varchar(50) DEFAULT NULL COMMENT '身份证号',
#   `birthday` varchar(10) DEFAULT NULL COMMENT '出生年月',
#   `email` varchar(50) DEFAULT NULL COMMENT '邮箱',
#   `cdate` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
#   PRIMARY KEY (`id`)
# )

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
    gender= random.choice(["男","女","NULL"])
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
db=pymysql.connect(host="xxxx",user="jimmy",passwd="xxx",db="jimmy",port=3306,use_unicode=True, charset="utf8")
#插入测试数据
fake = Faker(locale='zh_CN')
n=10 #修改需要插入的数据行数
for i in range(n):
    data=get_data()
    if data['性别']=="NULL": #插入NULL值
        sql = "INSERT INTO tb_personal_information(name,gender,age,address,province,city,phone,carid,birthday,email,cdate) \
        VALUES ('%s',%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
        (data['姓名'],data['性别'],data['年龄'],data['详细地址'],data['省份'],data['城市'],data['手机号'],data['身份证号'],data['出生年月'],data['邮箱'],data['创建时间'])
    else:
        sql = "INSERT INTO tb_personal_information(name,gender,age,address,province,city,phone,carid,birthday,email,cdate) \
        VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
        (data['姓名'],data['性别'],data['年龄'],data['详细地址'],data['省份'],data['城市'],data['手机号'],data['身份证号'],data['出生年月'],data['邮箱'],data['创建时间'])
    data_alter(db,sql)
print('插入%s行数据成功！'%n)
# 关闭数据库连接
db.close()
