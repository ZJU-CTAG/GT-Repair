import json
import os
import numpy as np
from collections import defaultdict


def rank_patches(key, raw_patches):

    patches = [p for p in raw_patches if p['validation_wo'] == 'plausible']
    
    if key == 'index':
        return sorted(patches, key=lambda x:x[key])
    elif key == 'random':
        np.random.shuffle(patches)
        return patches
    elif key == 'embedding_similarity':
        below_0_95 = [p for p in patches if p[key] < 0.95]
        above_or_equal_0_95 = [p for p in patches if p[key] >= 0.95]
        above_or_equal_0_95_sorted = sorted(above_or_equal_0_95, key=lambda x: x[key])
        sorted_list = above_or_equal_0_95_sorted + below_0_95
        return sorted_list
    elif key == 'mixed':
        return sorted(patches, key=lambda x:(x['pass_FIB_num'],x['mean_entropy'], -x['index']), reverse=True)
    elif key =='codet':
        consensus = defaultdict(set)
        patches = sorted(patches, key=lambda x:x['pass_FIB_num'], reverse=True)
        for p in patches:
            if p['pass_FIB_num'] == 0:
                break
            else:
                if tuple(p['pass_FIB']) in consensus:
                    consensus[tuple(p['pass_FIB'])].append(p['index'])
                else:
                    consensus[tuple(p['pass_FIB'])] = [p['index']]
        for p in patches:
            if p['pass_FIB_num'] == 0:
                p.update({'consensus_size':-1})
            else:
                consensus_size = 0.8 * p['pass_FIB_num'] * len(consensus[tuple(p['pass_FIB'])])
                p.update({'consensus_size': consensus_size})
        return sorted(patches, key=lambda x: x['consensus_size'], reverse= True)
    else:
        return sorted(patches, key=lambda x:x[key], reverse=True)


def evaluate(k, patches):
    i = 1 
    for p in patches:
        if i > k:
            break
        if 'correctness' in p and p['correctness'] == 'correct':
            return True
        i += 1
            
    return False
    
if __name__ == '__main__':
    directory = 'perfect_fl_add_test_gpt'
    rank_result = {}
    record = False
    for k in [1,3,5]:
        print(f'Consider top{k} ---------------------')
        for key in ['sum_entropy', 'mean_entropy', 'pass_FIB_num', 'embedding_similarity', 'mixed', 'codet']:
        # for key in ['mixed']:
        # for key in ['pass_FIB_num','codet']:
        # for key in ['random']:
        # key = 'random'
            if key != 'random':
                count = 0
                for file in os.listdir(directory):
                    if file.endswith('.json'):
                        with open(os.path.join(directory, file), 'r') as f:
                            data = json.load(f)
                        for bug_id, item in data.items():
                            patches = rank_patches(key, item['patches'])
                            rank_result[bug_id] = [p['index'] for p in patches]
                        if evaluate(k,patches):
                            count += 1
                print(f'{key}  {count}')   
            # if key == 'random':
            #     count = 0
            #     for _ in range(5):
            #         for file in os.listdir(directory):
            #             if file.endswith('.json'):
            #                 with open(os.path.join(directory, file), 'r') as f:
            #                     data = json.load(f)
            #                 for bug_id, item in data.items():
            #                     patches = rank_patches(key, item['patches'])
            #                 if evaluate(k,patches):
            #                     count += 1
            #     count /= 5
            #     print(f'{key}  {count}') 
    if record:
        with open('./ranking_result.json', 'w') as f:
            json.dump(rank_result, f, indent=2)