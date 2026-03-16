# import matplotlib.pyplot as plt
#
# def load_signal_from_txt(path):
#     values = []
#     with open(path, "r") as file:
#         for line in file:
#             line = line.strip()
#             if line:
#                 values.append(float(line))
#     return values
#
# def signal_min(values):
#     return min(values)
#
# def signal_max(values):
#     return max(values)
#
# def signal_avg(values):
#     return sum(values) / len(values)
#
# def plot_signal(values):
#     plt.plot(values)
#     plt.title("Signal")
#     plt.xlabel("Sample")
#     plt.ylabel("Value")
#     plt.show()
#
# if __name__ == "__main__":
#     path = "ekg_signal.txt"
#
# values = load_signal_from_txt(path)
#
# print("Min:", signal_min(values))
# print("Max:", signal_max(values))
# print("Avg:", signal_avg(values))
#
# plot_signal(values)
#
# import signal_plot_ops as spo
# path = "ekg_signal.txt"
# values = spo.load_signal_from_txt(path)
# print("Averge:", spo.signal_avg(values))
# spo.plot_signal(values)
