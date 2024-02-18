from typing import List, Dict, Tuple
from .client import FinClient
from .data.login_data import LoginData
from .data.market.ohlc_data import OHLCData
from .data.chart.chart_init_param_data import ChartInitParamData
from .data.chart.marker_graph_param_data import MarkerGraphParamData
from .data.chart.text_graph_param_data import TextGraphParamData
from .data.chart.financial_graph_param_data import FinancialGraphParamData
from .data.chart.line_graph_param_data import LineGraphParamData
from .data.chart.ohlc_value_data import OHLCValueData
from .data.chart.graph_value_data import GraphValueData
from .data.trade.order_data import OrderData
from .data.market.market_param_data import MarketParamData
from .data.market.query_param_data import QueryParamData
from .data.market.sub_ohlc_param_data import SubOHLCParamData
from .data.market.history_ohlc_param_data import HistoryOHLCParamData
from .data.market.save_ohlc_list_param_data import SaveOHLCListParamData
from .data.market.save_tick_list_param_data import SaveTickListParamData
from .data.market.history_tick_param_data import HistoryTickParamData
from .data.trade.trade_param_data import TradeParamData
from .data.trade.read_history_order_param_data import ReadHistoryOrderParamData
from .data.trade.read_history_tradeorder_param_data import ReadHistoryTradeOrderParamData
from .data.trade.get_account_param_data import GetAccountParamData
from .data.trade.get_orders_param_data import GetOrdersParamData
from .data.trade.get_tradeorders_param_data import GetTradeOrdersParamData
from .data.trade.get_positions_param_data import GetPositionsParamData
from .data.chart.bar_graph_param_data import BarGraphParamData


def conncet(host: str = None, port: int = None, ):
    return FinClient.instance().connect(host, port)

def is_connected():
    return FinClient.instance().is_connected()


def login(user_id: str = '', password: str = ''):
    return FinClient.instance().base_handle().login(LoginData(user_id, password))


def close():
    FinClient.instance().close()


def set_callback(**kwargs):
    '''
    设置行情回调
    :param kwargs OnTick=None,
    '''
    FinClient.instance().set_callback(**kwargs)


def set_auth_params(userid, password, host: str = None, port: int = None):
    '''
    设置登录信息
    :param userid:用户名
    :param password:密码
    :param host:网络地址默认为None
    :param port:端口号默认为None
    :return:result msg
    '''
    ret = conncet(host, port)
    if ret is None or ret[0] is False:
        return ret
    return login(userid, password)


def set_chart_init_params(params: ChartInitParamData):
    return FinClient.instance().chart_handle().set_chart_init_params(params)


def add_line_graph(id: str, plot_index=0, value_axis_id=-1, color: str = '#FFF', style=0, price_tick=0.01, tick_valid_mul=-1.0, bind_ins_id='', bind_range=''):
    '''
    添加线图
    :param id:图形ID
    :param plot_index:所在图层索引
    :param value_axis_id:所属Y轴
    :param color:颜色
    :param style:样式
    :param price_tick:最小变动刻度
    :param tick_valid_mul:显示有效的倍数 -1.0不做限制
    :param bind_ins_id:绑定合约
    :param bind_range:绑定合约周期
    :return:result msg
    '''
    return FinClient.instance().chart_handle().add_line_graph(
        LineGraphParamData(
            name=id,
            id=id,
            plot_index=plot_index,
            value_axis_id=value_axis_id,
            style=style,
            color=color,
            price_tick=price_tick,
            tick_valid_mul=tick_valid_mul,
            bind_ins_id=bind_ins_id,
            bind_range=bind_range)
    )


def add_bar_graph(id: str, plot_index=0, value_axis_id=-1, color: str = '#FFF', style=0, frame_style=2):
    """添加柱状图

    Args:
        id (str): 图形id
        plot_index (int, optional): 所在图层索引. Defaults to 0.
        value_axis_id (int, optional): 所属Y轴. Defaults to -1左边第一个Y轴.
        color (str, optional): 颜色. Defaults to '#FFF'.
        style (int, optional): 样式. Defaults to 0 box.
        frame_style (int, optional): 边框样式. Defaults to 2 线型.

    Returns:
        _type_: [bool,str]
    """

    return FinClient.instance().chart_handle().add_bar_graph(
        BarGraphParamData(
            name=id,
            id=id,
            plot_index=plot_index,
            valueaxis_id=value_axis_id,
            style=style,
            frame_style=frame_style,
            color=color,
        )
    )


