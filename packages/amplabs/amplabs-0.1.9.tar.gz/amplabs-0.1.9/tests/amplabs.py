from amplabs.reader import *
from amplabs.plot import *
from amplabs.utils import *
import os


current_directory = os.path.dirname(os.path.abspath(__file__))

relative_dat_path = os.path.join(current_directory, 'files','DATTest.dat')
relative_tdms_path = os.path.join(current_directory, 'files','TDMSTest.tdms')
relative_csv_path = os.path.join(current_directory, 'files','CSVTest.csv')


''' Test for reader '''

dat_data = readDAT(relative_dat_path)
tdms_data = readTDMS(relative_tdms_path)
csv_data = readCSV(relative_csv_path)

print("Reader methods working...")


''' Test for utils '''

dat_data["Test Time"] = minutesToSeconds(dat_data["Test Time"])
headers = showHeaders(dat_data)
newtdms = addHeaders(tdms_data, ['Amphenol', 'LT_Sens2', 'Voltage', 'WaterFlow', 'AbsoluteHumidity BSS_V7', 'AirTemperature BSS_V7', 'Ethanol BSS_V7', 'TotalVOC BSS_V7', 'H2_Concentration AX222058_V0', 'RelativeHumidity AX222058_V0'])
tdms_data = addTestTime(tdms_data, 0, 0.1)
csv_data["voltage"] = dataSmoothing(csv_data["voltage"])

print("Utils methods working...")


# ''' Test for plots - dashboard '''

# ax1 = plot(df=dat_data,df_name="AnD_data")

# ax1.set_color(["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"])
# ax1.set_xrange([0,100])
# ax1.set_yrange([10,90])
# ax1.set_xintervals(10)
# ax1.set_yintervals(10)
# ax1.set_xlabel("X test")
# ax1.set_ylabel("Y test")
# ax1.set_linewidth(3.5)

# plot.plot_on_dashboard()


''' Test for plots - svg ''' 

ax2 = plot(df=tdms_data, x_columns="Test Time", y_columns=["Voltage","Amphenol"])
ax2.set_color(["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"])
ax2.set_xrange([0,100])
ax2.set_yrange([10,90])
ax2.set_xintervals(10)
ax2.set_yintervals(10)
ax2.set_xlabel("X test")
ax2.set_ylabel("Y test")
ax2.set_linewidth(3.5)

plot.plot_as_svg()

print("Plots method working...")