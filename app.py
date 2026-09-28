import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Finance Calculator Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown(
    """
    <style>
        .main {
            padding-top: 1rem;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .dashboard-subtitle {
            color: #8b949e;
            font-size: 1.05rem;
            margin-top: -10px;
            margin-bottom: 25px;
        }
        .section-title {
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------
st.title("💰 Finance Calculator Dashboard")
st.markdown(
    '<div class="dashboard-subtitle">'
    "Interactive personal finance dashboard for income, expenses, savings, "
    "budget allocation and financial health."
    "</div>",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Sidebar inputs
# ---------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Financial Inputs")

    name = st.text_input("Name", value="Shubham")
    age = st.number_input("Age", min_value=1, max_value=100, value=30, step=1)

    st.divider()
    st.subheader("Monthly Income")

    income = st.number_input(
        "Income (₹)",
        min_value=0.0,
        value=50000.0,
        step=1000.0,
        format="%.0f",
    )

    st.divider()
    st.subheader("Monthly Expenses")

    housing = st.number_input(
        "🏠 Housing (₹)", min_value=0.0, value=12000.0, step=500.0, format="%.0f"
    )
    food = st.number_input(
        "🍱 Food (₹)", min_value=0.0, value=6000.0, step=500.0, format="%.0f"
    )
    transport = st.number_input(
        "🚗 Transport (₹)", min_value=0.0, value=4000.0, step=500.0, format="%.0f"
    )
    utilities = st.number_input(
        "💡 Utilities (₹)", min_value=0.0, value=3000.0, step=500.0, format="%.0f"
    )
    entertainment = st.number_input(
        "🎬 Entertainment (₹)",
        min_value=0.0,
        value=2500.0,
        step=500.0,
        format="%.0f",
    )
    other = st.number_input(
        "📦 Other (₹)", min_value=0.0, value=2500.0, step=500.0, format="%.0f"
    )

    st.divider()
    st.caption("Change any value to instantly update the dashboard.")

# ---------------------------------------------------------
# Calculations
# ---------------------------------------------------------
expense_dict = {
    "Housing": housing,
    "Food": food,
    "Transport": transport,
    "Utilities": utilities,
    "Entertainment": entertainment,
    "Other": other,
}

total_expenses = sum(expense_dict.values())
savings = income - total_expenses

if income > 0:
    expense_ratio = (total_expenses / income) * 100
    savings_rate = (savings / income) * 100
else:
    expense_ratio = 0
    savings_rate = 0

# Percentage of total expenses by category
expense_df = pd.DataFrame(
    {
        "Category": list(expense_dict.keys()),
        "Amount": list(expense_dict.values()),
    }
)

if total_expenses > 0:
    expense_df["Percentage"] = expense_df["Amount"] / total_expenses * 100
else:
    expense_df["Percentage"] = 0

expense_df = expense_df.sort_values("Amount", ascending=False)

# ---------------------------------------------------------
# KPI cards
# ---------------------------------------------------------
st.subheader("📊 Financial Overview")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric("Monthly Income", f"₹{income:,.0f}")

with k2:
    st.metric("Total Expenses", f"₹{total_expenses:,.0f}")

with k3:
    st.metric(
        "Monthly Savings",
        f"₹{savings:,.0f}",
        delta=f"{savings_rate:.1f}% savings rate",
        delta_color="normal" if savings >= 0 else "inverse",
    )

with k4:
    st.metric(
        "Expense Ratio",
        f"{expense_ratio:.1f}%",
        delta=f"{100 - expense_ratio:.1f}% left",
    )

# ---------------------------------------------------------
# Financial status
# ---------------------------------------------------------
if income == 0:
    st.warning("Add a monthly income to calculate your financial ratios.")
elif savings > 0:
    st.success(
        f"🎉 {name}, your current monthly surplus is ₹{savings:,.0f}. "
        f"Your savings rate is {savings_rate:.1f}%."
    )
elif savings == 0:
    st.warning(
        "⚠️ Your income and expenses are currently equal. "
        "There is no monthly surplus."
    )
else:
    st.error(
        f"🚨 Your expenses exceed income by ₹{abs(savings):,.0f}. "
        "Review the expense categories below."
    )

# ---------------------------------------------------------
# Main dashboard tabs
# ---------------------------------------------------------
tab1, tab2, tab3 = st.tabs(
    ["📈 Overview", "🥧 Expense Breakdown", "💡 Insights"]
)

# ---------------------------------------------------------
# TAB 1 — Overview
# ---------------------------------------------------------
with tab1:
    st.subheader("Income Allocation")

    overview_col1, overview_col2 = st.columns(2)

    with overview_col1:
        allocation_df = pd.DataFrame(
            {
                "Component": ["Expenses", "Savings"],
                "Amount": [max(total_expenses, 0), max(savings, 0)],
            }
        )

        fig_allocation = px.bar(
            allocation_df,
            x="Component",
            y="Amount",
            text="Amount",
            title="Income vs Expenses vs Savings",
        )
        fig_allocation.update_traces(
            texttemplate="₹%{text:,.0f}",
            textposition="outside",
        )
        fig_allocation.update_layout(
            yaxis_title="Amount (₹)",
            xaxis_title="",
            showlegend=False,
            height=420,
        )
        st.plotly_chart(fig_allocation, width="stretch")

    with overview_col2:
        gauge_value = max(min(savings_rate, 100), 0)

        fig_gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=gauge_value,
                number={"suffix": "%"},
                title={"text": "Savings Rate"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#00CC96"},
                    "steps": [
                        {"range": [0, 20], "color": "#FEE2E2"},
                        {"range": [20, 40], "color": "#FEF3C7"},
                        {"range": [40, 100], "color": "#DCFCE7"},
                    ],
                },
            )
        )
        fig_gauge.update_layout(height=420)
        st.plotly_chart(fig_gauge, width="stretch")

    st.subheader("Monthly Budget Summary")

    summary_df = pd.DataFrame(
        {
            "Metric": [
                "Income",
                "Expenses",
                "Savings",
                "Expense Ratio",
                "Savings Rate",
            ],
            "Value": [
                f"₹{income:,.0f}",
                f"₹{total_expenses:,.0f}",
                f"₹{savings:,.0f}",
                f"{expense_ratio:.1f}%",
                f"{savings_rate:.1f}%",
            ],
        }
    )

    st.dataframe(summary_df, hide_index=True, width="stretch")

# ---------------------------------------------------------
# TAB 2 — Expense Breakdown
# ---------------------------------------------------------
with tab2:
    left, right = st.columns(2)

    with left:
        fig_donut = px.pie(
            expense_df,
            names="Category",
            values="Amount",
            hole=0.58,
            title="Expense Distribution",
        )
        fig_donut.update_traces(
            textinfo="percent",
            hovertemplate="<b>%{label}</b><br>₹%{value:,.0f}<br>%{percent}<extra></extra>",
        )
        fig_donut.update_layout(height=450)
        st.plotly_chart(fig_donut, width="stretch")

    with right:
        fig_bar = px.bar(
            expense_df,
            x="Amount",
            y="Category",
            orientation="h",
            text="Percentage",
            title="Expense Categories",
        )
        fig_bar.update_traces(
            texttemplate="%{text:.1f}%",
            textposition="outside",
        )
        fig_bar.update_layout(
            xaxis_title="Amount (₹)",
            yaxis_title="",
            height=450,
        )
        st.plotly_chart(fig_bar, width="stretch")

    st.subheader("Expense Percentage Analysis")

    display_df = expense_df.copy()
    display_df["Amount"] = display_df["Amount"].map(lambda x: f"₹{x:,.0f}")
    display_df["Percentage"] = display_df["Percentage"].map(lambda x: f"{x:.1f}%")

    st.dataframe(
        display_df,
        hide_index=True,
        width="stretch",
    )

# ---------------------------------------------------------
# TAB 3 — Insights
# ---------------------------------------------------------
with tab3:
    st.subheader("💡 Automated Insights")

    if total_expenses > 0:
        largest_category = expense_df.iloc[0]
        largest_pct = largest_category["Percentage"]

        st.info(
            f"**Largest expense:** {largest_category['Category']} — "
            f"₹{largest_category['Amount']:,.0f} "
            f"({largest_pct:.1f}% of total expenses)."
        )

    if savings_rate >= 30:
        st.success(
            f"Your calculated savings rate is {savings_rate:.1f}%. "
            "A relatively large share of your income remains after the "
            "entered expenses."
        )
    elif savings_rate >= 10:
        st.warning(
            f"Your calculated savings rate is {savings_rate:.1f}%. "
            "There is a positive monthly surplus, but expense categories "
            "may still be worth reviewing."
        )
    else:
        st.error(
            f"Your calculated savings rate is {savings_rate:.1f}%. "
            "The entered expenses leave little or no monthly surplus."
        )

    st.subheader("📌 Budget Composition")

    composition_df = expense_df.copy()
    composition_df["Percentage of Income"] = (
        composition_df["Amount"] / income * 100 if income > 0 else 0
    )

    fig_income_share = px.bar(
        composition_df,
        x="Category",
        y="Percentage of Income",
        text="Percentage of Income",
        title="Each Expense Category as % of Income",
    )
    fig_income_share.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
    )
    fig_income_share.update_layout(
        yaxis_title="Percentage of Income",
        xaxis_title="",
        height=430,
    )
    st.plotly_chart(fig_income_share, width="stretch")

    st.caption(
        "This dashboard provides calculations based only on the values entered "
        "by the user. It is an educational budgeting tool, not financial advice."
    )

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.divider()
st.caption("Built with Python, Streamlit, Plotly and Pandas • Finance Calculator Dashboard")
