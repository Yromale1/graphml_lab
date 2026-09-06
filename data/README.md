# Dataset — Elliptic++

This directory contains the **Elliptic++ Transactions Dataset**, used for the GraphML-Lab project.

The dataset is used to study whether **graph-based features can improve the detection of illicit Bitcoin transactions compared with classical tabular machine learning**.

## Dataset

**Elliptic++** is a Bitcoin transaction dataset containing:

* **203,769 transactions**
* **234,355 transaction relationships**
* **49 temporal time steps**
* **183 transaction features**
* Labeled transactions: `licit` / `illicit`
* Unlabeled transactions: `unknown`

Official repository:

https://github.com/git-disl/EllipticPlusPlus

The raw dataset is distributed separately from the GitHub repository.

## Expected files

After downloading the dataset, this directory should contain:

```text
data/
├── txs_features.csv
├── txs_classes.csv
└── txs_edgelist.csv
```

### `txs_features.csv`

Feature matrix describing the transactions.

Each row represents a transaction and contains:

* transaction ID
* time step
* transaction-level features

These features are used as the **tabular ML baseline**.

### `txs_classes.csv`

Labels associated with transactions.

Expected classes:

```text
1 → illicit
2 → licit
3 → unknown
```

The exact encoding is verified by the EDA pipeline before training.

### `txs_edgelist.csv`

Edge list describing the Bitcoin transaction graph.

An edge represents a money-flow relationship between two transactions.

This file is used to construct the graph and derive features such as:

* in-degree
* out-degree
* total degree
* PageRank
* neighborhood statistics
* community information
* node embeddings

## Data handling

The raw CSV files are **not committed to Git** because of their size.

The repository should contain only:

```text
data/
└── README.md
```

The actual dataset should remain local:

```text
data/
├── README.md
├── txs_features.csv
├── txs_classes.csv
└── txs_edgelist.csv
```

The files are ignored by `.gitignore`.

If the dataset has not been downloaded yet, follow the instructions provided by the official Elliptic++ repository.

## Data split

Experiments use a **temporal split** rather than a random train/test split.

The objective is to avoid information leakage from future transactions.

The main experimental protocol is:

```text
Time steps

1 ───────────────────── 30 | 31 ─── 35 | 36 ───────── 49
          TRAIN                  VAL             TEST
```

The exact split is defined in the experiment configuration and should not be changed without documenting the change.

## License
### Project code

The code developed as part of GraphML-Lab is released under the MIT License.

See the root-level LICENSE file for the complete license text.

### Dataset

The Elliptic++ dataset is not covered by this project's MIT License.

The dataset remains subject to the terms and conditions specified by its original authors and distributors.

Users are responsible for complying with the original dataset's terms when downloading, using, modifying, or redistributing the data.

For the original dataset and its terms, refer to the official repository:

https://github.com/git-disl/EllipticPlusPlus

If you use the Elliptic++ dataset in your work, please cite the original KDD 2023 paper:

Elmougy, Y., & Liu, L. (2023). Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics. Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '23), 12 pages.
https://doi.org/10.1145/3580305.3599803

BibTeX
@article{elmougy2023demystifying,
  title={Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics},
  author={Elmougy, Youssef and Liu, Ling},
  journal={arXiv preprint arXiv:2306.06108},
  year={2023}
}

For the longer version of the paper, see the ArXiv version.

## Important

Do not modify the original CSV files.

All preprocessing and feature engineering should be performed programmatically in:

src/graphlab/

This ensures that experiments remain reproducible.
