from models.responseDto.ResponseDto import ResponseDto

# ============================================================
# ONCHAIN - BASE
# ============================================================

class OnchainResponseDto(ResponseDto):
    def __init__(self, network=None):
        super().__init__()
        self.network = network



# ============================================================
# ONCHAIN - PRICE
# ============================================================

class OnchainPriceResponseDto(OnchainResponseDto):
    endpoint = "/onchain/simple/networks/{network}/token_price/{addresses}"

    def __init__(
        self,
        network=None,
        addresses=None
    ):
        super().__init__(network)

        self.addresses = addresses


class OnchainMultiPriceResponseDto(OnchainResponseDto):
    endpoint = "/onchain/simple/token_price/multi"

    def __init__(self, addresses=None):
        super().__init__()
        self.addresses = addresses



# ============================================================
# ONCHAIN - SEARCH
# ============================================================

class OnchainSearchResponseDto(OnchainResponseDto):
    endpoint = "/onchain/search/pools"

    def __init__(self, query=None):
        super().__init__()
        self.query = query


class OnchainNetworksResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks"


class OnchainDexesResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/dexes"

    def __init__(self, network=None):
        super().__init__(network)



# ============================================================
# ONCHAIN - POOLS
# ============================================================
class OnchainPoolResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/pools/{address}"

    def __init__(
        self,
        network=None,
        address=None
    ):
        super().__init__(network)

        self.address = address


class OnchainPoolsMultiResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/pools/multi/{addresses}"

    def __init__(
        self,
        network=None,
        addresses=None
    ):
        super().__init__(network)

        self.addresses = addresses


class OnchainDexPoolsResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/dexes/{dex}/pools"

    def __init__(
        self,
        network=None,
        dex=None
    ):
        super().__init__(network)

        self.dex = dex


class OnchainNewPoolsResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/new_pools"

    def __init__(self, network=None):
        super().__init__(network)


class OnchainTrendingPoolsResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/trending_pools"

    def __init__(self, network=None):
        super().__init__(network)


class OnchainMegafilterResponseDto(OnchainResponseDto):
    endpoint = "/onchain/pools/megafilter"

    def __init__(self, **filters):
        super().__init__()
        self.filters = filters


class OnchainTrendingSearchResponseDto(OnchainResponseDto):
    endpoint = "/onchain/pools/trending_search"

    def __init__(self, query=None):
        super().__init__()
        self.query = query

class OnchainPoolsResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/pools"

    def __init__(self, network=None):
        super().__init__(network)


class OnchainTokenPoolsResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/tokens/{token_address}/pools"

    def __init__(
        self,
        network=None,
        token_address=None
    ):
        super().__init__(network)

        self.token_address = token_address
class OnchainNewPoolsGlobalResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/new_pools"


class OnchainTrendingPoolsGlobalResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/trending_pools"



# ============================================================
# ONCHAIN - TOKEN
# ============================================================
class OnchainTokenResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/tokens/{address}"

    def __init__(
        self,
        network=None,
        address=None
    ):
        super().__init__(network)

        self.address = address


class OnchainTokensMultiResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/tokens/multi/{addresses}"

    def __init__(
        self,
        network=None,
        addresses=None
    ):
        super().__init__(network)

        self.addresses = addresses


class OnchainTokensInfoResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/tokens/{address}/info"

    def __init__(
        self,
        network=None,
        address=None
    ):
        super().__init__(network)

        self.address = address


class OnchainTokensMultiInfoResponseDto(OnchainResponseDto):
    endpoint = "/onchain/tokens/multi"


class OnchainRecentlyUpdatedTokensResponseDto(OnchainResponseDto):
    endpoint = "/onchain/tokens/info_recently_updated"


# ============================================================
# ONCHAIN - CHARTS
# ============================================================
class OnchainOhlcvResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/pools/{pool_address}/ohlcv/{timeframe}"

    def __init__(
        self,
        network=None,
        pool_address=None,
        timeframe=None,
        aggregate=None
    ):
        super().__init__(network)

        self.pool_address = pool_address
        self.timeframe = timeframe
        self.aggregate = aggregate


class OnchainTokenOhlcvResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/tokens/{token_address}/ohlcv/{timeframe}"

    def __init__(
        self,
        network=None,
        token_address=None,
        timeframe=None,
        aggregate=None
    ):
        super().__init__(network)

        self.token_address = token_address
        self.timeframe = timeframe
        self.aggregate = aggregate


# ============================================================
# ONCHAIN - TRADES
# ============================================================
class OnchainPoolTradesResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/pools/{pool_address}/trades"

    def __init__(
        self,
        network=None,
        pool_address=None
    ):
        super().__init__(network)

        self.pool_address = pool_address


class OnchainPoolTradesRangeResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/pools/{pool_address}/trades/range"

    def __init__(
        self,
        network=None,
        pool_address=None,
        start_timestamp=None,
        end_timestamp=None
    ):
        super().__init__(network)

        self.pool_address = pool_address
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp


class OnchainTokenTradesResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/tokens/{token_address}/trades"

    def __init__(
        self,
        network=None,
        token_address=None
    ):
        super().__init__(network)

        self.token_address = token_address


class OnchainTokenTradesRangeResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/tokens/{token_address}/trades/range"

    def __init__(
        self,
        network=None,
        token_address=None,
        start_timestamp=None,
        end_timestamp=None
    ):
        super().__init__(network)

        self.token_address = token_address
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp


class OnchainTopTradersResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/tokens/{token_address}/top_traders"

    def __init__(
        self,
        network=None,
        token_address=None
    ):
        super().__init__(network)

        self.token_address = token_address


# ============================================================
# ONCHAIN - WALLETS
# ============================================================
class OnchainWalletResponseDto(OnchainResponseDto):
    def __init__(self, address=None):
        super().__init__()
        self.address = address


class OnchainWalletBalancesResponseDto(OnchainWalletResponseDto):
    endpoint = "/onchain/wallets/{address}/balances"

    def __init__(self, address=None):
        super().__init__(address)


class OnchainWalletTransfersResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/wallets/{address}/transfers"

    def __init__(
        self,
        network=None,
        address=None
    ):
        super().__init__(network)

        self.address = address


class OnchainWalletTradesResponseDto(OnchainResponseDto):
    endpoint = "/onchain/networks/{network}/wallets/{address}/trades"

    def __init__(
        self,
        network=None,
        address=None
    ):
        super().__init__(network)

        self.address = address


class OnchainWalletPnlResponseDto(OnchainWalletResponseDto):
    endpoint = "/onchain/wallets/{address}/pnl"

    def __init__(self, address=None):
        super().__init__(address)


# ============================================================
# ONCHAIN - HOLDERS
# ============================================================
class OnchainHoldersResponseDto(OnchainResponseDto):
    def __init__(
        self,
        network=None,
        token_address=None
    ):
        super().__init__(network)

        self.token_address = token_address


class OnchainTopHoldersResponseDto(OnchainHoldersResponseDto):
    endpoint = "/onchain/networks/{network}/tokens/{token_address}/top_holders"

    def __init__(
        self,
        network=None,
        token_address=None
    ):
        super().__init__(
            network,
            token_address
        )


class OnchainHoldersChartResponseDto(OnchainHoldersResponseDto):
    endpoint = "/onchain/networks/{network}/tokens/{token_address}/holders_chart"

    def __init__(
        self,
        network=None,
        token_address=None
    ):
        super().__init__(
            network,
            token_address
        )


# ============================================================
# ONCHAIN - CATEGORIES
# ============================================================
class OnchainCategoriesResponseDto(OnchainResponseDto):
    endpoint = "/onchain/categories"


class OnchainCategoryPoolsResponseDto(OnchainResponseDto):
    endpoint = "/onchain/categories/{category_id}/pools"

    def __init__(self, category_id=None):
        super().__init__()

        self.category_id = category_id
