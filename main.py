import streamlit as st
from openai_generator import generate_restaurant_name_and_items

st.title("Reasturant Name Generator")
cuisine = st.text_input('Cuisine name')

if cuisine:
    response = generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(',')
    st.write('**Menu Items**')
    for item in menu_items:
        st.write("-", item)


