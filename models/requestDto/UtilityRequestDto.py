from models.requestDto.RequestDto import RequestDto
# ============================================================
# UTILITY
# ============================================================

class UtilityRequestDto(RequestDto):
    pass


class ExchangeRatesRequestDto(UtilityRequestDto):
    endpoint = "/exchange_rates"


class PingRequestDto(UtilityRequestDto):
    endpoint = "/ping"


class KeyRequestDto(UtilityRequestDto):
    endpoint = "/key"
