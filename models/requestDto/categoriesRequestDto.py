from models.requestDto.requestDto import RequestDto
# ============================================================
# CATEGORIES
# ============================================================

class CategoriesRequestDto(RequestDto):
    pass


class CategoriesListRequestDto(CategoriesRequestDto):
    endpoint = "/coins/categories/list"


class CategoriesMarketsRequestDto(CategoriesRequestDto):
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
