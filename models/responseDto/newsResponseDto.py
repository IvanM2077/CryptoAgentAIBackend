from models.requestDto.requestDto import RequestDto
# ============================================================
# NEWS / INSIGHTS
# ============================================================

class NewsRequestDto(RequestDto):
    def __init__(
        self,
        page=None,
        per_page=None
    ):
        super().__init__()

        self.page = page
        self.per_page = per_page


class InsightsRequestDto(RequestDto):
    def __init__(
        self,
        page=None,
        per_page=None
    ):
        super().__init__()

        self.page = page
        self.per_page = per_page
