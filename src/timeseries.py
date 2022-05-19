from parse_data import parse_regional_data
from statsmodels.tsa.arima.model import ARIMA
import argparse
from copy import deepcopy
import csv

parser = argparse.ArgumentParser()
parser.add_argument("--region_path", type=str, default="./Shanghai_region_data_T.csv")
parser.add_argument("--fwd_date", type=int, default=3)
parser.add_argument("--refresh_csv", type=bool, default=True)
parser.add_argument("--refresh_html", type=bool, default=True)
args = parser.parse_args()

def arima(history, fwd_date, **kwargs):
    '''
        fwd_date:
            向前预测多少天
    '''
    pred = []
    hist = deepcopy(history)
    for _ in range(fwd_date):
        model = ARIMA(hist, order=(2, 2, 0))
        model = model.fit()
        p = model.forecast()
        pred.append(max(int(p[0].tolist()), 0))
        hist.append(p[0])

    if kwargs.get('key') is not None and kwargs.get('verbose') == True:
        print(kwargs['key'])
        print(pred)
    return pred

def savecsv(filename, dict):
    with open(filename, mode='w', newline="") as f:
        writer = csv.writer(f)
        for k, v in dict.items():
            row = [k] + v
            writer.writerow(row)

def return_dictionaries():
    '''
        For external usage (in backend.py: index())
    '''
    region_qz, region_wzz = parse_regional_data(args)
    print(region_qz.keys())
    pred_qz, pred_wzz = {}, {}
    for k, v in region_qz.items():
        pred_qz[k] = arima(v, fwd_date=args.fwd_date, key=k)
    for k ,v in region_wzz.items():
        pred_wzz[k] = arima(v, fwd_date=args.fwd_date, key=k)
    return region_qz, pred_qz, region_wzz, pred_wzz

if __name__ == "__main__":
    region_qz, pred_qz, region_wzz, pred_wzz = return_dictionaries()
    integrated_qz, integrated_wzz = {}, {}
        
    for k, v in region_qz.items():
        integrated_qz[k] = deepcopy(v)
        integrated_qz[k].extend(deepcopy(pred_qz[k]))

    for k, v in region_wzz.items():
        integrated_wzz[k] = deepcopy(v)
        integrated_wzz[k].extend(deepcopy(pred_wzz[k]))
    
    if args.refresh_csv:
        savecsv("pred_qz.csv", pred_qz)
        savecsv("pred_wzz.csv", pred_wzz)
        savecsv("qz.csv", region_qz)
        savecsv("wzz.csv", region_wzz)
