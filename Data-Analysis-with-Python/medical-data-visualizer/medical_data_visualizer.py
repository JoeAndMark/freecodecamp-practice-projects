import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Read data and convert it to dataframe.
df = pd.read_csv("medical_examination.csv")

# 2 Add 'overweight' column
df_bmi = df["weight"] / ((df["height"] / 100) ** 2)
df['overweight'] = df_bmi.apply(lambda x: 1 if x > 25 else 0)

# 3 Nomalize cholesterol and gluc data.
df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # 5
    column_selected = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=column_selected)


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name="total")
    

    # 7
    chart = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    )


    # 8
    fig = chart.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12, 8))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', square=True, linewidths=.5, ax=ax)


    # 16
    fig.savefig('heatmap.png')
    return fig
