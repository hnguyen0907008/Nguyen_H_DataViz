import matplotlib.pyplot as plt

hfont = {'fontname': 'Tahoma'}

#Number of gold medal achieved over the years 

years = [1924, 1928, 1932, 1948, 1952, 1960, 1964, 1968, 1976, 1984, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

pops = [9.0, 12.0, 14.0, 18.0, 16.0, 3.0, 4.0, 1.0, 1.0, 2.0, 5.0, 3.0, 14.0, 53.0, 29.0, 68.0, 63.0]

#set RGB color and width of chart
plt.plot(years, pops, color=(255/255, 0/255, 0/255), linewidth=3.0 );

#add some labels
plt.ylabel("Number of Gold Medals")
plt.xlabel("Years")
plt.title("Number of Gold Medals Canada Achieved From 1924-2014", **hfont)

#function
plt.show()