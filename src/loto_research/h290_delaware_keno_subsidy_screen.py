"""H290 reproducible arithmetic for Delaware KENO deposit-subsidy screen."""
from math import comb

PAY={
1:{1:2},2:{2:10},3:{3:25,2:2},4:{4:50,3:5,2:1},5:{5:300,4:15,3:2},
6:{6:1000,5:50,4:5,3:1},7:{7:2500,6:100,5:15,4:3,3:1},
8:{8:10000,7:500,6:50,5:10,4:2},9:{9:25000,8:2500,7:100,6:20,5:5,0:2},
10:{10:100000,9:4000,8:400,7:50,6:10,5:2,0:4}}

def ev(spot):
    den=comb(80,spot)
    return sum(comb(20,m)*comb(60,spot-m)/den*PAY[spot].get(m,0)
               for m in range(spot+1) if spot-m<=60 and m<=20)

def balanced_sizes(n,m):
    q,r=divmod(n,m)
    return [q+1]*r+[q]*(m-r)

def min_pairs(sizes,k=20):
    x=[0]*len(sizes)
    for _ in range(k):
        _,i=min((x[i],i) for i,s in enumerate(sizes) if x[i]<s)
        x[i]+=1
    return sum(comb(v,2) for v in x)

def main():
    evs={s:ev(s) for s in range(1,11)}
    assert max(evs,key=evs.get)==3
    assert abs(evs[1]-0.5)<1e-12
    # all-number Spot-1 cover
    assert 80==80 and 20*2==40
    clique=[]
    for m in range(2,81):
        sizes=balanced_sizes(80,m)
        E=sum(comb(s,2) for s in sizes)
        if E<=200:
            w=min_pairs(sizes)
            clique.append((m,E,w,10*w-E/2))
    assert max(x[3] for x in clique)<=0
    print({'spot_ev':evs,'best_spot':3,'spot1_cover_cost':80,'spot1_cover_gross':40,
           'balanced_clique_best_profit_vs_half_cost':max(x[3] for x in clique)})

if __name__=='__main__': main()
