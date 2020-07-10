# -*- coding: utf-8 -*-
from hashlib import sha256
from app.db import select_query,  select_psswrd_query, set_psswrd_query, update_query

def check_register(login, pswrd, pswrdCheck):
    if pswrd == pswrdCheck:
        return register(login, pswrd)
    else:
        False, 'Введенные пароли не равны'


def register(user, psswrd):
    check_result = check_user(user)
    print(check_result)
    if check_result[0]== True:
        update_query(set_psswrd_query, user, sha256(psswrd.encode('utf-8')).hexdigest())
        return True, ''
    else:
        return False, 'Авторизация Вам недоступна'


def check_user(user):
    result = select_query(select_psswrd_query, user)
    print('check user')
    print(result)
    if result is None:
        return False, 'Такой пользователь не существует'
    else:
        return True, result

def check_psswrd(user, psswrd):
    check_result = check_user(user)
    if check_result[0] ==True:
        if check_result[1] is None:
            return False, 'Пользователь еще не зарегистрирован'
        else:
            print(sha256(psswrd.encode('utf-8')).hexdigest())
            print(check_result[1])
            if sha256(psswrd.encode('utf-8')).hexdigest() == check_result[1]:
                return True, ''
            else:
                return False, 'Некорректный пароль'
    else:
        return False, 'Пользователь не зарегистрирован'

def authorize(user, psswrd):
    check_result = check_user(user)
    if check_result[0] == True:
        return check_psswrd(user, psswrd)
    else:
        return check_result



