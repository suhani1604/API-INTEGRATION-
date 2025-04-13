import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = f'da2923754d1b9c5610530a8aa95efdd'
CITY ="PUNE"
URL = URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={'fda2923754d1b9c5610530a8aa95efdd'}&units=metric"
response = requests.get(URL)
data = response.json()

#exetraction
dates = [items['dt_txt'] for items in 
         data ['list']]
temps = [item['main']['temp']for item in data['list']]

plt.figure(figsize=(11,6))
sns.lineplot(x=dates,y=temps)
plt.title(f'Temperature Forecast for {CITY}')
plt.xlabel('Date and Time')
plt.ylabel('temperature(°c)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
