from recommendations import critics
import matplotlib.pyplot as plt

points = []

for critic in critics:
    if 'Каникулы в Простоквашино' in critics[critic] and 'Винни-Пух' in critics[critic]:
        points.append((critics[critic]['Каникулы в Простоквашино'], critics[critic]['Винни-Пух']))

x_vals = [point[0] for point in points]
y_vals = [point[1] for point in points]

plt.xlabel('Каникулы в Простоквашино')
plt.ylabel('Винни-Пух')

for x, y, label in zip(x_vals, y_vals, critics):
    if 'Каникулы в Простоквашино' in critics[label] and 'Винни-Пух' in critics[label]:
        plt.annotate(label, (x, y), ha='left', va='bottom', fontsize=8)

plt.scatter(x_vals, y_vals, color='red')
plt.grid(True)
plt.show()