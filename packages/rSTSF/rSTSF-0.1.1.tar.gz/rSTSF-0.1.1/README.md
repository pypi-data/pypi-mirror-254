# Randomized-Supervised Time Series Forest (r-STSF)

The r-STSF is a Python package for fast, accurate, and explainable time series classification. It implements the methodology described in:

Cabello, N., Naghizade, E., Qi, J., et al. Fast, accurate and explainable time series classification through randomization. Data Min Knowl Disc (2023). [https://doi.org/10.1007/s10618-023-00978-w](https://doi.org/10.1007/s10618-023-00978-w)

An arXiv version of the paper is available here: [Fast, Accurate and Interpretable Time Series Classification Through Randomization](https://arxiv.org/abs/2105.14876) by Nestor Cabello, Elham Naghizade, Jianzhong Qi, and Lars Kulik.

## Installation

To install r-STSF, use pip:

```bash
pip install rSTSF
```

Ensure you have Python 3.6 or newer installed.


## Quick Start

To use r-STSF in your Python projects, import the rstsf classifier and initialize it as follows:

```bash
from rSTSF import rstsf

classifier = rstsf()
```

## Example Usage

Below is a simple example demonstrating how to train and predict with the r-STSF classifier:

```bash
# Assuming X_train, y_train, X_test are prepared data arrays
classifier.fit(X_train, y_train)
predictions = classifier.predict(X_test)
```

For more detailed examples, including how to prepare your data, refer to the Jupyter notebooks provided in the GitHub repository:


- [r-STSF Usage Example](https://github.com/stevcabello/r-STSF/blob/main/code/r-STSF.ipynb)
- [r-STSF Explainability Demo](https://github.com/stevcabello/r-STSF/blob/main/code/r-STSF_explainability_demo.ipynb)


## Features

- **Fast and Accurate**: Achieves state-of-the-art classification accuracy efficiently, suitable for large datasets or long time series.
- **Explainability**: Offers insights into classification decisions, aiding understanding and trust in predictions.
- **Flexible**: Utilizes multiple time series representations and aggregation functions to capture diverse patterns.


## License

r-STSF is licensed under the MIT License - see the LICENSE file for details.


## Citation
If you use r-STSF in your research, please cite the following paper:

```bibtext
@article{rSTSF2023,
  title={Fast, accurate and explainable time series classification through randomization},
  author={Cabello, Nestor and Naghizade, Elham and Qi, Jianzhong and Kulik, Lars},
  journal={Data Mining and Knowledge Discovery},
  year={2023},
  publisher={Springer}
}

