# encoding=utf-8
from csv import DictReader
from typing import List
import os
import json
from os.path import join
import logging
import argparse

from objects import GTInfo, Method

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = "/".join(CURRENT_PATH.split("/")[:-2])

class HitK:
    def __init__(self, k):
        self.k = k

    def eval(self, ranked_methods_list: List[List[Method]], gt_sig_list: List[GTInfo]):
        assert len(gt_sig_list) > 0
        hit = 0
        bugs = {}
        # This is the signature of the method
        for ranked_methods, gt_sig in zip(ranked_methods_list, gt_sig_list):
            topk_methods = ranked_methods[:self.k]
            for method in topk_methods:
                if method.cover(gt_sig):
                    hit += 1
                    proj = gt_sig.bug_id.split('_')[0]
                    bugid = gt_sig.bug_id.split('_')[1]
                    bugid = int(bugid)
                    if proj not in bugs.keys():
                        bugs[proj] = [bugid]
                    else:
                        bugs[proj].append(bugid)
                    break
        for proj in bugs.keys():
            bugs[proj].sort()
        with open(f'./top_{self.k}.txt','w') as f:
            sorted_proj = sorted(bugs.keys())
            for proj in sorted_proj:
                f.writelines(proj+':')
                f.writelines(str(bugs[proj])+'\n')
        # the number of defects

        return hit

class EXAM:
    def __init__(self):
        # EXAM should inspect all recommended results
        pass

    def eval(self, ranked_methods_list: List[List[Method]], gt_sig_list: List[GTInfo], defects: List):
        assert len(gt_sig_list) > 0
        sum_exam = 0
        fail = []
        for ranked_methods, gt_sig, defect in zip(ranked_methods_list, gt_sig_list, defects):
            inspected = 0
            for method in ranked_methods:
                # only inspect suspicious methods
                if method.score == 0:
                    break
                inspected += 1
                if method.cover(gt_sig):

                    break
            if inspected == len(ranked_methods):
                # logging.warning("Unable to localize: %s, %d, %d, %s", gt_sig.source_file, gt_sig.start_line,
                #                 gt_sig.end_line, str(defect))
                fail.append(defect)
                pass
            if len(ranked_methods) == 0:
                exam = 1
            else:
                exam = inspected / len(ranked_methods)
            sum_exam += exam
        avg_exam = sum_exam / len(gt_sig_list)
        with open('fail.txt', 'w') as f:
            f.write('\n'.join(fail))

        return avg_exam

def eval(method, result_dir):
    # bug_file: str = f"{ROOT_DIR}/data/bug_list/bug_list.txt"   
    bug_file: str = "C:\\APR\\FL\\FL\\data\\bug_list\\bug_list.txt"
    
    # gt_file: str = f"{ROOT_DIR}/data/ground_truth/BR2FIX_bug_dataset.json"
    gt_file: str = "C:\\APR\\FL\\FL\\data\\ground_truth\\ground_truth.json"
    # load the bugs
    bugs = []
    with open(bug_file, 'r') as f:
        for line in f.readlines():
            bugs.append(line.strip())

    with open(gt_file, 'r') as f:
        ground_truth = json.load(f)

    ranked_methods_list = []
    gt_sig_list = []
    num = 0
    for bug_id in bugs:
            # if bug_id == 'Closure_129':
            #     continue
            num += 1
            result_file = join(result_dir, f"{bug_id.split('_')[0]}-{bug_id.split('_')[1]}" + "_" + "method-susps.csv")
            gt_info = GTInfo(bug_id,**ground_truth[bug_id])
            gt_sig_list.append(gt_info)

            # load the results
            ranked_methods = []
            with open(result_file, 'r') as f:
                reader = DictReader(f)
                for row in reader:
                    ranked_methods.append(Method(**row,method=method))
            ranked_methods_list.append(ranked_methods)

    for k in [1, 3, 5, 10, 15, 20]:
        hitk_scorer = HitK(k)
        hitk = hitk_scorer.eval(ranked_methods_list, gt_sig_list)
        print("{}: {}".format(k, hitk))
    exam_scorer = EXAM()
    exam = exam_scorer.eval(ranked_methods_list, gt_sig_list, bugs)
    print('Exam:',exam)
    print(num)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--method', default='stat2func')
    parser.add_argument('-r', '--result_dir')
    args = parser.parse_args()
    eval(method=args.method, result_dir=args.result_dir)