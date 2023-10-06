import pandas as pd

final_stars_df = pd.read_csv('C:/Users/User/Documents/PROJETOS E AULAS PROGRAMACAO/projeto 127/final_scraped_data.py')

archive_stars_df = pd.read_csv('C:/Users/User/Documents/PROJETOS E AULAS PROGRAMACAO/projeto 127/PSCompPars_2023.10.06_12.38.44.csv')



merge_stars_df = pd.merge(final_stars_df, archive_stars_df, on = "id")

merge_stars_df.shape

merge_stars_df.to_csv('merge_stars.csv')