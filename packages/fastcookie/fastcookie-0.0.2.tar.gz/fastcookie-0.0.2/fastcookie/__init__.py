#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import requests


def selenium_to_requests(
        cookie_for_selenium
):
    """
    将selenium的cookie转换为requests可识别的cookie
    """
    cookie_temp = [item["name"] + '=' + item["value"] for item in cookie_for_selenium]
    cookie_formatted = '; '.join(item for item in cookie_temp)
    return cookie_formatted


def get_selenium_driver_cookie(
        driver
):
    """
    从selenium的driver中提取两种形式的cookie
    """
    cookie_for_selenium = driver.get_cookies()  # 获取原始cookie
    cookie_for_requests = selenium_to_requests(cookie_for_selenium)  # 转换为requests模块可以识别的cookie
    return {'cookie_for_selenium': cookie_for_selenium, 'cookie_for_requests': cookie_for_requests}


def cookie_jar_to_dict(
        cookie_jar
):
    # 将CookieJar转为字典：
    cookies = requests.utils.dict_from_cookiejar(cookie_jar)
    return cookies


def dict_to_cookie_jar(
        cookie_dict
):
    # 将字典转为CookieJar：
    # 其中cookie_dict是要转换字典, 转换完之后就可以把它赋给cookies 并传入到session中了：
    # s = requests.Session()
    # s.cookies = cookies
    cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
    return cookies


def get_requests_cookie(
        cookie_jar
):
    """:cvar
    从requests的CookieJar提取cookie
    """
    # CookieJar 直接转换为cookie字符串
    cookies = cookie_jar_to_dict(cookie_jar)
    cookie_list = list()
    for key in cookies:
        value = cookies.get(key)
        each_cookie = '%s=%s' % (key, value)
        cookie_list.append(each_cookie)
    cookie_str = '; '.join(cookie_list)
    return cookie_str
