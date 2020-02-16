from norgatedata import StockPriceAdjustmentType
from zipline_norgatedata import (
    register_norgatedata_equities_bundle,
    register_norgatedata_futures_bundle )

# DJIA Bundle for backtesting including all current & past constituents back to 1970-01
# and the DJIA Total Return index (useful for benchmarking and/or index trend filtering)
# (around 70 securities) [Jan 1950]
register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-dji',
    symbol_list = ['$DJITR'],
    watchlists = ['Dow Jones Industrial Average Current & Past'],
    start_session = '1970-01-01',
)

# Nasdaq 100 Bundle for backtesting including all current & past constituents back to 1995-01
# and the Nasdaq 100 Total Return index (useful for benchmarking and/or index trend filtering)
# (around 385 securities) [Jan 1995]
register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-nasdaq100',
    symbol_list = ['$NDXTR'],
    watchlists = ['NASDAQ 100 Current & Past'],
    start_session = '1995-01-01',
)

# S&P 100 Bundle for backtesting including all current & past constituents back to 1989
# and the S&P 100 Total Return index (useful for benchmarking and/or index trend filtering)
# (around 225 securities) [Sep 1989]
register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-sp100',
    symbol_list = ['$OEXTR'],
    watchlists = ['S&P 100 Current & Past'],
    start_session = '1989-09-01',
)

# S&P 500 Bundle for backtesting including all current & past constituents back to 1970
# and the S&P 500 Total Return index (useful for benchmarking and/or index trend filtering)
# (around 1800 securities) [Sep 1962]
register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-sp500',
    symbol_list = ['$SPXTR','$SPXTR1970','$SPXTR1936','$SPXATR','$SPXDTR','$SPXSTR','$SPXETR','$SPXFTR','$SPXITR','$SPXMTR','$SPXLTR','$SPXUTR','$SPXTTR','$SPXRTR'],
    watchlists = ['S&P 500 Current & Past'],
    start_session = '1970-01-01',
)

# S&P 400 Bundle for backtesting including all current & past constituents back to 1991-06
# and the S&P 400 Total Return index (useful for benchmarking and/or index trend filtering)
# (around 1500 securities) [Jun 1991]
register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-sp400',
    symbol_list = ['$MIDTR'],
    watchlists = ['S&P MidCap 400 Current & Past'],
    start_session = '1991-06-01',
)

# S&P 600 Bundle for backtesting including all current & past constituents back to 1994-10
# and the S&P 600 Total Return index (useful for benchmarking and/or index trend filtering)
# (around 2200 securities) [Oct 1994]
register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-sp600',
    symbol_list = ['$SMLTR'],
    watchlists = ['S&P SmallCap 600 Current & Past'],
    start_session = '1994-10-01',
)

# S&P 1500 Bundle for backtesting including all current & past constituents back to 1994-11
# and the S&P 1500 Total Return index (useful for benchmarking and/or index trend filtering)
# (around 3750 securities) [Nov 1994]
register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-sp1500',
    symbol_list = ['$SP1500TR','$SP1500ETR','$SP1500MTR','$SP1500ITR','$SP1500DTR','$SP1500STR','$SP1500ATR','$SP1500FTR','$SP1500TTR','$SP1500LTR','$SP1500UTR','$SP1500RTR','$SPXTR','$MIDTR','$SMLTR','$SPXTR1970','$SPXTR1936'],
    watchlists = ['S&P Composite 1500 Current & Past'],
    start_session = '1994-11-01',
)

# Russell 1000 bundle containing all current & past constituents back to 1990-07
# and the Russell 1000 Total Return Index (useful for benchmarking and/or index trend filtering)
# (about 3220 securities) [Jul 1990]

register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-r1000',
    watchlists = ['Russell 1000 Current & Past'],
    symbol_list = ['$RUITR'],
    start_session = '1990-07-01' ,
)

# Russell 2000 bundle containing all current & past constituents back to 1990-07
# and the Russell 2000 Total Return Index (useful for benchmarking and/or index trend filtering)
# (about 9860 securities) [Jul 1990]

register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-r2000',
    watchlists = ['Russell 2000 Current & Past'],
    symbol_list = ['$RUTTR'],
    start_session = '1990-07-01' ,
)

