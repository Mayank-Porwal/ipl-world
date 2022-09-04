import pandas as pd
from sqlalchemy import text
from app.db_pool.connector import db_engine


class General:
    def __init__(self):
        self.cols = ['match_id', 'team1', 'team2', 'season', 'date_of_match', 'match_number', 'venueID', 'toss_winner',
                     'toss_decision', 'player_of_match', 'umpire1', 'umpire2', 'reserve_umpire', 'tv_umpire',
                     'match_referee', 'winner', 'win_by', 'winner_type', 'method_of_win', 'outcome', 'eliminator']
        self.teams_df = self.create_dataframe()

    @staticmethod
    def season_with_most_matches():
        query = f"""
            select season, count(*)
            from match_details
            group by 1
            order by 2 desc
            limit 1;
            """
        query_result = db_engine.execute(text(query))
        result = query_result.fetchall()
        return result[0]

    @staticmethod
    def season_with_least_matches():
        query = f"""
            select season, count(*)
            from match_details
            group by 1
            order by 2
            limit 1;
            """
        query_result = db_engine.execute(text(query))
        result = query_result.fetchall()
        return result[0]


if __name__ == '__main__':
    obj = General('Rajasthan Royals')
    res = obj.matches_info_per_team()
    print(res)
