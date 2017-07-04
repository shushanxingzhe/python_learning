from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy as np
from funcat import *
from funcat.data.tushare_backend import TushareDataBackend


np.seterr(all='ignore')
rcParams['figure.figsize'] = (14, 6)

set_data_backend(TushareDataBackend())

set_start_date("2015-01-01")
S("000001.XSHG")  # 设置当前关注股票
#T("2016-06-01")   # 设置当前观察日期


ma3 = MA(C, 3)
ma5 = MA(C, 5)
ma6 = MA(C, 6)
ma8 = MA(C, 8)
ma10 = MA(C, 10)
ma15 = MA(C, 15)

buy_signal = CROSS(ma5, ma10)
sell_signal = CROSS(ma8, ma3)

plt.plot(C.series, label="close", linewidth=2)
plt.plot(ma5.series, label="ma5", alpha=0.7)
plt.plot(ma10.series, label="ma10", alpha=0.7)

plt.plot(np.where(buy_signal.series)[0], C.series[np.where(buy_signal.series)[0]], "^", label="buy", markersize=12, color="red")
plt.plot(np.where(sell_signal.series)[0], C.series[np.where(sell_signal.series)[0]], "v", label="sell", markersize=12, color="green")
plt.legend(loc="best")

plt.show()

