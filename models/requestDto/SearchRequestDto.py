from models.requestDto.RequestDto import RequestDto


# ============================================================
# SEARCH / ID MAP
# ============================================================

class SearchRequestDto(RequestDto):
    pass


class SearchCoinsRequestDto(SearchRequestDto):
    endpoint = "/search"

    def __init__(self, query=None):
        super().__init__()
        self.query = query


class CoinsListRequestDto(RequestDto):
    endpoint = "/coins/list"

    def __init__(self, include_platform=None):
        super().__init__()
        self.include_platform = include_platform


class AssetPlatformsRequestDto(RequestDto):
    endpoint = "/asset_platforms"


class TokenListRequestDto(RequestDto):
    endpoint = "/token_lists/{asset_platform_id}/all.json"

    def __init__(self, asset_platform_id=None):
        super().__init__()
        self.asset_platform_id = asset_platform_id
