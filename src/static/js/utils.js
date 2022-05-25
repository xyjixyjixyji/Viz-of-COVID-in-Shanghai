function get_cumulative(dict, region_name) {
    var datas = dict[region_name];
    var sum = 0;
    for (let i = 0; i < datas.length; i++) {
        sum += datas[i];
    }
    return sum;
}

function get_latest_date(dict, region_name) {
    var datas = dict[region_name];
    var days = datas.length;
    var d = get_start_date();
    for (let i = 0; i < days; i++) {
        d = next_day(d);
    }
    var str = (d.getMonth() + 1) + "月" + d.getDate() + "日";
    return str;
}

function get_latest_data(dict, region_name) {
    var datas = dict[region_name];
    return datas[datas.length - 1];
}