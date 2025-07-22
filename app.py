# placement_eligibility_app/app.py
import streamlit as st
import pandas as pd
import altair as alt
from database import DatabaseHandler
from queries import queries

st.set_page_config(page_title="Placement Eligibility App", layout="wide")
st.title("📊 Placement Eligibility Dashboard")

# Initialize DB
handler = DatabaseHandler()

# Sidebar filters
st.sidebar.header("🎯 Eligibility Criteria")
min_problems = st.sidebar.slider("Minimum Problems Solved", 0, 200, 50)
min_soft_skills = st.sidebar.slider("Minimum Avg. Soft Skills Score", 0, 100, 75)

# Fetch eligible students
data = handler.fetch_eligible_students(min_problems, min_soft_skills)
st.subheader("🎓 Eligible Students")
st.dataframe(data)

# Visual insights
st.markdown("---")
st.subheader("📈 Insights")
query_dict = queries()

selected_query = st.selectbox("Select an Insight", list(query_dict.keys()))
result = handler.run_query(query_dict[selected_query])

st.write(result)

# Optional charting
if "Count" in result.columns or "count" in result.columns:
    col_name = result.columns[0]
    chart = alt.Chart(result).mark_bar().encode(
        x=col_name + ":O",
        y=alt.Y(result.columns[1], title="Count")
    ).properties(width=700)
    st.altair_chart(chart)

