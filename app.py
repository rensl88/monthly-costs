import streamlit as st
import numpy as np

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
    st.subheader("Maandelijkse lasten")
    elec, water, vve, internet, municipality_taxes = st.columns(5)

    mortgage_min_out = mortgage_min.number_input("minimale hypotheekbedrag", value=300000,step = 10000)
    mortgage_max_out = mortgage_max.number_input("maximale hypotheekbedrag", value=500000, step = 10000)
    interest_rate_out = interest_rate.number_input("Hypotheekrente", value = 3.67)
    highest_income_out = highest_income.number_input("Hoogste inkomen", value = 30000, step = 1000)
    
    elec_out = elec.number_input("Gas/water/elektra", value = 160, step = 10)
    water_out = water.number_input("Water", value = 30, step = 5)
    vve_out = vve.number_input("VVE", value = 150, step = 10)
    internet_out = internet.number_input("Internet en tv", value = 40, step=5)
    municipality_taxes_out = municipality_taxes.number_input("Gemeentelijke bel.", value= 113, step = 1)

    extra_monthly_costs = {
    'gas en elektra': elec_out,
    'water' : water_out,
    'vve': vve_out,
    'internet en tv': internet_out,
    'gemeentelijke belastingen': municipality_taxes_out
    }

    total_extra_monthly_costs = np.sum(list(extra_monthly_costs.values()))

    df_mortgages = calc_mortgage_charge_range(mortgage_min_out, mortgage_max_out, interest_rate_out, highest_income_out)
    
    df_mortgages['maandlast totaal'] = total_extra_monthly_costs + df_mortgages['maandlast netto']
    df_mortgages['maandlast totaal pp'] = df_mortgages['maandlast totaal'] / 2
with table:
    st.dataframe(df_mortgages, width=700, hide_index=True)

with disclaimer:
    st.text("""
        Disclaimer: berekeningen zijn niet geverifieerd, de getoonde informatie is puur te
        gebruiken ter exploratie en kan dus fouten bevatten. Wees dus voorzichtig met gebruik van de info!""")
