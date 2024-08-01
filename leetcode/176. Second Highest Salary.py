import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salary_set = set(employee['salary'].to_list())
    salary_set.discard(max(salary_set))
    if len(salary_set) == 0:
        return pd.DataFrame([None], columns=['SecondHighestSalary'])
    return pd.DataFrame([max(salary_set)], columns=['SecondHighestSalary'])
