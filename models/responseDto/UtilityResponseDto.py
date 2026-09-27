from models.responseDto.ResponseDto import ResponseDto
# ============================================================
# UTILITY
# ============================================================

class UtilityResponseDto(ResponseDto):
    pass


class ExchangeRatesResponseDto(UtilityResponseDto):
    endpoint = "/exchange_rates"


class PingResponseDto(UtilityResponseDto):
    endpoint = "/ping"


class KeyResponseDto(UtilityResponseDto):
    endpoint = "/key"
