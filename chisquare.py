import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Function to get user input for observed and expected frequencies
def get_frequencies():
    print("Enter observed frequencies (space-separated): ")
    fo = np.array(list(map(float, input().split())))

    print("Enter expected frequencies (space-separated): ")
    fe = np.array(list(map(float, input().split())))

    return fo, fe

# Get user input
fo, fe = get_frequencies()

# Calculate chi-square statistic
chi_square_statistic = np.sum((fo - fe) ** 2 / fe)
print("Chi-Square Statistic:", chi_square_statistic)

# Parameters
df = len(fo) - 1  # degrees of freedom
alpha = 0.05  # significance level

# Critical value
critical_value = stats.chi2.ppf(1 - alpha, df)
print("Critical Value:", critical_value)

# Determine if the statistic falls in the rejection region
if chi_square_statistic > critical_value:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")

# Chi-square distribution values
x = np.linspace(0, 20, 1000)
y = stats.chi2.pdf(x, df)

# Plotting
plt.figure(figsize=(10, 6))

# Plot the chi-square distribution
plt.plot(x, y, label=f'Chi-Square Distribution (df={df})')

# Fill the rejection area
x_reject = np.linspace(critical_value, 20, 1000)
y_reject = stats.chi2.pdf(x_reject, df)
plt.fill_between(x_reject, y_reject, alpha=0.5, color='red', label='Rejection Region')

# Add a vertical line at the critical value
plt.axvline(critical_value, color='red', linestyle='--', label=f'Critical Value (α={alpha})')

# Add a vertical line at the chi-square statistic
plt.axvline(chi_square_statistic, color='blue', linestyle='-', label=f'Chi-Square Statistic')

# Labels and title
plt.xlabel('Chi-Square Value')
plt.ylabel('Probability Density')
plt.title('Chi-Square Distribution with Rejection Region')
plt.legend()
plt.grid(True)
plt.show()
