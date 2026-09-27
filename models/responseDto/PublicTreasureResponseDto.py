from models.responseDto.ResponseDto import ResponseDto
# ============================================================
# PUBLIC TREASURY
# ============================================================
class PublicTreasuryResponseDto(ResponseDto):
    def __init__(
        self,
        entity_id=None,
        coin_id=None
    ):
        super().__init__()

        self.entity_id = entity_id
        self.coin_id = coin_id


class PublicTreasuryEntitiesListResponseDto(PublicTreasuryResponseDto):
    endpoint = "/entities/list"


class PublicTreasuryByEntityCoinResponseDto(PublicTreasuryResponseDto):
    endpoint = "/{entity_id}/public_treasury/{coin_id}"

    def __init__(
        self,
        entity_id=None,
        coin_id=None
    ):
        super().__init__(
            entity_id,
            coin_id
        )


class PublicTreasuryByEntityResponseDto(PublicTreasuryResponseDto):
    endpoint = "/public_treasury/{entity_id}"

    def __init__(self, entity_id=None):
        super().__init__(entity_id=entity_id)


class PublicTreasuryHoldingChartResponseDto(PublicTreasuryResponseDto):
    endpoint = "/public_treasury/{entity_id}/{coin_id}/holding_chart"

    def __init__(
        self,
        entity_id=None,
        coin_id=None,
        days=None
    ):
        super().__init__(
            entity_id,
            coin_id
        )

        self.days = days


class PublicTreasuryTransactionHistoryResponseDto(PublicTreasuryResponseDto):
    endpoint = "/public_treasury/{entity_id}/transaction_history"

    def __init__(self, entity_id=None):
        super().__init__(entity_id=entity_id)
