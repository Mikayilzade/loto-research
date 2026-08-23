from math import comb
import json
from pathlib import Path

BASE={1:{1:2},2:{2:10},3:{3:25,2:2},4:{4:60,3:5,2:1},5:{5:330,4:20,3:2},6:{6:1000,5:55,4:6,3:1},7:{7:5000,6:100,5:15,4:2,3:1},8:{8:10000,7:550,6:75,5:6,4:2},9:{9:30000,8:3000,7:125,6:20,5:5,4:1},10:{10:100000,9:5000,8:300,7:45,6:10,5:2,0:5}}
BULL={1:{1:50},2:{2:62,1:15},3:{3:125,2:17,1:8},4:{4:300,3:25,2:11,1:5},5:{5:930,4:80,3:12,2:4,1:5},6:{6:3500,5:155,4:31,3:6,2:3,1:5},7:{7:12500,6:500,5:75,4:12,3:4,2:2,1:5},8:{8:50000,7:1800,6:200,5:26,4:7,3:2,2:2,1:5},9:{9:80000,8:8000,7:525,6:60,5:15,4:6,3:2,2:2,1:5},10:{10:300000,9:25000,8:1300,7:145,6:35,5:7,4:3,3:2,2:2,1:5}}
DOUBLE={2:{2:155},3:{3:313,2:43},4:{4:750,3:63,2:28},5:{5:2325,4:200,3:30,2:10},6:{6:8750,5:388,4:78,3:15,2:8},7:{7:31250,6:1250,5:188,4:30,3:10,2:5},8:{8:125000,7:4500,6:500,5:65,4:18,3:5,2:5},9:{9:200000,8:20000,7:1313,6:150,5:38,4:15,3:5,2:5},10:{10:1000000,9:62500,8:3250,7:363,6:88,5:18,4:8,3:5,2:5}}

def full_gross(spot, marked):
    gross=0
    seen=0
    other_winners=20-marked
    for r in range(marked+1):
        for m in range(spot+1):
            if m<r or m-r>other_winners or spot-m>60:
                continue
            count=comb(marked,r)*comb(other_winners,m-r)*comb(60,spot-m)
            seen += count
            if r==0:
                prize=BASE[spot].get(m,0)
            elif r==1:
                prize=BULL[spot].get(m,0)
            else:
                prize=DOUBLE.get(spot,{}).get(m,0)
            gross += count*prize
    assert seen==comb(80,spot)
    return gross

def main():
    rows=[]
    for s in range(1,11):
        n=comb(80,s)
        be=full_gross(s,1)
        dbe=full_gross(s,2)
        rows.append({
            'spot':s,'full_space_lines':n,
            'bulls_eye':{'cost_per_line_per_draw':2,'deterministic_gross_per_draw':be,'base_return_ratio':be/(2*n),'universal_50pct_upper_bound_return_ratio':1.5*be/(2*n)},
            'double_bulls_eye':{'cost_per_line_per_draw':3,'deterministic_gross_per_draw':dbe,'base_return_ratio':dbe/(3*n),'universal_50pct_upper_bound_return_ratio':1.5*dbe/(3*n)}
        })
    out={'packet':'H241','date':'2026-08-24','game':'Missouri Club Keno','promo_model':'universal +50% to every prize; stronger than real Bonus Hours','results':rows}
    Path('data/derived').mkdir(parents=True,exist_ok=True)
    Path('data/derived/h241_missouri_bullseye_bonus_hours_full_coverage.json').write_text(json.dumps(out,indent=2),encoding='utf-8')

if __name__=='__main__':
    main()
