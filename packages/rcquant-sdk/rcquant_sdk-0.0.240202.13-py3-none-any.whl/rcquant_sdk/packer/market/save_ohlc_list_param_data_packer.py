from ...interface import IPacker


class SaveOHLCListParamDataPacker(IPacker):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def obj_to_tuple(self):
        return [
            self._obj.MarketName,
            self._obj.ExchangeID,
            self._obj.InstrumentID,
            self._obj.Range,
            self._obj.TradingDay,
            self._obj.PreSettlementPrice,
            list(self._obj.ActionDayList),
            list(self._obj.ActionTimespanList),
            list(self._obj.TradingTimeList),
            list(self._obj.StartTimeList),
            list(self._obj.EndTimeList),
            list(self._obj.TotalTurnoverList),
            list(self._obj.OpenInterestList),
            list(self._obj.OpenPriceList),
            list(self._obj.OpenBidPriceList),
            list(self._obj.OpenAskPriceList),
            list(self._obj.OpenBidVolumeList),
            list(self._obj.OpenAskVolumeList),
            list(self._obj.HighPriceList),
            list(self._obj.HighBidPriceList),
            list(self._obj.HighAskPriceList),
            list(self._obj.HighBidVolumeList),
            list(self._obj.HighAskVolumeList),
            list(self._obj.LowerPriceList),
            list(self._obj.LowerBidPriceList),
            list(self._obj.LowerAskPriceList),
            list(self._obj.LowerBidVolumeList),
            list(self._obj.LowerAskVolumeList),
            list(self._obj.ClosePriceList),
            list(self._obj.CloseBidPriceList),
            list(self._obj.CloseAskPriceList),
            list(self._obj.CloseBidVolumeList),
            list(self._obj.CloseAskVolumeList),
        ]

    def tuple_to_obj(self, t):
        if len(t) >= 33:
            self._obj.MarketName = t[0]
            self._obj.ExchangeID = t[1]
            self._obj.InstrumentID = t[2]
            self._obj.Range = t[3]
            self._obj.TradingDay = t[4]
            self._obj.PreSettlementPrice = t[5]
            self._obj.ActionDayList = t[6]
            self._obj.ActionTimespanList = t[7]
            self._obj.TradingTimeList = t[8]
            self._obj.StartTimeList = t[9]
            self._obj.EndTimeList = t[10]
            self._obj.TotalTurnoverList = t[11]
            self._obj.OpenInterestList = t[12]
            self._obj.OpenPriceList = t[13]
            self._obj.OpenBidPriceList = t[14]
            self._obj.OpenAskPriceList = t[15]
            self._obj.OpenBidVolumeList = t[16]
            self._obj.OpenAskVolumeList = t[17]
            self._obj.HighPriceList = t[18]
            self._obj.HighBidPriceList = t[19]
            self._obj.HighAskPriceList = t[20]
            self._obj.HighBidVolumeList = t[21]
            self._obj.HighAskVolumeList = t[22]
            self._obj.LowerPriceList = t[23]
            self._obj.LowerBidPriceList = t[24]
            self._obj.LowerAskPriceList = t[25]
            self._obj.LowerBidVolumeList = t[26]
            self._obj.LowerAskVolumeList = t[27]
            self._obj.ClosePriceList = t[28]
            self._obj.CloseBidPriceList = t[29]
            self._obj.CloseAskPriceList = t[30]
            self._obj.CloseBidVolumeList = t[31]
            self._obj.CloseAskVolumeList = t[32]
            return True
        return False
