var oneDay = 1000*60*60*24;

function get_start_date() {
    var date = new Date();
    date.setMonth(3);
    date.setDate(1);
    console.log(date);
    return date;
}

function next_day(date) {
    var newdate = new Date(Date.parse(date));
    var time = newdate.getTime();
    var after = time + oneDay;//计算前一天的毫秒数
    newdate.setTime(after);
    return newdate;
}

function get_consecutive_days(days) {
    var ret = []
    var d = get_start_date();
    for (let i = 0; i < days; i++) {
        ret.push(d);
        d = next_day(d);
    }
    return ret;
}

// ========================== TL:DR; 上面的不用看 ============================

// return strings of dates
// _days of days from 2022.4.1
// e.g., _days = 3 =》ret (4-1, 4-2, 4-3), all strings
function days_to_strings(_days) {
    var ret = []
    var days = get_consecutive_days(_days);
    for (let i = 0; i < days.length; i++) {
        var day = days[i]; // date object
        var m = day.getMonth()+1;
        var d = day.getDate();
        var str = m.toString(10) + '-' + d.toString(10);
        ret.push(str)
    }
    return ret;
}

/*
 * chartdom: document.getelementbyid(id)
 * region_name: 'Shanghai', 'Changning' etc.
 * data_dict, pred_dict: passed by flask ({{qz|safe}})
 */
function draw_line_chart(chartdom_name, region_name, data_dict, pred_dict, title) {
    var chartdom = document.getElementById(chartdom_name);
    var chart = echarts.init(chartdom);
    var data = data_dict[region_name];
    var pred = pred_dict[region_name];

    var datas = data;
    for (let i = 0; i < pred.length; i++) {
        val = pred[i];
        datas.push({
            value: val,
            itemStyle: {
                color: "#a90000",
            }
        })
    }


    option = {
        title: {
            text: title + " " + region_name + " ()",
            left: 'center',
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross',
              label: {
                backgroundColor: '#6a7985'
              }
            }
        },
        xAxis: {
            type: "category",
            boundaryGap: false,
            data: days_to_strings(data.length+pred.length),
        },
        yAxis: {
            type: "value",
        },
        series: [
            {
                data: datas,
                type: "line",
                areaStyle: {},
            },
        ],
    };

    chart.setOption(option);
}

/*
 * chartdom: document.getelementbyid(id)
 * region_name: 'Shanghai', 'Changning' etc.
 * data_dict: passed by flask ({{qz|safe}})
 */
function draw_line_chart_for_district(chartdom_name, region_name, data_dict, title) {
    var chartdom = document.getElementById(chartdom_name);
    var chart = echarts.init(chartdom);
    var datas = data_dict[region_name];

    option = {
        title: {
            text: title + " " + region_name + " ()",
            left: 'center',
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross',
              label: {
                backgroundColor: '#6a7985'
              }
            }
        },
        xAxis: {
            type: "category",
            boundaryGap: false,
            data: days_to_strings(datas.length),
        },
        yAxis: {
            type: "value",
        },
        series: [
            {
                data: datas,
                type: "line",
                areaStyle: {},
            },
        ],
    };

    chart.setOption(option);
}