# Russell 3000 bundle containing all current & past constituents back to 1990-07
# and the Russell 3000 Total Return Index (useful for benchmarking and/or index trend filtering)
# (about 11000 securities) [Jul 1990]

register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-r3000',
    watchlists = ['Russell 3000 Current & Past'],
    symbol_list = ['$RUATR'],
    start_session = '1990-07-01' ,
)

# ETF
register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-etf',	
    watchlists = ['ETF Current & Past'],
    symbol_list = ['$SPXTR','$SPXTR1970','$SPXTR1936','$MIDTR','$SMLTR','$RUITR','$RUTTR','$RUATR','$SPXATR','$SPXDTR','$SPXSTR','$SPXETR','$SPXFTR','$SPXITR','$SPXMTR','$SPXLTR','$SPXUTR','$SPXTTR','$SPXRTR'],
    start_session = '1993-01-29',
)

# Select Sector SPDR ETF
register_norgatedata_equities_bundle(
    bundlename = 'norgate-select-sector-spdr',
    symbol_list = ['SPY','XLI','XLU','XLP','XLF','XLY','XLV','XLK','XLE','XLB','XLRE','XLC','$SPXATR','$SPXDTR','$SPXSTR','$SPXETR','$SPXFTR','$SPXITR','$SPXMTR','$SPXLTR','$SPXUTR','$SPXTTR','$SPXRTR'],
    start_session = '1998-12-16',
)

# iShares US Sector ETF
register_norgatedata_equities_bundle(
    bundlename = 'norgate-us-sector-ishares',
    symbol_list = ['IVV','IYE','IYZ','IYJ','IYW','IYF','IYG','IDU','IYK','IYC','IYR','IYH','IYM','$SPXATR','$SPXDTR','$SPXSTR','$SPXETR','$SPXFTR','$SPXITR','$SPXMTR','$SPXLTR','$SPXUTR','$SPXTTR','$SPXRTR'], 
    start_session = '2000-06-12',
)

# iShares Global Sector ETF
register_norgatedata_equities_bundle(
    bundlename = 'norgate-global-sector-ishares',
    symbol_list = ['IXN','IXC','IXJ','IXP','IXG','JXI','KXI','MXI','RXI','EXI','IGF','REET'], 
    start_session = '2000-06-12',
)

# Fixed Income ETF
register_norgatedata_equities_bundle(
    bundlename = 'norgate-fi-etf',
    symbol_list = ['IGOV','EMHY','CEMB','HYEM','VWOB','EMB','PCY','EMLC','LEMB','EBND','TOTL',
	'PGHY','BNDW','STOT','GSY','SRLN','IAGG','BNDX','WIP','BWX','IUSB','SPAB','BND','AGG',
	'FLRN','FLOT','BIV','GVI','BLV','BSV','NEAR','ICSH','ISTB','CMBS','ANGL','JNK','HYG',
	'USHY','BKLN','SJNK','SHYG','USIG','LQD','VCIT','SPIB','IGIB','IGLB','IGHG','VCLT',
	'SPLB','IGSB','SLQD','VCSH','SPSB','CWB','ICVT','PSK','PGF','PFF','PFXF','VRP','PGX',
	'SPIP','TIP','STIP','VTIP','HYD','HYMB','MUB','VTEB','ITM','SUB','SHM','VMBS','MBB',
	'GOVT','IEF','VGIT','IEI','SPTI','TLH','EDV','VGLT','SPTL','TLT','SPTS','SHY','VGSH',
	'SHV','CLTL','BIL','SJB','TBX','PST','TBF','TTT','TBT','UJB','UST','UBT'], 
    start_session = '2002-07-26',
)

