from models.requestDto.requestDto import RequestDto
# ============================================================
# ONCHAIN - BASE
# ============================================================

class OnchainRequestDto(RequestDto):
    def __init__(self, network=None):
        super().__init__()
        self.network = network



# ============================================================
# ONCHAIN - PRICE
# ============================================================

class OnchainPriceRequestDto(OnchainRequestDto):
    endpoint = "/onchain/simple/networks/{network}/token_price/{addresses}"

    def __init__(
        self,
        network=None,
        addresses=None
    ):
        super().__init__(network)

        self.addresses = addresses


class OnchainMultiPriceRequestDto(OnchainRequestDto):
    endpoint = "/onchain/simple/token_price/multi"

    def __init__(self, addresses=None):
        super().__init__()
        self.addresses = addresses



# ============================================================
# ONCHAIN - SEARCH
# ============================================================

class OnchainSearchRequestDto(OnchainRequestDto):
    endpoint = "/onchain/search/pools"

    def __init__(self, query=None):
        super().__init__()
        self.query = query


class OnchainNetworksRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks"


class OnchainDexesRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/dexes"

    def __init__(self, network=None):
        super().__init__(network)



# ============================================================
# ONCHAIN - POOLS
# ============================================================
class OnchainPoolRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/pools/{address}"

    def __init__(
        self,
        network=None,
        address=None
    ):
        super().__init__(network)

        self.address = address


class OnchainPoolsMultiRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/pools/multi/{addresses}"

    def __init__(
        self,
        network=None,
        addresses=None
    ):
        super().__init__(network)

        self.addresses = addresses


class OnchainDexPoolsRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/dexes/{dex}/pools"

    def __init__(
        self,
        network=None,
        dex=None
    ):
        super().__init__(network)

        self.dex = dex


class OnchainNewPoolsRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/new_pools"

    def __init__(self, network=None):
        super().__init__(network)


class OnchainTrendingPoolsRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/trending_pools"

    def __init__(self, network=None):
        super().__init__(network)


class OnchainMegafilterRequestDto(OnchainRequestDto):
    endpoint = "/onchain/pools/megafilter"

    def __init__(self, **filters):
        super().__init__()
        self.filters = filters


class OnchainTrendingSearchRequestDto(OnchainRequestDto):
    endpoint = "/onchain/pools/trending_search"

    def __init__(self, query=None):
        super().__init__()
        self.query = query

class OnchainPoolsRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/pools"

    def __init__(self, network=None):
        super().__init__(network)


class OnchainTokenPoolsRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/tokens/{token_address}/pools"

    def __init__(
        self,
        network=None,
        token_address=None
    ):
        super().__init__(network)

        self.token_address = token_address
class OnchainNewPoolsGlobalRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/new_pools"


class OnchainTrendingPoolsGlobalRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/trending_pools"



# ============================================================
# ONCHAIN - TOKEN
# ============================================================
class OnchainTokenRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/tokens/{address}"

    def __init__(
        self,
        network=None,
        address=None
    ):
        super().__init__(network)

        self.address = address


class OnchainTokensMultiRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/tokens/multi/{addresses}"

    def __init__(
        self,
        network=None,
        addresses=None
    ):
        super().__init__(network)

        self.addresses = addresses


class OnchainTokensInfoRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/tokens/{address}/info"

    def __init__(
        self,
        network=None,
        address=None
    ):
        super().__init__(network)

        self.address = address


class OnchainTokensMultiInfoRequestDto(OnchainRequestDto):
    endpoint = "/onchain/tokens/multi"


class OnchainRecentlyUpdatedTokensRequestDto(OnchainRequestDto):
    endpoint = "/onchain/tokens/info_recently_updated"


# ============================================================
# ONCHAIN - CHARTS
# ============================================================
class OnchainOhlcvRequestDto(OnchainRequestDto):
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


class OnchainTokenOhlcvRequestDto(OnchainRequestDto):
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
class OnchainPoolTradesRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/pools/{pool_address}/trades"

    def __init__(
        self,
        network=None,
        pool_address=None
    ):
        super().__init__(network)

        self.pool_address = pool_address


class OnchainPoolTradesRangeRequestDto(OnchainRequestDto):
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


class OnchainTokenTradesRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/tokens/{token_address}/trades"

    def __init__(
        self,
        network=None,
        token_address=None
    ):
        super().__init__(network)

        self.token_address = token_address


class OnchainTokenTradesRangeRequestDto(OnchainRequestDto):
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


class OnchainTopTradersRequestDto(OnchainRequestDto):
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
class OnchainWalletRequestDto(OnchainRequestDto):
    def __init__(self, address=None):
        super().__init__()
        self.address = address


class OnchainWalletBalancesRequestDto(OnchainWalletRequestDto):
    endpoint = "/onchain/wallets/{address}/balances"

    def __init__(self, address=None):
        super().__init__(address)


class OnchainWalletTransfersRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/wallets/{address}/transfers"

    def __init__(
        self,
        network=None,
        address=None
    ):
        super().__init__(network)

        self.address = address


class OnchainWalletTradesRequestDto(OnchainRequestDto):
    endpoint = "/onchain/networks/{network}/wallets/{address}/trades"

    def __init__(
        self,
        network=None,
        address=None
    ):
        super().__init__(network)

        self.address = address


class OnchainWalletPnlRequestDto(OnchainWalletRequestDto):
    endpoint = "/onchain/wallets/{address}/pnl"

    def __init__(self, address=None):
        super().__init__(address)


# ============================================================
# ONCHAIN - HOLDERS
# ============================================================
class OnchainHoldersRequestDto(OnchainRequestDto):
    def __init__(
        self,
        network=None,
        token_address=None
    ):
        super().__init__(network)

        self.token_address = token_address


class OnchainTopHoldersRequestDto(OnchainHoldersRequestDto):
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


class OnchainHoldersChartRequestDto(OnchainHoldersRequestDto):
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
class OnchainCategoriesRequestDto(OnchainRequestDto):
    endpoint = "/onchain/categories"


class OnchainCategoryPoolsRequestDto(OnchainRequestDto):
    endpoint = "/onchain/categories/{category_id}/pools"

    def __init__(self, category_id=None):
        super().__init__()

        self.category_id = category_id
