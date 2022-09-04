import pandas as pd
from sqlalchemy import text
from app.db_pool.connector import db_engine


class Venues:
    def __init__(self):
        self.cols = ['index', 'venue', 'city']
        self.venues_df = self.create_dataframe()

    def create_dataframe(self):
        query = f"""
            Select * from venues
            ;
            """
        query_result = db_engine.execute(text(query))
        result = query_result.fetchall()
        return pd.DataFrame(result, columns=self.cols)
