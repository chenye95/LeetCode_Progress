# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
t = np.array(range(10000))
t = t / 1000.0

k = 0.5
c = 0.855

p_t = k * np.exp(-t)
q_t = np.exp(k * (np.exp(-t) - 1))
limit_q_t = np.exp(-k)

assert q_t[0] == 1.0

c_date = -np.log(np.log(c) / k + 1)
print("Limit of Q_t", limit_q_t)
print('Reach {0:.1f}% in {1:.02f}% days'.format(c * 100, c_date))

# Create the plot
infection_fig, ax = plt.subplots()
ax.plot(t, p_t)
ax.set_title("Chance of Infection P(t)")
ax.set_xlabel("Days t")
ax.set_ylabel("Percentage P(t)")

_, ax = plt.subplots()
ax.plot(t, q_t)
ax.set_title("Cumulative Chance of Not Infected Q(t)")
ax.set_xlabel("Days t")
ax.set_ylabel("Percentage Q(t)")

# Show the plot
plt.show()
