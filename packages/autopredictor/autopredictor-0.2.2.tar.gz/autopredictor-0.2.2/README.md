# autopredictor

<figure>
    <img src="https://github.com/UBC-MDS/autopredictor/blob/main/docs/img/image.png?raw=true" width="150" height="150">
</figure>

![CI/CD](https://github.com/UBC-MDS/autopredictor/actions/workflows/ci-cd.yml/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/autopredictor/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/autopredictor) [![Documentation Status](https://readthedocs.org/projects/autopredictor/badge/?version=latest)](https://autopredictor.readthedocs.io/en/latest/?badge=latest) [![License: GNU](https://img.shields.io/badge/License-GNU-yellow.svg)](https://opensource.org/license/gpl-3-0/) [![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/) ![release](https://img.shields.io/github/release-date/UBC-MDS/autopredictor) ![version](https://img.shields.io/github/v/release/UBC-MDS/autopredictor)

[Summary](#summary) | [Functions](#functions) | [Installation](#installation) | [Usage](#usage) | [Dependencies](#dependencies)


## About
Autopredictor simplifies machine learning model selection for regression tasks. This Python package provides an intuitive approach, minimizing coding for model exploration. Assuming preprocessed data, it swiftly evaluates models with default settings, allowing quick comparison of their effectiveness.


## Summary

This Autopredictor Python package streamlines the process of selecting and assessing machine learning models, offering a simplified approach to assess various regression models without the need of intricate manual setup. Designed for datasets with continuous response variable, this tool expedites the exploration of multiple models, minimizing the coding effort required for model selection and fitting. Leveraging preprocessed and trained data, this package evaluates models using default settings, allowing users to swiftly comprehend model performance. By computing and showcasing diverse performance metrics for each model, it offers an efficient means to compare their effectiveness. The key metrics used for evaluating model performance include Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE), R2 Square, Mean Squared Error (MSE), and Root Mean Squared Error (RMSE). The Autopredictor package encompasses eight regression models, enhancing flexibility and choices in model selection:

- Linear Regression
- Lasso Regression
- Ridge Regression
- Linear Support Vector Machine
- Support Vector Machine
- Decision Tree
- Random Forest
- Gradient Boosting
- AdaBoost

 For a detailed explanation of each model, refer to the [Audopredictor Tutorial](https://autopredictor.readthedocs.io/en/latest/example.html). Overall, Autopredictor delivers a convenient and efficient framework for preliminary model evaluation and the comparison of regression models in machine learning workflows.

## Functions

This package includes four main functions:
- `fit`: Fits a clean, preprocessed training data into eight different regression models. This function returns a dictionary containing five metric scores for each model
- `show_all`: Generates a DataFrame presenting each scoring metric alongside the respective model, while outputting a clear overview of the results in a table format
- `display_best_score`: Identifies the best score with respect to a specific scoring metric along with the corresponding model
- `select_model`: Returns a summary of all the scoring metrics associated with a specific machine learning model

A comprehensize walkthrough of each function can be found in the [Audopredictor Tutorial](https://autopredictor.readthedocs.io/en/latest/example.html).

This package focuses on eight widely used regressor models, providing a curated selection that covers a broad range of algorithmic approaches. This package are designed to be user-friendly through automation with default configurations for each model. It is catered for both beginners by eliminating complicated model arguments and for experts by providing baseline results. However, this package may not be suitable for experienced practitioner who requires customized regressor models. Within the Python ecosystem, there is an existing, well developed and maintained library named [lazypredict](https://pypi.org/project/lazypredict/) that offer similar functionality with a wider range of models, including classification models.

## Installation

In order to use this package, please run the instructions provided below.

### For Users: Using PyPI

This package is published on PyPi. Run the following command to install autopredictor in the desired environment:
```bash
pip install autopredictor
```

### For Developers: Using Poetry

All [dependencies](#dependencies) installation used in this package will be handled by Poetry through the following commands:

1. Clone this GitHub repository using this command:
```bash
git clone https://github.com/UBC-MDS/autopredictor.git
```

2. Install poetry in your base environment by following these [instructions](https://python-poetry.org/docs/#installation).

3. Run the following commands from the root directory of this project to create a virtual environment for this package and install autopredictor through poetry:
```bash
conda create --name autopredictor python=3.9 -y
conda activate autopredictor
poetry install
```

## Usage

To use `autopredictor`, follow these simple steps:

1. Import the package:

    ```python
    import autopredictor
    ```

2. Load your preprocessed training data.

3. Once you have your data split into training and testing, you can start by fitting the data to obtain scores for eight different regression models:
    ```python
    results_test, results_train = autopredictor.fit(X_train,
                      X_test,
                      y_train,
                      y_test,
                      return_train=True)
    ```

    The `fit` function returns a dictionary containing four metric scores for each model.

4. Display an overview of the results in a table format:

    ```python
    scores_test = autopredictor.show_all(results_test)
    scores_train = autopredictor.show_all(results_train)
    ```

    By calling `autopredictor.show_all(results)`, the function will print a tabulated version of the resulting DataFrame for easier visualization.

5. Identify the best score with respect to a specific metric:

    ```python
    autopredictor.display_best_score(metric='r2')
    ```

6. Get a summary of all scoring metrics associated with a specific model:

    ```python
    autopredictor.select_model(model='Linear Regression')
    ```

### Example

```python
import autopredictor

# return_train will always default to False assuming the user does not want to see the train scores
scores, _ = autopredictor.fit(X_train, 
                           X_test, 
                           y_train, 
                           y_test)

# Display an overview of the results
test_df = autopredictor.show_all(scores)

# Identify the best score with respect to the R-squared metric
autopredictor.display_best_score(metric='r2')

# Get a summary of scoring metrics for the Linear Regression model
autopredictor.select_model(model='Linear Regression')
```

## Developer notes:

### Running The Tests

Run the following command in the terminal from the project's root directory to execute the tests written for each function in this package:
```bash
pytest tests/
```

To assess the branch coverage for this package:
```bash
pytest --cov=autopredictor --cov-branch
```

## Dependencies

This package relies on the following dependencies as outlined in [pyproject.toml](https://github.com/UBC-MDS/autopredictor/blob/main/pyproject.toml):

- python = "^3.9"
- pandas = "^2.1.4"
- tabulate = "^0.9.0"
- scikit-learn = "^1.3.2"
- pytest = "^7.4.4"
- pytest-cov = "^4.1.0"
- jupyter = "^1.0.0"
- myst-nb = "^1.0.0"
- sphinx-autoapi = "^3.0.0"
- sphinx-rtd-theme = "^2.0.0"

## Documentations

Online documentation is available [here](https://autopredictor.readthedocs.io/en/latest/?badge=latest).

## Contributing

Interested in contributing? Check out the contributing [guidelines](https://github.com/UBC-MDS/autopredictor/blob/main/CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](https://github.com/UBC-MDS/autopredictor/blob/main/CONDUCT.md). By contributing to this project, you agree to abide by its terms. Please find the list of contributors [here](https://github.com/UBC-MDS/autopredictor/blob/main/CONTRIBUTORS.md).

## License

`autopredictor` was created by Anu Banga, Arturo Rey, Sharon Voon, Zeily Garcia. It is licensed under the terms of the GNU GENERAL PUBLIC LICENSE.

## Important Links

* Official source code repo: https://github.com/UBC-MDS/autopredictor.git
* Official read the doc: https://autopredictor.readthedocs.io/en/latest/?badge=latest


This package uses the following models from [scikit-learn](https://scikit-learn.org/stable/):

* Linear Regression: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
* Linear Regression (L1) (Lasso): https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html
* Linear Regression (L2) (Ridge):https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html
* Support Vector Machine: https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html
* Decision Tree: https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html
* Random Forest: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
* Gradient Boosting: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html
* AdaBoost: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html


## References

Pandala, S. R. (2022). LazyPredict. Retrived from https://pypi.org/project/lazypredict/ 

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., … Duchesnay, É. (1970). Scikit-Learn: Machine learning in Python. Retrieved from https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html 

## Credits

`autopredictor` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
