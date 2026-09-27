from models.requestDto.RequestDto import RequestDto
# ============================================================
# PUBLIC TREASURY
# ============================================================
class PublicTreasuryRequestDto(RequestDto):
    def __init__(
        self,
        entity_id=None,
        coin_id=None
    ):
        super().__init__()

        self.entity_id = entity_id
        self.coin_id = coin_id


class PublicTreasuryEntitiesListRequestDto(PublicTreasuryRequestDto):
    endpoint = "/entities/list"


class PublicTreasuryByEntityCoinRequestDto(PublicTreasuryRequestDto):
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


class PublicTreasuryByEntityRequestDto(PublicTreasuryRequestDto):
    endpoint = "/public_treasury/{entity_id}"

    def __init__(self, entity_id=None):
        super().__init__(entity_id=entity_id)


class PublicTreasuryHoldingChartRequestDto(PublicTreasuryRequestDto):
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


class PublicTreasuryTransactionHistoryRequestDto(PublicTreasuryRequestDto):
    endpoint = "/public_treasury/{entity_id}/transaction_history"

    def __init__(self, entity_id=None):
        super().__init__(entity_id=entity_id)