# Equity ETF
register_norgatedata_equities_bundle(
    bundlename = 'norgate-eq-etf',
    symbol_list = ['SPY','IVV','VTI','VOO','QQQ','VEA','IEFA','VWO','EFA','IEMG','VTV','IJH',
	'IJR','IWM','VIG','VNQ','USMV','VO','EEM','VB','XLF','XLK','VEU','ITOT','VGT','DIA',
	'IWB','IWR','SCHF','SDY','SCHX','MDY','XLV','DVY','IXUS','VXUS','SCHB','VV','EWJ',
	'VBR','XLY','VGK','XLP','EFAV','VT','SPLV','IWS','XLU','XLI','SCHD','ACWI','XLE',
	'SCZ','IWV','VHT','EWZ','SCHA','VXF','VFH','AMLP','SCHM','SCHE','XLC','EZU','SCHH',
	'VNQI','ITA','ACWV','EEMV','VSS','OEF','VDC','INDA','SPDW','IYW','IDV','IYR','IHI',
	'FXI','EWY','VPU','XBI','MCHI','ACWX','SPTM','AAXJ','XLRE','IEUR','VPL','VIS','XLB',
	'IGF','EWT','SPLG','IXN','SPEM','VCR','VDE','EWC','FTEC','IGV','RWR','EWU','ICF',
	'XSLV','EPP','RWX','RWO','FEZ','EWG','VOX','IOO','SOXX','IYH','XOP','IXJ','VAW',
	'VIOO','FNCL','IDU','IDLV','FREL','IYC','IVOO','IYJ','EWP','LGLV','KIE','FUTY','IXC',
	'IHF','GWX','KXI','URTH','IWC','XHB','EWW','INDY','ESGE','FDIS','MOO','NANR','KSA',
	'ERUS','OIH','SPXU','REZ','ONEV','IYE','FSTA','XHE','EWS','EWX','IYT','THD','EWM',
	'EIDO','FM','IYK','VTHR','FCOM','GMF','FIDU','EEMA','XME','SPYX','XSD','SMMV','GII',
	'EZA','FENY','IFGL','TUR','ECH','IEUS','XTN','EWZS','EIS','SCJ','WPS'], 
    start_session = '1993-01-29',
)

# Equity & Fixed Income ETF
register_norgatedata_equities_bundle(
    bundlename = 'norgate-eq-fi-etf',
    symbol_list = ['SPY','IVV','VTI','VOO','QQQ','VEA','IEFA','VWO','EFA','IEMG','VTV','IJH',
	'IJR','IWM','VIG','VNQ','USMV','VO','EEM','VB','XLF','XLK','VEU','ITOT','VGT','DIA',
	'IWB','IWR','SCHF','SDY','SCHX','MDY','XLV','DVY','IXUS','VXUS','SCHB','VV','EWJ',
	'VBR','XLY','VGK','XLP','EFAV','VT','SPLV','IWS','XLU','XLI','SCHD','ACWI','XLE',
	'SCZ','IWV','VHT','EWZ','SCHA','VXF','VFH','AMLP','SCHM','SCHE','XLC','EZU','SCHH',
	'VNQI','ITA','ACWV','EEMV','VSS','OEF','VDC','INDA','SPDW','IYW','IDV','IYR','IHI',
	'FXI','EWY','VPU','XBI','MCHI','ACWX','SPTM','AAXJ','XLRE','IEUR','VPL','VIS','XLB',
	'IGF','EWT','SPLG','IXN','SPEM','VCR','VDE','EWC','FTEC','IGV','RWR','EWU','ICF',
	'XSLV','EPP','RWX','RWO','FEZ','EWG','VOX','IOO','SOXX','IYH','XOP','IXJ','VAW',
	'VIOO','FNCL','IDU','IDLV','FREL','IYC','IVOO','IYJ','EWP','LGLV','KIE','FUTY','IXC',
	'IHF','GWX','KXI','URTH','IWC','XHB','EWW','INDY','ESGE','FDIS','MOO','NANR','KSA',
	'ERUS','OIH','SPXU','REZ','ONEV','IYE','FSTA','XHE','EWS','EWX','IYT','THD','EWM',
	'EIDO','FM','IYK','VTHR','FCOM','GMF','FIDU','EEMA','XME','SPYX','XSD','SMMV','GII',
	'EZA','FENY','IFGL','TUR','ECH','IEUS','XTN','EWZS','EIS','SCJ','WPS',
	'IGOV','EMHY','CEMB','HYEM','VWOB','EMB','PCY','EMLC','LEMB','EBND','TOTL',
	'PGHY','BNDW','STOT','GSY','SRLN','IAGG','BNDX','WIP','BWX','IUSB','SPAB','BND','AGG',
	'FLRN','FLOT','BIV','GVI','BLV','BSV','NEAR','ICSH','ISTB','CMBS','ANGL','JNK','HYG',
	'USHY','BKLN','SJNK','SHYG','USIG','LQD','VCIT','SPIB','IGIB','IGLB','IGHG','VCLT',
	'SPLB','IGSB','SLQD','VCSH','SPSB','CWB','ICVT','PSK','PGF','PFF','PFXF','VRP','PGX',
	'SPIP','TIP','STIP','VTIP','HYD','HYMB','MUB','VTEB','ITM','SUB','SHM','VMBS','MBB',
	'GOVT','IEF','VGIT','IEI','SPTI','TLH','EDV','VGLT','SPTL','TLT','SPTS','SHY','VGSH',
	'SHV','CLTL','BIL','SJB','TBX','PST','TBF','TTT','TBT','UJB','UST','UBT',
	'$SPXATR','$SPXDTR','$SPXSTR','$SPXETR','$SPXFTR','$SPXITR','$SPXMTR','$SPXLTR','$SPXUTR',
	'$SPXTTR','$SPXRTR','$SPXTR'], 
    start_session = '1993-01-29',
)

