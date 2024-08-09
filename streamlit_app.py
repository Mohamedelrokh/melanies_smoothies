# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests


# Write directly to the app
st.title(":cup_with_straw: MOOOO Customize Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the fruits in your custom Smoothie"""
)

# Option to select favorite fruit
# option = st.selectbox('What is your favorite fruit?', ('banana', 'apple'))
# st.write('Your favorite fruit is:', option)

name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be:', name_on_order)

# Establish connection to Snowflake
cnx = st.experimental_connection("snowflake")
session = cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)

ingredient_list = st.multiselect(
    'Choose up to 5 ingredients', my_dataframe.to_pandas()['FRUIT_NAME'], max_selections=5
)

# st.write(ingredient_list)
if ingredient_list: 
    ingredient_string = ''
    for fruit_chosen in ingredient_list :
        ingredient_string += fruit_chosen + ' '
        st.subheader(fruit_chosen + ' Nutrition info ')
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon" )
        # st.text(fruityvice_response.json())
        st_df=st.dataframe(data=fruityvice_response.json(),use_container_width=True)

    # st.text(ingredient_list)
    # ingredient_string = ', '.join(ingredient_list)
    
    # my_insert_stmt = f"""INSERT INTO smoothies.public.orders (ingredients, name_on_order)
    #                      VALUES ('{ingredient_string}', '{name_on_order}')"""
    
    # st.write(my_insert_stmt)
    
    # time_to_insert = st.button('Submit Order')
    
    # if time_to_insert:
    #     session.sql(my_insert_stmt).collect()
    #     st.success('Your Smoothie is ordered!', icon="✅")
        
