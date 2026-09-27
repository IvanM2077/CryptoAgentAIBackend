from models.requestDto.requestDto import RequestDto
# ============================================================
# SIMPLE
# ============================================================

class SimpleRequestDto(RequestDto):
    pass


class SimplePriceRequestDto(SimpleRequestDto):
    endpoint = "/simple/price"

    def __init__(
        self,
        ids=None,
        vs_currencies=None,
        include_market_cap=None,
        include_24hr_vol=None,
        include_24hr_change=None,
        include_last_updated_at=None
    ):
        super().__init__()

        self.ids = ids
        self.vs_currencies = vs_currencies
        self.include_market_cap = include_market_cap
        self.include_24hr_vol = include_24hr_vol
        self.include_24hr_change = include_24hr_change
        self.include_last_updated_at = include_last_updated_at


class SimpleTokenPriceRequestDto(SimpleRequestDto):
    endpoint = "/simple/token_price/{asset_platform_id}"

    def __init__(
        self,
        asset_platform_id=None,
        contract_addresses=None,
        vs_currencies=None,
        include_market_cap=None,
        include_24hr_vol=None,
        include_24hr_change=None,
        include_last_updated_at=None
    ):
        super().__init__()

        self.asset_platform_id = asset_platform_id
        self.contract_addresses = contract_addresses
        self.vs_currencies = vs_currencies
        self.include_market_cap = include_market_cap
        self.include_24hr_vol = include_24hr_vol
        self.include_24hr_change = include_24hr_change
        self.include_last_updated_at = include_last_updated_at


class SupportedVsCurrenciesRequestDto(SimpleRequestDto):
    endpoint = "/simple/supported_vs_currencies"
