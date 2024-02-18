from ...interface import IPacker


class SaveTickListParamDataPacker(IPacker):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def obj_to_tuple(self):
        ret = [
            str(self._obj.MarketName),
            str(self._obj.ExchangeID),
            str(self._obj.InstrumentID),
            str(self._obj.ProductID),
            str(self._obj.TradingDay),
            float(self._obj.PreClosePrice),
            float(self._obj.PreSettlementPrice),
            float(self._obj.PreOpenInterest),
            float(self._obj.UpperLimitPrice),
            float(self._obj.LowerLimitPrice),
            list(self._obj.ActionDayList),
            list(self._obj.TradingTimeList),
            list(self._obj.UpdateMillSecList),
            list(self._obj.LocalTimeList),
            list(self._obj.LastPriceList),
            list(self._obj.LastVolumeList),
            list(self._obj.BidPriceList),
            list(self._obj.BidVolumeList),
            list(self._obj.AskPriceList),
            list(self._obj.AskVolumeList),
            list(self._obj.AvgPriceList),
            list(self._obj.OpenPriceList),
            list(self._obj.HighPriceList),
            list(self._obj.LowerPriceList),
            list(self._obj.TotalTurnoverList),
            list(self._obj.TotalVolumeList),
            list(self._obj.OpenInterestList),
            list(self._obj.ClosePriceList),
            list(self._obj.SettlementPriceList),
            list(self._obj.TotalValueList)
        ]
        return ret

    def tuple_to_obj(self, t):
        if len(t) >= 30:
            self._obj.MarketName = t[0]
            self._obj.ExchangeID = t[1]
            self._obj.InstrumentID = t[2]
            self._obj.ProductID = t[3]
            self._obj.TradingDay = t[4]
            self._obj.PreClosePrice = t[5]
            self._obj.PreSettlementPrice = t[6]
            self._obj.PreOpenInterest = t[7]
            self._obj.UpperLimitPrice = t[8]
            self._obj.LowerLimitPrice = t[9]
            self._obj.ActionDayList = t[10]
            self._obj.TradingTimeList = t[11]
            self._obj.UpdateMillSecList = t[12]
            self._obj.LocalTimeList = t[13]
            self._obj.LastPriceList = t[14]
            self._obj.LastVolumeList = t[15]
            self._obj.BidPriceList = t[16]
            self._obj.BidVolumeList = t[17]
            self._obj.AskPriceList = t[18]
            self._obj.AskVolumeList = t[19]
            self._obj.AvgPriceList = t[20]
            self._obj.OpenPriceList = t[21]
            self._obj.HighPriceList = t[22]
            self._obj.LowerPriceList = t[23]
            self._obj.TotalTurnoverList = t[24]
            self._obj.TotalVolumeList = t[25]
            self._obj.OpenInterestList = t[26]
            self._obj.ClosePriceList = t[27]
            self._obj.SettlementPriceList = t[28]
            self._obj.TotalValueList = t[29]
            return True
        return False
