import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snb
import numpy as np
#from google.colab import drive
#drive.mount("content/drive/")

toros = pd.read_csv("./toros.csv")
toros.head()

toros.loc[toros['Libido sexual'] == "regular", 'Libido sexual'] == "Regular"
toros.loc[toros['Libido sexual'] == "bueno", 'Libido sexual'] == "Bueno"