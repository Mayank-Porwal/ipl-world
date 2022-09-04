import pandas as pd
from sqlalchemy import text
from app.db_pool.connector import db_engine
from app.venue.logic import Venues


class Teams:
    def __init__(self, name):
        self.name = name
        self.cols = ['match_id', 'team1', 'team2', 'season', 'date_of_match', 'match_number', 'venueID', 'toss_winner',
                     'toss_decision', 'player_of_match', 'umpire1', 'umpire2', 'reserve_umpire', 'tv_umpire',
                     'match_referee', 'winner', 'win_by', 'winner_type', 'method_of_win', 'outcome', 'eliminator']
        self.teams_df = self.create_dataframe()
        self.venues_df = Venues().create_dataframe()

    def create_dataframe(self):
        query = f"""
            Select * from match_details
            where team1 = '{self.name}' 
            or team2 = '{self.name}'
            ;
            """
        query_result = db_engine.execute(text(query))
        result = query_result.fetchall()
        return pd.DataFrame(result, columns=self.cols)

    def matches_info_per_team(self, year=None, venue=None):
        total_matches_played = self.teams_df.shape[0]
        matches_won = self.teams_df[self.teams_df['winner'].eq(self.name)].shape[0]
        matches_lost = self.teams_df[(~self.teams_df['winner'].eq(self.name)) & (self.teams_df['winner'].notna())] \
            .shape[0]
        matches_tied = self.teams_df[self.teams_df['outcome'].eq('tie')].shape[0]
        matches_no_result = self.teams_df[self.teams_df['outcome'].eq('no result')].shape[0]

        return {
            "Matches": total_matches_played,
            "Won": matches_won,
            "Lost": matches_lost,
            "Tie": matches_tied,
            "NR": matches_no_result
        }


if __name__ == '__main__':
    obj = Teams('Rajasthan Royals')
    res = obj.matches_info_per_team()
    print(res)
