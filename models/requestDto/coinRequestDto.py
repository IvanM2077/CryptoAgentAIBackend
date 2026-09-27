from models.requestDto.requestDto import RequestDto
# ============================================================
# COINS
# ============================================================
class CoinsRequestDto(RequestDto):
    def __init__(self, coin_id=None):
        super().__init__()
        self.coin_id = coin_id


class CoinsMarketsRequestDto(CoinsRequestDto):
    endpoint = "/coins/markets"

    def __init__(
        self,
        coin_id=None,
        vs_currency=None,
        ids=None,
        category=None,
        order=None,
        per_page=None,
        page=None,
        sparkline=None,
        price_change_percentage=None,
        locale=None
    ):
        super().__init__(coin_id)

        self.vs_currency = vs_currency
        self.ids = ids
        self.category = category
        self.order = order
        self.per_page = per_page
        self.page = page
        self.sparkline = sparkline
        self.price_change_percentage = price_change_percentage
        self.locale = locale


class CoinDetailRequestDto(CoinsRequestDto):
    endpoint = "/coins/{coin_id}"

    def __init__(
        self,
        coin_id=None,
        localization=None,
        tickers=None,
        market_data=None,
        community_data=None,
        developer_data=None,
        sparkline=None
    ):
        super().__init__(coin_id)

        self.localization = localization
        self.tickers = tickers
        self.market_data = market_data
        self.community_data = community_data
        self.developer_data = developer_data
        self.sparkline = sparkline


class CoinContractRequestDto(CoinsRequestDto):
    endpoint = "/coins/{coin_id}/contract/{contract_address}"

    def __init__(
        self,
        coin_id=None,
        contract_address=None,
        localization=None
    ):
        super().__init__(coin_id)

        self.contract_address = contract_address
        self.localization = localization


class CoinTickersRequestDto(CoinsRequestDto):
    endpoint = "/coins/{coin_id}/tickers"

    def __init__(
        self,
        coin_id=None,
        exchange_ids=None,
        include_exchange_logo=None,
        page=None,
        order=None,
        depth=None
    ):
        super().__init__(coin_id)

        self.exchange_ids = exchange_ids
        self.include_exchange_logo = include_exchange_logo
        self.page = page
        self.order = order
        self.depth = depth


class CoinHistoryRequestDto(CoinsRequestDto):
    endpoint = "/coins/{coin_id}/history"

    def __init__(
        self,
        coin_id=None,
        date=None,
        localization=None
    ):
        super().__init__(coin_id)

        self.date = date
        self.localization = localization


class CoinMarketChartRequestDto(CoinsRequestDto):
    endpoint = "/coins/{coin_id}/market_chart"

    def __init__(
        self,
        coin_id=None,
        vs_currency=None,
        days=None,
        interval=None,
        precision=None
    ):
        super().__init__(coin_id)

        self.vs_currency = vs_currency
        self.days = days
        self.interval = interval
        self.precision = precision


class CoinMarketChartRangeRequestDto(CoinsRequestDto):
    endpoint = "/coins/{coin_id}/market_chart/range"

    def __init__(
        self,
        coin_id=None,
        vs_currency=None,
        from_timestamp=None,
        to_timestamp=None,
        interval=None,
        precision=None
    ):
        super().__init__(coin_id)

        self.vs_currency = vs_currency
        self.from_timestamp = from_timestamp
        self.to_timestamp = to_timestamp
        self.interval = interval
        self.precision = precision


class CoinOhlcRequestDto(CoinsRequestDto):
    endpoint = "/coins/{coin_id}/ohlc"

    def __init__(
        self,
        coin_id=None,
        vs_currency=None,
        days=None,
        interval=None,
        precision=None
    ):
        super().__init__(coin_id)

        self.vs_currency = vs_currency
        self.days = days
        self.interval = interval
        self.precision = precision


class CoinContractMarketChartRequestDto(CoinsRequestDto):
    endpoint = "/coins/{coin_id}/contract/{contract_address}/market_chart"

    def __init__(
        self,
        coin_id=None,
        contract_address=None,
        vs_currency=None,
        days=None,
        interval=None,
        precision=None
    ):
        super().__init__(coin_id)

        self.contract_address = contract_address
        self.vs_currency = vs_currency
        self.days = days
        self.interval = interval
        self.precision = precision


class CoinContractMarketChartRangeRequestDto(CoinsRequestDto):
    endpoint = "/coins/{coin_id}/contract/{contract_address}/market_chart/range"

    def __init__(
        self,
        coin_id=None,
        contract_address=None,
        vs_currency=None,
        from_timestamp=None,
        to_timestamp=None,
        interval=None,
        precision=None
    ):
        super().__init__(coin_id)

        self.contract_address = contract_address
        self.vs_currency = vs_currency
        self.from_timestamp = from_timestamp
        self.to_timestamp = to_timestamp
        self.interval = interval
        self.precision = precision
