import pandas as pd
import numpy as np
import inspect

def check_parameter_count(func, expected_params):
    parameters = inspect.signature(func).parameters
    if len(parameters) != expected_params:
        raise ValueError(f"Function {func.__name__} should have {expected_params} parameters, but it has {len(parameters)}.")

def convert_to_numeric(column):
    try:
        return pd.to_numeric(column)
    except ValueError:
        raise ValueError(f"Error: Unable to convert column '{column.name}' to numeric.")


def TOPSIS(input_file , input_weights , input_impacts , output_file) :

    #Checking correct number of inputs 
    check_parameter_count(TOPSIS, 4)

    #Checking if files are not present
    try:
        input_df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    
    try:
        output_df = pd.read_csv(output_file)
    except FileNotFoundError:
        print(f"Error: The file '{output_file}' was not found.")

    final_df = input_df.copy() #To be used in the end
    print(final_df)
    
    #Checking if columns are less than 3
    no_of_col = input_df.shape[1]
    if no_of_col < 3 :
        raise ValueError("Input file should contain atleast 3 columns.")
    
    #Converting columns to numeric starting from 2nd column
    try:
        input_df.iloc[:, 1:] = input_df.iloc[:, 1:].apply(convert_to_numeric)
    except ValueError as ve:
        print(ve)
    
    #Extracting weights and checking length of weights
    weights = []

    for i in input_weights:
        if(i==','):
            continue
        else:
            weights.append(i)
    
    if(len(weights) != no_of_col-1):
        raise ValueError("Number of weights is not same as number of criteria.")
    
    #Converting weights to integer
    try:
        weights = list(map(int, weights)) 
    except ValueError as e:
        raise ValueError(f"Error: Unable to convert weights to integers. Details: {e}")

    #Extracting impacts and checking length and type of impacts
    impacts = []

    for i in input_impacts:
        if(i==','):
            continue
        else:
            if(i=="+" or i=="-"):
                impacts.append(i)
            else:
                raise ValueError("Impacts can be of type -> + or - ")
        
    if(len(impacts) != no_of_col-1):
        raise ValueError("Number of impacts is not same as number of criteria.")
    
    #Algorithm to for TOPSIS :
    squared_input_df = input_df
    for i in input_df.iloc[:,1:]:
        squared_input_df[i] = squared_input_df[i]**2
    criteria_wise_sum = squared_input_df.iloc[:,1:].sum()

    normalized_input_df = squared_input_df
    normalized_input_df.iloc[:, 1:] = normalized_input_df.iloc[:, 1:] / criteria_wise_sum.values

    weighted_input_df = normalized_input_df
    weighted_input_df.iloc[:,1:] = weighted_input_df.iloc[:,1:] * weights

    ideal = []
    negative_ideal = []
    for i in range(no_of_col-1):
        if impacts[i] == "+":
            ideal.append(pd.to_numeric(weighted_input_df.iloc[:, i+1:i+2].max().max(), errors='coerce'))
            negative_ideal.append(pd.to_numeric(weighted_input_df.iloc[:, i+1:i+2].min().min(), errors='coerce'))
        else:
            ideal.append(pd.to_numeric(weighted_input_df.iloc[:, i+1:i+2].min().min(), errors='coerce'))
            negative_ideal.append(pd.to_numeric(weighted_input_df.iloc[:, i+1:i+2].max().max(), errors='coerce'))
    
    ideal = np.array(ideal)
    negative_ideal = np.array(negative_ideal)

    # Calculate Euclidean distance for each row
    from_ideal = np.linalg.norm(weighted_input_df.iloc[:, 1:] - ideal, axis=1)
    from_negative_ideal = np.linalg.norm(weighted_input_df.iloc[:, 1:] - negative_ideal, axis=1)

    relative_scores = from_negative_ideal / (from_ideal + from_negative_ideal)
    final_df['Topsis Score'] = relative_scores
    final_df["Rank"] = final_df['Topsis Score'].rank(ascending = False)
    final_df.to_csv(output_file,index=False)

    print(final_df)
    
if __name__ == '__main__':
    TOPSIS()