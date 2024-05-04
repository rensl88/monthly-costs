import streamlit as st

from monthly_costs. calculators import calc_mortgage_charge_range


# --- container setup
header = st.container()
top_params = st.container()
graph = st.container()
table = st.container()
disclaimer = st.container()
# --- filing containers
with header:
    st.title("Maandlasten")
    st.text("""
            Vergelijk simpel de maandlasten van diverse hyoptheekbedragen. Bereken de 
            maandlasten voor een annuteitenhypotheek met 30 jaar looptijd, af te sluiten 
            in Nederland. 
            Ontwikkelt als exploratieve tool, zie disclaimer onderaan de pagina""")

with top_params:
    st.subheader("Opgave hypotheek range")
    mortgage_min, mortgage_max, interest_rate, highest_income = st.columns(4)

    mortgage_min_out = mortgage_min.number_input("minimale hypotheekbedrag", value=300000,step = 10000)
    mortgage_max_out = mortgage_max.number_input("maximale hypotheekbedrag", value=500000, step = 10000)
    interest_rate_out = interest_rate.number_input("Hypotheekrente", value = 3.67)
    highest_income_out = highest_income.number_input("Hoogste inkomen", value = 30000, step = 1000)

    df_mortgages = calc_mortgage_charge_range(mortgage_min_out, mortgage_max_out, interest_rate_out, highest_income_out)

with table:
    st.dataframe(df_mortgages, width=700, hide_index=True)

with disclaimer:
    st.text("""
        Disclaimer: berekeningen zijn niet geverifieerd, de getoonde informatie is puur te
        gebruiken ter exploratie en kan dus fouten bevatten. Wees dus voorzichtig met gebruik van de info!""")
