import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

room_temp = ctrl.Antecedent(np.arange(0, 41, 1), 'room_temp')
heater_power = ctrl.Antecedent(np.arange(0, 11, 1), 'heater_power')

temperature = ctrl.Consequent(np.arange(0, 41, 1), 'temperature')

room_temp['cold'] = fuzz.trimf(room_temp.universe,[0,0,20])
room_temp['warm'] = fuzz.trimf(room_temp.universe,[0,20,40])
room_temp['hot'] = fuzz.trimf(room_temp.universe,[20,40,40])

heater_power['low'] = fuzz.trimf(heater_power.universe,[0,0,5])
heater_power['medium'] = fuzz.trimf(heater_power.universe,[0,5,10])
heater_power['high'] = fuzz.trimf(heater_power.universe,[5,10,10])

temperature['low'] = fuzz.trimf(temperature.universe, [0,0,20])
temperature['moderate'] = fuzz.trimf(temperature.universe, [0,20,40])
temperature['high'] = fuzz.trimf(temperature.universe, [20,40,40])

rule1 = ctrl.Rule(room_temp['cold'] & heater_power['low'], temperature['low'])
rule2 = ctrl.Rule(room_temp['cold'] & heater_power['medium'], temperature['moderate'])
rule3 = ctrl.Rule(room_temp['cold'] & heater_power['high'], temperature['high'])
rule4 = ctrl.Rule(room_temp['warm'] & heater_power['low'], temperature['low'])
rule5 = ctrl.Rule(room_temp['warm'] & heater_power['medium'], temperature['moderate'])
rule6 = ctrl.Rule(room_temp['warm'] & heater_power['high'], temperature['high'])
rule7 = ctrl.Rule(room_temp['hot'] & heater_power['low'], temperature['low'])
rule8 = ctrl.Rule(room_temp['hot'] & heater_power['medium'], temperature['moderate'])
rule9 = ctrl.Rule(room_temp['hot'] & heater_power['high'], temperature['high'])

temperature_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
temperature_sim = ctrl.ControlSystemSimulation(temperature_ctrl)

#input
temperature_sim.input['room_temp'] = int(input("Room Temperature: "))
temperature_sim.input['heater_power'] = int(input("Heater Power: "))

temperature_sim.compute()

print(f"Suggested Temperature: {temperature_sim.output['temperature']:.2f}°C")

room_temp.view()
heater_power.view()
temperature.view()
