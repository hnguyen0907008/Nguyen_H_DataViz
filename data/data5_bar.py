import matplotlib.pyplot as plt
import numpy as np


hfont = {'fontname': 'Tahoma'}

countries = ['Canada', 'USA', 'Switzerland', 'Finland', 'UK']
value=[9, 1, 8, 4, 6]

y_pos = np.arange(len(countries))

plt.barh(y_pos, value, align='center', alpha=0.5, color="green")
plt.yticks(y_pos, countries)

#plt.bar(y_pos, value, color='green')

plt.ylabel("Number of Gold Medals")
plt.xlabel("Countries")
plt.title("Number of Gold Medals Canada Won Compared to Other Countries in 1924", **hfont)

plt.show()