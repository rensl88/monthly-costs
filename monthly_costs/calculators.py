import numpy as np 
import pandas as pd

def calc_mortgage_deduction(mortgage, highest_income, interest):
    interest = interest / 100
    gross_interest = interest*mortgage
    own_house_forfait = 0.0045*mortgage
    mortgage_deduction= gross_interest - own_house_forfait
    payed_income_tax = 0.3697*highest_income
    new_income_tax= (highest_income - mortgage_deduction) * 0.3697 
    tax_payback = payed_income_tax-new_income_tax
    monthly_tax_payback = tax_payback / 12
    return monthly_tax_payback

def calc_mortgage_charge_range(min: int, max: int, interest_rate: float, highest_income: int, years: int=30, step: int= 10000):
    mortgages = np.arange(min, max, step)
    monthly = (interest_rate / 100) / 12
    n_months = years*12
    df = pd.DataFrame(mortgages, columns=['hypotheek'])
    df['maandlast bruto'] = ((monthly*df.hypotheek) / (1-((1+monthly)**-n_months))).round(2)
    df['hypotheekrenteaftrek'] = df['hypotheek'].apply(calc_mortgage_deduction,args=(highest_income, interest_rate) ).round(2)
    df['maandlast netto'] = df['maandlast bruto'] - df['hypotheekrenteaftrek']
    df = df.drop('hypotheekrenteaftrek', axis=1)
    return df