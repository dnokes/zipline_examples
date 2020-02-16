#
# Copyright 2013 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#import pandas as pd
#import requests
#
#
#def get_benchmark_returns(symbol):
#    """
#    Get a Series of benchmark returns from IEX associated with `symbol`.
#    Default is `SPY`.
#
#    Parameters
#    ----------
#    symbol : str
#        Benchmark symbol for which we're getting the returns.
#
#    The data is provided by IEX (https://iextrading.com/), and we can
#    get up to 5 years worth of data.
#    """
#    r = requests.get(
#        'https://api.iextrading.com/1.0/stock/{}/chart/5y'.format(symbol)
#    )
#    data = r.json()
#
#    df = pd.DataFrame(data)
#
#    df.index = pd.DatetimeIndex(df['date'])
#    df = df['close']
#
#    return df.sort_index().tz_localize('UTC').pct_change(1).iloc[1:]


import pandas as pd
import requests
from trading_calendars import get_calendar

# Clenow fix - turns off benchmark
# Modified to avoid downloading data from obsolete IEX interface
def get_benchmark_returns(symbol):
    cal = get_calendar('NYSE')
    first_date = pd.Timestamp('1896-01-01', tz='utc')
    last_date = pd.Timestamp.today(tz='utc')
    dates = cal.sessions_in_range(first_date, last_date)
    data = pd.DataFrame(0.0, index=dates, columns=['close'])
    data = data['close']
    return data.sort_index().iloc[1:]

#import norgatedata
#
# custom norgate fix - did not work
#def get_benchmark_returns(symbol):
#    # define Norgate start date
#    startDate='1900-01-01'
#    # define time series format to pandas dataframe
#    timeseriesformat = 'pandas-dataframe'
#    # define price adjustment setting to unadjusted
#    padding_setting = norgatedata.PaddingType.NONE
#    # fetch unadjusted time series
#    df = norgatedata.price_timeseries(symbol,
#        stock_price_adjustment_setting = priceAdjustmentSettingNone,
#        padding_setting = padding_setting,
#        start_date = startDate,
#        format=timeseriesformat)
#    # return sorted returns with datetime converted to UTC
#    return df.sort_index().tz_localize('UTC').pct_change(1).iloc[1:]
