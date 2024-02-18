from typing import List
from ...interface import IData
from ...packer.market.save_tick_list_param_data_packer import SaveTickListParamDataPacker


class SaveTickListParamData(IData):
    _PreClosePrice: float = -1.0

    def __init__(self,
                 market_name: str = '',
                 exchange_id: str = '',
                 instrument_id: str = '',
                 product_id: str = '',
                 trading_day: str = '',
                 pre_close_price: float = -1.0,
                 pre_settlement_price: float = -1.0,
                 pre_open_interest: float = -1.0,
                 upper_limit_price: float = -1.0,
                 lower_limit_price: float = -1.0,
                 action_day_list: List[str] = [],
                 trading_time_list: List[str] = [],
                 update_mill_sec_list: List[int] = [],
                 local_time_list: List[int] = [],
                 last_price_list: List[float] = [],
                 last_volume_list: List[int] = [],
                 bid_price_list: List[float] = [],
                 bid_volume_list: List[int] = [],
                 ask_price_list: List[float] = [],
                 ask_volume_list: List[int] = [],
                 avg_price_list: List[float] = [],
                 open_price_list: List[float] = [],
                 high_price_list: List[float] = [],
                 lower_price_list: List[float] = [],
                 total_turnover_list: List[float] = [],
                 total_volume_list: List[int] = [],
                 open_interest_list: List[float] = [],
                 close_price_list: List[float] = [],
                 settlement_price_list: List[float] = [],
                 total_value_list: List[float] = []
                 ):
        super().__init__(SaveTickListParamDataPacker(self))
        self._MarketName: str = market_name
        self._ExchangeID: str = exchange_id
        self._InstrumentID: str = instrument_id
        self._ProductID: str = product_id
        self._TradingDay: str = trading_day
        self._PreClosePrice: float = float(pre_close_price)
        self._PreSettlementPrice: float = pre_settlement_price
        self._PreOpenInterest: float = pre_open_interest
        self._UpperLimitPrice: float = upper_limit_price
        self._LowerLimitPrice: float = lower_limit_price
        self._ActionDayList: List[str] = action_day_list
        self._TradingTimeList: List[str] = trading_time_list
        self._UpdateMillSecList: List[int] = update_mill_sec_list
        self._LocalTimeList: List[int] = local_time_list
        self._LastPriceList: List[float] = last_price_list
        self._LastVolumeList: List[int] = last_volume_list
        self._BidPriceList: List[float] = bid_price_list
        self._BidVolumeList: List[int] = bid_volume_list
        self._AskPriceList: List[float] = ask_price_list
        self._AskVolumeList: List[int] = ask_volume_list
        self._AvgPriceList: List[float] = avg_price_list
        self._OpenPriceList: List[float] = open_price_list
        self._HighPriceList: List[float] = high_price_list
        self._LowerPriceList: List[float] = lower_price_list
        self._TotalTurnoverList: List[float] = total_turnover_list
        self._TotalVolumeList: List[int] = total_volume_list
        self._OpenInterestList: List[float] = open_interest_list
        self._ClosePriceList: List[float] = close_price_list
        self._SettlementPriceList: List[float] = settlement_price_list
        self._TotalValueList: List[float] = total_value_list

    @property
    def MarketName(self):
        return self._MarketName

    @MarketName.setter
    def MarketName(self, value: str):
        self._MarketName = value

    @property
    def ExchangeID(self):
        return self._ExchangeID

    @ExchangeID.setter
    def ExchangeID(self, value: str):
        self._ExchangeID = value

    @property
    def InstrumentID(self):
        return self._InstrumentID

    @InstrumentID.setter
    def InstrumentID(self, value: str):
        self._InstrumentID = value

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, value: str):
        self._ProductID = value

    @property
    def TradingDay(self):
        return self._TradingDay

    @TradingDay.setter
    def TradingDay(self, value: str):
        self._TradingDay = value

    @property
    def PreClosePrice(self):
        return self._PreClosePrice

    @PreClosePrice.setter
    def PreClosePrice(self, value: float):
        self._PreClosePrice = value

    @property
    def PreSettlementPrice(self):
        return self._PreSettlementPrice

    @PreSettlementPrice.setter
    def PreSettlementPrice(self, value: float):
        self._PreSettlementPrice = value

    @property
    def PreOpenInterest(self):
        return self._PreOpenInterest

    @PreOpenInterest.setter
    def PreOpenInterest(self, value: float):
        self._PreOpenInterest = value

    @property
    def UpperLimitPrice(self):
        return self._UpperLimitPrice

    @UpperLimitPrice.setter
    def UpperLimitPrice(self, value: float):
        self._UpperLimitPrice = value

    @property
    def LowerLimitPrice(self):
        return self._LowerLimitPrice

    @LowerLimitPrice.setter
    def LowerLimitPrice(self, value: float):
        self._LowerLimitPrice = value

    @property
    def ActionDayList(self):
        return self._ActionDayList

    @ActionDayList.setter
    def ActionDay(self, value: List[str]):
        self._ActionDayList = value

    @property
    def TradingTimeList(self):
        return self._TradingTimeList

    @TradingTimeList.setter
    def TradingTimeList(self, value: List[str]):
        self._TradingTimeList = value

    @property
    def UpdateMillSecList(self):
        return self._UpdateMillSecList

    @UpdateMillSecList.setter
    def UpdateMillSecList(self, value: List[int]):
        self._UpdateMillSecList = value

    @property
    def LocalTimeList(self):
        return self._LocalTimeList

    @LocalTimeList.setter
    def LocalTimeList(self, value: List[int]):
        self._LocalTimeList = value

    @property
    def LastPriceList(self):
        return self._LastPriceList

    @LastPriceList.setter
    def LastPriceList(self, value: List[float]):
        self._LastPriceList = value

    @property
    def LastVolumeList(self):
        return self._LastVolumeList

    @LastVolumeList.setter
    def LastVolumeList(self, value: List[int]):
        self._LastVolumeList = value

    @property
    def BidPriceList(self):
        return self._BidPriceList

    @BidPriceList.setter
    def BidPriceList(self, value: List[float]):
        self._BidPriceList = value

    @property
    def BidVolumeList(self):
        return self._BidVolumeList

    @BidVolumeList.setter
    def BidVolumeList(self, value: List[int]):
        self._BidVolumeList = value

    @property
    def AskPriceList(self):
        return self._AskPriceList

    @AskPriceList.setter
    def AskPriceList(self, value: List[float]):
        self._AskPriceList = value

    @property
    def AskVolumeList(self):
        return self._AskVolumeList

    @AskVolumeList.setter
    def AskVolumeList(self, value: List[int]):
        self._AskVolumeList = value

    @property
    def AvgPriceList(self):
        return self._AvgPriceList

    @AvgPriceList.setter
    def AvgPriceList(self, value: List[float]):
        self._AvgPriceList = value

    @property
    def OpenPriceList(self):
        return self._OpenPriceList

    @OpenPriceList.setter
    def OpenPriceList(self, value: List[float]):
        self._OpenPriceList = value

    @property
    def HighPriceList(self):
        return self._HighPriceList

    @HighPriceList.setter
    def HighPriceList(self, value: List[float]):
        self._HighPriceList = value

    @property
    def LowerPriceList(self):
        return self._LowerPriceList

    @LowerPriceList.setter
    def LowerPriceList(self, value: List[float]):
        self._LowerPriceList = value

    @property
    def TotalTurnoverList(self):
        return self._TotalTurnoverList

    @TotalTurnoverList.setter
    def TotalTurnoverList(self, value: List[float]):
        self._TotalTurnoverList = value

    @property
    def TotalVolumeList(self):
        return self._TotalVolumeList

    @TotalVolumeList.setter
    def TotalVolumeList(self, value: List[int]):
        self._TotalVolumeList = value

    @property
    def OpenInterestList(self):
        return self._OpenInterestList

    @OpenInterestList.setter
    def OpenInterestList(self, value: List[float]):
        self._OpenInterestList = value

    @property
    def ClosePriceList(self):
        return self._ClosePriceList

    @ClosePriceList.setter
    def ClosePriceList(self, value: List[float]):
        self._ClosePriceList = value

    @property
    def SettlementPriceList(self):
        return self._SettlementPriceList

    @SettlementPriceList.setter
    def SettlementPriceList(self, value: List[float]):
        self._SettlementPriceList = value

    @property
    def TotalValueList(self):
        return self._TotalValueList

    @TotalValueList.setter
    def TotalValueList(self, value: List[float]):
        self._TotalValueList = value
