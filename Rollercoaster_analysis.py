import pandas as pd
import matplotlib.pyplot as plt

rollercoaster_wood = pd.read_csv('/Users/olly/Downloads/Roller Coaster/Golden_Ticket_Award_Winners_Wood.csv')
pd.set_option('display.max_columns', None)
# print(rollercoaster_wood.head())

rollercoaster_steel = pd.read_csv('/Users/olly/Downloads/Roller Coaster/Golden_Ticket_Award_Winners_Steel.csv')
pd.set_option('display.max_columns', None)
# print(rollercoaster_steel.head())

def coaster_rankings(coaster_name_1, park_name_1, coaster_name_2, park_name_2, rankings_df):
    coaster_1_ranking = rankings_df[(rankings_df['Name'] == coaster_name_1) & (rankings_df['Park'] == park_name_1)]
    coaster_2_ranking = rankings_df[(rankings_df['Name'] == coaster_name_2) & (rankings_df['Park'] == park_name_2)]
    fig, ax = plt.subplots()
    ax.plot(coaster_1_ranking['Year of Rank'], coaster_1_ranking['Rank'])
    ax.plot(coaster_2_ranking['Year of Rank'], coaster_2_ranking['Rank'])
    ax.set_yticks(coaster_1_ranking['Rank'].values)
    ax.set_xticks(coaster_1_ranking['Year of Rank'].values)
    ax.invert_yaxis()
    plt.title('{} vs {} Rankings'.format(coaster_name_1, coaster_name_2))
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.show()
    plt.close()

# coaster_rankings('El Toro', 'Six Flags Great Adventure' ,'Boulder Dash', 'Lake Compounce', rollercoaster_wood)
plt.clf()

def n_plot_coaster_rankings(rankings_df, n):
    top_n_rankings = rankings_df[rankings_df['Rank'] <= n]
    fig, ax = plt.subplots(figsize=(8, 8))
    for coaster in set(top_n_rankings['Name']):
        coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
        ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label=coaster)
    ax.set_yticks([i for i in range(1, 11)])
    ax.invert_yaxis()
    plt.title("Top Ten Rankings")
    plt.xlabel("Year")
    plt.ylabel("Ranking")
    plt.legend(loc=4)
    plt.show()
    plt.close()

# n_plot_coaster_rankings(rollercoaster_wood, 10)
plt.clf()

roller_coasters = pd.read_csv('/Users/olly/Downloads/Roller Coaster/roller_coasters.csv')
pd.set_option('display.max_columns', None)
print(roller_coasters.head())

def coaster_hist_plot(coaster_df, column):
    plt.hist(coaster_df[column].dropna())
    plt.title('Histogram of Roller Coaster {}'.format(column))
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()
    plt.close()

# coaster_hist_plot(roller_coasters, 'speed')
plt.clf()

def bar_of_park_inversions(coaster_df, park_name):
    park_coasters = coaster_df[coaster_df['park'] == park_name]
    park_coasters = park_coasters.sort_values('num_inversions', ascending=False)
    coaster_names = park_coasters['name']
    number_inversions = park_coasters['num_inversions']
    plt.bar(range(len(number_inversions)), number_inversions)
    ax = plt.subplot()
    ax.set_xticks(range(len(coaster_names)))
    ax.set_xticklabels(coaster_names, rotation=90)
    plt.title("Number of Inversions per Coaster at {}".format(park_name))
    plt.xlabel("Roller Coaster")
    plt.ylabel("# of Inversions")
    plt.show()
    plt.close()

# bar_of_park_inversions(roller_coasters, 'Six Flags Great Adventure')
plt.clf()

def coaster_status_piechart(coaster_df):
    operating_coasters = coaster_df[coaster_df['status'] == 'status.operating']
    closed_coasters = coaster_df[coaster_df['status'] == 'status.closed.definitely']
    num_operating = len(operating_coasters)
    num_closed = len(closed_coasters)
    status_counts = [num_operating, num_closed]
    plt.pie(status_counts, autopct='%0.1f%%', labels=['Operating', 'Closed'])
    plt.axis('equal')
    plt.show()
    plt.close()

# coaster_status_piechart(roller_coasters)
plt.clf()

def coaster_scatter_plot(coaster_df, column_x, column_y):
    plt.scatter(coaster_df[column_x], coaster_df[column_y])
    plt.title("Scatter Plot of {} vs {}".format(column_x, column_y))
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.show()
    plt.close()

coaster_scatter_plot(roller_coasters, 'length', 'speed')
plt.clf()