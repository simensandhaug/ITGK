month = input("Måned: ")
day = int(input("Dag: "))

if month in ('januar', 'februar', 'mars'):
	season = 'Vinter'
elif month in ('april', 'mai', 'juni'):
	season = 'Vår'
elif month in ('juli', 'august', 'september'):
	season = 'Sommer'
else:
	season = 'Høst'

if (month == 'mars') and (day > 19):
	season = 'Vår'
elif (month == 'juni') and (day > 20):
	season = 'Sommer'
elif (month == 'september') and (day > 21):
	season = 'Høst'
elif (month == 'desember') and (day > 20):
	season = 'Vinter'

print(season)