def add_financial_graph(id: str, plot_index=0, value_axis_id=-1, style=0, price_tick=0.01, tick_valid_mul=-1.0, bind_ins_id='', bind_range=''):
    '''
    添加线图
    :param id:图形编号
    :param name:图形名称
    :param style:样式
    :param plot_index:所在图层索引
    :param value_axis_id:所属Y轴
    :param price_tick:最小变动刻度
    :param tick_valid_mul:显示有效的倍数 -1.0不做限制
    :param bind_ins_id:绑定合约
    :param bind_range:绑定合约周期
    :return: [result,msg] True 添加成功, False 添加失败
    '''
    return FinClient.instance().chart_handle().add_financial_graph(
        FinancialGraphParamData(
            id=id,
            name=id,
            style=style,
            plot_index=plot_index,
            value_axis_id=value_axis_id,
            price_tick=price_tick,
            tick_valid_mul=tick_valid_mul,
            bind_ins_id=bind_ins_id,
            bind_range=bind_range)
    )


def chart_init_show():
    return FinClient.instance().chart_handle().chart_init_show()


def add_line_value(graphid: str, key: float = 0.0, value: float = 0.0, mill_ts: int = -1):
    return FinClient.instance().chart_handle().add_graph_value(GraphValueData(
        graph_id=graphid,
        key=key,
        mill_ts=mill_ts,
        value=value)
    )


def add_marker_graph(param: MarkerGraphParamData):
    return FinClient.instance().chart_handle().add_marker_graph(param)


def add_graph_value(gv: GraphValueData):
    return FinClient.instance().chart_handle().add_graph_value(gv)


def add_graph_value_list(gvl):
    gvdl = []
    for gv in gvl:
        gvdl.append(GraphValueData(graph_id=gv[0], mill_ts=gv[1], value=gv[2]))
    return FinClient.instance().chart_handle().add_graph_value_list(gvdl)


def add_timespan_graphvalue_list(timespans: List[int], graph_values: Dict[str, List[float]] = {}, ohlc_values: Dict[str, Tuple[List[float], List[float], List[float], List[float]]] = {}):
    return FinClient.instance().chart_handle().add_timespan_graphvalue_list(timespans, graph_values, ohlc_values)


def add_ohlc_value(ov: OHLCValueData):
    return FinClient.instance().chart_handle().add_ohlc_value(ov)


def add_ohlc_value_list(ovl: List[OHLCValueData]):
    return FinClient.instance().chart_handle().add_ohlc_value_list(ovl)


def add_ohlc(graph_id: str, o: OHLCData):
    '''
    添加OHLC值
    :param graph_id:图形名称
    :param o:ohlc
    :return:result,msg
    '''
    return FinClient.instance().chart_handle().add_ohlc_value(
        OHLCValueData(
            graph_id=graph_id,
            ohlc_data=o)
    )


def draw_text(plot_index: int, value_axis_id: int, key: float, value: float, text: str, color: str = '#FFF'):
    '''
    画文本
    :param plot_index:所在图层索引
    :param value_axis_id:所属Y轴
    :param key:x轴值
    :param value:y轴值
    :param text:文本
    :param color:颜色
    :return:[result,msg]
    '''
    return FinClient.instance().chart_handle().add_text_graph(
        TextGraphParamData(
            plot_index=plot_index,
            value_axis_id=value_axis_id,
            key=key,
            value=value,
            text=text,
            color=color)
    )


def add_text_graph(param: TextGraphParamData):
    return FinClient.instance().chart_handle().add_text_graph(param)


def draw_text_milltime(plot_index, value_axis_id, mill_ts, value, text, color='#FFF'):
    '''
    画文本
    :param plot_index:所在图层索引
    :param value_axis_id:所属Y轴
    :param mill_ts:x时间戳
    :param value:y轴值
    :param text:文本
    :param color:颜色
    :return:result,msg
    '''
    return FinClient.instance().chart_handle().add_text_graph(
        TextGraphParamData(
            plot_index=plot_index,
            value_axis_id=value_axis_id,
            mill_ts=mill_ts,
            value=value,
            text=text,
            color=color)
    )


def set_market_params(market_names):
    '''
    设置行情参数
    :param market_names:行情名称多个时候用逗号分隔
    :return:result,msg
    '''
    return FinClient.instance().market_handle().set_market_params(
        MarketParamData(market_names=market_names)
    )


