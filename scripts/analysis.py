import os
import pandas as pd
import matplotlib.pyplot as plt

def create_results_directory():
    if not os.path.exists("results"):
        os.makedirs("results")

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path, sep=";")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def compute_summary_statistics(df1, df2, fields):
    summary_stats1 = df1[fields].describe()
    summary_stats1.to_csv('results/summary_statistics-red.csv')
    summary_stats2 = df2[fields].describe()
    summary_stats2.to_csv('results/summary_statistics-white.csv')

def perform_classification_task(df1, df2):
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score
    import numpy as np

    target_variable = 'quality'
    X = df1.drop(target_variable, axis=1)
    y = df1[target_variable]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("Prediction on Red:")
    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')
    plt.scatter(y_test, y_pred)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.title('Regression Model on Quality Prediction vs True Values')
    plt.savefig('results/regression_prediction_plot-red.png')



    X = df2.drop(target_variable, axis=1)
    y = df2[target_variable]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("Prediction on White:")
    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')
    plt.scatter(y_test, y_pred)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.title('Regression Model on Quality Prediction vs True Values')
    plt.savefig('results/regression_prediction_plot-white.png')

def create_simple_visualization(df1, df2, field):
    plt.figure(figsize=(8, 6))
    plt.hist(df1[field], bins=20, color='blue', edgecolor='black')
    plt.title(f'Histogram of {field}')
    plt.xlabel(field)
    plt.ylabel('Frequency')
    plt.savefig(f'results/{field}_histogram-red.png')

    plt.figure(figsize=(8, 6))
    plt.hist(df2[field], bins=20, color='blue', edgecolor='black')
    plt.title(f'Histogram of {field}')
    plt.xlabel(field)
    plt.ylabel('Frequency')
    plt.savefig(f'results/{field}_histogram-white.png')

def main():
    create_results_directory()

    # Change the file path to your dataset
    file_path1 = 'data/winequality-red.csv'
    df1 = load_dataset(file_path1)

    file_path2 = 'data/winequality-white.csv'
    df2 = load_dataset(file_path2)

    fields_of_interest = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
                               'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality']
    
    compute_summary_statistics(df1, df2, fields_of_interest)
    
    perform_classification_task(df1, df2)

    field_to_visualize = 'alcohol'
    create_simple_visualization(df1, df2, field_to_visualize)

if __name__ == "__main__":
    main()
