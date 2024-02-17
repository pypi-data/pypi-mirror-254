# GNNUERS: Explaining Unfairness in GNNs for Recommendation

GNNUERS generates explanations in the form of user-item interactions that make
a GNN-based recommender system favor a demographic group over another. \
GNNUERS learns a perturbation vector that modifies the adjacency matrix representing
the training network. The edges modified by the perturbation vector are the explanations
genereated by the framework. \
GNNUERS then needs to work on a slight extended version of a recommender system
in order to include the perturbation vector. In our study we applied our framework on
GCMC, LightGCN and NGCF, all provided in the [Recbole](https://github.com/RUCAIBox/RecBole)
library, from which GNNUERS depend on for the data handling, the training and evaluation.
Instead, the provided models are independent of the Recbole library.

# Cite

This repository contains the source code of the paper [Robustness in Fairness against Edge-level Perturbations in GNN-based Recommendation]().

If you find this repostiory useful for your research or development cite our paper as

```bibtex
@article{DBLP:journals/corr/abs-2304-06182,
  author       = {Giacomo Medda and
                  Francesco Fabbri and
                  Mirko Marras and
                  Ludovico Boratto and
                  Gianni Fenu},
  title        = {{GNNUERS:} Fairness Explanation in GNNs for Recommendation via Counterfactual
                  Reasoning},
  journal      = {CoRR},
  volume       = {abs/2304.06182},
  year         = {2023},
  url          = {https://doi.org/10.48550/arXiv.2304.06182},
  doi          = {10.48550/ARXIV.2304.06182},
  eprinttype    = {arXiv},
  eprint       = {2304.06182},
  timestamp    = {Wed, 19 Apr 2023 12:42:23 +0200},
  biburl       = {https://dblp.org/rec/journals/corr/abs-2304-06182.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```

# Requirements
Our framework was tested on Python 3.9.
GNNUERS can be installed using the commands in [install-env.sh](install-env.sh) by passing as argument
the backend for pytorch, e.g., `cpu`, `cu***`, where `***` represents the
CUDA version, such as 116, 117. For instance, for CUDA 12.1:
```bash
./install-env.sh cu121
```
The file is configured to install pytorch (and the corresponding torch_geometric, torch_sparse, torch_scatter)
based on the version 2.1.2. For other version the file [install-env.sh](install-env.sh) must be modified accordingly.
GNNUERS can also be directly installed through the file [requirements.txt](gnnuers/requirements.txt) as follows:
```bash
pip install -r gnnuers/requirements.txt
```
requirements.txt contains the same command line arguments for pip that are included in the install-env.sh file.
Some dependencies related to PyTorch, e.g., torch-scatter, could be hard to retrieve
directly from pip depending on the PyTorch and CUDA version you are using, so you should
specify the PyTorch FTP link storing the right libraries versions.
For instance, to install the right version of torch-scatter for PyTorch 1.12.0
you should use the following command:
```bash
pip install torch-scatter -f https://data.pyg.org/whl/torch-1.12.0+${CUDA}.html
```
where `${CUDA}` should be replaced by either `cpu`, `cu***`, where `***` represents the
CUDA version, e.g., 116, 117.

__NOTE!__ \
The Recbole Dataset class does not support the usage of custom dataset splits like ours,
and we cannot guarantee that, even if provided in new versions, it will match our
modification. Hence, we implemented a modified [Dataset](gnnuers/data/dataset.py) on top of the Recbole one,
which support the usage of custom data splits, and it is used to perform our experiments

The current versions of Recbole also contain a bug related to the NGCF model. A Dropout layer is instantiated inside
the `forward` method, which makes the generation of new embeddings (after the perturbation) not reproducible
even if `eval` is called on the model. To run our experiments, we fixed this issue by creating an extended
[NGCF](gnnuers/models/ngcf.py) version on top of the respective Recbole model.

# Datasets

The datasets used in our experiments are MovieLens 1M, Last.FM 1K, Ta Feng, Insurance and
can be downloaded from [Zenodo](https://doi.org/10.5281/zenodo.7602406).
They should be placed in a folder named _dataset_ in the project root folder,
so next to the _config_ and _gnnuers_ folders, e.g.:
```
|-- config/*
|-- dataset |-- ml-1m
            |-- lastfm-1k
|-- gnnuers/*
```

# Usage

The file [main.py](gnnuers/main.py) is the entry point for every step to execute our pipeline.

## 1. Configuration

GNNUERS scripts are based on similar Recbole config files that can be found in the
-[config](config) folder. The structure is hierarchical, hence the file _base_explainer.yaml_
-can be used to set the parameters shared for all the experiments and for each dataset specify
-the necessary parameters.
-For each dataset there is a config file for:
- __training__: it is named after the dataset, e.g. _ml-1m.yaml_ for MovieLens-1M,
_tafeng.yaml_ for Ta Feng
- __explaining__: the suffix __explainer_ is added to training config filename, e.g.
_ml-1m_explainer.yaml_ for MovieLens 1M, _tafeng_explainer.yaml_ for Ta Feng

The __training__ config type parameters description can be found in the Recbole repository
and website, except for this part:
```yaml
eval_args:
    split: {'LRS': None}
    order: RO  # not relevant
    group_by: '-'
    mode: 'full'
```
where `LRS` (Load Ready Splits) is not a Recbole split type, but it is added in
our _modified_recbole_dataset.py_ to support custom data splits.

The description of each parameter in the __explaining__ config type can be found in the
relative files. In particular, for the explainer_policies:
- __force_removed_edges__: it should be always True to reproduce our results, it represents
the policy that prevents the restore of a previously deleted edge, such that the edges
deletions follow a monotonic trend
- edge_additions: True => edges are added, not removed
- exp_rec_data: "test" => the ground truth lables of the test set are used to measure the approximated NDCG
- __only_adv_group__: "local" => the global issue is measured w.r.t to each batch
- __perturb_adv_group__: the group to be perturbed. False to perturb the disadvantaged group, used when adding nodes.
  True to perturb the advantaged group, used when removing nodes.
- __group_deletion_constraint__: it is the Connected Nodes (CN) policy
- __random_perturbation__: if True executes the baseline algorithm RND-P

## 2. Train Recommender System

The recommender systems need first to be trained:
```bash
python -m gnnuers.main --run train --model MODEL --dataset DATASET --config_file_list config/TRAINING_CONFIG.yaml
```
where __MODEL__ should be one of [GCMC, LightGCN, NGCF], __DATASET__ should match the folder
of dataset, e.g. insurance, ml-1m, __TRAINING_CONFIG__ should be a config file of the
__training__ type.

## 3. Train GNNUERS explainer
```bash
python -m gnnuers.main --run explain --model MODEL --dataset DATASET --config_file_list config/TRAINING_CONFIG.yaml --explainer_config_file config/EXPLAINING_CONFIG.yaml --model_file saved/MODEL_FILE
```
where __MODEL__, __DATASET__, __TRAINING_CONFIG__ were already explained above.
__EXPLAINING_CONFIG__ should be the config file relative to the same dataset.

# GNNUERS Output

GNNUERS creates a folder
_gnnuers/experiments/dp_explanations/DATASET/MODEL/dpbg/LOSS_TYPE/SENSITIVE_ATTRIBUTE/epochs_EPOCHS/CONF_ID_
where __SENSITIVE_ATTRIBUTE__ can be one of [gender, age], __EPOCHS__ is the number of
epochs used to train GNNUERS, __CONF_ID__ is the configuration/run ID of the just run
experiment. The folder contains the __EXPLAINING_CONFIG__ file in yaml and pkl format used
for the experiment, a file _cf_data.pkl_ containing the information about the perturbed edges for each epoch,
a file _model_rec_test_preds.pkl_ containing the original recommendations on the rec (perturbation) set and
test set, a file _users_order_.pkl containing the users ids in the order _model_rec_test_preds.pkl_ are sorted,
a file _checkpoint.pth_ containing data used to resume the training if stopped earlier.

_cf_data.pkl_ file contains a list of lists where each inner list has 5 values, relative to the perturbed edges at a certain epoch:
1) GNNUERS total loss
2) GNNUERS distance loss
3) GNNUERS fair loss
4) fairness measured with the __fair_metric__ (absolute difference of NDCG)
5) the perturbed edges in a 2xN array, where the first row contains the user ids,
the second the item ids, such that each one of the N columns is a perturbed edge
6) epoch relative to the generated explanations

# Plotting

The scripts inside the folder [scripts](scripts) can be used to plot the
results used in the paper. They should be run from the root folder of this project.
[eval_info.py](scripts/eval_info.py) can be used as follows:
```bash
python scripts/eval_info.py --e biga/experiments/dp_explanations/DATASET/MODEL/dpbg/LOSS_TYPE/SENSITIVE_ATTRIBUTE/epochs_EPOCHS/CONF_ID
```
where the argument --e stands for the path of a specific experiment.
