import matplotlib.pyplot as plt
import time
import subprocess
times = []
print_to_file = 0
n_list = [5000, 500000, 5000000, 50000000]
path = r"C:\Users\dvrxx\OneDrive - Delft University of Technology\_MSc Offshore & Dredging Engineering\Q5\GEO1000 - Python Programming for Geomatics\Assignment 4\nbody-main\cmake-build-release\nbody.exe"
for i in n_list:
    start_time = time.time()
    subprocess.check_call([path, str(i), str(print_to_file)])
    times.append((time.time() - start_time))
print(times)
plt.plot(n_list, times)
plt.xlabel("Number of iterations")
plt.ylabel("Time (seconds)")
plt.title("Calculation time C++ Release build")
plt.loglog()
plt.show()
