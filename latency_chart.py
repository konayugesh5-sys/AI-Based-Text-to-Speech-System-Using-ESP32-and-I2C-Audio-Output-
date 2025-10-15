
import matplotlib.pyplot as plt

text_length = [10, 50, 100, 200, 500]
latency = [500, 1200, 2100, 3800, 8500]

plt.figure(figsize=(10, 6))
plt.bar(range(len(text_length)), latency, tick_label=[str(x) for x in text_length])
plt.xlabel("Text Length (characters)")
plt.ylabel("Latency (ms)")
plt.title("TTS System Latency vs. Text Length")
plt.savefig("latency_chart.png")


