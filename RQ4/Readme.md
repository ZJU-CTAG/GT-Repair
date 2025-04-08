File Structure:
- RQ4_combine_fl_rank       // patches of ground truth fault localization, not include uncompilable patches and fail-in-validation patches
- RQ4_lowerbound_rank       // patches of ground truth fault localization for lowerbound evaluation
- RQ4_combine_fl_previous_validation.json   // patches of wrong fault localization that ranked ahead of the patches of ground truth
- RQ4_lowerbound_fl_previous_validation.json  // patches of wrong fault localization that ranked ahead of the patches of ground truth, for lowerbound evaluation

- baselines.xlsx            // fixed bug list of compared approaches
- draw_venn.py & venn.py    // scripts to draw the venn figure in paper
- iFixR_bug_list.txt        // datasets used by iFixR



# evaluate lowerbound performance on iFixR dataset
python ./rq4_ranking.py --eval lowerbound --dataset ifixr
# evaluate lowerbound performance on GT-Repair dataset
python ./rq4_ranking.py --eval lowerbound --dataset gt
# evaluate GT-Repair performance on iFixR dataset
python ./rq4_ranking.py --eval combine_fl --dataset ifixr
# evaluate GT-Repair performance on GT-Repair dataset
python ./rq4_ranking.py --eval combine_fl --dataset gt
