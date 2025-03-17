import streamlit as st

# Function for conversion
def convert_units(value, from_unit, to_unit):


    # ******************************* Old Code *******************************
    # HEre The written Code below for celcius to fahrenheit and fahrenheit to celcius is not needed because we can use lambda function to do the same thing, So That's why I have commented the below code and used lambda function to do the same thing. I have Also used the dictionary to store the conversion factors for different units. (Remember I already Study before Python so I know how to do this, But I have also learned this from the course, So I have used the dictionary to store the conversion factors for different units.). So you can do as your knowledge.
    # ******************************* Old Code *******************************

    # def celsius_to_fahrenheit(c):
    #     return (c * 9/5) + 32

    # def fahrenheit_to_celsius(f):
    #     return (f - 32) * 5/9

    conversion_factors = {
        "meters_feet": 3.28084,
        "feet_meters": 0.3048,
        "celsius_fahrenheit": lambda c: (c * 9/5) + 32,
        "fahrenheit_celsius": lambda f: (f - 32) * 5/9
    }

    if from_unit == "meters" and to_unit == "feet":
        return value * conversion_factors["meters_feet"]
    elif from_unit == "feet" and to_unit == "feet":
        return value * conversion_factors["feet_meters"]
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return conversion_factors["celsius_fahrenheit"](value)
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return conversion_factors["fahrenheit_celsius"](value)
    else:
        return "Error: Invalid Conversion"

# Here I Use Custom CSS for better design of the app (I have also learned this from the course, So I have used the custom CSS for better design of the app.) nothing else we can also use the default design of the app. So you can do as your knowledge.


st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .stApp {
            background-color: #687F96;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #4CAF50;
            text-align: center;
        }
        .stButton>button {
            background-color: #2CAF1E
            color: white;
            padding: 10px;
            border-radius: 5px;
            width: 100%;
            border: none;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI elements and layout design for the app 
st.title("🌟 Unit Converter App")
st.markdown("<h2 style='text-align: center;'>Assignment 01</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center; border: 1px solid #ccc; background-color: #0E5752; padding: 10px; border-radius: 10px;'>
        Convert between different units of Length and Temperature.<br>
        Select the category and units for conversion.
    </div>
    """,
    unsafe_allow_html=True
)

# Dropdown menu for selecting conversion category
category = st.selectbox("Select Category", ["Length", "Temperature"])

if category == "Length":
    from_unit = st.selectbox("From", ["meters", "feet"])
    to_unit = st.selectbox("To", ["feet", "meters"])
elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Fahrenheit", "Celsius"])

# Input field for value
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.write(f"🎯 Converted Value: **{result}**")
