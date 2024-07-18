import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.lines as mlines
data_folder = 'data/step8'

# Import all CSV files in the folder
csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

# Create a color list for different plots
colors = plt.colormaps.get_cmap('tab20').colors

# Create the plot
plt.figure(figsize=(10, 6))

for i, csv_file in enumerate(csv_files):
   data = pd.read_csv(os.path.join(data_folder, csv_file), encoding='latin-1')

   frequency = data[' Frequency (Hz)']
   gain = data[' Gain (dB)']
   gain = 10 ** (gain / 20)  # Preprocess gain data

   max_gain_index = gain.idxmax()
   max_gain_frequency = frequency.iloc[max_gain_index]
   max_gain_value = gain.iloc[max_gain_index]

   # Find 3dB corner frequency (index closest to where gain drops to 0.707 of max gain)
   corner_freq_index = (abs(gain - 0.707 * max_gain_value)).idxmin()
   corner_freq = frequency.iloc[corner_freq_index]
   
   # Plot the line
   plt.loglog(frequency, gain, label=csv_file[:-4], color=colors[i % len(colors)], linewidth=2)

   # Mark maximum gain point
   plt.plot(
       max_gain_frequency, max_gain_value, marker='o', color=colors[i % len(colors)], markersize=10, label='Max Gain'
   )
#     # annotate the numerical values 
#    plt.annotate(f'{max_gain_frequency:.2f}', (max_gain_frequency, max_gain_value), textcoords="offset points", xytext=(0,10), ha='center') 
   # Mark 3dB corner frequency point
   plt.plot(
       corner_freq, gain.iloc[corner_freq_index], marker='v', color=colors[i % len(colors)], markersize=10, label='3dB Corner'
   )
#    plt.annotate(f'{corner_freq:.2f}', (corner_freq, gain.iloc[corner_freq_index]), textcoords="offset points", xytext=(0,10), ha='center')


plt.xlim(10, 1e6)
# plt.ylim(0, 1)  # Adjust based on your gain values
plt.xlabel('Frequency (Hz)')
# add increments to the x-axis
plt.xticks([10, 100, 1000, 10000, 100000, 1000000], ['10', '100', '1k', '10k', '100k', '1M'])
plt.ylabel('Gain (dB)')
# add many small increments to the y-axis in from 0.1 to 10
plt.yticks([0.1, 1, 10], ['0.1', '1', '10'])
plt.title('Gain vs Frequency (loglog scale)')
plt.grid(True)


# Create proxy artists for markers
proxy_circle = mlines.Line2D([], [], color='gray', marker='o', markersize=10, label='Maximum Gain')
proxy_triangle = mlines.Line2D([], [], color='gray', marker='v', markersize=10, label='3dB Corner')

handles1=[proxy_circle, proxy_triangle]

# Add colour of csv files to the handles
for i in range(len(csv_files)):
    handles1.append(mlines.Line2D([], [], color=colors[i % len(colors)], label=csv_files[i][:-4]))
    
plt.legend(handles=handles1, loc='upper right')

plt.tight_layout()
plt.show()