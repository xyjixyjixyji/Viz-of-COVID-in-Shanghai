import csv

# 返回两个dict，一个是region_quezhen, 一个是region_wuzhengzhuang
# 按照地名为key，返回对应的序列，开始时间是4.1日
def parse_regional_data(args):
    path = args.region_path
    title = []
    datas = []
    with open(path, mode='r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                title = row
            else:
                datas.append(row)
    # start date = 4.1
    data_dict = {}
    for data in datas:
        data_dict[data[0]] = data[1:]
    
    # data_dict[name] = data
    region_qz = {}
    region_wzz = {}
    for k, v in data_dict.items():
        region_qz[k] = []
        region_wzz[k] = []
        for i, data in enumerate(v):
            data = float(data)
            if i % 2 == 0:
                region_qz[k].append(data)  # quezhen
            else:
                region_wzz[k].append(data)
    
    return region_qz, region_wzz
