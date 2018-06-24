# PTT(PictureToText)
    识别截图中的文字并添加到剪贴板

# 简介
    学习python的练手项目，也是为了方便自己从网上收集资料
    本项目使用百度云文字识别api（自行注册申请）识别截图（使用qq截图工具）中的文字，并将文字发送到剪贴板。

# 使用方法
    1.确认电脑已经安装了 QQ(推荐Tim) python 以及requments.txt中的库，
    2.注册百度云服务，并申请自己的api，将app_id,api_key,secret_key填入setup.ini文件中，
    3.运行ScreenToText.py 使用ctrl+alt+a截取含有文字的图片，再按一下ctrl进行文字识别。识别成功后，会在控制台打印识别到的内容，并显示“Successful send to clipboard”，此时可将文字粘贴到需要的地方。
