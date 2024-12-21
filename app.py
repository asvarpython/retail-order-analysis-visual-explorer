import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px  

# Function to establish a database connection
def create_connection():
    return mysql.connector.connect(
        host=st.secrets["db_config"]["server"],
        user=st.secrets["db_config"]["username"],
        password=st.secrets["db_config"]["password"],
        port=st.secrets["db_config"]["port"]
    )

# Function to load SQL scripts from a file
def load_sql_script(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to execute an SQL script and return the results as a DataFrame
def execute_query(sql_query, connection):
    cursor = connection.cursor()
    cursor.execute(f"USE {st.secrets['db_config']['database']}") 
    return pd.read_sql_query(sql_query, connection)

# Function to display a graph based on the DataFrame
def display_graph(df, question):
    if df.empty:
        st.write("No data available for visualization.")
        return

    if "revenue" in question.lower():
        fig = px.bar(df, x=df.columns[0], y=df.columns[1], title="Revenue Analysis")
    elif "profit" in question.lower():
        fig = px.pie(df, names=df.columns[0], values=df.columns[1], title="Profit Distribution")
    elif "discount" in question.lower():
        fig = px.bar(df, x=df.columns[0], y=df.columns[1], title="Discount Analysis")
    elif "quantity" in question.lower():
        fig = px.bar(df, x=df.columns[0], y=df.columns[1], title="Quantity Sold")
    elif "order" in question.lower():
        fig = px.line(df, x=df.columns[0], y=df.columns[1], title="Order Trends")
    elif "average" in question.lower():
        fig = px.box(df, x=df.columns[0], y=df.columns[1], title="Average Analysis")
    elif "segment" in question.lower():
        fig = px.bar(df, x=df.columns[0], y=df.columns[1], title="Segment Performance")
    elif "category" in question.lower():
        fig = px.bar(df, x=df.columns[0], y=df.columns[1], title="Category Performance")
    elif "city" in question.lower() or "state" in question.lower():
        fig = px.choropleth(df, 
                            locations=df.columns[0], 
                            locationmode='country names', 
                            color=df.columns[1], 
                            title="Geographical Analysis")
    else:
        fig = px.bar(df, x=df.columns[0], y=df.columns[1], title="General Analysis")

    st.plotly_chart(fig)

# Mapping categories and questions to their corresponding SQL script paths
def get_question_to_script_map():
    default_script_path = st.secrets["sql"]["script"]
    return {
        "Revenue and Sales Performance": {
            "Top 10 highest revenue-generating products ": f"{default_script_path}1.sql",
            "Total revenue generated per year": f"{default_script_path}10.sql",
            "Total revenue generated by each segment": f"{default_script_path}15.sql",
            "Total discount amount given for each product category": f"{default_script_path}21.sql",
            "Total quantity of products sold in each region": f"{default_script_path}13.sql",
            "Total number of unique products sold in each category": f"{default_script_path}20.sql",
            "Total number of orders placed in each year": f"{default_script_path}17.sql",
            "Total profit generated by each state": f"{default_script_path}19.sql",
        },
        "Profitability and Margins": {
            "Top 5 cities with the highest profit margins": f"{default_script_path}2.sql",
            "Average sale price per product category": f"{default_script_path}4.sql",
            "Region with the highest average sale price": f"{default_script_path}5.sql",
            "Total profit per category": f"{default_script_path}6.sql",
            "Product category with the highest total profit": f"{default_script_path}9.sql",
            "Product category with the highest average profit margin": f"{default_script_path}12.sql",
            "Product category with the highest average quantity per order": f"{default_script_path}18.sql",
            "Top 3 segments with the highest quantity of orders": f"{default_script_path}7.sql",
        },
        "Discounts and Pricing": {
            "Total discount given for each category": f"{default_script_path}3.sql",
            "Average discount percentage given per region": f"{default_script_path}8.sql",
            "Product subcategory with the lowest average discount percentage": f"{default_script_path}16.sql",
        },
        "Customer and Segments": {
            "Customer segment with the highest average order value": f"{default_script_path}11.sql",
            "Top 3 segments with the highest quantity of orders": f"{default_script_path}7.sql",
        },
        "Order Analysis": {
            "City with the highest average order value": f"{default_script_path}14.sql",
            "Product with the highest total sales quantity": f"{default_script_path}22.sql",
        },
    }

# Streamlit App Header
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50; font-size: 42px; '>Retail Order Analysis Visual Explorer</h1>", 
    unsafe_allow_html=True
)

# Fetch the question-to-script map
question_to_script_map = get_question_to_script_map()

# Step 1: Select a category using a dropdown
selected_category = st.selectbox("Select a Category", list(question_to_script_map.keys()))

# Step 2: Select a question within the chosen category
st.write("### Select a Question from the Category")

# Create a collapsible section for each category
selected_question = None
with st.expander(f"{selected_category} Questions", expanded=True):
    questions_in_category = question_to_script_map[selected_category]
    selected_question = st.selectbox("Choose a question", list(questions_in_category.keys()))

# Display the SQL script for the selected question
with st.expander("View SQL Query"):
    script_file = questions_in_category[selected_question]
    sql_script = load_sql_script(script_file)
    st.code(sql_script, language='sql')

# Execute the query and display results
if selected_question:
    try:
        conn = create_connection()
        df = execute_query(sql_script, conn)

        # Display the results as a table
        st.table(df.style.set_properties(**{'text-align': 'left'}))

        # Display a graph based on the query
        display_graph(df, selected_question)

    except Exception as e:
        st.error(f"An error occurred: {e}")

    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
