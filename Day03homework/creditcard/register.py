#/user/bin/env python
# _*_ coding:utf-8 _*_
import random

#生成信用卡ID，随机生成6个数字，组成卡号，返回卡号
def creditcard_id():
    card_id = [] 
    for i in range(6):
        num = random.randint(0,9)
        num = str(num)
        card_id.append(num)
    card_id = ''.join(card_id)
    return card_id     

#密码确认
def Creditcard_passwd():
    

#注册信用卡
def register():
    user_list = []
    name = input('请输入您的姓名：')
    age = input('情输入您的年龄：')
    profession = input('请输入您的职业：')
    card_id = creditcard_id()
    print('您的信用卡号为：%S',card_id)
    passwd = input('请输入您的密码：')
    passwd1 = input('请确认您的密码：')
    if passwd == passwd1 :
        print('注册成功！')
    else:
        print('密码不一致，请重新输入')
    
    
    