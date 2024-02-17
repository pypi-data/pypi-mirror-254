import pandas as pd

def run(Application, combined_values, i_var_paths, d_var_paths):
    """Use to run a sensitivity analysis

    :return: DataFrame containing all tested combinations and respective results.
    """
    # Create a DataFrame for the Results of the Dependent Variables
    res_col_name = []
    for i in d_var_paths.keys():
        res_col_name.append(i)
    results = pd.DataFrame(columns=res_col_name)

    e = 0  # resetting the iterator
    for row in combined_values.index:
        # Go through and set independent vars
        for (i_call, cv_col) in zip(i_var_paths.values(), combined_values.columns):
            i_call.Value = combined_values.loc[row, cv_col]
        # Run the Sim
        Application.Engine.Run2()
        # Collect results for dependent vars
        for (d_call, res_col) in zip(d_var_paths.values(), results.columns):
            results.loc[row, res_col] = d_call.Value
        e += 1
        print(f"Iteration {e} out of {len(combined_values)} complete")
    results = results.apply(pd.to_numeric)  # convert all columns of results
    final = pd.merge(combined_values, results, left_index=True, right_index=True)
    return final
