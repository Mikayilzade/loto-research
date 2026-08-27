# H316 STATUS — Punter Prizes postal-bundle bound

Updated: 2026-08-27
State: **CLOSED / NO SUCCESS**

## Terminal checkpoint

Current Punter Prizes `CASH DASH 3` was tested because its free-entry route credits multiple competition entries per separate postal item when ticket price is below second-class postage, and the competition advertises itself as `no margin`.

Rigorous result:
- full pool: 20,000 × £0.10 = **£2,000** acquisition cost;
- deliberately favourable total advertised face liability: **£2,000**;
- impossible-perfect paid takeover = **100% gross exactly**, therefore no strict profit;
- current 91p second-class postage yields at most 9 credited 10p entries per letter;
- full postal takeover would cost **£2,022.93**, return **98.8665%**;
- live snapshot already had 1,811 tickets sold and only £1,800 favourable prize face remaining against £1,818.90 paid or £1,839.11 postal remaining-pool takeover cost.

Independent execution blocker: postal entries are not atomically reserved; each must arrive before close/cap and the promoter does not pre-confirm receipt/correctness.

## Reusable conclusion

If a postal route awards at most `floor(postage/ticket_price)` entries, its effective cost per credited entry can never be below the paid ticket price. This mechanism is not a deterministic subsidy.

## NEXT ACTION

Do **not** reopen H316 unless the operator changes the rule materially. Continue with a genuinely new finite-pool mechanism satisfying at least one of:
- deterministic liabilities > exact paid full-pool acquisition cost;
- electronic/free route gives entries at a true below-ticket acquisition cost and reserves them immediately;
- exact prize-bearing identifiers can be selected/reserved before external interception.

H225-X* remains separately `CLOSED / EXHAUSTED` at X20 and must not be extended without broadening the mathematical family.
