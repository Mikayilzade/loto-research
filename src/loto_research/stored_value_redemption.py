from __future__ import annotations


def redemption_profit(balance: float, acquisition_cost: float, redemption_fee: float = 0.0, other_costs: float = 0.0) -> float:
    """Deterministic nominal profit if an already-valid stored-value balance is redeemed at face.

    This function is deliberately mechanical. Contractual blocking, provenance,
    transfer legality, counterparty/atomicity and execution risks must be cleared
    separately before any terminal guarantee claim.
    """
    if min(balance, acquisition_cost, redemption_fee, other_costs) < 0:
        raise ValueError("inputs cannot be negative")
    return balance - acquisition_cost - redemption_fee - other_costs


def max_safe_acquisition_cost(balance: float, redemption_fee: float = 0.0, other_costs: float = 0.0) -> float:
    """Strict break-even acquisition price before requiring a positive epsilon margin."""
    if min(balance, redemption_fee, other_costs) < 0:
        raise ValueError("inputs cannot be negative")
    return balance - redemption_fee - other_costs


def m10_qr_cashout_fee(balance: float) -> float:
    """Published QR cash-out fee: 0.5% with AZN 1 minimum."""
    if balance < 0:
        raise ValueError("balance cannot be negative")
    return max(0.005 * balance, 1.0) if balance else 0.0
