# ContextFair
Exploring the Impact of Temporal Bias in Point-of-Interest Recommendation (RecSys 22) 

## Note
The paper has been submitted to the RecSys conference and upon acceptance, the details of codes, datasets, and results will be made available.

# Context Fairness

## Contents

- Folders:
    - __datasets__: including datasets (Gowalla and Yelp)
        - In Yelp dataset we do not have the frequecny of ckeck-ins, we have the rating to each location. For example, in _Yelp_checkins.txt_ file we have 39 check-ins for user 0 and the numebr of records in _Yelp_train.txt_ + _Yelp_test.txt_ + _Yelp_tune.txt_ is equal to 39. Should we consdier them as a frequency score?
    - __item_groups__: groups of items (leisure and working items)
    - __plots__: plots of analysis and results
    - __results__: results of models
    - __user_groups__: groups of users
- Notebooks:
    - __XXX__:


## How to run the pipeline?

1. We use the generated results from the previous experiments (from `ESWA'21`) on Gowalla (i.e., files in `results/Gowalla`)
    - Each folder indicates a model.
    - The main files are `results_top_N.txt` which are the user scores per metric.
2. Run `temporalSplit.ipynb` to split users based on the different timestamp and generate some plots to show the correlation between attributes.
    - Outputs: plots in `\plots` and user and item groups in `\groups`
3. `compute_results.py`
4. `merge_results.ipynb`
