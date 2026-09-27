from models.responseDto.ResponseDto import ResponseDto

# ============================================================
# DERIVATIVES
# ============================================================
class DerivativesResponseDto(ResponseDto):
    def __init__(self, exchange_id=None):
        super().__init__()
        self.exchange_id = exchange_id


class DerivativesExchangesListResponseDto(DerivativesResponseDto):
    endpoint = "/derivatives/exchanges/list"


class DerivativesRequest(DerivativesResponseDto):
    endpoint = "/derivatives"

    def __init__(self, include_tickers=None):
        super().__init__()
        self.include_tickers = include_tickers


class DerivativesExchangesResponseDto(DerivativesResponseDto):
    endpoint = "/derivatives/exchanges"

    def __init__(
        self,
        exchange_id=None,
        include_tickers=None
    ):
        super().__init__(exchange_id)

        self.include_tickers = include_tickers


class DerivativesExchangeDetailResponseDto(DerivativesResponseDto):
    endpoint = "/derivatives/exchanges/{exchange_id}"

    def __init__(
        self,
        exchange_id=None,
        include_tickers=None
    ):
        super().__init__(exchange_id)

        self.include_tickers = include_tickers
