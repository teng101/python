import numpy as np
import matplotlib.pyplot as pyplt

P_values = np.linspace(1,10,30)

A_values = (P_values + np.log(10))/np.log(10)


pyplt.plot(P_values,A_values)
pyplt.title("PLOT")
pyplt.xlabel('p')
pyplt.ylabel('A')
pyplt.grid(True)
pyplt.show()