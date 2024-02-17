# -*- coding: utf-8 -*-
"""国内交易所及部分国外交易所枚举"""
from collections import namedtuple
from enum import auto, Enum
from typing import Dict, List
from .base import ByKey

# https://www.iso20022.org/market-identifier-codes
# https://www.tradinghours.com/mic?country[]=CN&page=1#results

field_names: List[str] = ['acronym', 'mic', 'en_name', 'cn_name', 'website']
ExchangeDetail = namedtuple(typename='ExchangeDetail', field_names=field_names, defaults=['', '', '', '', ''])
tsv: str = '''
BSE\tBJSE\tBEIJING STOCK EXCHANGE\t北京证券交易所\twww.bse.cn
CFFEX\tCCFX\tCHINA FINANCIAL FUTURES EXCHANGE\t中国金融期货交易所\twww.cffex.com.cn
NEEQ\tNEEQ\tNATIONAL EQUITIES EXCHANGE AND QUOTATIONS\t全国中小企业股份转让系统\twww.neeq.com.cn
SGE\tSGEX\tSHANGHAI GOLD EXCHANGE\t上海黄金交易所\twww.sge.sh
CFETS\tXCFE\tCHINA FOREIGN EXCHANGE TRADE SYSTEM\t中国外汇交易系统\twww.chinamoney.com.cn
SSE\tXSHG\tSHANGHAI STOCK EXCHANGE\t上海证券交易所\twww.szse.cn
SZSE\tXSHE\tSHENZHEN STOCK EXCHANGE\t深圳证券交易所\twww.szse.cn
CSI\t\tCHINA SECURITIES INDEX\t中证指数\twww.csindex.com.cn
SHFE\tXSGE\tSHANGHAI FUTURES EXCHANGE\t上海期货交易所\twww.shfe.com.cn
INE\tXINE\tSHANGHAI INTERNATIONAL ENERGY EXCHANGE\t上海国际能源交易中心\twww.ine.cn
DCE\tXDCE\tDALIAN COMMODITY EXCHANGE\t大连商品交易所\twww.dce.com.cn
ZCE\tXZCE\tZHENGZHOU COMMODITY EXCHANGE\t郑州商品交易所\twww.czce.com.cn
GFEX\tXGCE\tGUANGZHOU COMMODITY EXCHANGE\t广州商品交易所\twww.gfex.com.cn
CBOT\tCBTS\tCME SWAPS MARKETS (CBOT)\t芝加哥期货交易所\twww.cmegroup.com
COMEX\tCECS\tCME SWAPS MARKETS (COMEX)\t纽约商品交易所\twww.cmegroup.com
CME\tCMES\tCME SWAPS MARKETS (CME)\t芝加哥商业交易所\twww.cmegroup.com
NYMEX\tNYMS\tCME SWAPS MARKETS (NYMEX)\t纽约商品交易所\twww.cmegroup.com
NYBOT\t\tTHE NEW YORK BOARD OF TRADE\t纽约期货交易所\twww.nybot.com
LME\tXLME\tLONDON METAL EXCHANGE\t伦敦金属交易所\twww.lme.co.uk
TOCOM\tXTKT\tTOKYO COMMODITY EXCHANGE\t东京商品交易所\twww.tocom.or.jp
SICOM\tXSCE\tSINGAPORE COMMODITY EXCHANGE\t新加坡商品交易所\twww.sgx.com
HKEX\tXHKG\tHONG KONG EXCHANGES AND CLEARING LTD\t香港交易及结算所\twww.hkex.com.hk
NASDAQ\tXNAS\tNASDAQ - ALL MARKETS\t纳斯达克股票电子交易市场\twww.nasdaq.com
NYSE\tXNYS\tNEW YORK STOCK EXCHANGE, INC.\t纽约证券交易所\twww.nyse.com
AMEX\tXASE\tNYSE MKT LLC\t美国证券交易所\twww.nyse.com
LSE\tXLON\tLONDON STOCK EXCHANGE\t伦敦证券交易所\twww.lodonstockexchange.com
SIX\tXSWX\tSIX SWISS EXCHANGE\t瑞士证券交易所\twww.six-group.com
ICE\t\tINTERCONTINENTAL EXCHANGE\t洲际交易所\twww.theice.com
BMD\tXKLS\tBURSA MALAYSIA DERIVATIVES\t马来西亚衍生品交易所\twww.bursamalaysia.com
SGX\tXSES\tSINGAPORE EXCHANGE\t新加坡交易所\twww.sgx.com
'''

Items: List[ExchangeDetail] = [ExchangeDetail(*line.strip().split('\t')) for line in tsv.splitlines() if line]


class ByAcronym(ByKey):
    map: Dict[str, ExchangeDetail] = {getattr(item, field_names[0]): item for item in Items}


class Exchange(Enum):
    """交易所简称枚举"""
    BSE = ByAcronym.map['BSE']
    CFFEX = ByAcronym.map['CFFEX']
    NEEQ = ByAcronym.map['NEEQ']
    SGE = ByAcronym.map['SGE']
    CFETS = ByAcronym.map['CFETS']
    SSE = ByAcronym.map['SSE']
    SZSE = ByAcronym.map['SZSE']
    CSI = ByAcronym.map['CSI']
    SHFE = ByAcronym.map['SHFE']
    INE = ByAcronym.map['INE']
    DCE = ByAcronym.map['DCE']
    ZCE = ByAcronym.map['ZCE']
    GFEX = ByAcronym.map['GFEX']
    CBOT = ByAcronym.map['CBOT']
    COMEX = ByAcronym.map['COMEX']
    CME = ByAcronym.map['CME']
    NYMEX = ByAcronym.map['NYMEX']
    NYBOT = ByAcronym.map['NYBOT']
    LME = ByAcronym.map['LME']
    TOCOM = ByAcronym.map['TOCOM']
    SICOM = ByAcronym.map['SICOM']
    HKEX = ByAcronym.map['HKEX']
    NASDAQ = ByAcronym.map['NASDAQ']
    NYSE = ByAcronym.map['NYSE']
    AMEX = ByAcronym.map['AMEX']
    LSE = ByAcronym.map['LSE']
    SIX = ByAcronym.map['SIX']
    ICE = ByAcronym.map['ICE']
    BMD = ByAcronym.map['BMD']
    SGX = ByAcronym.map['SGX']


# 数据完整性和一致性检验
ByAcronym.check(obj=Exchange)
