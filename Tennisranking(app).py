import streamlit as st
import mysql.connector
import pandas as pd

# MySQL connection details
host = '127.0.0.1'
database = 'tennis_miniproject'
user = 'root'
password = 'lojana1106'

# Function to connect to MySQL
def create_connection():
    conn = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    return conn

# Function to fetch data from the MySQL table
def fetch_data():
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM comp_data;" 
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description] 
    cursor.close() 
    conn.close()
    print(result)
    return pd.DataFrame(result, columns=columns)

# Streamlit interface
def main():
    st.title('Tennis Ranking Explorer')

    
    data = fetch_data()

    
    st.subheader('Competitions Data')
    st.write(data)

    
    st.sidebar.title('Filters(competitions)')

    
    st.subheader('Category')
    category_filter = st.sidebar.selectbox('Select Category', data['category_name'].unique())
    filtered_data = data[data['category_name'] == category_filter]
    st.write(filtered_data)
    st.subheader('Type')
    category_filter=st.sidebar.selectbox('select type',data['type'].unique())
    filtered_data=data[data['type']== category_filter]
    st.write(filtered_data)
    total_competitors = len(data)
    st.subheader(f"Total Number of Competitors: {total_competitors}")
    competition_represented = data["competition_name"].nunique()
    st.subheader(f"Number of Competition Represented: {competition_represented}")

# Running the app
if __name__ == '__main__':
    main()

import streamlit as st
import mysql.connector
import pandas as pd

# MySQL connection details
host = '127.0.0.1'
database='complexes'
user = 'root'
password = 'lojana1106'

# Function to connect to MySQL
def create_connection():
    conn = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    return conn

# Function to fetch data from the MySQL table
def fetch_data():
    conn = create_connection()
    cursor = conn.cursor()
    query="SELECT * FROM complex_data;"
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description] 
    cursor.close() 
    conn.close()
    return pd.DataFrame(result, columns=columns)

# Streamlit interface
def main():
     
    
    data = fetch_data()

    
    st.subheader('complex Data')
    st.write(data)

    
    st.sidebar.title('Filters(complexes)')
    st.subheader('Filtered data')

    st.subheader('Venue')
    category_filter = st.sidebar.selectbox('Select venue', data['venue_name'].unique())
    filtered_data=data[data['venue_name']==category_filter]
    st.write(filtered_data)
    st.subheader('Country')
    category_filter=st.sidebar.selectbox('select country',data['country_name'].unique())
    filtered_data=data[data['country_name']==category_filter]
    st.write(filtered_data)
    countries_represented = data["country_name"].nunique()
    st.subheader(f"Number of Countries Represented: {countries_represented}")


# Running the app
if __name__ == '__main__':
    main()

import streamlit as st
import mysql.connector
import pandas as pd

# MySQL connection details
host = '127.0.0.1'
database = 'doubles'
user = 'root'
password = 'lojana1106'

# Function to connect to MySQL
def create_connection():
    conn = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    return conn

# Function to fetch data from the MySQL table
def fetch_data():
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM double_data;" 
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description] 
    cursor.close() 
    conn.close()
    return pd.DataFrame(result, columns=columns)

# Streamlit interface
def main():
    
    
    data = fetch_data()

 
    st.subheader('Double competitor Rankings')
    st.write(data)

    
    st.sidebar.subheader('Filters(Double competitions)')

    st.subheader('List of Rank')
    category_filter = st.sidebar.selectbox('Select Rank', data['rank'].unique())
    filtered_data=data[data['rank']==category_filter]
    st.write(filtered_data)
    st.subheader('List of Country')
    category_filter = st.sidebar.selectbox('Select Country', data['country'].unique())
    filtered_data=data[data['country']==category_filter]
    st.write(filtered_data)
    total_points = len(data)
    st.subheader(f"Total Number of points: {total_points}")
    competition_represented = data["points"].nunique()
    st.subheader(f"Number of Competition Represented: {competition_represented}")
    
# Running the app
if __name__ == '__main__':
    main()