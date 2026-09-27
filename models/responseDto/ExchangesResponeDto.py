from models.responseDto.ResponseDto import ResponseDto

# ============================================================
# EXCHANGES
# ============================================================
class ExchangesResponseDto(ResponseDto):
    def __init__(self, exchange_id=None):
        super().__init__()
        self.exchange_id = exchange_id


class ExchangesListResponseDto(ExchangesResponseDto):
    endpoint = "/exchanges/list"


class ExchangeDetailResponseDto(ExchangesResponseDto):
    endpoint = "/exchanges/{exchange_id}"

    def __init__(self, exchange_id=None):
        super().__init__(exchange_id)


class ExchangeTickersResponseDto(ExchangesResponseDto):
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


class ExchangeVolumeChartResponseDto(ExchangesResponseDto):
    endpoint = "/exchanges/{exchange_id}/volume_chart"

    def __init__(
        self,
        exchange_id=None,
        days=None
    ):
        super().__init__(exchange_id)

        self.days = days


class ExchangeVolumeChartRangeResponseDto(ExchangesResponseDto):
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
