from math import inf

DRAWS = {
    "flight_centre_5000": {
        "entries": 2000,
        "packs": [(1,10),(4,34),(8,60)],
        "player_prize_value": 5000,
        "cash_alternative": 4000,
    },
    "dji_osmo_769": {
        "entries": 500,
        "packs": [(1,5),(5,22),(10,40)],
        "player_prize_value": 769,
        "cash_alternative": 600,
    },
    "apple_watch_airpods_618": {
        "entries": 1000,
        "packs": [(1,1),(8,7),(19,15)],
        "player_prize_value": 618,
        "cash_alternative": 500,
    },
    "airpods_219": {
        "entries": 90,
        "packs": [(1,5),(3,13),(6,24)],
        "player_prize_value": 219,
        "cash_alternative": 150,
    },
}

def min_exact_cost(n, packs):
    dp=[inf]*(n+1); dp[0]=0
    for i in range(1,n+1):
        for count,cost in packs:
            if i>=count:
                dp[i]=min(dp[i], dp[i-count]+cost)
    return int(dp[n])

def main():
    out={}
    for name,d in DRAWS.items():
        cost=min_exact_cost(d['entries'], d['packs'])
        value=d['player_prize_value']
        cash=d['cash_alternative']
        assert cost>0 and value<cost and cash<cost
        out[name]={
            "entries":d['entries'],
            "min_exact_full_acquisition_cost_aud":cost,
            "player_prize_value_aud":value,
            "cash_alternative_aud":cash,
            "retail_value_return":value/cost,
            "cash_return":cash/cost,
            "retail_value_deficit_aud":cost-value,
            "cash_deficit_aud":cost-cash,
        }
    best=max(out.items(), key=lambda kv: kv[1]['retail_value_return'])
    assert best[0]=='apple_watch_airpods_618'
    assert best[1]['retail_value_return'] < 1
    print(out)

if __name__=='__main__':
    main()
