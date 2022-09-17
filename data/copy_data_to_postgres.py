import pandas as pd
from sqlalchemy import create_engine
import connection_params as cp

engine = create_engine(f'postgresql://{cp.user}:{cp.password}@localhost:5432/youtube')

data = pd.read_csv('./clean_airbnb.csv')
data.to_sql('airbnb_python', engine, if_exists='replace')
print('DONE!')