import pandas as pd
from tabulate import tabulate

def show_all(result):
    """
    This function converts the trained regression model scores stored in a dictionary by 
    the "fit" function into a DataFrame, sorted alphabetically by model. It also 
    outputs the DataFrame in a table format.

    Parameters
    ----------
    result : dict
        A dictionary containing scoring metrics data for each regression model. The keys 
        represent model names where the values represent the scoring results and should 
        be numeric.

    Returns
    -------
    DataFrame
        A DataFrame containing all scoring metrics results alongside the corresponding 
        model, sorted alphabetically.


    Raises
    ------
    TypeError
        If result is not a dictionary.
    ValueError
        If result dictionary is empty.
        If there is invalid scoring metrics in the result dictionary's value.
        If the number of scoring metrics are not correct.

    Examples
    --------
    >>> from autopredictor.show_all import show_all
    >>> model_scores = {
        'Linear Regression': {'Mean Absolute Error': 0.453,
                            'Mean Absolute Percentage Error': 0.346,
                            'R2 Score': 0.512,
                            'Mean Squared Error': 0.567,
                            'Root Mean Squared Error': 0.987},
        'Linear Regression (L1)': {'Mean Absolute Error': 61.2,
                                    'Mean Absolute Percentage Error': 0.457,
                                    'R2 Score': 0.239,
                                    'Mean Squared Error': 0.873,
                                    'Root Mean Squared Error': 72.4}
                                }
    >>> test_scores = show_all(model_scores)        
    """

    # Check if result is of type dictionary
    if not isinstance(result, dict):
        raise TypeError("Input should be of dictionary type.")
    
    # Check if result is an empty dictionary
    if result == {}:
        raise ValueError("Input should not be an empty dictionary. No training scores are avaialble. Call fit function to test the model.")
    
    # Check if inner dictionaries have correct scoring metrics
    valid_metrics = {"MEAN ABSOLUTE ERROR", "MEAN ABSOLUTE PERCENTAGE ERROR", "R2 SCORE", "MEAN SQUARED ERROR", "ROOT MEAN SQUARED ERROR"}
    for model_name, model_score in result.items():
        if not all(metric.upper() in valid_metrics for metric in model_score):
            raise ValueError(f"Invalid scoring metrics for model.")
        if len(model_score) != 5:
            raise ValueError(f"Scoring metrics is incomplete.")
    
    # Convert scoring metrics into acronym
    key_mapping = {
        'MEAN ABSOLUTE ERROR': 'MAE',
        'MEAN ABSOLUTE PERCENTAGE ERROR': 'MAPE',
        'R2 SCORE': 'R2',
        'MEAN SQUARED ERROR': 'MSE',
        'ROOT MEAN SQUARED ERROR': 'RMSE'
    }

    for model_name, model_metric in result.items():
        updated_scores = {key_mapping[key.upper()]:value for key, value in model_metric.items()}
        result[model_name] = updated_scores
    
        
    # Convert the dictionary to a DataFrame
    result_df = pd.DataFrame.from_dict(result, orient='index')
    result_df = result_df.sort_index()

    # Convert DataFrame to tabulate and print it in table format
    result_table = tabulate(result_df, headers='keys', tablefmt='github')
    print(result_table)

    return result_df