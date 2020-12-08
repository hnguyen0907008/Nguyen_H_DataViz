import matplotlib.pyplot as plt

#Which Sport won the most medals 

hfont = {'fontname': 'Tahoma'}

values = [351, 3, 22, 50, 40, 159]
labels = ["Ice Hockey", "Biathlon", "Bobsleigh", "Curling", "Skiing", "Skating"]
colors = ["#011f4b", "#03396c", "#005b96", "#6497b1", "#b3cde0", "white"]
explode = (0.1, 0, 0, 0, 0, 0)

patches, text = plt.pie(values, colors=colors, explode=explode, shadow=True)
plt.legend(patches, labels, loc="best")

plt.axis('equal')

plt.title("Sports that won the Most Medals in Canada From 1924-2014", **hfont)

plt.show()