def subscribe(market_name: str, exchang_id: str, instrument_id: str):
    '''
    订阅行情
    :param market_name:行情名称
    :param exchang_id:交易所编码
    :param instrument_id:合约编码
    :return:result,msg
    '''
    return FinClient.instance().market_handle().subscribe(
        QueryParamData(
            market_name=market_name,
            exchange_id=exchang_id,
            instrument_id=instrument_id)
    )


def subscribe_ohlc(market_name: str, exchang_id: str, instrument_id: str, range: str):
    '''
    订阅行情
    :param market_name:行情名称
    :param exchang_id:交易所编码
    :param instrument_id:合约编码
    :param range:周期
    :return:result,msg
    '''
    return FinClient.instance().market_handle().subscribe_ohlc(
        SubOHLCParamData(
            market_name=market_name,
            exchange_id=exchang_id,
            instrument_id=instrument_id,
            range=range)
    )


def get_history_ohlc(market_name: str, exchang_id: str, instrument_id: str, range: str,
                     start_date: str, end_date: str, is_return_list: bool = False):
    '''
    获取历史ohlc数据
    :param market_name:行情名称
    :param exchang_id:交易所编码
    :param instrument_id:合约编码
    :param range:周期
    :param start_date 开始日期
    :param end_date 结束日期
    :param is_return_list 是否返回list格式
    :return:result,msg
    '''
    return FinClient.instance().market_handle().get_history_ohlc(
        HistoryOHLCParamData(
            market_name=market_name,
            exchange_id=exchang_id,
            instrument_id=instrument_id,
            range=range,
            start_date=start_date,
            end_date=end_date,
            is_return_list=is_return_list)
    )


def get_history_tick(market_name: str, exchang_id: str, instrument_id: str, date: str, is_return_list: bool = False):
    '''
    获取历史ohlc数据
    :param market_name:行情名称
    :param exchang_id:交易所编码
    :param instrument_id:合约编码
    :param date 日期
    :param is_return_list 是否返回list格式
    :return:result,msg
    '''
    return FinClient.instance().market_handle().get_history_tick(
        HistoryTickParamData(
            market_name=market_name,
            exchange_id=exchang_id,
            instrument_id=instrument_id,
            date = date,
            is_return_list=is_return_list)
    )



