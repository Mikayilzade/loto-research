from __future__ import annotations


def free_bet_equal_profit(
    token_stake: float,
    bookmaker_odds: float,
    lay_odds: float,
    exchange_commission: float = 0.0,
) -> tuple[float, float]:
    """Equal-profit conversion of a stake-not-returned free-bet token.

    Returns (lay_stake, guaranteed_cash_profit) after both legs are accepted.

    Bookmaker-win branch:
        token_stake * (bookmaker_odds - 1) - lay_stake * (lay_odds - 1)
    Bookmaker-loss branch:
        lay_stake * (1 - exchange_commission)
    """
    if token_stake <= 0:
        raise ValueError("token_stake must be positive")
    if bookmaker_odds <= 1 or lay_odds <= 1:
        raise ValueError("decimal odds must exceed 1")
    if not 0 <= exchange_commission < 1:
        raise ValueError("exchange_commission must be in [0,1)")
    denominator = lay_odds - exchange_commission
    lay_stake = token_stake * (bookmaker_odds - 1) / denominator
    guaranteed_profit = lay_stake * (1 - exchange_commission)
    return lay_stake, guaranteed_profit


def qualifying_cash_bet_equal_profit(
    cash_stake: float,
    bookmaker_odds: float,
    lay_odds: float,
    exchange_commission: float = 0.0,
) -> tuple[float, float]:
    """Equal-profit hedge for a normal cash qualifying bet.

    Returns (lay_stake, guaranteed_net_profit). The result is commonly a small
    negative 'qualifying loss' when the lay price/commission is slightly worse.
    """
    if cash_stake <= 0:
        raise ValueError("cash_stake must be positive")
    if bookmaker_odds <= 1 or lay_odds <= 1:
        raise ValueError("decimal odds must exceed 1")
    if not 0 <= exchange_commission < 1:
        raise ValueError("exchange_commission must be in [0,1)")
    denominator = lay_odds - exchange_commission
    lay_stake = cash_stake * bookmaker_odds / denominator
    guaranteed_profit = -cash_stake + lay_stake * (1 - exchange_commission)
    return lay_stake, guaranteed_profit


def welcome_offer_floor(
    token_values: list[float],
    token_bookmaker_odds: float,
    token_lay_odds: float,
    qualifying_stake: float,
    qualifying_bookmaker_odds: float,
    qualifying_lay_odds: float,
    exchange_commission: float = 0.0,
) -> float:
    """Mechanical all-outcome floor after all bookmaker/exchange legs fill.

    This is a settlement-math result only. It is not a contractual guarantee:
    eligibility, promotion-abuse/clawback terms, voids, market-rule mismatch,
    liquidity and jurisdiction must be separately cleared.
    """
    total = 0.0
    for token in token_values:
        _, floor = free_bet_equal_profit(
            token,
            token_bookmaker_odds,
            token_lay_odds,
            exchange_commission,
        )
        total += floor
    _, qualifier = qualifying_cash_bet_equal_profit(
        qualifying_stake,
        qualifying_bookmaker_odds,
        qualifying_lay_odds,
        exchange_commission,
    )
    return total + qualifier
