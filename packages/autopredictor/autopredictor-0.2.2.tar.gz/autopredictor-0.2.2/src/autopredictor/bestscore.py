import pandas as pd
from tabulate import tabulate

def display_best_score(X, scoring_metric):
    """
    This function identifies the best score with respect to a specific scoring metric along with the corresponding model.
    It returns a DataFrame and displays the result in a table format.

    Parameters
    ----------
    X : DataFrame
        A DataFrame containing all scoring metrics results alongside the corresponding model, sorted alphabetically.
    scoring_metric : str
        A string containing the regression scoring metric, which is used to display best model.    

    Returns
    -------
    DataFrame
        If the scoring metric is found, a dataframe containing the best score and the corresponding model is returned.
        If the scoring metric is not found, a ValueError is raised.

    Examples
    --------
    >>> from autopredictor.bestscore import display_best_score
    >>> df = pd.DataFrame({'MAE': [5.6, 3.4],
                                  'MSE': [9.4, 21.4],
                                  'MAPE': [0.34, 0.45],
                                  'R2': [0.239, 0.712]},
                                 index=['Linear Regression', 'Random Forest'])
    >>> display_best_score(df, 'MAE')
                       MAE  
    Random Forest  3.4
    
    >>> display_best_score(df, 'F1')
    ValueError: Invalid Scoring metric 'F1'.The specified metric is not in the list of available metrics. Available metrics: MAE, MSE, MAPE, R2.
   """
    if X is None or not isinstance(X, pd.DataFrame):
        raise TypeError("Invalid DataFrame provided.")
    
    if X.empty:
        raise TypeError("DataFrame is empty.")
    
    if not isinstance(scoring_metric, str):
        raise ValueError("scoring_metric must be a string.")

    if scoring_metric not in X.columns:
        available_metrics = X.columns.tolist()
        available_metrics_string = ", ".join(available_metrics)
        raise ValueError (f"Invalid Scoring metric '{scoring_metric}'. The specified metric is not in the list of available metrics. Available metrics: {available_metrics_string}.")
    
    if X[scoring_metric].isnull().any():
        raise ValueError(f"Invalid Scoring metric '{scoring_metric}'. The specified metric contains null values. Please handle or remove null values before using this function.")

    if scoring_metric == 'R2':
        best_model = X[scoring_metric].idxmax()
        best_score = X.loc[best_model, scoring_metric]
    else:
        best_model = X[scoring_metric].idxmin()
        best_score = X.loc[best_model, scoring_metric]

    result_table = pd.DataFrame({scoring_metric: [best_score]}, index=[best_model])
    print(tabulate(result_table, headers='keys', tablefmt='github', showindex=True))

    return result_table