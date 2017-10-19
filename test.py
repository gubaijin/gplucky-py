import tushare as ts
import threading
# print ts.get_hist_data('600848');

def fun_timer():
    df = ts.get_realtime_quotes('300699') #Single stock symbol
    print df[['code','name','price','time']];
    timer = threading.Timer(2, fun_timer);
    timer.start();

timer = threading.Timer(2, fun_timer);
timer.start();