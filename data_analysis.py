import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Math": [80, 90, 70, 85, 60],
    "Science": [75, 85, 65, 80, 70],
    "English": [90, 88, 72, 85, 65]
}

df = pd.DataFrame(data)

print(df.describe())

sns.heatmap(df.corr(), annot=True)

plt.show()