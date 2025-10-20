# Projecting Tesla FSD miles starting from known 2nd Qtr 2025 results of 4.5 billion out to June 2030.
# Used 40% as the anticipated quarterly increase in FSD miles driven.
import matplotlib.pyplot as plt
import numpy as np

# Data from projection
dates = [
    'Jun 2025', 'Sep 2025', 'Dec 2025', 'Mar 2026', 'Jun 2026',
    'Sep 2026', 'Dec 2026', 'Mar 2027', 'Jun 2027',
    'Sep 2027', 'Dec 2027', 'Mar 2028', 'Jun 2028',
    'Sep 2028', 'Dec 2028', 'Mar 2029', 'Jun 2029',
    'Sep 2029', 'Dec 2029', 'Mar 2030', 'Jun 2030'
]

v12_plus = [
    4.5, 6.31, 8.66, 11.88, 16.30,
    22.36, 30.69, 42.10, 57.77,
    79.27, 108.77, 149.24, 204.77,
    280.97, 385.53, 528.99, 725.83,
    995.92, 1366.52, 1875.02, 2572.74
]

# Convert to numpy array
v12_np = np.array(v12_plus)

# Set the figure style for a black background
plt.style.use('dark_background')

# Plot as a single line chart
plt.figure(figsize=(12, 6))
plt.fill_between(dates, v12_np, color='blue', alpha=0.7, label='FSD Miles on V12 and Beyond')

# Annotate the starting value (4.5 billion at Jun 2025)
plt.annotate('4.5B (Jun 2025)', xy=('Jun 2025', 4.5), xytext=('Jun 2025', 4.5),
             textcoords='data', ha='center', va='bottom', fontsize=10,
             bbox=dict(facecolor='white', alpha=0.8))

plt.title('Projected Cumulative FSD Miles on V12+ to 2030')
plt.xlabel('Date')
plt.ylabel('Cumulative miles driven with FSD (Supervised) (billions)')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
