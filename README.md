# Viz-of-COVID-inShanghai

此项目是上海交通大学CS239课程项目，请根据如下步骤使用此项目。



## 获取白玉兰项目数据：

```bash
bash fetch.sh
```



## 微博评论爬取

进入 **微博评论爬虫** 文件夹，按照其中README进行操作即可。



## 情绪分析

todo： 

（注意：数据处理完，存储在哪个位置写一下）



## 运行项目

在src文件夹下，运行：

```bash
python backend.py
```

点击运行产生的网址端口进入项目界面，如下图所示：

<img src=".\src\static\images\1.png" alt="1" style="zoom:30%;" />



## 项目使用

分为三个可使用界面和一个团队介绍界面



### 全市信息概览

地图中蓝色标记代表区，点击可以看到该区的每日新增变化折线图：

<img src=".\src\static\images\2.png" alt="2" style="zoom:40%;" />



带颜色的点表示通报的病例，将鼠标悬停在其上可以查看其通报时间，地点和次数：
<img src=".\src\static\images\3.png" alt="4" style="zoom:80%;" />



点击右上角柱状图/折线图按钮，可以切换左侧图表类型。



### 舆情分析

<img src=".\src\static\images\4.png" alt="4" style="zoom:80%;" />

拖动中间的进度条，可以查看4月2日到5月28日之间每一天的舆情分析结果



### 全市分区统计数据

<img src=".\src\static\images\5.png" alt="5" style="zoom:30%;" />

点击对应区板块（标黄），即可查看该区每日新增病例的变化折线图
