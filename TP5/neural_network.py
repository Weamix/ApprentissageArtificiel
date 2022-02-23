from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def analyze(data, type):
    print(data.shape)
    print(data.info())
    print(data.describe())
    print(data.head())
    print(data[type].value_counts())


def analyze_good_employees(data):
    averages = data.mean()
    average_last_evaluation = averages['last_evaluation']
    average_project = averages['number_project']
    average_montly_hours = averages['average_monthly_hours']
    average_time_spend = averages['time_spend_company']
    average_salary = averages['salary']

    good_employees = data[data['last_evaluation'] > average_last_evaluation]
    good_employees = good_employees[good_employees['number_project'] > average_project]
    good_employees = good_employees[good_employees['average_monthly_hours'] > average_montly_hours]
    good_employees = good_employees[good_employees['time_spend_company'] > average_time_spend]
    good_employees = good_employees[good_employees['salary'] > average_salary]

    sns.set()
    plt.figure(figsize=(15, 8))
    plt.hist(data['left'])
    print(good_employees.shape)
    sns.heatmap(good_employees.corr(), vmax=0.5, cmap="PiYG")
    plt.title('Correlation matrix')
    plt.show()


def label_encode(data, col):
    # Transforme un type catégorie en entier
    le = LabelEncoder()
    # On récupère tous les noms de catégories possibles
    unique_values = list(data[col].unique())
    le_fitted = le.fit(unique_values)
    # On liste l'ensemble des valeurs
    values = list(data[col].values)
    # On transforme les catégories en entier
    values_transformed = le.transform(values)
    # On fait le remplacement de la colonne dans le dataframe d'origine
    data[col] = values_transformed
    #print(data)


def read_file(file):
    with open(file, 'r') as file:
        lines = file.readlines()
        #print(lines)
    return lines


if __name__ == '__main__':
    data = pd.read_csv('human_resources.csv')
    analyze(data, 'left')
    label_encode(data, 'category')
    label_encode(data, 'salary')
    analyze_good_employees(data)
