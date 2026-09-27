from models.responseDto.ResponseDto import ResponseDto

# ============================================================
# GLOBAL
# ============================================================

class GlobalResponseDto(ResponseDto):
    pass


class GlobalDataResponseDto(GlobalResponseDto):
    endpoint = "/global"


class GlobalDefiResponseDto(GlobalResponseDto):
    endpoint = "/global/decentralized_finance_defi"


class GlobalMarketCapChartResponseDto(GlobalResponseDto):
    endpoint = "/global/market_cap_chart"

    def __init__(self, days=None):
        super().__init__()
        self.days = days
