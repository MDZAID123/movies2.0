import webbrowser

import streamlit as st
import json
from streamlit_lottie import st_lottie
import pickle
import pandas as pd
#to hit api in python we require a library called requests
import requests
import streamlit as st
import streamlit.components.v1 as components
def load_lottieurl(url:str):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

st.sidebar.info('Made by Mohd Zaid')
cols1, cols2 = st.sidebar.columns(2)
cols1.markdown(
    "[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/mohdzaidiiitd/)")
cols2.markdown("[![Foo](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/MDZAID123)")
col3 ,col4=st.sidebar.columns(2)
with col3:
    lottie_h = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_1pxqjqps.json")
    st_lottie(
        lottie_h,


    )

components.html(
    """
        <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" 
        data-text="Check my cool Streamlit Web-App🎈" 
        data-url="https://streamlit.io"
        data-show-count="false">
        data-size="Large" 
        data-hashtags="streamlit,python"
        Tweet
        </a>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    """
)


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1518235506717-e1ed3306a89b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

def fetch_poster(movie_id):
    import requests

    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MmMxZWJmYWEzOWM2NjYzZTEyNjhkZDQ3NDBhZDlmNiIsInN1YiI6IjY0NzQ4YzdlNWNkMTZlMDBiZjEyMzJjMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.te12tReWZRZLDbiz8txDsBeD8QdkZPRtBNyG_wE9EsU"
    }

    response = requests.get(url, headers=headers)
    data=response.json()
    print(data)
    # https: // image.tmdb.org / t / p / w300 / bOGkgRGdhrBYJSLpXaxhXVstddV.jpg

    # st.write(response.text)
    return "https://image.tmdb.org/t/p/w300/" + data.get('poster_path', '')



movies_list=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_list)
st.header("Movies2.0")
hide_st_style="""
            <style>
            #MainMenu {visibility=:hidden;}
            footer {visibility:hidden;}
            header {visibility:hidden;}
            </style>
            """
lottie_h = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_cbrbre30.json")
st_lottie(
    lottie_h,
    height=100,

)
st.title("get movies recommended")
similarity=pickle.load(open('similarity.pkl','rb'),protocol=2)



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    recommended_movies=[]
    recommended_movies_posters=[]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #now we need to fetch the poster for this recommended movies and show it to the user
        #using an api
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        # st.write(movies.iloc[i[0]].title)

    return recommended_movies,recommended_movies_posters


selected=st.selectbox('how would you like to be contacted?',movies['title'].values)

if st.button('Recommend'):
    lottie_hello=load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_F6EtR7.json")
    st_lottie(
        lottie_hello,
        height=200,

    )
    names,posters=recommend(selected)
    st.write(selected)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

if st.button("Watch now"):
    webbrowser.open("https://www.netflix.com/")

# col11,coll12=st.columns(2)
# col11.markdown(“[![Title](<https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Logo.svg.original.svg>)](<Website URL>)”)
# col12.markdown(“[![Title](<Icon/Logo URL>)](<Website URL>)”)
co1,col2=st.columns(2)
co1.markdown("[![](‘https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Logo.svg.original.svg’)](‘https://www.linkedin.com/in/mohdzaidiiitd/’)")





