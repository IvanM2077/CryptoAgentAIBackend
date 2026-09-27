from models.requestDto.RequestDto import RequestDto
# ============================================================
# GLOBAL
# ============================================================

class GlobalRequestDto(RequestDto):
    pass


class GlobalDataRequestDto(GlobalRequestDto):
    endpoint = "/global"


class GlobalDefiRequestDto(GlobalRequestDto):
    endpoint = "/global/decentralized_finance_defi"


class GlobalMarketCapChartRequestDto(GlobalRequestDto):
    endpoint = "/global/market_cap_chart"

    def __init__(self, days=None):
        super().__init__()
        self.days = days
