import numpy as np
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.dates import date2num, num2date
from datetime import timedelta,datetime


def get_start_date(start_date='', gettype='down'):

    if not start_date:
        diff = 400
    else:
        start_time = datetime.strptime(start_date,'%Y-%m-%d')
        diff_time = datetime.now() - start_time
        diff = diff_time.days

        if gettype == 'up':
            diff = int(diff / 1.4)
        else:
            diff = int(diff * 1.4)

    diff_date = timedelta(days=diff)
    start_date = datetime.now() - diff_date
    x_str = start_date.strftime('%Y-%m-%d')
    return x_str





def plot_candle(stock,start_date,ax1,ax2):
    data = ts.get_h_data(stock, start=start_date)
    sh_data = data.sort_index()
    print(sh_data)

    close_arr = sh_data['close'].values
    stock_array = np.array(sh_data.reset_index()[['date', 'open', 'high', 'low', 'close']])
    stock_array[:, 0] = date2num(pd.to_datetime(stock_array[:, 0]).to_pydatetime())

    x = stock_array[:, 0]
    x_min = np.min(x)
    x_max = np.max(x)
    ax1.set_xlim(x_min, x_max)
    ax2.set_xlim(x_min, x_max)
    volume_arr = sh_data['volume'].values



def pandas_candlestick_ohlc(stock):
    # 设置绘图参数，主要是坐标轴

    fig = plt.figure()
    fig_manager = plt.get_current_fig_manager()
    fig_manager.window.showMaximized()
    fig.canvas.set_window_title(stock)
    np.seterr(all='ignore')
    rcParams['figure.figsize'] = (14, 6)
    rcParams['axes.xmargin'] = 0

    ax1 = plt.subplot2grid((4, 1), (0, 0), rowspan=3)
    ax2 = plt.subplot2grid((4, 1), (3, 0))

    start_date = get_start_date()

    cursor = plot_candle(stock, start_date, ax1, ax2)

    ax1.legend(loc="best")
    ax1.xaxis_date()
    ax2.xaxis_date()
    ax1.can_zoom()
    ax1.can_pan()
    ax1.autoscale_view()
    ax2.can_zoom()
    ax2.can_pan()
    ax2.autoscale_view()
    ax1.grid(True)
    ax2.grid(True)



pandas_candlestick_ohlc('600352')
plt.show()

#002123 梦网荣信
#603019 中科曙光
#600649 城投控股
#000550 江铃汽车
#300005 探路者
#002657 中科金财
#001696 宗申动力
#002763 汇洁股份