from models.responseDto.ResponseDto import ResponseDto
# ============================================================
# TRENDING
# ============================================================

class TrendingResponseDto(ResponseDto):
    pass


class TrendingSearchResponseDto(TrendingResponseDto):
    endpoint = "/search/trending"


class NewsResponseDto(ResponseDto):
    endpoint = "/news"

    def __init__(
        self,
        page=None,
        per_page=None
    ):
        super().__init__()

        self.page = page
        self.per_page = per_page


class InsightsResponseDto(ResponseDto):
    endpoint = "/insights"

    def __init__(
        self,
        page=None,
        per_page=None
    ):
        super().__init__()

        self.page = page
        self.per_page = per_page
