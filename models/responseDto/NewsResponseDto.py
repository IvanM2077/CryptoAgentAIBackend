from models.responseDto.ResponseDto import ResponseDto

# ============================================================
# NEWS / INSIGHTS
# ============================================================

class NewsResponseDto(ResponseDto):
    def __init__(
        self,
        page=None,
        per_page=None
    ):
        super().__init__()

        self.page = page
        self.per_page = per_page


class InsightsResponseDto(ResponseDto):
    def __init__(
        self,
        page=None,
        per_page=None
    ):
        super().__init__()

        self.page = page
        self.per_page = per_page
