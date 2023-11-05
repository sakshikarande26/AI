from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create an empty Bayesian Network
model = BayesianNetwork()

# Define the nodes in the network
model.add_nodes_from(['Weather', 'Temperature', 'PlaySoccer'])

# Define the edges between nodes
model.add_edge('Weather', 'PlaySoccer')
model.add_edge('Temperature', 'PlaySoccer')

# Define conditional probability distributions (CPDs) for each node
cpd_weather = TabularCPD(variable='Weather', variable_card=2, values=[[0.7], [0.3]])
cpd_temperature = TabularCPD(variable='Temperature', variable_card=2, values=[[0.8], [0.2]])
cpd_play_soccer = TabularCPD(variable='PlaySoccer', variable_card=2,
                            values=[[0.9, 0.6, 0.7, 0.1],  # P(PlaySoccer | Weather, Temperature)
                                    [0.1, 0.4, 0.3, 0.9]],
                            evidence=['Weather', 'Temperature'],
                            evidence_card=[2, 2])

# Add CPDs to the model
model.add_cpds(cpd_weather, cpd_temperature, cpd_play_soccer)

# Check if the model is valid
assert model.check_model()

# Perform inference
inference = VariableElimination(model)
probability = inference.query(variables=['PlaySoccer'], evidence={'Weather': 1, 'Temperature': 0})
print(probability)