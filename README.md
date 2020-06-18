# 使用Django框架搭建博客。

## 步骤如下：
1. 创建项目；
	django-admin startproject myblog
2. 创建应用：
	打开命令行，进入项目中manage.py同级目录；
	命令行输入：python manage.py startapp blog
	添加应用名到settings.py中的INSTALLED_APPS里
3. 应用目录介绍;
- migrations：数据迁移模块，都是自动生成的
- admin.py：后台管理系统配置
- apps.py：该应用的一些配置，只在Django1.9以后生成
- models.py：数据模块，使用ORM们框架
- tests.py：自动化测试，可以编写脚本。
- views.py：执行响应的代码所在模块，代码逻辑处理的主要地点，主要代码编辑区
4. 创建第一个页面：
	编辑blog.views
5. 配置url：
	编辑urls.py
6. 编写models：
7. 页面呈现数据：
8. Admin配置

具体可以参考 [我的有道云笔记](http://note.youdao.com/noteshare?id=47cbbe553e2354336c1b7ea27f838dc1 Django框架搭建博客)

也可以参考https://blog.csdn.net/LinRuiC/article/details/84871684
