
# evaluate lowerbound performance on iFixR dataset
python ./rq4_ranking.py --eval lowerbound --dataset ifixr
# evaluate lowerbound performance on GT-Repair dataset
python ./rq4_ranking.py --eval lowerbound --dataset gt
# evaluate GT-Repair performance on iFixR dataset
python ./rq4_ranking.py --eval combine_fl --dataset ifixr
# evaluate GT-Repair performance on GT-Repair dataset
python ./rq4_ranking.py --eval combine_fl --dataset gt
