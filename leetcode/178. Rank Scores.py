import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    rank_scores = pd.DataFrame({
        'score': scores['score'].sort_values(ascending=False),
        'rank': [None for _ in range(len(scores))]
    })
    unique_scores = rank_scores.drop_duplicates()

    for i in range(len(unique_scores)):
        rank_scores.loc[rank_scores['score'] == unique_scores['score'].iloc[i], 'rank'] = i + 1

    return rank_scores
