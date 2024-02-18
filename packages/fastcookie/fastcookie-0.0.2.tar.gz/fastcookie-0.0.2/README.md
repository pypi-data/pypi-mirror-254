# fastcookie

#### 介绍
cookie工具包

#### 软件架构
软件架构说明


#### 安装教程

1.  pip安装
```shell script
pip install fastcookie
```
2.  pip安装（使用淘宝镜像加速）
```shell script
pip install fastcookie -i https://mirrors.aliyun.com/pypi/simple
```

#### 使用说明

1.  demo
```python
import fastcookie
import requests
test_res = fastcookie.get_requests_cookie(cookie_jar=requests.session().cookies)
```
