import json
import os
import numpy as np
from collections import defaultdict
import argparse


def rank_patches(key, raw_patches):

    patches = [p for p in raw_patches if p['validation_wo'] == 'plausible']
    
    if key == 'mixed':
        return sorted(patches, key=lambda x:(x['pass_FIB_num'], x['mean_entropy'],-x['index']), reverse=True)

    else:
        return sorted(patches, key=lambda x:x[key], reverse=True)


def evaluate(k, patches, bug_id):
    i = 1 
    for p in patches:
        if i > k:
            break
        if p['correctness'] == 'correct':
            return True
        i += 1
            
    return False

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--eval', default='combine_fl', choices=['combine_fl','lowerbound'])
    parser.add_argument('--dataset', default='gt', choices=['gt', 'ifixr'])
    args = parser.parse_args()

    if args.dataset == 'ifixr':
        with open('iFixR_bug_list.txt', 'r') as f:
            ifixr_bug = f.readlines()
        ifixr_bug = [b.strip() for b in ifixr_bug]

    if args.eval == 'combine_fl':
        directory = 'RQ4_combine_fl_rank'
        rank_method = ['mixed']
        with open('RQ4_combine_fl_previous_validation.json', 'r') as f:
            previous_data = json.load(f)
    elif args.eval == 'lowerbound':
        directory = 'RQ4_lowerbound_rank'
        rank_method = ['mean_entropy']
        with open('RQ4_irfl_previous_validation.json', 'r') as f:
            previous_data = json.load(f)
    


    rank_result = {}
    record = False
    for k in [1,5, 10, 100]:
        correct_bugs = []
        print(f'Consider top{k} ---------------------')
        # for key in ['sum_entropy', 'mean_entropy', 'pass_FIB_num', 'embedding_similarity', 'mixed', 'codet']:
        # for key in ['mixed']:
        for key in rank_method:
            if key != 'random':
                count = 0
                count_ = 0
                for file in os.listdir(directory):
                    if file.endswith('.json'):
                        with open(os.path.join(directory, file), 'r') as f:
                            data = json.load(f)
                        for nlkey, item in data.items():
                            patches = []
                            bug_id = '_'.join(nlkey.split('_')[:2])
                            patches = rank_patches(key, item['patches'])
                            if bug_id in previous_data:
                                patches = previous_data[bug_id] + patches
                            if args.dataset != 'gt':
                                if bug_id not in ifixr_bug:
                                    patches = []
                                    break
                        if evaluate(k,patches,bug_id):
                            count += 1
                            if bug_id not in correct_bugs:
                                correct_bugs.append(bug_id)
                            # if bug_id_ in bug_cat['single_method_bug']:
                            #     count_ += 1
                print(f'{key}  {count}')   

    if record:
        with open('ranking_result.json', 'w') as f:
            json.dump(rank_result, f, indent=2)
    with open('final_fixed_bug.txt', 'w') as f:
        f.write('\n'.join(correct_bugs))