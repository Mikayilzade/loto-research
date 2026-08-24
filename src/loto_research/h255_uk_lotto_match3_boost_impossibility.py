from math import comb
import json

N=comb(59,6)
p3=comb(6,3)*comb(53,3)/N
p4=comb(6,4)*comb(53,2)/N
p5=6*52/N
p5b=6/N

ev_match3_100=100*p3
ev_fixed_cash=100*p3+140*p4+1750*p5+1_000_000*p5b

out={
  'packet':'H255',
  'game':'UK Lotto 6/59 historical Match-3 £100 boost structure',
  'ticket_price_gbp':2.0,
  'combination_space':N,
  'p_exact_match3':p3,
  'expected_match3_100_cash_per_ticket':ev_match3_100,
  'expected_fixed_cash_per_ticket_including_match4_match5_match5bonus':ev_fixed_cash,
  'fixed_cash_ratio_to_ticket_price':ev_fixed_cash/2,
  'necessary_condition_for_all_draw_cash_profit':'average payout per ticket must exceed ticket price',
  'result':'fails; additive fixed-tier portfolio cannot have strictly positive cash profit on every draw because its average over draws is below spend',
}
print(json.dumps(out,indent=2))
