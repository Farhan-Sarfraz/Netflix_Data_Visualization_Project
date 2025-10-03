import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')

df.dropna(subset=['type','duration','title', 'rating','release_year', 'country', 'description', 'date_added','cast', 'listed_in', 'director', 'show_id'])

type_counts = df['type'].value_counts()
plt.figure(figsize=(8,6))
plt.bar(type_counts.index, type_counts.values, color=['blue', 'orange'])
plt.title('Comparison of Movies VS Tv Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movies_vs_TVshows.png')
plt.show()

country_counts = df['country'].value_counts().head(20)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index , country_counts.values , color = 'teal')
plt.title('Top 10 countries By Number of Shows ')
plt.xlabel('Number Of Shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top10_countries_barh.png')
plt.show()

rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts , labels=rating_counts.index , autopct= '%1.1f%%' , startangle = 90)
plt.title('Percentage of The Content Ratings')
plt.tight_layout()
plt.savefig('content_rating_pie.png')
plt.show()

movie_df = df[df['type'] == 'Movie'].copy()
movie_df = movie_df.dropna(subset=['duration'])
movie_df['duration_int'] = movie_df['duration'].str.replace(' min','', regex=False)
movie_df = movie_df[movie_df['duration_int'].str.isnumeric()]
movie_df['duration_int'] = movie_df['duration_int'].astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'] , bins = 30 , color = 'purple' , edgecolor = 'black')
plt.xlabel('Duration in Minutes')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('movie_duration_histogram.png')
plt.show()

release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,5))
plt.scatter(release_counts.index , release_counts.values , color = 'red')
plt.title('Release Year Vs Number of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.savefig('release_year_scatter.png')
plt.show()

content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)

fig, ax = plt.subplots(1,2, figsize = (12,8))

ax[0].plot(content_by_year.index, content_by_year['Movie'], color = 'blue')
ax[0].set_title('movie released per year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

ax[1].plot(content_by_year.index, content_by_year['TV Show'], color = 'orange')
ax[1].set_title('tv shows released per year')
ax[1].set_xlabel('year')
ax[1].set_ylabel('number of tv shows')


fig.suptitle('comparison of movies and tv shows released over years')
plt.tight_layout()
plt.savefig('movies_tv_shows_comparison.png')
plt.show()