register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-sp-etf-fi',
    symbol_list = ['$SPXTR','$SPXTR1970','$SPXTR1936','$MIDTR','$SMLTR','$RUITR','$RUTTR','$RUATR','$SPXATR','$SPXDTR','$SPXSTR','$SPXETR','$SPXFTR','$SPXITR','$SPXMTR','$SPXLTR','$SPXUTR','$SPXTTR','$SPXRTR','SHV','SHY','IEI','IEF','TLH','TLT','AGG','TIP','LQD','HYG','MBB','REM','REET','EMB','LEMB','FLOT','IGSB','USIG','IGIB'],
    watchlists = ['S&P 500 Current & Past','S&P MidCap 400 Current & Past','S&P SmallCap 600 Current & Past'],
    start_session = '1970-01-01',
)

register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-sp-etf',
    symbol_list = ['$SPXTR','$SPXTR1970','$SPXTR1936','$MIDTR','$SMLTR','$RUITR','$RUTTR','$RUATR','$SPXATR','$SPXDTR','$SPXSTR','$SPXETR','$SPXFTR','$SPXITR','$SPXMTR','$SPXLTR','$SPXUTR','$SPXTTR','$SPXRTR'],
    watchlists = ['S&P 500 Current & Past','S&P MidCap 400 Current & Past','S&P SmallCap 600 Current & Past','ETF Current & Past'],
    start_session = '1970-01-01',
)

register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-sp500-etf',
    symbol_list = ['$SPXTR','$SPXTR1970','$SPXTR1936','$SPXATR','$SPXDTR','$SPXSTR','$SPXETR','$SPXFTR','$SPXITR','$SPXMTR','$SPXLTR','$SPXUTR','$SPXTTR','$SPXRTR'],
    watchlists = ['S&P 500 Current & Past','ETF Current & Past'],
    start_session = '1970-01-01',
)

register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-all-eq',
    symbol_list = ['$SPXTR','$SPXTR1970','$SPXTR1936','$SPXATR','$SPXDTR','$SPXSTR','$SPXETR','$SPXFTR','$SPXITR','$SPXMTR','$SPXLTR','$SPXUTR','$SPXTTR','$SPXRTR'],
    watchlists = ['All EQ Current & Past'],
    start_session = '1970-01-01',
)

register_norgatedata_equities_bundle(
    bundlename = 'norgatedata-all-eq-dr',
    symbol_list = ['$SPXTR','$SPXTR1970','$SPXTR1936','$SPXATR','$SPXDTR','$SPXSTR','$SPXETR','$SPXFTR','$SPXITR','$SPXMTR','$SPXLTR','$SPXUTR','$SPXTTR','$SPXRTR'],
    watchlists = ['All EQ DR Current & Past'],
    start_session = '1970-01-01',
)

import pandas as pd

from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities

start_session = pd.Timestamp('1990-1-2', tz='utc')
end_session = pd.Timestamp('2019-11-22', tz='utc')

inputDirectory='F:/marketData/global_monitoring/premium/zipline/SP500/raw/'

register(
    'custom-sp500-bundle',
    csvdir_equities(
        ['daily'],
        inputDirectory,
    ),
    calendar_name='NYSE', # US equities
    start_session=start_session,
)
