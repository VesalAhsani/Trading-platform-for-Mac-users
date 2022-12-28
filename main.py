import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)
    # Here you should paste your Binance and Bitmex API
    binance = BinanceClient("e97bc84966a034c80ef27233b1132d953b2e9a55493328f091401b2956b46119",
                            "4f9e82b81fed18494838767b25e537c34a88a3b36a6de0a896cfb48185baf453",
                            testnet=True, futures=True)
    bitmex = BitmexClient("69tlFKyfuL002YmR3tUGt92_", "tTz73n3S_bZtcicueYYX9mebGeDM4rrco_tGWonIoS60K_kl", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
