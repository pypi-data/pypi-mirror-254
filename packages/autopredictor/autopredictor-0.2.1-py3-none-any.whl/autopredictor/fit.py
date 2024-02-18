from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.svm import LinearSVR, SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.metrics import mean_absolute_error, r2_score, mean_absolute_percentage_error, mean_squared_error
import numpy as np
import pandas as pd


def fit(X_train,X_test,y_train,y_test,return_train=False):
    """
    Train and evaluate multiple regression models on the given training and test data.

    Parameters
    ----------
    X_train : DataFrame
        Training data features.
    X_test : DataFrame
        Test data features.
    y_train : Series
        Training data target values.
    y_test : Series
        Test data target values.
    return_train : bool, optional, default=False
        If True, returns scores for training data as well.

    Raises
    ------
    ValueError
        If any of the inputs are empty or None.

    Returns
    -------
    tuple of dict
        A tuple containing dictionaries with performance scores for each model and metric.
        The first dictionary contains scores for test data, and the second for training data.

    Examples
    --------
    >>> X_train = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    >>> y_train = pd.Series([10, 20, 30])
    >>> X_test = pd.DataFrame({'feature1': [7, 8, 9], 'feature2': [10, 11, 12]})
    >>> y_test = pd.Series([40, 50, 60])

    >>> scores_train, scores_test = fit(X_train, X_test, y_train, y_test, return_train=True)
    >>> print(scores_train['Linear Regression']['Mean Absolute Error'])
    0.0
    >>> print(scores_test['Linear Regression']['R2 Score'])
    -3.0
    """


    if X_train is not None and X_test is not None and y_train is not None and y_test is not None:
        scores_list_train = {}
        scores_list_test = {}

        models = {
            'Linear Regression': LinearRegression(),
            'Linear Regression (L1)': Lasso(),
            'Linear Regression (L2)': Ridge(),
            'Linear Support Vector Machine': LinearSVR(),
            'Support Vector Machine': SVR(),
            'Decision Tree': DecisionTreeRegressor(),
            'Random Forest': RandomForestRegressor(),
            'Gradient Boosting': GradientBoostingRegressor(),
            'AdaBoost': AdaBoostRegressor()
        }

        

        for name, model in models.items():
            model.fit(X_train,y_train)
            print(f'{name} trained.')

            scores_list_train[name] = {}

            # Train scores

            if return_train:
                metrics_train = {
                    'Mean Absolute Error': mean_absolute_error(y_train, model.predict(X_train)),
                    'Mean Absolute Percentage Error': mean_absolute_percentage_error(y_train, model.predict(X_train)),
                    'R2 Score': r2_score(y_train, model.predict(X_train)),
                    'Mean Squared Error': mean_squared_error(y_train, model.predict(X_train)),
                    'Root Mean Squared Error': np.sqrt(mean_squared_error(y_train, model.predict(X_train)))
                }


                for metric_name, metric in metrics_train.items():

                    scores_list_train[name][metric_name] = metric

            else:
                pass

            scores_list_test[name] = {}

            metrics_test = {
                'Mean Absolute Error': mean_absolute_error(y_test, model.predict(X_test)),
                'Mean Absolute Percentage Error': mean_absolute_percentage_error(y_test, model.predict(X_test)),
                'R2 Score': r2_score(y_test, model.predict(X_test)),
                'Mean Squared Error': mean_squared_error(y_test, model.predict(X_test)),
                'Root Mean Squared Error': np.sqrt(mean_squared_error(y_test, model.predict(X_test)))
            }


            for metric_name, metric in metrics_test.items():

                scores_list_test[name][metric_name] = metric

    else:
        raise Exception('Please input a valid DataFrame')

    if return_train:
        return (scores_list_test, scores_list_train)
    else:
        return (scores_list_test,{})
