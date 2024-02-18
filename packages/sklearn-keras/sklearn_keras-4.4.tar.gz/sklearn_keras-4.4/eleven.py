import inspect
def func():
	'''
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import ParameterEstimator, MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pydot
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'  

 

names = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"]
data = pd.read_csv("C:/Users/hp/OneDrive/Desktop/New folder/heart (1).csv", names=names, na_values="?")

data = data.dropna()

model = BayesianModel([
    ('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'), ('sex', 'trestbps'),
    ('exang', 'trestbps'), ('trestbps', 'target'), ('fbs', 'target'),
    ('target', 'restecg'), ('target', 'thalach'), ('target', 'chol')
])

model.fit(data, estimator=MaximumLikelihoodEstimator)

plt.figure(figsize=(12, 8))
pos = graphviz_layout(model, prog="dot")
nx.draw(model, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, arrowsize=20)
plt.show()

 

inference = VariableElimination(model)
predicted_values = inference.map_query(variables=['target'], evidence={'age': 34, 'sex': 0})
print("Predicted Heart Disease:", predicted_values['target'])
'''
def px():
    code=inspect.getsource(func)
    print(code)
px()
