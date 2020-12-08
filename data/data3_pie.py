import matplotlib.pyplot as plt

#Gold-Silver-Bronze Canada achieved 

hfont = {'fontname': 'Tahoma'}

values = [315,203,107]
labels = ["Gold", "Silver", "Bronze" ]
colors = ["lightyellow", "white", "orange"]
explode = (0, 0, 0)

patches, text = plt.pie(values, colors=colors, explode=explode, shadow=True)
plt.legend(patches, labels, loc="best")

plt.axis('equal')

plt.title("Number Medals Canada Achieved From 1924-2014", **hfont)

plt.show()