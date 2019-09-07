#!/usr/bin/python3.5

import numpy as np
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from talib import MA
from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import date2num, num2date
from datetime import timedelta,datetime


def get_start_date(start_date='', gettype='down'):

    if not start_date:
        diff = 200
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


class Cursor(object):
    def __init__(self, ax1, ax2, sh_data, stock, start_date):
        self.ax1 = ax1
        self.ax2 = ax2
        self.stock = stock
        self.start_date = start_date
        self.ly1 = ax1.axvline(color='k')  # the vert line
        self.ly2 = ax2.axvline(color='k')  # the vert line
        self.sh_data = sh_data
        self.xdata = 0
        self.ydata = 0
        self.max_x = self.ax1.get_xlim()[1]
        self.max_y = self.ax1.get_ylim()[1]

        # text location in axes coords
        self.txt1 = ax1.text(0.7, 0.9, '', transform=ax1.transAxes)
        self.txt2 = ax2.text(0.7, 0.9, '', transform=ax2.transAxes)

    def mouse_move(self, event):
        if not event.inaxes:
            return

        x, y = event.xdata, event.ydata
        self.ly1.set_xdata(x)
        self.ly2.set_xdata(x)
        self.xdata = x
        self.ydata = y

        x_date = num2date(x)
        x_str = x_date.strftime('%Y-%m-%d')

        indexs = self.sh_data.index
        if x_str not in indexs :
            return

        close = self.sh_data.loc[x_str,'close']
        volume = self.sh_data.loc[x_str, 'volume']
        volume = volume / 1000000

        self.txt1.set_text('x=%s, y=%1.2f' % (x_str, close))
        self.txt2.set_text('x=%s, y=%1.2f' % (x_str, volume))
        plt.draw()

    def key_release(self, event):

        if event.key == 'down':
            self.start_date = get_start_date(self.start_date)
            plot_candle(self.stock, self.start_date, self.ax1, self.ax2)
            return
        elif event.key == 'up':
            self.start_date = get_start_date(self.start_date, 'up')
            plot_candle(self.stock, self.start_date, self.ax1, self.ax2)
            return

        x, y = self.xdata, self.ydata
        if x <= 0 or y <= 0 or x >= self.max_x or y > self.max_y:
            return
        oneday = timedelta(days=1)
        x_date = num2date(x)
        if event.key == 'right':
            x_date = x_date + oneday
        elif event.key == 'left':
            x_date = x_date - oneday

        x_str = x_date.strftime('%Y-%m-%d')

        indexs = self.sh_data.index

        while x_str not in indexs:

            if event.key == 'right':
                x_date = x_date + oneday
            elif event.key == 'left':
                x_date = x_date - oneday

            x_str = x_date.strftime('%Y-%m-%d')

        x = date2num(x_date)
        self.xdata, self.ydata = x, y
        self.ly1.set_xdata(x)
        self.ly2.set_xdata(x)

        close = self.sh_data.loc[x_str, 'close']
        volume = self.sh_data.loc[x_str, 'volume']
        volume = volume / 1000000

        self.txt1.set_text('x=%s, y=%1.2f' % (x_str, close))
        self.txt2.set_text('x=%s, y=%1.2f' % (x_str, volume))
        plt.draw()


def fit_series(s1, s2):
    size = min(len(s1), len(s2))
    if size == 0:
        raise Exception("series size == 0")
    s1, s2 = s1[-size:], s2[-size:]
    return s1, s2


def CrossOver(s1, s2):
    """s1金叉s2
    :param s1:
    :param s2:
    :returns: bool序列
    :rtype: BoolSeries
    """

    series1, series2 = fit_series(s1, s2)
    cond1 = series1 > series2
    cond2 = series1 <= series2  # s1[1].series <= s2[1].series
    cond1 = np.roll(cond1, -1)
    cond1, cond2 = fit_series(cond1, cond2)
    s = cond1 & cond2
    return s


def plot_candle(stock,start_date,ax1,ax2):
    data = ts.get_hist_data(stock, start=start_date)
    sh_data = data.sort_index()

    close_arr = sh_data['close'].values
    stock_array = np.array(sh_data.reset_index()[['date', 'open', 'high', 'low', 'close']])
    stock_array[:, 0] = date2num(pd.to_datetime(stock_array[:, 0]).to_pydatetime())

    x = stock_array[:, 0]
    x_min = np.min(x)
    x_max = np.max(x)
    ax1.set_xlim(x_min, x_max)
    ax2.set_xlim(x_min, x_max)

    ma3 = MA(close_arr, 3)
    ma6 = MA(close_arr, 6)
    ma8 = MA(close_arr, 8)
    buy_signal = CrossOver(ma3, ma6)
    sell_signal = CrossOver(ma6, ma3)

    volume_arr = sh_data['volume'].values

    v_ma4 = MA(volume_arr, 4)
    v_ma5 = MA(volume_arr, 5)
    v_ma7 = MA(volume_arr, 7)
    v_ma10 = MA(volume_arr, 10)

    v_buy_signal = CrossOver(v_ma4, v_ma7)
    v_sell_signal = CrossOver(v_ma7, v_ma4)

    # ax1.plot(close_arr, label="close", linewidth=2)
    ax1.plot(x, ma3, label="ma3", alpha=0.7)
    ax1.plot(x, ma8, label="ma8", alpha=0.7)

    ax1.plot(x[np.where(buy_signal)[0]], sh_data['close'][np.where(buy_signal)[0]], "^", label="buy", markersize=12,
             color="red")
    ax1.plot(x[np.where(sell_signal)[0]], sh_data['close'][np.where(sell_signal)[0]], "v", label="sell", markersize=12,
             color="green")

    ax2.bar(x, volume_arr)
    ax2.plot(x, v_ma5, label="ma5", alpha=0.7)
    ax2.plot(x, v_ma10, label="ma10", alpha=0.7)
    ax2.plot(x[np.where(v_buy_signal)[0]], sh_data['volume'][np.where(v_buy_signal)[0]], "^", label="buy",
             markersize=12,
             color="red")
    ax2.plot(x[np.where(v_sell_signal)[0]], sh_data['volume'][np.where(v_sell_signal)[0]], "v", label="sell",
             markersize=12, color="green")

    candlestick_ohlc(ax1, stock_array, colorup="red", colordown="green", width=0.4)
    cursor = Cursor(ax1, ax2, sh_data, stock, start_date)
    return cursor


def pandas_candlestick_ohlc(stock):
    # 设置绘图参数，主要是坐标轴

    np.seterr(all='ignore')
    rcParams['figure.figsize'] = (20, 12)
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

    plt.connect('motion_notify_event', cursor.mouse_move)
    plt.connect('key_release_event', cursor.key_release)

    plt.show()


pandas_candlestick_ohlc('sh')
#pandas_candlestick_ohlc('600649')
