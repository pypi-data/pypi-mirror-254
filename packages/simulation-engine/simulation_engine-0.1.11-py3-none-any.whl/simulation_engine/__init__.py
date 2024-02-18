from random import random, choice

import relic_engine
import itertools

num_runs_dict = {
    'Solo': 1,
    '1b1': 4,
    '2b2': 2,
    '3b3': (4 / 3),
    '4b4': 1,
    '8b8': 1,
}


def get_set_price(prime_part):
    set_name = relic_engine.get_set_name(prime_part) + " Set"

    return relic_engine.get_price(set_name)


def get_drop_priority(relics, min_price=30):
    plat_list = []
    ducat_list = []

    relic_dict = relic_engine.get_relic_dict()

    for relic in relics:
        for drop in relic_dict[relic]:
            if get_set_price(drop) >= min_price:
                plat_list.append([drop, relic_engine.get_price(drop)])
            else:
                ducat_list.append([drop, relic_engine.get_ducats(drop)])

    drop_prioity = {k: v + 1 for v, k in enumerate([item[0] for item in
                                                    sorted(plat_list, key=lambda x: x[1], reverse=True)])}

    drop_prioity.update({k: v + 101 for v, k in enumerate([item[0] for item in
                                                           sorted(ducat_list, key=lambda x: x[1], reverse=True)])})

    return drop_prioity


def get_possible_rewards(relics, refinement):
    drops = []
    for relic in relics:
        relic_drops = relic_engine.get_relic_drops(relic, refinement)
        drop_dict = {}
        for drop in relic_drops:
            drop_dict[drop] = {'chance': relic_drops[drop],
                               'refinement': refinement}
        drops.append(drop_dict)

    return drops


__rarity_dict = {
    'i': {
        ((25 + (1 / 3)) / 100): "Common",
        .11: "Uncommon",
        .02: "Rare"
    },
    'e': {
        ((23 + (1 / 3)) / 100): "Common",
        .13: "Uncommon",
        .04: "Rare"
    },
    'f': {
        .2: "Common",
        .17: "Uncommon",
        .06: "Rare"
    },
    'r': {
        (1 / 6): "Common",
        .2: "Uncommon",
        .1: "Rare"
    },
}


def get_rarity(chance, refinement):
    return __rarity_dict[refinement][chance]


def get_drop(reward_lists):
    random_num = random()

    reward_list = choice(reward_lists)

    chance = 0
    for i in reward_list:
        chance += reward_list[i]['chance']
        if random_num < chance:
            return [i, get_rarity(reward_list[i]['chance'], reward_list[i]['refinement'])]

    return ['Forma Blueprint', "Uncommon"]


def get_best_drop(drops, drop_order):
    return sorted(drops, key=lambda val: drop_order[val[0]])[0][0], drops


def get_reward_screen(relics):
    reward_screen = []
    for relic in relics:
        reward_screen.append(get_drop(relic))

    return reward_screen


def process_run(drops, offcycle_drops, style, drop_priority):
    if style == 'Solo':
        num_drops = 1
    else:
        num_drops = int(style.split('b')[0])

    num_offcycle_drops = []
    if style != "4b4":
        if len(offcycle_drops) > 0:
            if len(offcycle_drops) == 1:
                num_offcycle_drops = [4 - num_drops]
            elif len(offcycle_drops) == 2:
                if style == "2b2":
                    num_offcycle_drops = [1, 1]
                elif style == "1b1":
                    num_offcycle_drops = random.sample([1, 2], 2)
            elif len(offcycle_drops) == 3:
                if style == "2b2":
                    num_offcycle_drops = random.sample([0, 1, 2], 3)
                elif style == "1b1":
                    num_offcycle_drops = [1, 1, 1]
            else:
                num_offcycle_drops = [4 - num_drops]
    elif style == "4b4" and len(offcycle_drops) == 1:
        num_offcycle_drops = [4]

    relics = []
    relics.extend(drops for _ in range(num_drops))
    for i in range(len(offcycle_drops)):
        relics.extend(offcycle_drops[i] for _ in range(num_offcycle_drops[i]))

    best_drop, reward_screen = get_best_drop(get_reward_screen(relics), drop_priority)

    return best_drop, reward_screen


def simulate_relic(relics, offcycle_relics, refinement, offcycle_refinement, style, amount,
                   drop_priority=None):
    reward_list = []
    reward_screen = []
    offcycle_drops = []

    drops = get_possible_rewards(relics, refinement[0].lower())

    for i in range(len(offcycle_relics)):
        offcycle_drops.append(get_possible_rewards(offcycle_relics[i], offcycle_refinement[i][0].lower()))

    if drop_priority is None:
        drop_priority = get_drop_priority(relics + [j for i in offcycle_relics for j in i])

    if style in num_runs_dict:
        num_runs = num_runs_dict[style]
    else:
        num_runs = 1

    reward_list, reward_screen = zip(*[process_run(drops, offcycle_drops, style, drop_priority)
                                       for _ in itertools.repeat(None, int(amount * num_runs))])

    return list(reward_list), list(reward_screen)
