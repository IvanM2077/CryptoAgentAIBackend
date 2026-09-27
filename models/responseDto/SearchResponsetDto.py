from models.responseDto.ResponseDto import ResponseDto
# ============================================================
# SEARCH / ID MAP
# ============================================================

class SearchResponseDto(ResponseDto):
    pass


class SearchCoinsResponseDto(SearchResponseDto):
    endpoint = "/search"

    def __init__(self, query=None):
        super().__init__()
        self.query = query


class CoinsListResponseDto(ResponseDto):
    endpoint = "/coins/list"

    def __init__(self, include_platform=None):
        super().__init__()
        self.include_platform = include_platform


class AssetPlatformsResponseDto(ResponseDto):
    endpoint = "/asset_platforms"


class TokenListResponseDto(ResponseDto):
    endpoint = "/token_lists/{asset_platform_id}/all.json"

    def __init__(self, asset_platform_id=None):
        super().__init__()
        self.asset_platform_id = asset_platform_id
