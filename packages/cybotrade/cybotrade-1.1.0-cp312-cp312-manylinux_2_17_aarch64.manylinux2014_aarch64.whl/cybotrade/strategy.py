import logging
import asyncio

from json import JSONDecodeError
from aiohttp import web
from typing import List, Dict

from .models import Candle, FloatWithTime, OpenedTrade, OrderUpdate, RuntimeMode, Interval


class ControlAPIServer():
    def __init__(self, logger: logging.Logger, handlers: List[logging.Handler], port=int):
        self.logger = logger
        self.port = port
        self.handlers: List[logging.Handler] = handlers

    async def start(self):
        app = web.Application()
        app.add_routes([web.get('/log_level', self.log_level_get()), web.post('/log_level', self.log_level_post())])
        logging.info(f"Starting Control API on Port {self.port}")
        await web._run_app(app, port=self.port, access_log=self.logger)

    def log_level_get(self):
        def get_log_level_name(level: int) -> str:
            if level == logging.NOTSET:
                return "NOTSET"
            elif level == logging.DEBUG:
                return "DEBUG"
            elif level == logging.INFO:
                return "INFO"
            elif level == logging.WARN:
                return "WARN"
            elif level == logging.ERROR:
                return "ERROR"
            elif level == logging.CRITICAL:
                return "CRITICAL"
            else:
                return "UNKNOWN"

        async def handler(request: web.Request) -> web.StreamResponse:
            return web.Response(status=200, text=get_log_level_name(self.logger.level))

        return handler

    def log_level_post(self):
        ALLOWED_LEVELS = ["NOTSET", "DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]

        def get_log_level_value(level: str) -> int:
            if level == "NOTSET":
                return logging.NOTSET
            elif level == "DEBUG":
                return logging.DEBUG
            elif level == "INFO":
                return logging.INFO
            elif level == "WARN":
                return logging.WARN
            elif level == "ERROR":
                return logging.ERROR
            elif level == "CRITICAL":
                return logging.CRITICAL
            else:
                raise Exception(f"{level} must be one of {ALLOWED_LEVELS}")

        async def handler(request: web.Request) -> web.StreamResponse:
            try:
                body = await request.json()
                if "logLevel" not in body:
                    raise Exception("'logLevel' must exists in the body and must be a string")

                if not isinstance(body["logLevel"], str):
                    raise Exception("'logLevel' must be a string")

                if body["logLevel"] not in ALLOWED_LEVELS:
                    raise Exception(f"'logLevel' must be one of {ALLOWED_LEVELS}")
            except JSONDecodeError:
                return web.Response(status=400, reason="Bad request, failed to parse body as JSON")
            except Exception as e:
                return web.Response(status=400, reason=f"Bad request, {e}")

            try:
                log_level = get_log_level_value(body["logLevel"])
                self.logger.setLevel(level=log_level)
                for handler in self.handlers:
                    handler.setLevel(level=log_level)
                logging.info(f"Log level has been set to {body['logLevel']} through Control API")
            except Exception as e:
                return web.Response(status=404, reason=f"Failed to set log level: {e}")

            return web.Response(status=200, text=f"Log level has been successfully set to {body['logLevel']}")

        return handler


class Strategy:
    """
    This class is a handler that will be used by the Runtime to handle events such as
    `on_candle_closed`, `on_execution_update`, etc. The is a base class and every new strategy
    should be inheriting this class and override the methods.
    """

    logger = logging
    LOG_FORMAT = (
        "%(levelname)s %(name)s %(asctime)-15s %(filename)s:%(lineno)d %(message)s"
    )

    def __init__(
            self,
            log_level: int = logging.INFO,
            handlers: List[logging.Handler] = [],
    ):
        """
        Set up the logger
        """
        if len(handlers) == 0:
            default_handler = logging.StreamHandler()
            default_handler.setFormatter(logging.Formatter(self.LOG_FORMAT))
            handlers.append(default_handler)

        logging.root.setLevel(log_level)
        for handler in handlers:
            logging.root.addHandler(handler)

        # Start Control API Server
        self.control_api_server = ControlAPIServer(logger=logging.root, handlers=handlers, port=3000)
        asyncio.create_task(self.control_api_server.start(), name="Control API")

    async def on_init(self, strategy):
        logging.info(f"[on_init] Strategy successfully started.")

    async def on_trade(self, strategy, trade: OpenedTrade):
        logging.info(f"[on_trade] Received opened trade: {trade.__repr__()}")

    async def on_market_update(self, strategy, equity: FloatWithTime, available_balance: FloatWithTime):
        logging.info(
            f"[on_market_update] Received market update: equity({equity.__repr__()}), available_balance({available_balance.__repr__()})")

    async def on_order_update(self, strategy, update: OrderUpdate):
        logging.info(f"[on_order_update] Received order update: {update.__repr__()}")

    async def on_active_order_interval(self, strategy, active_orders: List[str]):
        logging.info(f"[on_active_order_interval] Received active orders: {active_orders.__repr__()}")

    async def on_backtest_complete(self, strategy):
        logging.info(f"[on_backtest_complete] Backtest completed.")
