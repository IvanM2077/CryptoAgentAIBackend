from models.requestDto.requestDto import RequestDto
# ============================================================
# TRENDING
# ============================================================

class TrendingRequestDto(RequestDto):
    pass


class TrendingSearchRequestDto(TrendingRequestDto):
    endpoint = "/search/trending"


class NewsRequestDto(RequestDto):
    endpoint = "/news"

    def __init__(
        self,
        page=None,
        per_page=None
    ):
        super().__init__()

        self.page = page
        self.per_page = per_page


class InsightsRequestDto(RequestDto):
    endpoint = "/insights"

    def __init__(
        self,
        page=None,
        per_page=None
    ):
        super().__init__()

        self.page = page
        self.per_page = per_page
