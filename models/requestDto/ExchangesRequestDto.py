from models.requestDto.RequestDto import RequestDto
# ============================================================
# EXCHANGES
# ============================================================
class ExchangesRequestDto(RequestDto):
    def __init__(self, exchange_id=None):
        super().__init__()
        self.exchange_id = exchange_id


class ExchangesListRequestDto(ExchangesRequestDto):
    endpoint = "/exchanges/list"


class ExchangeDetailRequestDto(ExchangesRequestDto):
    endpoint = "/exchanges/{exchange_id}"

    def __init__(self, exchange_id=None):
        super().__init__(exchange_id)


class ExchangeTickersRequestDto(ExchangesRequestDto):
    endpoint = "/exchanges/{exchange_id}/tickers"

    def __init__(
        self,
        exchange_id=None,
        coin_ids=None,
        include_exchange_logo=None,
        page=None,
        depth=None,
        order=None
    ):
        super().__init__(exchange_id)

        self.coin_ids = coin_ids
        self.include_exchange_logo = include_exchange_logo
        self.page = page
        self.depth = depth
        self.order = order


class ExchangeVolumeChartRequestDto(ExchangesRequestDto):
    endpoint = "/exchanges/{exchange_id}/volume_chart"

    def __init__(
        self,
        exchange_id=None,
        days=None
    ):
        super().__init__(exchange_id)

        self.days = days


class ExchangeVolumeChartRangeRequestDto(ExchangesRequestDto):
    endpoint = "/exchanges/{exchange_id}/volume_chart/range"

    def __init__(
        self,
        exchange_id=None,
        from_timestamp=None,
        to_timestamp=None
    ):
        super().__init__(exchange_id)

        self.from_timestamp = from_timestamp
        self.to_timestamp = to_timestamp
