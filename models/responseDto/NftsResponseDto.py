from models.responseDto.ResponseDto import ResponseDto

# ============================================================
# NFTS
# ============================================================
class NftsResponseDto(ResponseDto):
    def __init__(
        self,
        nft_id=None,
        asset_platform_id=None,
        contract_address=None
    ):
        super().__init__()

        self.nft_id = nft_id
        self.asset_platform_id = asset_platform_id
        self.contract_address = contract_address


class NftsListResponseDto(NftsResponseDto):
    endpoint = "/nfts/list"

    def __init__(
        self,
        asset_platform_id=None,
        page=None,
        per_page=None
    ):
        super().__init__(
            asset_platform_id=asset_platform_id
        )

        self.page = page
        self.per_page = per_page


class NftDetailResponseDto(NftsResponseDto):
    endpoint = "/nfts/{nft_id}"

    def __init__(self, nft_id=None):
        super().__init__(nft_id=nft_id)


class NftContractResponseDto(NftsResponseDto):
    endpoint = "/nfts/{asset_platform_id}/contract/{contract_address}"

    def __init__(
        self,
        asset_platform_id=None,
        contract_address=None
    ):
        super().__init__(
            asset_platform_id=asset_platform_id,
            contract_address=contract_address
        )


class NftsMarketsResponseDto(NftsResponseDto):
    endpoint = "/nfts/markets"

    def __init__(
        self,
        asset_platform_id=None,
        order=None,
        per_page=None,
        page=None
    ):
        super().__init__(
            asset_platform_id=asset_platform_id
        )

        self.order = order
        self.per_page = per_page
        self.page = page


class NftMarketChartResponseDto(NftsResponseDto):
    endpoint = "/nfts/{nft_id}/market_chart"

    def __init__(
        self,
        nft_id=None,
        days=None
    ):
        super().__init__(nft_id=nft_id)

        self.days = days


class NftTickersResponseDto(NftsResponseDto):
    endpoint = "/nfts/{nft_id}/tickers"

    def __init__(
        self,
        nft_id=None,
        page=None,
        order=None
    ):
        super().__init__(nft_id=nft_id)

        self.page = page
        self.order = order
