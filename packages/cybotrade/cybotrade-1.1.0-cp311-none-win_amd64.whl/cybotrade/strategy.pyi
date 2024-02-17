from typing import List, Dict
from .models import (
    ActiveOrder,
    Candle,
    FloatWithTime,
    OpenedTrade,
    OrderUpdate,
    Interval,
    Symbol
)
from .runtime import StrategyTrader

import logging

class Strategy:
    """
    This class is a handler that will be used by the Runtime to handle events such as
    `on_candle_closed`, `on_order_update`, etc. The is a base class and every new strategy
    should be inheriting this class and override the methods.
    """

    logger = logging
    LOG_FORMAT: str

    def __init__(
            self,
            log_level: int = logging.INFO,
            handlers: List[logging.Handler] = [],
    ):
        """
        Set up the logger
        """

    def on_init(
            self,
            strategy: StrategyTrader,
    ):
        """
        This method is called when the strategy is started successfully.
        """

    async def on_order_update(
            self,
            strategy: StrategyTrader,
            update: OrderUpdate,
    ):
        """
        This method is called when receiving an order update from the exchange.
        """

    async def on_backtest_complete(
            self, strategy: StrategyTrader
    ):
        """
        This method is called when backtest is completed.
        """

    async def on_datasource_interval(
            self, strategy: StrategyTrader, topic: str, data_map: Dict[str, List[Dict[str, str]]],
    ):
        """
        This method is called when the requested Datasources' Interval has elapsed.
        E.g 'liquidation-4h-BTC/USDT-bybit' -> this gets called every 4h
        """

    async def on_trade(
            self, strategy: StrategyTrader, trade: OpenedTrade
    ):
        """
        This method is called when a trade is opened.
        """

    async def on_active_order_interval(
            self, strategy: StrategyTrader, active_orders: List[ActiveOrder]
    ):
        """
        This method is called when the passed in `active_order_interval` time has elapsed. This will return a list of client_order_ids of all active orders.
        """

    async def on_market_update(
            self, strategy: StrategyTrader, equity: FloatWithTime, available_balance: FloatWithTime
    ):
        """
        This method is called when market stats is updated.
        """

    async def on_candle_closed(
            self, strategy: StrategyTrader, topic: str, symbol: Symbol, candle_map: Dict[str, List[Dict[str, str]]] 
    ):
        """
        This method is called when the requested candles have closed.
        """
