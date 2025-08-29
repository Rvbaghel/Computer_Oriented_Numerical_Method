import streamlit as st
import pandas as pd

# --- Initialize session data ---
if "salary_data" not in st.session_state:
    st.session_state.salary_data = pd.DataFrame(columns=["Name", "Salary", "Expense", "Month"])

# --- CSS for UI ---
def inject_style():
    st.markdown("""
        <style>
        .main-container {
            background-color: #ffffff;
            padding: 2em;
            border-radius: 10px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.05);
            margin-bottom: 2em;
        }
        </style>
    """, unsafe_allow_html=True)

# --- CSV Upload Section ---
def csv_upload_section():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.subheader("📤 Upload Salary CSV")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            required_cols = {"Name", "Salary", "Expense", "Month"}
            if not required_cols.issubset(df.columns):
                st.error("CSV must contain columns: Name, Salary, Expense, Month")
            else:
                st.session_state.salary_data = pd.concat([st.session_state.salary_data, df], ignore_index=True)
                st.success("✅ File uploaded successfully!")
        except Exception as e:
            st.error(f"❌ Error reading file: {e}")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Manual Entry Form ---
def manual_entry_form():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.subheader("✍️ Enter Salary & Expense Manually")

    with st.form("manual_form"):
        name = st.text_input("Employee Name")
        salary = st.number_input("Salary Amount", min_value=0.0, format="%.2f")
        expense = st.number_input("Expense Amount", min_value=0.0, format="%.2f")
        month = st.selectbox("Month", ["January", "February", "March", "April", "May", "June", 
                                       "July", "August", "September", "October", "November", "December"])
        submitted = st.form_submit_button("Add Record")

        if submitted:
            new_entry = pd.DataFrame([[name, salary, expense, month]],
                                     columns=["Name", "Salary", "Expense", "Month"])
            st.session_state.salary_data = pd.concat([st.session_state.salary_data, new_entry], ignore_index=True)
            st.success("✅ Record added successfully!")

    st.markdown("</div>", unsafe_allow_html=True)

# --- Display Data Table ---
def show_data_table():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.subheader("📊 Current Salary Data")

    if not st.session_state.salary_data.empty:
        st.dataframe(st.session_state.salary_data)
    else:
        st.info("No data available. Upload a CSV or add records manually.")

    st.markdown("</div>", unsafe_allow_html=True)

# --- Main App ---
def main():
    st.title("💼 Salary Management Platform")
    inject_style()
    csv_upload_section()
    manual_entry_form()
    show_data_table()

main()
