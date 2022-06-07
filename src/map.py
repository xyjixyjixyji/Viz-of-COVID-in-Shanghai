import csv
import pandas
import json
import folium
import requests
import re
import branca
import os
from pyecharts.charts import Line
from pyecharts import options as opts
# from .source.code import utils


def decode_address(encode):
    decode_file = './source/data/daily_info/address_decode.json'
    with open(decode_file, "r", encoding='utf-8') as f:
        decode_data = json.load(f)
    if encode in decode_data.keys():
        return decode_data[encode]
    else:
        return None

def parse_to_dict(csvname, saved_dict):
    with open(csvname, mode='r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            saved_dict[row[0]] = row[1:]
def days_to_string(start_day = "4-1", duration = 40):
    all_days=[]
    current_day = start_day
    for i in range(duration):
        all_days.append(current_day)
        day = int(current_day.split('-')[1])
        month = int(current_day.split('-')[0])
        day += 1
        if(day==31):
            day=1
            month += 1
        current_day = "%s-%s"%(month,day)
    print(all_days)
    return all_days

def getGPS(address: str, myAK='27gAPLcAkOCzK6NGQVyRyMQYPGjRBa9F'):
    # myAK = '27gAPLcAkOCzK6NGQVyRyMQYPGjRBa9F'
    url = 'https://api.map.baidu.com/geocoding/v3/?address=' + \
        address + '&output=json&coordtype=bd09ll&ak=' + myAK
    res = requests.get(url)
    res.data = res.content.decode()
    # print(res.data)
    pattern = '\"lng\"\:(\d+\.\d+),\"lat\"\:(\d+\.\d+)'
    try:
        return re.findall(pattern, res.data)[0]
    except:
        print(res.data)


def parse_zhch(s):
    return str(str(s).encode('ascii', 'xmlcharrefreplace'))[2:-1]


def mapping():
    qz = {}
    wzz = {}
    parse_to_dict('./qz.csv',qz)
    parse_to_dict('./wzz.csv',wzz)
    pre_qz = {}
    pre_wzz = {}
    parse_to_dict('./pred_qz.csv',pre_qz)
    parse_to_dict('./pred_wzz.csv',pre_wzz)

    all_days = days_to_string("4-1",duration=len(qz["Shanghai"]))

    pudongnew_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    pudongnew_charts.add_xaxis(xaxis_data=all_days)
    pudongnew_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["PudongNew"],label_opts = opts.LabelOpts(is_show=False))
    pudongnew_charts.set_global_opts(title_opts = opts.TitleOpts(title="浦东新区每日新增确诊人数", pos_top = "20px"))
    pudongnew_charts.render("pudongnew_charts.html")
    pudongnew_html = open("pudongnew_charts.html","r",encoding="utf-8").read()
    pudongnew_iframe = branca.element.IFrame(html=pudongnew_html, width=500, height=300)
    pudongnew_popup = folium.Popup(pudongnew_iframe, max_width=500) 

    huangpu_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    huangpu_charts.add_xaxis(xaxis_data=all_days)
    huangpu_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Huangpu"],label_opts = opts.LabelOpts(is_show=False))
    huangpu_charts.set_global_opts(title_opts = opts.TitleOpts(title="黄浦区每日新增确诊人数", pos_top = "20px"))
    huangpu_charts.render("huangpu_charts.html")
    huangpu_html = open("huangpu_charts.html","r",encoding="utf-8").read()
    huangpu_iframe = branca.element.IFrame(html=huangpu_html, width=500, height=300)
    huangpu_popup = folium.Popup(huangpu_iframe, max_width=500) 
    
    xuhui_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    xuhui_charts.add_xaxis(xaxis_data=all_days)
    xuhui_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Xuhui"],label_opts = opts.LabelOpts(is_show=False))
    xuhui_charts.set_global_opts(title_opts = opts.TitleOpts(title="徐汇区每日新增确诊人数", pos_top = "20px"))
    xuhui_charts.render("xuhui_charts.html")
    xuhui_html = open("xuhui_charts.html","r",encoding="utf-8").read()
    xuhui_iframe = branca.element.IFrame(html=xuhui_html, width=500, height=300)
    xuhui_popup = folium.Popup(xuhui_iframe, max_width=500) 

    changning_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    changning_charts.add_xaxis(xaxis_data=all_days)
    changning_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Changning"],label_opts = opts.LabelOpts(is_show=False))
    changning_charts.set_global_opts(title_opts = opts.TitleOpts(title="长宁区每日新增确诊人数", pos_top = "20px"))
    changning_charts.render("changning_charts.html")
    changning_html = open("changning_charts.html","r",encoding="utf-8").read()
    changning_iframe = branca.element.IFrame(html=changning_html, width=500, height=300)
    changning_popup = folium.Popup(changning_iframe, max_width=500) 

    jingan_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    jingan_charts.add_xaxis(xaxis_data=all_days)
    jingan_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Jingan"],label_opts = opts.LabelOpts(is_show=False))
    jingan_charts.set_global_opts(title_opts = opts.TitleOpts(title="静安区每日新增确诊人数", pos_top = "20px"))
    jingan_charts.render("jingan_charts.html")
    jingan_html = open("jingan_charts.html","r",encoding="utf-8").read()
    jingan_iframe = branca.element.IFrame(html=jingan_html, width=500, height=300)
    jingan_popup = folium.Popup(jingan_iframe, max_width=500) 

    putuo_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    putuo_charts.add_xaxis(xaxis_data=all_days)
    putuo_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Putuo"],label_opts = opts.LabelOpts(is_show=False))
    putuo_charts.set_global_opts(title_opts = opts.TitleOpts(title="普陀区每日新增确诊人数", pos_top = "20px"))
    putuo_charts.render("putuo_charts.html")
    putuo_html = open("putuo_charts.html","r",encoding="utf-8").read()
    putuo_iframe = branca.element.IFrame(html=putuo_html, width=500, height=300)
    putuo_popup = folium.Popup(putuo_iframe, max_width=500) 

    hongkou_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    hongkou_charts.add_xaxis(xaxis_data=all_days)
    hongkou_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Hongkou"],label_opts = opts.LabelOpts(is_show=False))
    hongkou_charts.set_global_opts(title_opts = opts.TitleOpts(title="虹口区每日新增确诊人数", pos_top = "20px"))
    hongkou_charts.render("hongkou_charts.html")
    hongkou_html = open("hongkou_charts.html","r",encoding="utf-8").read()
    hongkou_iframe = branca.element.IFrame(html=hongkou_html, width=500, height=300)
    hongkou_popup = folium.Popup(hongkou_iframe, max_width=500) 

    yangpu_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    yangpu_charts.add_xaxis(xaxis_data=all_days)
    yangpu_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Yangpu"],label_opts = opts.LabelOpts(is_show=False))
    yangpu_charts.set_global_opts(title_opts = opts.TitleOpts(title="杨浦区每日新增确诊人数", pos_top = "20px"))
    yangpu_charts.render("yangpu_charts.html")
    yangpu_html = open("yangpu_charts.html","r",encoding="utf-8").read()
    yangpu_iframe = branca.element.IFrame(html=yangpu_html, width=500, height=300)
    yangpu_popup = folium.Popup(yangpu_iframe, max_width=500) 

    minhang_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    minhang_charts.add_xaxis(xaxis_data=all_days)
    minhang_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Minhang"],label_opts = opts.LabelOpts(is_show=False))
    minhang_charts.set_global_opts(title_opts = opts.TitleOpts(title="闵行区每日新增确诊人数", pos_top = "20px"))
    minhang_charts.render("minhang_charts.html")
    minhang_html = open("minhang_charts.html","r",encoding="utf-8").read()
    minhang_iframe = branca.element.IFrame(html=minhang_html, width=500, height=300)
    minhang_popup = folium.Popup(minhang_iframe, max_width=500) 

    baoshan_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    baoshan_charts.add_xaxis(xaxis_data=all_days)
    baoshan_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Baoshan"],label_opts = opts.LabelOpts(is_show=False))
    baoshan_charts.set_global_opts(title_opts = opts.TitleOpts(title="宝山区每日新增确诊人数", pos_top = "20px"))
    baoshan_charts.render("baoshan_charts.html")
    baoshan_html = open("baoshan_charts.html","r",encoding="utf-8").read()
    baoshan_iframe = branca.element.IFrame(html=baoshan_html, width=500, height=300)
    baoshan_popup = folium.Popup(baoshan_iframe, max_width=500) 

    jiading_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    jiading_charts.add_xaxis(xaxis_data=all_days)
    jiading_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Jiading"],label_opts = opts.LabelOpts(is_show=False))
    jiading_charts.set_global_opts(title_opts = opts.TitleOpts(title="嘉定区每日新增确诊人数", pos_top = "20px"))
    jiading_charts.render("jiading_charts.html")
    jiading_html = open("jiading_charts.html","r",encoding="utf-8").read()
    jiading_iframe = branca.element.IFrame(html=jiading_html, width=500, height=300)
    jiading_popup = folium.Popup(jiading_iframe, max_width=500) 

    jinshan_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    jinshan_charts.add_xaxis(xaxis_data=all_days)
    jinshan_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Jinshan"],label_opts = opts.LabelOpts(is_show=False))
    jinshan_charts.set_global_opts(title_opts = opts.TitleOpts(title="金山区每日新增确诊人数", pos_top = "20px"))
    jinshan_charts.render("jinshan_charts.html")
    jinshan_html = open("jinshan_charts.html","r",encoding="utf-8").read()
    jinshan_iframe = branca.element.IFrame(html=jinshan_html, width=500, height=300)
    jinshan_popup = folium.Popup(jinshan_iframe, max_width=500) 

    songjiang_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    songjiang_charts.add_xaxis(xaxis_data=all_days)
    songjiang_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Songjiang"],label_opts = opts.LabelOpts(is_show=False))
    songjiang_charts.set_global_opts(title_opts = opts.TitleOpts(title="松江区每日新增确诊人数", pos_top = "20px"))
    songjiang_charts.render("songjiang_charts.html")
    songjiang_html = open("songjiang_charts.html","r",encoding="utf-8").read()
    songjiang_iframe = branca.element.IFrame(html=songjiang_html, width=500, height=300)
    songjiang_popup = folium.Popup(songjiang_iframe, max_width=500) 

    qingpu_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    qingpu_charts.add_xaxis(xaxis_data=all_days)
    qingpu_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Qingpu"],label_opts = opts.LabelOpts(is_show=False))
    qingpu_charts.set_global_opts(title_opts = opts.TitleOpts(title="青浦区每日新增确诊人数", pos_top = "20px"))
    qingpu_charts.render("qingpu_charts.html")
    qingpu_html = open("qingpu_charts.html","r",encoding="utf-8").read()
    qingpu_iframe = branca.element.IFrame(html=qingpu_html, width=500, height=300)
    qingpu_popup = folium.Popup(qingpu_iframe, max_width=500) 

    fengxian_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    fengxian_charts.add_xaxis(xaxis_data=all_days)
    fengxian_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Fengxian"],label_opts = opts.LabelOpts(is_show=False))
    fengxian_charts.set_global_opts(title_opts = opts.TitleOpts(title="奉贤区每日新增确诊人数", pos_top = "20px"))
    fengxian_charts.render("fengxian_charts.html")
    fengxian_html = open("fengxian_charts.html","r",encoding="utf-8").read()
    fengxian_iframe = branca.element.IFrame(html=fengxian_html, width=500, height=300)
    fengxian_popup = folium.Popup(fengxian_iframe, max_width=500) 

    chongming_charts = Line(init_opts = opts.InitOpts(width = '500px',height = '300px'))
    chongming_charts.add_xaxis(xaxis_data=all_days)
    chongming_charts.add_yaxis(series_name = '当日新增确诊人数',y_axis = qz["Chongming"],label_opts = opts.LabelOpts(is_show=False))
    chongming_charts.set_global_opts(title_opts = opts.TitleOpts(title="崇明区每日新增确诊人数", pos_top = "20px"))
    chongming_charts.render("chongming_charts.html")
    chongming_html = open("chongming_charts.html","r",encoding="utf-8").read()
    chongming_iframe = branca.element.IFrame(html=chongming_html, width=500, height=300)
    chongming_popup = folium.Popup(chongming_iframe, max_width=500) 

    csv_file = './source/data/CaseInfo_April/daily_report_by_address.csv'
    colormap = branca.colormap.linear.YlOrRd_09.scale(0, 1).to_step(4)
    df = pandas.read_csv(csv_file, encoding='utf-8', dtype={'addressID': str})
    shanghai = folium.Map(
        location=[31.2304, 121.4737], zoom_start=12, min_zoom=10)
    colormap.caption = "距离最近一次通报疫情天数"
    colormap.add_to(shanghai)
    # print(df[0]['encode'])
    PudongNew = folium.FeatureGroup(name=parse_zhch("浦东新区"))
    Huangpu = folium.FeatureGroup(name=parse_zhch("黄浦区"))
    Xuhui = folium.FeatureGroup(name=parse_zhch("徐汇区"))
    Changning = folium.FeatureGroup(name=parse_zhch("长宁区"))
    Jingan = folium.FeatureGroup(name=parse_zhch("静安区"))
    Putuo = folium.FeatureGroup(name=parse_zhch("普陀区"))
    Hongkou = folium.FeatureGroup(name=parse_zhch("虹口区"))
    Yangpu = folium.FeatureGroup(name=parse_zhch("杨浦区"))
    Minhang = folium.FeatureGroup(name=parse_zhch("闵行区"))
    Baoshan = folium.FeatureGroup(name=parse_zhch("宝山区"))
    Jiading = folium.FeatureGroup(name=parse_zhch("嘉定区"))
    Jinshan = folium.FeatureGroup(name=parse_zhch("金山区"))
    Songjiang = folium.FeatureGroup(name=parse_zhch("松江区"))
    Qingpu = folium.FeatureGroup(name=parse_zhch("青浦区"))
    Fengxian = folium.FeatureGroup(name=parse_zhch("奉贤区"))
    Chongming = folium.FeatureGroup(name=parse_zhch("崇明区"))
    gps_xuhui = [31.194804,121.443108]
    gps_hongkou = [31.270886,121.510373]
    gps_minhang = [31.11866,121.387916]
    gps_pudongnew = [31.226114,121.558216]
    gps_putuo = [31.254588,121.403438]
    gps_changning = [31.22643,121.430459]
    gps_jingan = [31.234088,121.453169]
    gps_yangpu = [31.265577,121.532651]
    gps_baoshan = [31.410168,121.496]
    gps_jiading = [31.413445,121.268854]
    gps_songjiang = [31.057646,121.237961]
    gps_qingpu = [31.154218,121.131413]
    gps_fengxian = [30.923968,121.480217]
    gps_chongming = [31.629307,121.405567]
    gps_jinshan = [30.746611,121.348767]
    gps_huangpu = [31.236351,121.480342]
    pudongnew = folium.Marker(location=gps_pudongnew,popup=pudongnew_popup).add_to(shanghai)
    xuhui = folium.Marker(location=gps_xuhui,popup=xuhui_popup).add_to(shanghai)
    hongkou = folium.Marker(location=gps_hongkou,popup=hongkou_popup).add_to(shanghai)
    minhang = folium.Marker(location=gps_minhang,popup=minhang_popup).add_to(shanghai)
    putuo = folium.Marker(location=gps_putuo,popup=putuo_popup).add_to(shanghai)
    changning = folium.Marker(location=gps_changning,popup=changning_popup).add_to(shanghai)
    jingan = folium.Marker(location=gps_jingan,popup=jingan_popup).add_to(shanghai)
    yangpu = folium.Marker(gps_yangpu,popup=yangpu_popup).add_to(shanghai)
    baoshan = folium.Marker(gps_baoshan,popup=baoshan_popup).add_to(shanghai)
    jiading = folium.Marker(gps_jiading,popup=jiading_popup).add_to(shanghai)
    songjiang = folium.Marker(gps_songjiang,popup=songjiang_popup).add_to(shanghai)
    qingpu = folium.Marker(gps_qingpu,popup=qingpu_popup).add_to(shanghai)
    fengxian = folium.Marker(gps_fengxian,popup=fengxian_popup).add_to(shanghai)
    chongming = folium.Marker(gps_chongming,popup=chongming_popup).add_to(shanghai)
    jinshan = folium.Marker(gps_jinshan,popup=jinshan_popup).add_to(shanghai)
    huangpu = folium.Marker(gps_huangpu,popup=huangpu_popup).add_to(shanghai)
    for i, item in df.iterrows():
        encode = item['addressID']
        # print(encode)
        decode_gps = decode_address(encode)
        # print(decode_gps)
        if(decode_gps == None):
            continue
        gps = getGPS(decode_gps)
        if (gps == None):
            continue
        gps = list(gps)
        tmp = float(gps[1])
        gps[1] = float(gps[0])
        gps[0] = tmp
        total_day = len(item)-1
        last_report = 15
        report_times = 0
        base_radius = 10
        add_radius = 3
        for j, Item in enumerate(item):
            if j == 0:
                continue
            if Item == 1:
                report_times += 1
                last_report = total_day - j
        text = folium.Popup((parse_zhch(decode_gps)+"。累计通报次数为%s次，最近一次通报为%s天前。"%(report_times,last_report)),max_width=100)
        if last_report > 14:
            tmp_circle = folium.Circle(location=gps, color=colormap.rgb_hex_str(
                1/4.0), fill=colormap.rgb_hex_str(1/4.0), radius=base_radius + add_radius * report_times, popup=text)
            # tmp_circle.add_to(data_15)
            if encode[3:5]=='01':
                tmp_circle.add_to(PudongNew)
            elif encode[3:5]=='02':
                tmp_circle.add_to(Hongkou)
            elif encode[3:5]=='03':
                tmp_circle.add_to(Minhang)
            elif encode[3:5]=='04':
                tmp_circle.add_to(Xuhui)
            elif encode[3:5]=='05':
                tmp_circle.add_to(Huangpu)
            elif encode[3:5]=='06':
                tmp_circle.add_to(Jiading)
            elif encode[3:5]=='07':
                tmp_circle.add_to(Jingan)
            elif encode[3:5]=='08':
                tmp_circle.add_to(Yangpu)
            elif encode[3:5]=='09':
                tmp_circle.add_to(Baoshan)
            elif encode[3:5]=='10':
                tmp_circle.add_to(Fengxian)
            elif encode[3:5]=='11':
                tmp_circle.add_to(Songjiang)
            elif encode[3:5]=='12':
                tmp_circle.add_to(Chongming)
            elif encode[3:5]=='13':
                tmp_circle.add_to(Qingpu)
            elif encode[3:5]=='14':
                tmp_circle.add_to(Jinshan)
            elif encode[3:5]=='15':
                tmp_circle.add_to(Changning)
            elif encode[3:5]=='16':
                tmp_circle.add_to(Putuo)
            # print(1)
        elif last_report <= 14 and last_report > 7:
            tmp_circle = folium.Circle(location=gps, color=colormap.rgb_hex_str(
                2/4.0), fill=colormap.rgb_hex_str(2/4.0), radius=base_radius + add_radius * report_times, popup=text)
            # tmp_circle.add_to(data_7_14)
            if encode[3:5]=='01':
                tmp_circle.add_to(PudongNew)
            elif encode[3:5]=='02':
                tmp_circle.add_to(Hongkou)
            elif encode[3:5]=='03':
                tmp_circle.add_to(Minhang)
            elif encode[3:5]=='04':
                tmp_circle.add_to(Xuhui)
            elif encode[3:5]=='05':
                tmp_circle.add_to(Huangpu)
            elif encode[3:5]=='06':
                tmp_circle.add_to(Jiading)
            elif encode[3:5]=='07':
                tmp_circle.add_to(Jingan)
            elif encode[3:5]=='08':
                tmp_circle.add_to(Yangpu)
            elif encode[3:5]=='09':
                tmp_circle.add_to(Baoshan)
            elif encode[3:5]=='10':
                tmp_circle.add_to(Fengxian)
            elif encode[3:5]=='11':
                tmp_circle.add_to(Songjiang)
            elif encode[3:5]=='12':
                tmp_circle.add_to(Chongming)
            elif encode[3:5]=='13':
                tmp_circle.add_to(Qingpu)
            elif encode[3:5]=='14':
                tmp_circle.add_to(Jinshan)
            elif encode[3:5]=='15':
                tmp_circle.add_to(Changning)
            elif encode[3:5]=='16':
                tmp_circle.add_to(Putuo)
        elif last_report <= 7 and last_report > 1:
            tmp_circle = folium.Circle(location=gps, color=colormap.rgb_hex_str(
                3/4.0), fill=colormap.rgb_hex_str(3/4.0), radius=base_radius + add_radius * report_times, popup=text)
            # tmp_circle.add_to(data_1_7)
            if encode[3:5]=='01':
                tmp_circle.add_to(PudongNew)
            elif encode[3:5]=='02':
                tmp_circle.add_to(Hongkou)
            elif encode[3:5]=='03':
                tmp_circle.add_to(Minhang)
            elif encode[3:5]=='04':
                tmp_circle.add_to(Xuhui)
            elif encode[3:5]=='05':
                tmp_circle.add_to(Huangpu)
            elif encode[3:5]=='06':
                tmp_circle.add_to(Jiading)
            elif encode[3:5]=='07':
                tmp_circle.add_to(Jingan)
            elif encode[3:5]=='08':
                tmp_circle.add_to(Yangpu)
            elif encode[3:5]=='09':
                tmp_circle.add_to(Baoshan)
            elif encode[3:5]=='10':
                tmp_circle.add_to(Fengxian)
            elif encode[3:5]=='11':
                tmp_circle.add_to(Songjiang)
            elif encode[3:5]=='12':
                tmp_circle.add_to(Chongming)
            elif encode[3:5]=='13':
                tmp_circle.add_to(Qingpu)
            elif encode[3:5]=='14':
                tmp_circle.add_to(Jinshan)
            elif encode[3:5]=='15':
                tmp_circle.add_to(Changning)
            elif encode[3:5]=='16':
                tmp_circle.add_to(Putuo)
        else:
            tmp_circle = folium.Circle(location=gps, color=colormap.rgb_hex_str(
                4/4.0), fill=colormap.rgb_hex_str(4/4.0), radius=base_radius + add_radius * report_times, popup=text)
            # tmp_circle.add_to(data_1)
            if encode[3:5]=='01':
                tmp_circle.add_to(PudongNew)
            elif encode[3:5]=='02':
                tmp_circle.add_to(Hongkou)
            elif encode[3:5]=='03':
                tmp_circle.add_to(Minhang)
            elif encode[3:5]=='04':
                tmp_circle.add_to(Xuhui)
            elif encode[3:5]=='05':
                tmp_circle.add_to(Huangpu)
            elif encode[3:5]=='06':
                tmp_circle.add_to(Jiading)
            elif encode[3:5]=='07':
                tmp_circle.add_to(Jingan)
            elif encode[3:5]=='08':
                tmp_circle.add_to(Yangpu)
            elif encode[3:5]=='09':
                tmp_circle.add_to(Baoshan)
            elif encode[3:5]=='10':
                tmp_circle.add_to(Fengxian)
            elif encode[3:5]=='11':
                tmp_circle.add_to(Songjiang)
            elif encode[3:5]=='12':
                tmp_circle.add_to(Chongming)
            elif encode[3:5]=='13':
                tmp_circle.add_to(Qingpu)
            elif encode[3:5]=='14':
                tmp_circle.add_to(Jinshan)
            elif encode[3:5]=='15':
                tmp_circle.add_to(Changning)
            elif encode[3:5]=='16':
                tmp_circle.add_to(Putuo)
        if(i%400==0):
            # break
            print(i)
        # print(last_report)
        # print(gps)
    Minhang.add_to(shanghai)
    PudongNew.add_to(shanghai)
    Xuhui.add_to(shanghai)
    Changning.add_to(shanghai)
    Jingan.add_to(shanghai)
    Putuo.add_to(shanghai)
    Hongkou.add_to(shanghai)
    Yangpu.add_to(shanghai)
    Baoshan.add_to(shanghai)
    Jiading.add_to(shanghai)
    Jinshan.add_to(shanghai)
    Songjiang.add_to(shanghai)
    Qingpu.add_to(shanghai)
    Fengxian.add_to(shanghai)
    Chongming.add_to(shanghai)
    folium.LayerControl().add_to(shanghai)
    os.remove("pudongnew_charts.html")
    os.remove("huangpu_charts.html")
    os.remove("xuhui_charts.html")
    os.remove("changning_charts.html")
    os.remove("jingan_charts.html")
    os.remove("putuo_charts.html")
    os.remove("hongkou_charts.html")
    os.remove("yangpu_charts.html")
    os.remove("minhang_charts.html")
    os.remove("baoshan_charts.html")
    os.remove("jiading_charts.html")
    os.remove("jinshan_charts.html")
    os.remove("songjiang_charts.html")
    os.remove("qingpu_charts.html")
    os.remove("fengxian_charts.html")
    os.remove("chongming_charts.html")
    shanghai.save("test.html")
mapping()
