File Structure:
- data
    - bug_list.txt          // Bug List of 374 bugs we research
    - ground_truth.json     // Ground Truth for method-level FL
- res
    - combine               // results of combined FL (sbfl+irfl)
    - irfl                  // results of irfl
    - sbfl                  // results of sbfl
        - max               // MA using max
        - max_var           // MA using max+var
        - var               // MA using var

- src
    - main.py               // Source Code for evaluation
                            // There are two arguments
                            // -m : If you want to evaluate results of sbfl, use `-m stat2func`
                                    If you want to evaluate results of irfl or combine, use `-m irfl`
                            // -r : the dir of results you want to evaluate
    - objects.py            // Assistance Class for evaluation

### Here are complete scripts for evaluation

# evaluate irfl
python ./src/main.py -m irfl -r ./res/irfl
# evaluate sbfl
python ./src/main.py -m stat2func -r ./res/sbfl/max_var

# evaluate combine results of irfl and sbfl
python ./src/main.py -m irfl -r ./res/combine
