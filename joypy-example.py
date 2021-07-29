import joypy
import pandas as pd

# Age banded vaccine coverage data
df = pd.read_csv('https://api.coronavirus.data.gov.uk/v2/data?areaName=England&areaType=nation&metric=vaccinationsAgeDemographics&format=csv')

df['date'] = pd.to_datetime(df['date'])
for x in range(0,len(df)):
    df.loc[x,'day'] = (df.loc[x,'date']-min(df['date'])).days

df_plot = df.pivot(index=['day'], columns='age', values='newPeopleVaccinatedFirstDoseByVaccinationDate').reset_index()
df_plot = df_plot.drop(['day'],axis = 1)
x_range = list(range(0,len(df_plot)))
fig, axes = joypy.joyplot(df_plot,kind='values',x_range=x_range)