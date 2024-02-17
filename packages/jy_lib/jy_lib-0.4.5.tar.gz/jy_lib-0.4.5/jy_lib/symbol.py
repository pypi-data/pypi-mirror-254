# -*- coding: utf-8 -*-
"""国内外交易品种类型枚举"""
from dataclasses import dataclass
from enum import Enum


class SymbolSubType(Enum):
    def parent(self) -> 'SymbolType':
        """获取当前的父类型"""
        return SymbolType(self.__class__)


class StockType(SymbolSubType):
    """股票"""
    STOCK_A = '以人民币交易的股票（主板）'  # 主板A股 SH:ASH
    STOCK_B = '以美元交易的股票'  # 主板B股 SH:BSH
    STOCK_K = '以人民币交易的股票（科创板）'  # 科创板 SH:KSH
    STOCK_G = '创业板'  # 创业板GEM SZ:GEM
    STOCK_P = '优先股'  # SH:OPS,PPS SZ:33
    STOCK_OTHER = '其它股票'  # SH:OEQ,OPS,PPS


class FundType(SymbolSubType):
    """基金"""
    FUND_CLOSE = '封闭式基金'  # SH:CEF
    FUND_OPEN = '开放式基金'  # SH:OEF
    FUND_ETF = '交易所交易基金'  # SH:EBS
    FUND_LOF = 'LOF基金'  # SH:LOF
    FUND_REITS = '公募REITs'  # SH:RET
    FUND_STOCK = '股票基金'
    FUND_BOND = '债券型基金'
    FUND_DERIVATIVES = '衍生品基金'
    FUND_HYBRID = '混合型基金'
    FUND_FOF = 'FOF基金'
    FUND_OTHER = '其它基金'  # SH:OFN


class BondType(SymbolSubType):
    """债券"""
    BOND_NATIONAL = '国债、地方债、政府支持债、政策性金融债'  # SH:GBF
    BOND_ENTERPRISE = '企业债'  # SH:CBF
    BOND_CONVERTIBLE = '可转换企业债'  # SH:CCF
    BOND_EXCHANGEABLE = '可交换债'
    BOND_COMPANY = '公司债、企业债、可交换债、政府支持债'  # SH:CPF
    BOND_BUYBACK = '质押式回购'  # SH:CRP SZ:12
    BOND_ABS = '资产支持证券'
    BOND_OTHER = '其它债券'  # SH:DST,DVP,OBD,WIT,QRP,AMP,TCB


class OptionsType(SymbolSubType):
    """期权"""
    OPTIONS_STOCK = '个股期权'  # SZ:29
    OPTIONS_ETF = 'ETF期权'  # SZ:30
    OPTIONS_INDEX = '指数期权'  # CFFEX
    OPTIONS_COMMODITY = '商品期权'
    OPTIONS_FOREX = '外汇期权'
    OPTIONS_OTHER = '其他期权'


class DrType(SymbolSubType):
    """存托凭证"""
    DR_GDR = '全球存托凭证'
    DR_OTHER = '其他存托凭证'


class IndexType(SymbolSubType):
    """指数"""
    INDEX_OTHER = '其他指数'


class FuturesType(SymbolSubType):
    """期货"""
    FUTURES_STOCK = '股票期货'
    FUTURES_INDEX = '指数期货'
    FUTURES_COMMODITY = '商品期货'
    FUTURES_BOND = '债券期货'
    FUTURES_OTHER = '其他期货'


class WarrantsType(SymbolSubType):
    """权证"""
    WARRANTS_CBBC = '牛熊证'
    WARRANTS_INLINE = '界内证'
    WARRANTS_OTHER = '其他权证'


class BlockType(SymbolSubType):
    """板块"""
    BLOCK_CONCEPT = '概念板块'
    BLOCK_REGION = '地域板块'
    BLOCK_INDUSTRY = '行业板块'
    BLOCK_OTHER = '其他板块'


class SpotType(SymbolSubType):
    """现货"""
    SPOT_COMMODITY = '商品现货'
    SPOT_OTHER = '其他现货'


class SymbolType(Enum):
    """基础类别"""
    STOCK = StockType
    BOND = BondType
    FUND = FundType
    INDEX = IndexType
    FUTURES = FuturesType
    OPTIONS = OptionsType
    WARRANTS = WarrantsType
    DR = DrType
    SPOT = SpotType
    BLOCK = BlockType


@dataclass
class SymbolFlag:
    is_st: bool | None = None                       # 风险警示=True
    is_new: bool | None = None                      # 新股=True
    is_approval: bool | None = None                 # 核准制=True
    is_registration: bool | None = None             # 注册制=True
    is_base_market: bool | None = None              # 基础层=True
    is_innovation_market: bool | None = None        # 创新层=True
    is_call_auction: bool | None = None             # 集合竞价=True
    is_market_making: bool | None = None            # 做市=True
    is_pt: bool | None = None                       # 两网及退市=True
    is_call: bool | None = None                     # 看涨=True
    is_put: bool | None = None                      # 看跌=True
    is_northbound: bool | None = None               # 北向=True
    is_southbound: bool | None = None               # 南向=True
    is_main_contract: bool | None = None            # 主力合约=True
    is_second_main_contract: bool | None = None     # 次主力合约=True
    is_main_perpetual_contract: bool | None = None          # 主力永续合约=True
    is_second_main_perpetual_contract: bool | None = None   # 次主力永续合约=True
