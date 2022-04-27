import string
from sza_saa_grena import solar_zenith_and_azimuth_angle  # noqa
import pandas as pd
import matplotlib.pyplot as plt
import csv;
# A random time series:
time_array = pd.date_range("1997/11/20 00:00", periods=1440, freq="1T", tz="America/Fortaleza")
sza, saa = solar_zenith_and_azimuth_angle(longitude=-53.50,  # London longitude
                                          latitude=-28.28,   # London latitude
                                          time_utc=time_array)

f_zenith = open('./zenith.csv', 'w')
writer_zenith = csv.writer(f_zenith, dialect="excel")

f_azimuth = open('./azimuth.csv', 'w')
writer_azimuth = csv.writer(f_azimuth)

print('Solar Zenith:\n');
i = 0;
for item in sza:
    # To print all results:
    # print(time_array[i],',',item);
    writer_zenith.writerow([time_array[i],item])
    i += 1;

print('Solar Azimuth:\n');
r = 0;
for item_saa in saa:
    # To print all results:
    # print(time_array[r],item_saa);
    writer_azimuth.writerow([time_array[r],item_saa])
    r += 1;

# Graph Zenith
plt.plot(time_array, sza)
plt.legend()
plt.show()

# Graph Azimuth
plt.plot(time_array, saa)
plt.legend()
plt.show()