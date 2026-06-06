    
# Import all necessary libraries
!pip install scikit-learn pandas numpy matplotlib seaborn alibi-detect scipy joblib tqdm PyYAML

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, confusion_matrix
import joblib
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# [Include all the classes and functions we created]
# ProductionCyberDefense, NetworkTrafficMonitor, etc.

print("Cyber Defense System ready!")
