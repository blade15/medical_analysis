# -----------------------------
# MEDICAL DATA ANALYSIS SCRIPT
# -----------------------------
# Answers to Questions 1–13 using pandas, seaborn, matplotlib, numpy
# -----------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the data
df = pd.read_csv("medical_examination.csv")

# 2. Add an 'overweight' column based on BMI > 25
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalize 'cholesterol' and 'gluc' values
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4–8. Create categorical plot
def draw_cat_plot():
    # 5. Melt the data to long format for seaborn
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group and count values
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7–8. Draw bar plot with seaborn and return figure
    fig = sns.catplot(x="variable", y="total", hue="value", col="cardio",
                      data=df_cat, kind="bar").fig
    fig.suptitle("Categorical Plot of Health Indicators", y=1.05)
    return fig

# 9–13. Create heatmap
def draw_heat_map():
    # 9. Clean data by filtering based on logical constraints
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 10. Calculate correlation matrix
    corr = df_heat.corr()

    # 11. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 12. Set up matplotlib figure and draw heatmap
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0, square=True, cbar_kws={"shrink": 0.5})
    plt.title("Correlation Heatmap of Medical Features")
    return fig

# Execute and display plots
if __name__ == "__main__":
    cat_plot_fig = draw_cat_plot()
    plt.show()

    heat_map_fig = draw_heat_map()
    plt.show()
