#!/usr/bin/env python
import sys
import time
sys.path.append('../src')
from coalitions.util import *
from coalitions.coalitionalgame import *
from coalitions.typedcoalitionalgame import *

def un_security_old(player_counts):
    """According to "old" security council rules for a ruling to pass it needs supprt of all
       5 permanent 'P' members and 2 temporary '2' Members.
       Argument pass to fun will look like (('P', 4), ('T':2))"""
    perms = 0
    temps = 0
    for elm in player_counts:
        if elm[0] == 'P':
            perms = elm[1]
        elif elm[0] == 'T':
            temps = elm[1]
    if perms >= 5 and temps >= 2:
        return 1
    return 0

def us_bill(player_counts):
    """For a us bill to become a law, it must have either
       A majority in congress C and the senate S and be signed by the president P OR
       A 2/3 majority in both C and S
    """
    counts = dict_from_tuple(player_counts)
    if counts['S'] > 50 and counts['C'] > 217 and counts['P'] > 0:
        return 1
    if counts['S'] > 66 and counts['C'] > 289:
        return 1
    return 0


if __name__ == '__main__':
    # gloves game. Shapley and banzhaf values must be the same for Colition and TypedCoalition
    started = time.time()
    vals = {('L1', 'R'):1,('L2', 'R'):1}
    cgg =  CoalitionalGame(vals)
    print('coalitional gloves game shapeley', cgg.get_shapley_values())
    print('coalitional gloves game shapeley simulated ', cgg.simulate_shapley_values(10000))
    print('coalitional gloves games banzhaf', cgg.get_banzhaf_values())
    print('coalitional gloves games is_simple', cgg.get_is_simple())
    print('coalitional gloves games is_superadditive', cgg.get_is_superadditive())
    print('coalitional gloves games is_monotonic', cgg.get_is_monotonic())
    vals = {(('L', 1), ('R',1)):1}
    tgp = {'L':2, 'R':1}
    tgg = create_typed_game(player_types=tgp, coalition_values=vals)
    print('typed gloves game valuation', tgg.get_valuation())
    print('typed gloves game shapeley', tgg.get_shapley_values())
    print('typed gloves game shapeley simulated ', tgg.simulate_shapley_values(10000))
    print('typed gloves games banzhaf', tgg.get_banzhaf_values())
    print('typed gloves games is_simple', tgg.get_is_simple())
    print('typed gloves games is_monotonic', tgg.get_is_monotonic())
    print('typed gloves games is_superadditive', tgg.get_is_superadditive())

    # renormalized gloves game
    vals =  {('L1',): 3, ('L1', 'R'):6,('L2', 'R'):3}
    cggr =  CoalitionalGame(vals)
    cggn, _  = cggr.zero_normalize()
    print('gloves game zero nomalized', cggn.coalition_values)
    print('gloves equivalent?', cgg.is_equivalent(cggr))
    vals = {(('L', 1), ('R',1)):3, (('L', 1), ('R', 0)):1}
    tggr = create_typed_game(player_types=tgp, coalition_values=vals)
    print('typed gloves game renormalized valuaation', tggr.get_valuation())
    print('typed gloves equivalent?', tgg.is_equivalent(tggr))

    tg_un = TypedCoalitionalGame(player_types = {'T':6, 'P':5}, coalition_valuation=un_security_old)
    print('un security old shapeley', tg_un.get_shapley_values())
    print('un security old banzhaf', tg_un.get_banzhaf_values())

    # test is core
    # Maschler et all firt game p 737
    # core values staisfy x1 + x2 + x3 = 1
    # x1 + x2 ≥ 1
    # x1 + x3 ≥ 2
    # x2 + x3 ≥ 1
    # x1, x2, x3 ≥ 0
    vals = {(1,2):1, (2,3):1, (1,3):2, (1,2,3):3}
    corgi = CoalitionalGame(vals)
    print('is_core yes', corgi.is_core({1:0, 2:1, 3:2}))
    print('is_core no', corgi.is_core({1:1, 2:2, 3:0}))

    # bill becomes a law
    if False:
        tg_bill =  TypedCoalitionalGame(player_types = {'P':1, 'S':100, 'C':435}, coalition_valuation = us_bill)
        print('us bill shapeley simulated', tg_bill.simulate_shapley_values(10000)) # actual calculation takes forever
        print('us bill banzhaf', tg_bill.get_banzhaf_values())

    # voting games must give the same value
    player_strengths = {'o1':1, 'o2':1, 'o3':1, 'o4':1, 'o5':1, 'o6':1, 'o7':1, 't1':3, 't2':3, 't3':3}
    vg = create_voting_game(player_strengths)
    print('voting game shapley', vg.get_shapley_values())
    print('voting game banzhaf', vg.get_banzhaf_values())

    player_types = {'three':3, 'one':7}
    type_strengths = {'three':3, 'one':1}
    tgv = create_typed_voting_game(player_types=player_types, type_strengths=type_strengths)
    print('typed voting game shapley', tgv.get_shapley_values())
    print('typed voting game banzhaf', tgv.get_banzhaf_values())



    print('elapsed', round(time.time() - started, 2))

