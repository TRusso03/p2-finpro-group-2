import streamlit as st
from chatbot import get_recommendations

def app():
    st.title("Restaurant Recommendation System 🍽️✨")

    # Create input fields for user input
    restaurant_type = st.text_input("Enter restaurant type:")
    comments = st.text_input("Enter restaurant ambiance:")
    city = st.text_input("Enter city:")
    state = st.text_input("Enter state:")
    price = st.text_input("Enter price range from 1 to 3:")
    num_recommendations = st.number_input("Enter number of recommended restaurants to display:", value=5)

    # Create a button to trigger the chatbot
    if st.button("Submit"):
        try:
            price_list = [int(x) for x in price.split(',')]
            recommendations = get_recommendations(restaurant_type, comments, city, state, price_list, num_recommendations)
            # st.write('### **Results Top 5 restaurant recommendations**🤩')
            # st.divider()

            # for i, row in recommendations.iterrows():

            #     st.write(f'### {row['name']}')
            #     st.write(f'Address: {row['street_address']}, {row['city']}, {row['state']}')
            #     st.write('\n')
            #     st.divider()
            st.write("You might like:")
            st.write(recommendations)
        except Exception as e:
            st.write("Sorry, I couldn't find any recommendations for that restaurant.")

if __name__ == "__main__":
    app()