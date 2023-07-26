import numpy as np
import pandas as pd

def predict(movie):

    credits = pd.read_csv("tmdb_5000_credits.csv")

    movies= pd.read_csv("tmdb_5000_movies.csv")

    movies

    movies=movies.merge(credits,on='title')
    movies.shape

    movies = movies [['genres','id','keywords','title','overview','cast','crew']]
    movies.head(1)

    movies.isnull().sum()

    movies=movies.dropna()
    movies.isnull().sum()

    movies.duplicated().sum()

    movies.iloc[0].genres

    import ast

    def convert(obj):
        l=[]
        for i in ast.literal_eval(obj):
            l.append(i['name'])
        return l

    movies['genres']=movies['genres'].apply(convert)
    movies['genres']

    movies.head(1)

    movies['keywords']=movies['keywords'].apply(convert)
    movies.head(1)

    movies['cast']


    def convert3(obj):
        l=[]
        count=0
        for i in ast.literal_eval(obj):
            if (count<3):
                l.append(i['character'])
                count+=1
        return l



    movies['cast']=movies['cast'].apply(convert3)

    movies.head(1)

    import ast

    def fetch_director(obj):
        l=[]

        for i in ast.literal_eval(obj):
            if i['job']=='Director':
                l.append(i['name'])
                break
        return l

    movies['crew']=movies['crew'].apply(fetch_director)

    movies['crew']

    movies['overview']=movies['overview'].apply(lambda x:x.split())

    movies['overview']

    movies['genres']=movies['genres'].apply(lambda x : [i.replace(" ","") for i in x])
    movies['overview']=movies['overview'].apply(lambda x : [i.replace(" ","") for i in x])
    movies['crew']=movies['crew'].apply(lambda x : [i.replace(" ","") for i in x])
    movies['cast']=movies['cast'].apply(lambda x : [i.replace(" ","") for i in x])
    movies['keywords']=movies['keywords'].apply(lambda x : [i.replace(" ","") for i in x])

    movies.head(1)

    movies['tags']=movies['genres']+movies['overview']+movies['crew']+movies['cast']+movies['keywords']
    movies.head(1)

    new_df = movies[['id','title','tags']]

    new_df

    new_df['tags']=new_df['tags'].apply(lambda x:" ".join(x))

    new_df['tags']

    new_df['tags']=new_df['tags'].apply(lambda x:x.lower())

    new_df['tags']

    new_df['tags'][0]

    new_df[['tags']]

    from nltk.stem.porter import PorterStemmer
    ps=PorterStemmer()

    def stem(text):
        y=[]
        for i in text.split():
            y.append(ps.stem(i))
        return " ".join(y)

    #pd.options.mode.chained_assignment = None
    new_df['tags']=new_df['tags'].apply(stem)

    new_df['tags'][1300]


    from sklearn.feature_extraction.text import CountVectorizer
    cv=CountVectorizer(max_features=5000,stop_words='english')

    vectors=cv.fit_transform(new_df['tags']).toarray()

    vectors

    #cv.get_feature_names()

    from sklearn.metrics.pairwise import cosine_similarity


    similarity=cosine_similarity(vectors)

    def recommed(movie):
        movie_index = new_df[new_df['title']==movie].index[0]
        x=similarity[movie_index]
        l = sorted(list(enumerate(x)),reverse=True,key=lambda x:x[1])[0:6]

        ans=[]

        for i in l:
            ans.append(new_df.iloc[i[0]].title)

        return ans

    ans=recommed(movie)
    return ans


