from models.requestDto.RequestDto import RequestDto
# ============================================================
# DERIVATIVES
# ============================================================
class DerivativesRequestDto(RequestDto):
    def __init__(self, exchange_id=None):
        super().__init__()
        self.exchange_id = exchange_id


class DerivativesExchangesListRequestDto(DerivativesRequestDto):
    endpoint = "/derivatives/exchanges/list"


class DerivativesRequest(DerivativesRequestDto):
    endpoint = "/derivatives"

    def __init__(self, include_tickers=None):
        super().__init__()
        self.include_tickers = include_tickers


class DerivativesExchangesRequestDto(DerivativesRequestDto):
    endpoint = "/derivatives/exchanges"

    def __init__(
        self,
        exchange_id=None,
        include_tickers=None
    ):
        super().__init__(exchange_id)

        self.include_tickers = include_tickers


class DerivativesExchangeDetailRequestDto(DerivativesRequestDto):
    endpoint = "/derivatives/exchanges/{exchange_id}"

    def __init__(
        self,
        exchange_id=None,
        include_tickers=None
    ):
        super().__init__(exchange_id)

        self.include_tickers = include_tickers
