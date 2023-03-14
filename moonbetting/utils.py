import kaggle
import pandas as pd


def download_dataset(dataset_name: str, path: str):
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset_name, path=path, unzip=True)


def merge_games_clubs(games, clubs):
    home_clubs = games.merge(
        clubs[["club_id", "name"]], left_on="home_club_id", right_on="club_id"
    )
    away_clubs = games.merge(
        clubs[["club_id", "name"]], left_on="away_club_id", right_on="club_id"
    )

    home_clubs = home_clubs.rename(columns={"name": "home_club_name"})
    away_clubs = away_clubs.rename(columns={"name": "away_club_name"})

    return home_clubs.merge(away_clubs[["game_id", "away_club_name"]], on="game_id")


def read_data(dir, name):
    df = pd.read_csv(f"{dir}/{name}.csv")
    print(f"{name}: {df.shape}")
    return df


def is_home_win(row):
    if row["home_club_goals"] > row["away_club_goals"]:
        return "1"
    elif row["home_club_goals"] < row["away_club_goals"]:
        return "2"
    else:
        return "x"
