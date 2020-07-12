# XIHAHABOT

基于酷Q和NoneBot的QQ机器人

感谢NoneBot的开发者们：
https://github.com/nonebot/nonebot

以下为配料表及食用方式

# 0. 初始化

需要在酷Q Air或酷Q Pro中安装CQHTTP插件

（推荐使用酷Q Pro，部分功能需要发送图片和音频）

推荐按照NoneBot官方文档<https://nonebot.cqp.moe/guide/installation.html>和<https://nonebot.cqp.moe/guide/getting-started.html>进行配置。

配置成功后，机器人应能对发送的指令进行相应的反馈。

# 1. ana

没什么好说的，发送ANA的LOGO及登机音乐《Another Sky》

（音乐文件请自行下载并放至酷Q文件夹中的/data/record/ana（新建ana文件夹）中）

（图片文件请自行下载并放至酷Q文件夹中的/data/image/ana（新建ana文件夹）中）

# 2. bus_beijing

感谢bjbus-query的作者Himryang：<https://github.com/Himryang/bjbus-query>

本功能参考其部分代码而得以实现。

发送指令“北京公交”+线路号即可查询该线路上的实时公交运行状态。

例如发送“北京公交 1”，查询结果为：

![Image text](https://github.com/xihahaha/XIHAHABOT/blob/master/images/1.png)

数据来源为北京公共交通集团官网<http://www.bjbus.com/>，实时公交经常无数据，以后考虑换个API

# 3. bus_wuhan

发送指令“武汉公交”+线路号即可查询该线路上的实时公交运行状态。

例如发送“武汉公交 1”，查询结果为：

![Image text](https://github.com/xihahaha/XIHAHABOT/blob/master/images/2.png)

电X路请输入100X，如“武汉公交 1003”，查询结果为：

![Image text](https://github.com/xihahaha/XIHAHABOT/blob/master/images/3.png)

# 4. bus_shanghai

感谢shanghai-bus的作者lark930及ark930：<https://github.com/ark930/shanghai-bus>

本功能参考其部分代码而得以实现。

发送指令“上海公交”+线路号（发送全名，如01路、隧道夜宵线）即可查询该线路上的实时公交运行状态。

例如发送“上海公交 151路”，查询结果为：

![Image text](https://github.com/xihahaha/XIHAHABOT/blob/master/images/4.png)

# 5. express

基于快递鸟的查询快递功能

前往快递鸟官网<http://www.kdniao.com/>注册账号并申请ID与KEY填入py文件中

# 6. laji

我是什么垃圾？

# 7. light

物联网功能，通过IFTTT控制智能家居

该例中使用IFTTT控制小米床头灯2，需在IFTTT申请自己的KEY并配置好通信方式

# 8. melody

JR发车音乐随机选曲，♫♫♫ドアが閉まります、ご注意ください！

（音乐文件请自行下载并放至酷Q文件夹中的/data/record/melody（新建melody文件夹）中）

# 9. sh71

71路进站辣！！！

（音乐文件请自行下载并放至酷Q文件夹中的/data/record/sh71（新建sh71文件夹）中）

（图片文件请自行下载并放至酷Q文件夹中的/data/image/sh71（新建sh71文件夹）中）

# 10. timer

G114514次列车即将进站，请工作人员做好接车准备！

（音乐文件请自行下载并放至酷Q文件夹中的/data/record/melody（新建melody文件夹）中）

（ATOS接近音请自行下载并放至酷Q文件夹中的/data/record/ATOS（新建ATOS文件夹）中）

# 11. weather

也没什么好说的，教程自带的查询天气功能

# 12. yolo

使用yolo v3进行发送图片的目标检测

需要从<https://pjreddie.com/media/files/yolov3.weights>下载yolo v3权重文件并放入/cfg文件夹中

使用方式如下图

![Image text](https://github.com/xihahaha/XIHAHABOT/blob/master/images/5.png)