def save_ohlc_list(
    market_name: str = '',
    exchange_id: str = '',
    instrument_id: str = '',
    range: int = 60,
    trading_day: str = '',
    pre_settlement_price: float = 0.0,
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
    """批量按天保存OHLC数据

    Args:
        market_name (str, optional): 行情名称. Defaults to ''.
        exchange_id (str, optional): 交易所编码. Defaults to ''.
        instrument_id (str, optional): 合约编码. Defaults to ''.
        range (int, optional): 周期. Defaults to 60.
        trading_day (str, optional): 交易日. Defaults to ''.
        pre_settlement_price (float, optional): 昨结算价. Defaults to 0.0.
        action_day_list (List[str], optional): 自然日. Defaults to ''.
        action_timespan_list (List[int], optional): 自然日时间戳. Defaults to [].
        trading_time_list (List[str], optional): 交易时间. Defaults to [].
        start_time_list (List[str], optional): 开始时间. Defaults to [].
        end_time_list (List[str], optional): 结束时间. Defaults to [].
        total_turnover_list (List[float], optional): 成交金额. Defaults to [].
        open_interest_list (List[float], optional): 持仓量. Defaults to [].
        open_price_list (List[float], optional): 开盘价. Defaults to [].
        open_bid_price_list (List[float], optional): 开买价. Defaults to [].
        open_ask_price_list (List[float], optional): 开卖价. Defaults to [].
        open_bid_volume_list (List[int], optional): 开买量. Defaults to [].
        open_ask_volume_list (List[int], optional): 开卖量. Defaults to [].
        high_price_list (List[float], optional): 最高价. Defaults to [].
        high_bid_price_list (List[float], optional): 高买价. Defaults to [].
        high_ask_price_list (List[float], optional): 高卖价. Defaults to [].
        high_bid_volume_list (List[int], optional): 高买量. Defaults to [].
        high_ask_volume_list (List[int], optional): 高卖量. Defaults to [].
        lower_price_list (List[float], optional): 最低价. Defaults to [].
        lower_bid_price_list (List[float], optional): 低买价. Defaults to [].
        lower_ask_price_list (List[float], optional): 低卖价. Defaults to [].
        lower_bid_volume_list (List[int], optional): 低买量. Defaults to [].
        lower_ask_volume_list (List[int], optional): 低卖量. Defaults to [].
        close_price_list (List[float], optional): 收价. Defaults to [].
        close_bid_price_list (List[float], optional): 收买价. Defaults to [].
        close_ask_price_list (List[float], optional): 收卖价. Defaults to [].
        close_bid_volume_list (List[int], optional): 收买量. Defaults to [].
        close_ask_volume_list (List[int], optional): 收卖量. Defaults to [].

    Returns:
        _type_: [bool,str]
    """
    return FinClient.instance().market_handle().save_ohlc_list(
        SaveOHLCListParamData(market_name=market_name,
                              exchange_id=exchange_id,
                              instrument_id=instrument_id,
                              range=range,
                              trading_day=trading_day,
                              action_day_list=action_day_list,
                              pre_settlement_price=pre_settlement_price,
                              action_timespan_list=action_timespan_list,
                              trading_time_list=trading_time_list,
                              start_time_list=start_time_list,
                              end_time_list=end_time_list,
                              total_turnover_list=total_turnover_list,
                              open_interest_list=open_interest_list,
                              open_price_list=open_price_list,
                              open_bid_price_list=open_bid_price_list,
                              open_ask_price_list=open_ask_price_list,
                              open_bid_volume_list=open_bid_volume_list,
                              open_ask_volume_list=open_ask_volume_list,
                              high_price_list=high_price_list,
                              high_bid_price_list=high_bid_price_list,
                              high_ask_price_list=high_ask_price_list,
                              high_bid_volume_list=high_bid_volume_list,
                              high_ask_volume_list=high_ask_volume_list,
                              lower_price_list=lower_price_list,
                              lower_bid_price_list=lower_bid_price_list,
                              lower_ask_price_list=lower_ask_price_list,
                              lower_bid_volume_list=lower_bid_volume_list,
                              lower_ask_volume_list=lower_ask_volume_list,
                              close_price_list=close_price_list,
                              close_bid_price_list=close_bid_price_list,
                              close_ask_price_list=close_ask_price_list,
                              close_bid_volume_list=close_bid_volume_list,
                              close_ask_volume_list=close_ask_volume_list)
    )


def save_tick_list(
    market_name: str = '',
    exchange_id: str = '',
    instrument_id: str = '',
    product_id: str = '',
    trading_day: str = '',
    pre_close_price: float = float("NaN"),
    pre_settlement_price: float = float("NaN"),
    pre_open_interest: float = float("NaN"),
    upper_limit_price: float = float("NaN"),
    lower_limit_price: float = float("NaN"),
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
    """批量按天保存行情数据

    Args:
        market_name (str, optional): 行情名称. Defaults to ''.
        exchange_id (str, optional): 交易所编码. Defaults to ''.
        instrument_id (str, optional): 合约编码. Defaults to ''.
        product_id (str, optional): 品种编码. Defaults to ''.
        trading_day (str, optional): 交易日. Defaults to ''.
        pre_close_price (float, optional): 昨收价. Defaults to float("NaN").
        pre_settlement_price (float, optional): 昨结算价. Defaults to float("NaN").
        pre_open_interest (float, optional): 昨持仓量. Defaults to float("NaN").
        upper_limit_price (float, optional): 涨停板价. Defaults to float("NaN").
        lower_limit_price (float, optional): 跌停板价. Defaults to float("NaN").
        action_day_list (List[str], optional): 自然日列表. Defaults to [].
        trading_time_list (List[str], optional): 行情时间. Defaults to [].
        update_mill_sec_list (List[int], optional): 最后修改毫秒值. Defaults to [].
        local_time_list (List[int], optional): 本地日期纳秒时间. Defaults to [].
        last_price_list (List[float], optional): 最新价. Defaults to [].
        last_volume_list (List[int], optional): 最新量. Defaults to [].
        bid_price_list (List[float], optional): 买价. Defaults to [].
        bid_volume_list (List[int], optional): 买量. Defaults to [].
        ask_price_list (List[float], optional): 卖价. Defaults to [].
        ask_volume_list (List[int], optional): 卖量. Defaults to [].
        avg_price_list (List[float], optional): 当日均价. Defaults to [].
        open_price_list (List[float], optional): 今开盘. Defaults to [].
        high_price_list (List[float], optional): 最高价. Defaults to [].
        lower_price_list (List[float], optional): 最低价. Defaults to [].
        total_turnover_list (List[float], optional): 成交金额. Defaults to [].
        total_volume_list (List[int], optional): 成交量. Defaults to [].
        open_interest_list (List[float], optional): 持仓量. Defaults to [].
        close_price_list (List[float], optional): 今收盘. Defaults to [].
        settlement_price_list (List[float], optional): 本次结算价. Defaults to [].
        total_value_list (List[float], optional): 总市值. Defaults to [].

    Returns:
        _type_: [bool,str]
    """
    return FinClient.instance().market_handle().save_tick_list(
        SaveTickListParamData(
            market_name=market_name,
            exchange_id=exchange_id,
            instrument_id=instrument_id,
            product_id=product_id,
            trading_day=trading_day,
            pre_close_price=pre_close_price,
            pre_settlement_price=pre_settlement_price,
            pre_open_interest=pre_open_interest,
            upper_limit_price=upper_limit_price,
            lower_limit_price=lower_limit_price,
            action_day_list=action_day_list,
            trading_time_list=trading_time_list,
            update_mill_sec_list=update_mill_sec_list,
            local_time_list=local_time_list,
            last_price_list=last_price_list,
            last_volume_list=last_volume_list,
            bid_price_list=bid_price_list,
            bid_volume_list=bid_volume_list,
            ask_price_list=ask_price_list,
            ask_volume_list=ask_volume_list,
            avg_price_list=avg_price_list,
            open_price_list=open_price_list,
            high_price_list=high_price_list,
            lower_price_list=lower_price_list,
            total_turnover_list=total_turnover_list,
            total_volume_list=total_volume_list,
            open_interest_list=open_interest_list,
            close_price_list=close_price_list,
            settlement_price_list=settlement_price_list,
            total_value_list=total_value_list
        )
    )


def set_trade_params(tradenames: str):
    return FinClient.instance().trade_handle().set_trade_params(
        TradeParamData(
            trade_names=tradenames)
    )


def insert_order(trade_name, exchange_id: str, instrument_id: str, direc: int, price: float, vol: int, open_close_type: int):
    return FinClient.instance().trade_handle().insert_order(
        OrderData(
            exchange_id=exchange_id,
            instrument_id=instrument_id,
            price=price,
            direction=direc,
            volume=vol,
            investor_id=trade_name,
            open_close_type=open_close_type
        )
    )


def cancel_order_by_data(order: OrderData):
    return FinClient.instance().trade_handle().cancel_order(order)


def cancel_order(trade_name: str, order_id: str, instrument_id: str, order_ref: str, price: float):
    return FinClient.instance().trade_handle().cancel_order(
        OrderData(
            investor_id=trade_name,
            order_id=order_id,
            instrument_id=instrument_id,
            order_ref=order_ref,
            price=price
        )
    )


def read_history_orders(start_date: str, end_date: str):
    return FinClient.instance().trade_handle().read_history_orders(
        ReadHistoryOrderParamData(
            start_date=start_date,
            end_date=end_date
        )
    )


def read_history_tradeorders(start_date: str, end_date: str):
    return FinClient.instance().trade_handle().read_history_tradeorders(
        ReadHistoryTradeOrderParamData(
            start_date=start_date,
            end_date=end_date
        )
    )


def get_orders(trade_name: str):
    return FinClient.instance().trade_handle().get_orders(
        GetOrdersParamData(
            trade_name=trade_name
        )
    )


def get_tradeorders(trade_name: str):
    return FinClient.instance().trade_handle().get_tradeorders(
        GetTradeOrdersParamData(
            trade_name=trade_name
        )
    )


def get_positions(trade_name: str):
    return FinClient.instance().trade_handle().get_positions(
        GetPositionsParamData(
            trade_name=trade_name
        )
    )


def get_account(trade_name: str):
    return FinClient.instance().trade_handle().get_account(
        GetAccountParamData(
            trade_name=trade_name
        )
    )


def save_chart_data(file_name: str):
    '''
    保存图数据
    :param file_name 文件名称
    :return [result,msg]
    '''
    return FinClient.instance().chart_handle().save_chart_data(file_name)


def load_chart_data(file_name: str):
    '''
    加载图数据
    :param file_name 文件名称
    :return [result,msg]
    '''
    return FinClient.instance().chart_handle().load_chart_data(file_name)
