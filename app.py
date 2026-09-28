import streamlit as st


# --------------------------------
# Page configuration
# --------------------------------

st.set_page_config(
    page_title="Personal Finance App",
    page_icon="💰",
    layout="centered"
)


# --------------------------------
# App title
# --------------------------------

st.title("💰 Personal Finance App")

st.write(
    "Enter your monthly income and expenses "
    "to calculate your savings."
)


# --------------------------------
# User information
# --------------------------------

name = st.text_input(
    "Your Name"
)

age = st.number_input(
    "Your Age",
    min_value=1,
    max_value=100,
    value=25
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)


# --------------------------------
# Financial information
# --------------------------------

income = st.number_input(
    "Monthly Income (₹)",
    min_value=0,
    value=50000,
    step=1000
)

expenses = st.number_input(
    "Monthly Expenses (₹)",
    min_value=0,
    value=30000,
    step=1000
)


# --------------------------------
# Calculate
# --------------------------------

if st.button("Calculate Savings"):

    savings = income - expenses

    if income > 0:
        savings_rate = (savings / income) * 100
    else:
        savings_rate = 0


    # --------------------------------
    # Display results
    # --------------------------------

    st.subheader("📊 Financial Summary")

    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")

    st.metric(
        "Monthly Income",
        f"₹{income:,.0f}"
    )

    st.metric(
        "Monthly Expenses",
        f"₹{expenses:,.0f}"
    )

    st.metric(
        "Monthly Savings",
        f"₹{savings:,.0f}"
    )

    st.metric(
        "Savings Rate",
        f"{savings_rate:.1f}%"
    )


    # --------------------------------
    # Chart
    # --------------------------------

    st.subheader("Income vs Expenses")

    chart_data = {
        "Income": income,
        "Expenses": expenses,
        "Savings": savings
    }

    st.bar_chart(chart_data)


    # --------------------------------
    # Message
    # --------------------------------

    if savings > 0:

        st.success(
            "🎉 You are saving money every month!"
        )

    elif savings == 0:

        st.warning(
            "⚠️ Your income and expenses are equal."
        )

    else:

        st.error(
            "🚨 Your expenses are higher than your income."
        )
