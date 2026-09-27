from models.responseDto.ResponseDto import ResponseDto
# ============================================================
# CATEGORIES
# ============================================================

class CategoriesResponseDto(ResponseDto):
    pass


class CategoriesListResponseDto(CategoriesResponseDto):
    endpoint = "/coins/categories/list"


class CategoriesMarketsResponseDto(CategoriesResponseDto):
    endpoint = "/coins/categories"

    def __init__(
        self,
        vs_currency=None,
        order=None,
        per_page=None,
        page=None
    ):
        super().__init__()

        self.vs_currency = vs_currency
        self.order = order
        self.per_page = per_page
        self.page = page
