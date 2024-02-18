from typing import List
from ...interface import IData
from ...packer.market.save_ohlc_list_param_data_packer import SaveOHLCListParamDataPacker


class SaveOHLCListParamData(IData):
    def __init__(self, market_name: str = '', exchange_id: str = '', instrument_id: str = '',
                 range: int = 60, trading_day: str = '', pre_settlement_price: float = 0.0,
                 action_day_list: List[str] = [],
                 action_timespan_list: List[int] = [],
                 trading_time_list: List[str] = [],
                 start_time_list: List[str] = [],
                 end_time_list: List[str] = [],
                 total_turnover_list: List[float] = [],
                 open_interest_list: List[float] = [],
                 open_price_list: List[float] = [],
                 open_bid_price_list: List[float] = [],
                 open_ask_price_list: List[float] = [],
                 open_bid_volume_list: List[int] = [],
                 open_ask_volume_list: List[int] = [],
                 high_price_list: List[float] = [],
                 high_bid_price_list: List[float] = [],
                 high_ask_price_list: List[float] = [],
                 high_bid_volume_list: List[int] = [],
                 high_ask_volume_list: List[int] = [],
                 lower_price_list: List[float] = [],
                 lower_bid_price_list: List[float] = [],
                 lower_ask_price_list: List[float] = [],
                 lower_bid_volume_list: List[int] = [],
                 lower_ask_volume_list: List[int] = [],
                 close_price_list: List[float] = [],
                 close_bid_price_list: List[float] = [],
                 close_ask_price_list: List[float] = [],
                 close_bid_volume_list: List[int] = [],
                 close_ask_volume_list: List[int] = []
                 ):
        super().__init__(SaveOHLCListParamDataPacker(self))
        self._MarketName: str = market_name
        self._ExchangeID: str = exchange_id
        self._InstrumentID: str = instrument_id
        self._Range: int = range
        self._TradingDay: str = trading_day
        self._ActionDayList: List[str] = action_day_list
        self._PreSettlementPrice: float = pre_settlement_price
        self._ActionTimespanList: List[int] = action_timespan_list
        self._TradingTimeList: List[str] = trading_time_list
        self._StartTimeList: List[str] = start_time_list
        self._EndTimeList: List[str] = end_time_list
        self._TotalTurnoverList: List[float] = total_turnover_list
        self._OpenInterestList: List[float] = open_interest_list
        self._OpenPriceList: List[float] = open_price_list
        self._OpenBidPriceList: List[float] = open_bid_price_list
        self._OpenAskPriceList: List[float] = open_ask_price_list
        self._OpenBidVolumeList: List[int] = open_bid_volume_list
        self._OpenAskVolumeList: List[int] = open_ask_volume_list

        self._HighPriceList: List[float] = high_price_list
        self._HighBidPriceList: List[float] = high_bid_price_list
        self._HighAskPriceList: List[float] = high_ask_price_list
        self._HighBidVolumeList: List[int] = high_bid_volume_list
        self._HighAskVolumeList: List[int] = high_ask_volume_list

        self._LowerPriceList: List[float] = lower_price_list
        self._LowerBidPriceList: List[float] = lower_bid_price_list
        self._LowerAskPriceList: List[float] = lower_ask_price_list
        self._LowerBidVolumeList: List[int] = lower_bid_volume_list
        self._LowerAskVolumeList: List[int] = lower_ask_volume_list

        self._ClosePriceList: List[float] = close_price_list
        self._CloseBidPriceList: List[float] = close_bid_price_list
        self._CloseAskPriceList: List[float] = close_ask_price_list
        self._CloseBidVolumeList: List[int] = close_bid_volume_list
        self._CloseAskVolumeList: List[int] = close_ask_volume_list

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
    def Range(self):
        return self._Range

    @Range.setter
    def Range(self, value: int):
        self._Range = value

    @property
    def TradingDay(self):
        return self._TradingDay

    @TradingDay.setter
    def TradingDay(self, value: str):
        self._TradingDay = value

    @property
    def ActionDayList(self):
        return self._ActionDayList

    @ActionDayList.setter
    def ActionDayList(self, value: List[str]):
        self._ActionDayList = value

    @property
    def PreSettlementPrice(self):
        return self._PreSettlementPrice

    @PreSettlementPrice.setter
    def PreSettlementPrice(self, value: float):
        self._PreSettlementPrice = value

    @property
    def ActionTimespanList(self):
        return self._ActionTimespanList

    @ActionTimespanList.setter
    def ActionTimespanList(self, value: List[int]):
        self._ActionTimespanList = value

    @property
    def TradingTimeList(self):
        return self._TradingTimeList

    @TradingTimeList.setter
    def TradingTimeList(self, value: List[str]):
        self._TradingTimeList = value

    @property
    def StartTimeList(self):
        return self._StartTimeList

    @StartTimeList.setter
    def StartTimeList(self, value: List[str]):
        self._StartTimeList = value

    @property
    def EndTimeList(self):
        return self._EndTimeList

    @EndTimeList.setter
    def EndTimeList(self, value: List[str]):
        self._EndTimeList = value

    @property
    def TotalTurnoverList(self):
        return self._TotalTurnoverList

    @TotalTurnoverList.setter
    def TotalTurnoverList(self, value: List[float]):
        self._TotalTurnoverList = value

    @property
    def OpenInterestList(self):
        return self._OpenInterestList

    @OpenInterestList.setter
    def OpenInterestList(self, value: List[float]):
        self._OpenInterestList = value

    @property
    def OpenPriceList(self):
        return self._OpenPriceList

    @OpenPriceList.setter
    def OpenPriceList(self, value: List[float]):
        self._OpenPriceList = value

    @property
    def OpenBidPriceList(self):
        return self._OpenBidPriceList

    @OpenBidPriceList.setter
    def OpenBidPriceList(self, value: List[float]):
        self._OpenBidPriceList = value

    @property
    def OpenAskPriceList(self):
        return self._OpenAskPriceList

    @OpenAskPriceList.setter
    def OpenAskPriceList(self, value: List[float]):
        self._OpenAskPriceList = value

    @property
    def OpenBidVolumeList(self):
        return self._OpenBidVolumeList

    @OpenBidVolumeList.setter
    def OpenBidVolumeList(self, value: List[int]):
        self._OpenBidVolumeList = value

    @property
    def OpenAskVolumeList(self):
        return self._OpenAskVolumeList

    @OpenAskVolumeList.setter
    def OpenAskVolumeList(self, value: List[int]):
        self._OpenAskVolumeList = value

    @property
    def HighPriceList(self):
        return self._HighPriceList

    @HighPriceList.setter
    def HighPriceList(self, value: List[float]):
        self._HighPriceList = value

    @property
    def HighBidPriceList(self):
        return self._HighBidPriceList

    @HighBidPriceList.setter
    def HighBidPriceList(self, value: List[float]):
        self._HighBidPriceList = value

    @property
    def HighAskPriceList(self):
        return self._HighAskPriceList

    @HighAskPriceList.setter
    def HighAskPriceList(self, value: List[float]):
        self._HighAskPriceList = value

    @property
    def HighBidVolumeList(self):
        return self._HighBidVolumeList

    @HighBidVolumeList.setter
    def HighBidVolumeList(self, value: List[int]):
        self._HighBidVolumeList = value

    @property
    def HighAskVolumeList(self):
        return self._HighAskVolumeList

    @HighAskVolumeList.setter
    def HighAskVolumeList(self, value: List[int]):
        self._HighAskVolumeList = value

    @property
    def LowerPriceList(self):
        return self._LowerPriceList

    @LowerPriceList.setter
    def LowerPriceList(self, value: List[float]):
        self._LowerPriceList = value

    @property
    def LowerBidPriceList(self):
        return self._LowerBidPriceList

    @LowerBidPriceList.setter
    def LowerBidPriceList(self, value: List[float]):
        self._LowerBidPriceList = value

    @property
    def LowerAskPriceList(self):
        return self._LowerAskPriceList

    @LowerAskPriceList.setter
    def LowerAskPriceList(self, value: List[float]):
        self._LowerAskPriceList = value

    @property
    def LowerBidVolumeList(self):
        return self._LowerBidVolumeList

    @LowerBidVolumeList.setter
    def LowerBidVolumeList(self, value: List[int]):
        self._LowerBidVolumeList = value

    @property
    def LowerAskVolumeList(self):
        return self._LowerAskVolumeList

    @LowerAskVolumeList.setter
    def LowerAskVolumeList(self, value: List[int]):
        self._LowerAskVolumeList = value

    @property
    def ClosePriceList(self):
        return self._ClosePriceList

    @ClosePriceList.setter
    def ClosePriceList(self, value: List[float]):
        self._ClosePriceList = value

    @property
    def CloseBidPriceList(self):
        return self._CloseBidPriceList

    @CloseBidPriceList.setter
    def CloseBidPriceList(self, value: List[float]):
        self._CloseBidPriceList = value

    @property
    def CloseAskPriceList(self):
        return self._CloseAskPriceList

    @CloseAskPriceList.setter
    def CloseAskPriceList(self, value: List[float]):
        self._CloseAskPriceList = value

    @property
    def CloseBidVolumeList(self):
        return self._CloseBidVolumeList

    @CloseBidVolumeList.setter
    def CloseBidVolumeList(self, value: List[int]):
        self._CloseBidVolumeList = value

    @property
    def CloseAskVolumeList(self):
        return self._CloseAskVolumeList

    @CloseAskVolumeList.setter
    def CloseAskVolumeList(self, value: List[int]):
        self._CloseAskVolumeList = value
