from typing import Optional
from .models import (
    OrderSide,
    Position,
    RuntimeConfig,
    OrderParams,
    OrderResponse,
    Symbol,
)
from .strategy import Strategy

class StrategyTrader:
    config: RuntimeConfig
    async def open(self, side: OrderSide, quantity: float, limit: float | None, take_profit: float | None, stop_loss: float | None, symbol: Symbol) -> OrderResponse:
        """
        Places an open order. This method guarantees that take_profit/stop_loss will be handled for the User.
        """
    async def order(self, params: OrderParams) -> OrderResponse:
        """
        Places an order, do note that this function does not take into account current position,
        it merely executes whatever parameters was given.
        """
    async def cancel(self, id: str, symbol: Symbol) -> OrderResponse:
        """
        Cancels a specific order by its id.
        """
    async def close(self, side: OrderSide, quantity: float, symbol: Symbol):
        """
        Closes position with the same given side and given quantity. This function closes the trade with market
        order.
        """
    # async def get_current_equity(self) -> float:
    #     """
    #     Get the current equity of the running strategy.
    #     """
    async def get_current_available_balance(self, symbol: Symbol) -> float:
        """
        Get the current available balance of the running strategy.
        """
    async def get_current_price(self, symbol: Symbol) -> float:
        """
        Get the current price of the symbol requested.
        """
    # async def get_current_wallet_balance(self) -> float:
    #     """
    #     Get the current wallet balance of the running strategy.
    #     """
    async def position(self, symbol: Symbol) -> Position:
        """
        Get the current position of the strategy.
        """
    async def continue_permutations(self, permutation_id, permutation_params):
        """
        Used in backtests to continue the backtest with a new permutation in parameters.
        """


class Runtime:
    """
    A class representation of the underlying strategy runtime which handle backtest,
    paper trade, live trade.
    """

    @staticmethod
    async def connect(config: RuntimeConfig, strategy: Strategy) -> Runtime:
        """
        Instantiate the `Runtime` class by providing the configurations and a `Strategy`
        class which acts as the event handler.

        Parameters
        ----------
        config : RuntimeConfig
            the configuration for the runtime.
        strategy : Strategy
            the strategy to run within the runtime.

        Returns
        -------
        Runtime
            a Runtime instance

        Raises
        ------
        Exception
            If there is an error creating the runtime.
        """
    async def start(self) -> None:
        """
        Start the runtime and this method ideally will never return under live trade /
        paper trade unless interrupted, however this function will return when the backtest
        finishes.

        Raises
        ------
        Exception
            If there is an error during the runtime.
        """
