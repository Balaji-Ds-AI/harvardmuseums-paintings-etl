import streamlit as st
import pandas as pd
import mysql.connector
st.set_page_config(layout="wide", page_title="Harvard Art Paintings")

st.title("🖼️ Harvard Art Museum - Paintings Explorer")

st.markdown("""
This Streamlit app allows you to explore, query, and visualize painting records from the Harvard Art Museum.

- View locally saved painting data
- Check SQL insertion counts
- Run prebuilt analytical queries
""")


tab1, tab2, tab3 = st.tabs([" Show Data", " SQL Status", " Query & Visualize"])

with tab1:
    st.subheader(" Preview Painting Data")
    if st.button("View paintings Data"):
        try:
            df = pd.read_json("paintings_raw.json", orient='records')
            st.dataframe(df.head(2500))
        except FileNotFoundError:
            st.error(" paintings_raw.json not found.")

with tab2:
    st.subheader(" Check SQL Insertion Status")
    if st.button("Check SQL Tables"):
        try:
            conn = mysql.connector.connect(
                host="host.docker.internal",
                user="root",
                password="root",
                database="harvard_ds"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM artifact_metadata")
            st.success(f" artifact_metadata: {cursor.fetchone()[0]} rows")

            cursor.execute("SELECT COUNT(*) FROM artifact_media")
            st.success(f" artifact_media: {cursor.fetchone()[0]} rows")

            cursor.execute("SELECT COUNT(*) FROM artifact_colors")
            st.success(f" artifact_colors: {cursor.fetchone()[0]} rows")

            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f" SQL Error: {e}")

with tab3:
    st.subheader("📊 Run Queries on Paintings")

    query_options = {
        "Top 10 Titles in Paintings": """
            SELECT title FROM artifact_metadata 
            WHERE classification = 'Paintings'
            LIMIT 10
        """,
        "Top 5 Cultures (Paintings)": """
            SELECT culture, COUNT(*) as count 
            FROM artifact_metadata 
            WHERE classification = 'Paintings'
            GROUP BY culture 
            ORDER BY count DESC 
            LIMIT 5
        """,
        "Top 10 Colors Used in Paintings": """
            SELECT color, COUNT(*) 
            FROM artifact_colors 
            GROUP BY color 
            ORDER BY COUNT(*) DESC 
            LIMIT 10
        """
    }

    selected_query = st.selectbox("Choose a query to run", list(query_options.keys()))

    if st.button("Run Selected Query"):
        try:
            conn = mysql.connector.connect(
                host="host.docker.internal",
                user="root",
                password="root",
                database="harvard_ds"
            )
            cursor = conn.cursor()
            cursor.execute(query_options[selected_query])
            rows = cursor.fetchall()
            cols = [desc[0] for desc in cursor.description]
            df = pd.DataFrame(rows, columns=cols)
            st.dataframe(df)
            st.code(query_options[selected_query])
            cursor.close()
            conn.close()
        except Exception as e:
            st.error(f" Query failed: {e}")
