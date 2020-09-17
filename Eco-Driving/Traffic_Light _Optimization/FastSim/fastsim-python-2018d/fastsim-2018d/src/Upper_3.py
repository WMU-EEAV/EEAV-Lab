import FASTSim
import pandas as pd
import matplotlib.pyplot as plt
cyc = FASTSim.get_standard_cycle("Nic drive cycle -3 - upper")
veh = FASTSim.get_veh(12)
output = FASTSim.sim_drive(cyc, veh)
df = pd.DataFrame.from_dict(output)[['soc','fcKwInAch', 'fcKwOutAch','fsKwhOutAch','mpgge','initial_soc','final_soc','electric_kWh_per_mi']]
df['speed'] = cyc['cycMps'] * 2.23694  # Convert mps to mph
fcKwInAch=output['fcKwInAch']
fcKwOutAch=output['fcKwOutAch']
soc=output['soc']
mpgge=output['mpgge']
initial_soc=output['initial_soc']
final_soc=output['final_soc']
df['fsKwOutAch']=output['fsKwhOutAch']*3600
speed=cyc['cycMps']* 2.23694
#fuel_gallon=output['fsKwhOutAch']*33.41
#total_fuel_gallon=sum(fsKwhOutAch)*33.41
#1/output['mpgge']
Gallons_gas_equivalent_per_mile =output['electric_kWh_per_mi']/33.7
fig, ax = plt.subplots(figsize=(9, 5))
kwh_line = df.fsKwOutAch.plot(ax=ax, label='gallon')

ax2 = ax.twinx()
speed_line = df.speed.plot(color='xkcd:pale red', ax=ax2, label='Speed')

ax.set_xlabel('Cycle Time [s]', weight='bold')
ax.set_ylabel('Fuel usage [kW]', weight='bold', color='xkcd:bluish')
ax.tick_params('y', colors='xkcd:bluish')

ax2.set_ylabel('Speed [MPH]', weight='bold', color='xkcd:pale red')
ax2.grid(False)
ax2.tick_params('y', colors='xkcd:pale red')