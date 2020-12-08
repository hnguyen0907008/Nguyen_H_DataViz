import matplotlib.pyplot as plt
import numpy as np

 

hfont = {'fontname': 'Tahoma'}

countries = ['Canada', 'USA', 'Switzerland', 'Finland', 'UK']
value=[63, 10, 6, 2, 1]

y_pos = np.arange(len(countries))

plt.barh(y_pos, value, align='center', alpha=0.5, color="blue")
plt.yticks(y_pos, countries)

#plt.bar(y_pos, value, color='green')

plt.ylabel("Number of Gold Medals")
plt.xlabel("Countries")
plt.title("Number of Gold Medals Canada Won Compared to Other Countries in 2014", **hfont)

plt.show()