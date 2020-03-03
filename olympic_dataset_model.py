import pandas as pd

#load Csv file
oo = pd.read_csv("Data/Summer Olympic medallists 1896 to 2008 - ALL MEDALISTS.csv")

#In which of these events did Jesse Owens win a medal
jo = oo[oo["Athlete"] == 'OWENS, Jesse']
jo.Event.value_counts()

# Which country has won the most men's gold medals in singles badminton over the years?
# Sort the results alphabetically by the player's names.

gms = oo[(oo['Gender'] == 'Men') & (oo['Medal'] == 'Gold') & (oo['Sport'] == 'Badminton')]
gms.sort_values(by='Athlete')

# Which three countries have won the most medals in recent years (from 1984)
recent = oo[oo['Edition'] >= 1984]
recent.NOC.value_counts().head(3)

# Display the male gold medal winners for the 100 meters track and field
# sprint event over the years. List the results starting with the most recent.
# Show the Olympic city, edition, athlete, and the country they represent

mgh = oo[(oo.Gender == 'Men') & (oo.Medal == 'Gold') & (oo.Event == '100m')]
mgh.sort_values(by='Edition', ascending = False)[['City', 'Edition', 'Athlete', 'NOC']]