import streamlit as st
import pandas as pd
import numpy as np


# Logical Functions
#-----------------------

# @st.cache_data
def recommended_movie_df(movie):
    movie_index = movie_df[movie_df['title']  == movie].index[0]
    similarity_row = similarity_vector[movie_index]
    recommended_movie_index = np.argsort(similarity_row)[::-1][1:10]
    
    df_list = [] 
    for i in recommended_movie_index:
        df_temp = movie_df.loc[[i]]
        df_list.append(df_temp)
    df = pd.concat(df_list, ignore_index=True)
    return df
# ----------------------------------------------------
#          Streamlit App
# ----------------------------------------------------
# -------------Import data------------------------------------------
@st.cache_data
def load_movies():
    return pd.read_csv('data/movie_df_processed.csv')

@st.cache_data
def load_similarity():
    return np.load('data/similarity_vector.npy')

movie_df = load_movies()
similarity_vector = load_similarity()
movie_list = sorted(movie_df['title'].unique())
BASE_URL = "https://image.tmdb.org/t/p/w500"
#--------------End Import Data-------------------------------------------

st.title('🎥 You might like these Movies !!!')

tab1, tab2 = st.tabs(['Movie Recommendation', 'Movie Info'])
#------------ Movie Recommendation---------------------------------------------------

with tab1:
    st.markdown("🔍 **Looking for movies like your favorite one? Just enter a title and discover similar films!**")
    with st.container(border=True):
        selected_movie = st.selectbox('Choose your favourite movie', options= ['Select a movie'] + movie_list, key='recom')
        
        if selected_movie != 'Select a movie':
            
            for i in range(9):
                df = recommended_movie_df(selected_movie)

                col1, col2 = st.columns([1,1])
                with col1.container(border=True):
                    st.image(BASE_URL+df['poster_path'][i])
                    st.caption(f"🎥**{df['title'][i]}**")
                
                with col2.container(border=True):
                    st.markdown(f"**Release Year:** {int(df['release_year'][i])}")
                    st.markdown(f"**Director:** {df['director'][i]}")
                    st.markdown(f"**Stars:** • {df['star1'][i]} • {df['star2'][i]} • {df['star2'][i]}")
                    col1, col2, col3 = st.columns(3)
                    col1.metric('Viewer Rating',df['vote_average'][i])
                    col2.metric('Vote Count', df['vote_count'][i])
                    col3.metric('Minutes:', int(df['runtime'][i]))
                    st.markdown(f"**Overview:** {df['overview'][i]}")
                    st.markdown(f"[🌐 View on TMDB](https://www.themoviedb.org/movie/{df['id'][i]})", unsafe_allow_html=True)
 
        else:
            pass     
# ----------  Details information of a movie-------------------------------------------
with tab2:
    st.markdown("🍿 **Curious about a movie? Choose one and discover the details!**")

    with st.container(border=True):
        selected_movie_info = st.selectbox('Choose a movie for Details', options= ['Select a movie'] + movie_list, key=1)
        
        if selected_movie_info != 'Select a movie':
            df_single = movie_df[movie_df['title'] == selected_movie_info]
            col1, col2 = st.columns([1,1])
            with col1.container(border=True):
                st.image(BASE_URL + df_single['poster_path'].iloc[0])
                st.caption(f"🎥**{df_single['title'].iloc[0]}**")
            
            with col2.container(border=True):
                st.markdown(f"**Release Year:** {int(df_single['release_year'].iloc[0])}")
                st.markdown(f"**Director:** {df_single['director'].iloc[0]}")
                st.markdown(f"**Stars:** • {df_single['star1'].iloc[0]} • {df_single['star2'].iloc[0]} • {df_single['star2'].iloc[0]}")
                col1, col2, col3 = st.columns(3)
                col1.metric('Viewer Rating',df_single['vote_average'].iloc[0])
                col2.metric('Vote Count', df_single['vote_count'].iloc[0])
                col3.metric('Minutes:', int(df_single['runtime'].iloc[0]))
                st.markdown(f"**Overview:** {df_single['overview'].iloc[0]}") 
                st.markdown(f"[🌐 View on TMDB](https://www.themoviedb.org/movie/{df_single['id'].iloc[0]})", unsafe_allow_html=True)
                
            
        else:
            pass




# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<hr style="margin-top: 30px;">
<div style="text-align: center; font-size: 0.9em; color: gray;">
    Created by <b>Partho Sarothi Das</b><br>
    <i>Aspiring Data Scientist | Passionate about ML & Visualization</i><br>
    Email: <a href="mailto:partho52@gmail.com">partho52@gmail.com</a><br>
    Powered by Streamlit & TMDB Data
</div>
""", unsafe_allow_html=True)