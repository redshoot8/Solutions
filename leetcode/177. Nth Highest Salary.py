import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salary = employee['salary'].drop_duplicates()
    sorted_salary = unique_salary.sort_values(ascending=False)

    if len(unique_salary) < N or N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})': None}, index=[0])
    elif len(unique_salary) > 0 and N == 1:
        return pd.DataFrame({'getNthHighestSalary(1)': sorted_salary.iloc[0]}, index=[0])
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})': sorted_salary.iloc[N - 1]}, index=[0])
