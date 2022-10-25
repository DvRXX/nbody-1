from nbody import main
import matplotlib.pyplot as plt
import time
times = []
n_list = [5000, 500000, 5000000, 50000000]
for i in n_list:
    start_time = time.time()
    main(i)
    times.append((time.time() - start_time))
print(times)
plt.plot(n_list, times)
plt.xlabel("Number of iterations")
plt.ylabel("Time (seconds)")
plt.title("Calculation time Python")
plt.loglog()
plt.show()
