import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%

def readcsv(filename):
    """Reading the initial excel file into Python and creating a dataframe"""
    df_one = pd.read_csv(filename)
    
    """Removing all unwanted/incomplete data, cleaning the data"""
    df_two = df_one.drop(["Country Code", "Indicator Name", "Indicator Code", "1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "2023", "2024", "2025"], axis=1)
    
    """Setting the index of the data with the "Country Name" """
    df_two.set_index('Country Name', inplace=True)
    
    """Transposing the dataframe to enable a column for both years and countries"""
    df_thr = df_two.T
    
    """Producing two dataframes, one with countries as the column (df_two) and one with years as the column (df_thr)"""
    return df_two, df_thr

country, years = readcsv(r"C:\Users\ahabe\OneDrive - University of Hertfordshire\Methane datasheet.csv")
print(country)
print(years['Nepal'])

plt.figure()
plt.plot(years['World'], color="Green", label="World emissions")
plt.xticks([0,10,20,30])
plt.grid()
plt.ylabel("Methane (CH4) emissions")
plt.xlabel("Years")
plt.legend(loc = 'upper left')
plt.title("Level of Methane emissions from agriculture over time")

print(country.describe())
print(years.describe())
# %%

plt.figure()
plt.plot(years['Nepal'], color='Red', label='Nepal')
plt.plot(years['Japan'], color = 'Green', label='Japan')
plt.plot(years['Australia'], color = 'Black', label='Australia')
plt.plot(years['Madagascar'], color='Blue', label='Madagascar')
plt.xticks([0,10,20,30])
plt.yticks([0,20,40,60,80,100,120,140])
plt.grid()
plt.ylabel("Methane (CH4) emissions")
plt.ylim(0, 145)
plt.xlabel("Years")
plt.legend(loc = 'upper left')
plt.title("Level of Methane emissions from agriculture over time")
# %%

plt.figure()
plt.plot(years['Nepal'].iloc[0:22], color='Red', label='Nepal')
plt.plot(years['Japan'].iloc[0:22], color = 'Green', label='Japan')
plt.plot(years['Madagascar'].iloc[0:22], color='Blue', label='Madagascar')
plt.plot(years['Australia'].iloc[0:22], color = 'Black', label='Australia')
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22])
plt.yticks([0,20,40,60,80,100,120,140])
plt.grid()
plt.ylabel("Methane (CH4) emissions")
plt.xlabel("Years")
plt.ylim(0, 145)
plt.legend(loc = 'upper left')
plt.title("Level of Methane emissions from agriculture over time\n 1990 to 2010")

# %%

plt.figure()
plt.plot(years['Japan'].iloc[12:33], color = 'Green', label='Japan')
plt.plot(years['Nepal'].iloc[12:33], color='Red', label='Nepal')
plt.plot(years['Madagascar'].iloc[12:33], color='Blue', label='Madagascar')
plt.plot(years['Australia'].iloc[12:33], color = 'Black', label='Australia')
plt.xticks([0,2,4,6,8,10,12,14,16,18,20])
plt.yticks([0,20,40,60,80,100,120,140])
plt.grid()
plt.ylabel("Methane (CH4) emissions")
plt.xlabel("Years")
plt.ylim(0, 145)
plt.legend(loc = 'upper left')
plt.title("Level of Methane emissions from agriculture over time")
# %%

def readcsv(filename):
    """Reading the initial excel file into Python and creating a dataframe"""
    df_onegdp = pd.read_csv(filename)
    
    """Removing all unwanted/incomplete data, cleaning the data"""
    df_twogdp = df_onegdp.drop(["Country Code", "Indicator Name", "Indicator Code", "1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "2023", "2024", "2025"], axis=1)
    
    """Setting the index of the data with the "Country Name" """
    df_twogdp.set_index('Country Name', inplace=True)
    
    """Transposing the dataframe to enable a column for both years and countries"""
    df_thrgdp = df_twogdp.T
    
    """Producing two dataframes, one with countries as the column (df_two) and one with years as the column (df_thr)"""
    return df_twogdp, df_thrgdp

countrygdp, yearsgdp = readcsv(r"C:\Users\ahabe\OneDrive - University of Hertfordshire\Energy use data.csv")

print(countrygdp)
print(yearsgdp['Nepal'])

plt.figure()
plt.plot(yearsgdp['World'], color="goldenrod", label="World")
plt.xticks([0,10,20,30])
plt.ylabel("Energy quantity")
plt.grid()
plt.xlabel("Years")
plt.legend(loc = 'upper left')
plt.title("Energy usage")

plt.figure()
plt.plot(yearsgdp['Nepal'], color='Red', label='Nepal')
plt.plot(yearsgdp['Japan'], color = 'Green', label='Japan')
plt.plot(yearsgdp['Australia'], color = 'Black', label='Australia')
plt.plot(yearsgdp['Madagascar'], color='Blue', label='Madagascar')
plt.xticks([0,10,20,30])
plt.yticks([1000,2000,3000,4000,5000,6000,7000,8000,9000])
plt.grid()
plt.ylabel("Energy use (kg of oil equivalent per capita)")
plt.xlabel("Years")
plt.legend(loc = 'upper left')
plt.title("Energy use over time")
# %%
plt.figure()
plt.plot(yearsgdp['Nepal'].iloc[0:22], color='Red', label='Nepal')
plt.plot(yearsgdp['Japan'].iloc[0:22], color = 'Green', label='Japan')
plt.plot(yearsgdp['Madagascar'].iloc[0:22], color='Blue', label='Madagascar')
plt.plot(yearsgdp['Australia'].iloc[0:22], color = 'Black', label='Australia')
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22])
plt.yticks([1000,2000,3000,4000,5000,6000,7000,8000,9000])
plt.grid()
plt.ylabel("Energy use (kg of oil equivalent per capita)")
plt.xlabel("Years")
plt.legend(loc = 'upper left')
plt.title("Energy use over time, 1970 to 1990")
# %%

plt.figure()
plt.plot(yearsgdp['Japan'].iloc[12:33], color = 'Green', label='Japan')
plt.plot(yearsgdp['Nepal'].iloc[12:33], color='Red', label='Nepal')
plt.plot(yearsgdp['Madagascar'].iloc[12:33], color='Blue', label='Madagascar')
plt.plot(yearsgdp['Australia'].iloc[12:33], color = 'Black', label='Australia')
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22])
plt.yticks([1000,2000,3000,4000,5000,6000,7000,8000,9000])
plt.grid()
plt.ylabel("Energy use (kg of oil equivalent per capita)")
plt.xlabel("Years")
plt.legend(loc = 'upper left')
plt.title("Energy use over time, 2004 to 2024")

# %%

# Calculating averate rate of change

def ratechange(dataframe):
    """Calculate the average rate of change in the last 20 years, 2002 to 2022"""
    Recent_20_years = (dataframe['2022'] - dataframe['2002'])/(2022-2002)
    
    """Calculate the average rate of change in the initial 20 years, 1990 to 2010"""
    Initial_20_years = (dataframe['2010'] - dataframe['1990'])/(2010-1990)

    return Recent_20_years, Initial_20_years

Nepalgdp_recent, Nepalgdp_initial = ratechange(yearsgdp["Nepal"])
Madagascargdp_recent, Madagascargdp_initial = ratechange(yearsgdp["Madagascar"])
Japangdp_recent, Japangdp_initial = ratechange(yearsgdp["Japan"])
Australiagdp_recent, Australiagdp_initial = ratechange(yearsgdp["Australia"])

Nepal_recent, Nepal_initial = ratechange(years["Nepal"])
Madagascar_recent, Madagascar_initial = ratechange(years["Madagascar"])
Japan_recent, Japan_initial = ratechange(years["Japan"])
Australia_recent, Australia_initial = ratechange(years["Australia"])



ratemetdf = pd.DataFrame({
    "Country": ["Nepal", "Australia", "Japan", "Madagascar"],
    "Income level": ["Low", "High", "High", "Low"],
    "Average rate change 1990-2010": [Nepal_initial, Australia_initial, Japan_initial, Madagascar_initial],
    "Average rate change 2002-2022": [Nepal_recent, Australia_recent, Japan_recent, Madagascar_recent]
    })

print(yearsgdp["Australia"]["2022"])
print(yearsgdp["Australia"]["2002"])
print(ratechange(yearsgdp["Australia"]))

rategdpdf = pd.DataFrame({
    "Country": ["Nepal", "Australia", "Japan", "Madagascar"],
    "Income level": ["Low", "High", "High", "Low"],
    "Average rate change 1990-2010": [Nepalgdp_initial, Australiagdp_initial, Japangdp_initial, Madagascargdp_initial],
    "Average rate change 2002-2022": [Nepalgdp_recent, Australiagdp_recent, Japangdp_recent, Madagascargdp_recent]
    })

print(ratemetdf)
print(rategdpdf)

# %%

# Moving average for methane production in agriculture
Moving_averagemet = (years['Nepal'] + years['Australia'] + years['Japan'] + years['Madagascar'])/4
print(Moving_averagemet)

plt.figure()
plt.figure()
plt.plot(years['Nepal'], color='Red', label='Nepal')
plt.plot(years['Japan'], color = 'Green', label='Japan')
plt.plot(years['Australia'], color = 'Black', label='Australia')
plt.plot(years['Madagascar'], color='Blue', label='Madagascar')
plt.plot(Moving_averagemet, color='goldenrod', label='Moving Average')
plt.xticks([0,5,10,15,20,25,30])
plt.yticks([0,20,40,60,80,100, 120, 140, 160, 180])
plt.grid()
plt.ylabel("Methane (CH4) emissions from agriculture\n(Mt CO2e)")
plt.ylim(0, 170)
plt.xlabel("Years")
plt.legend(loc = 'upper left')
plt.title("Level of Methane emissions from agriculture over time\n 1990 to 2022")

plt.figure()
plt.plot(years['Nepal'].iloc[0:22], color='Red', label='Nepal')
plt.plot(years['Japan'].iloc[0:22], color = 'Green', label='Japan')
plt.plot(years['Madagascar'].iloc[0:22], color='Blue', label='Madagascar')
plt.plot(years['Australia'].iloc[0:22], color = 'Black', label='Australia')
plt.plot(Moving_averagemet.iloc[0:22], color='goldenrod', label='Moving Average')
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22])
plt.yticks([0,20,40,60,80,100,120,140,160,180])
plt.grid()
plt.ylabel("Methane (CH4) emissions from agriculture\n(Mt CO2e)")
plt.xlabel("Years")
plt.ylim(0, 170)
plt.legend(loc = 'upper left')
plt.title("Level of Methane emissions from agriculture over time,\n1990 to 2010")

plt.figure()
plt.plot(years['Australia'].iloc[12:33], color = 'Black', label='Australia')
plt.plot(years['Japan'].iloc[12:33], color = 'Green', label='Japan')
plt.plot(years['Madagascar'].iloc[12:33], color='Blue', label='Madagascar')
plt.plot(years['Nepal'].iloc[12:33], color='Red', label='Nepal')
plt.plot(Moving_averagemet.iloc[12:33], color='goldenrod', label='Moving Average')
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22])
plt.yticks([0,20,40,60,80,100,120,140,160,180])
plt.grid()
plt.ylabel("Methane (CH4) emissions from agriculture\n(Mt CO2e)")
plt.xlabel("Years")
plt.ylim(0, 170)
plt.legend(loc = 'upper left')
plt.title("Level of Methane emissions from agriculture over time,\n2002 to 2022")
# %%


# Moving average for urban gdpulation
Moving_averagegdp = (yearsgdp['Nepal'] + yearsgdp['Australia'] + yearsgdp['Japan'] + yearsgdp['Madagascar'])/4
print(Moving_averagegdp)

plt.figure()
plt.plot(yearsgdp['Nepal'], color='Red', label='Nepal')
plt.plot(yearsgdp['Japan'], color = 'Green', label='Japan')
plt.plot(yearsgdp['Australia'], color = 'Black', label='Australia')
plt.plot(yearsgdp['Madagascar'], color='Blue', label='Madagascar')
plt.plot(Moving_averagegdp, color='goldenrod', label='Moving Average')
plt.xticks([0,5,10,15,20,25,30])
plt.yticks([1000,2000,3000,4000,5000,6000,7000,8000,9000])
plt.ylim(0, 9550)
plt.grid()
plt.ylabel("Energy use (kg of oil equivalent per capita)")
plt.xlabel("Years")
plt.legend(loc = 'upper left')
plt.title("Energy use over time, \n1990 to 2022")

plt.figure()
plt.plot(yearsgdp['Nepal'].iloc[0:22], color='Red', label='Nepal')
plt.plot(yearsgdp['Japan'].iloc[0:22], color = 'Green', label='Japan')
plt.plot(yearsgdp['Madagascar'].iloc[0:22], color='Blue', label='Madagascar')
plt.plot(yearsgdp['Australia'].iloc[0:22], color = 'Black', label='Australia')
plt.plot(Moving_averagegdp.iloc[0:22], color='goldenrod', label='Moving Average')
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22])
plt.yticks([1000,2000,3000,4000,5000,6000,7000,8000,9000])
plt.ylim(0, 9550)
plt.grid()
plt.ylabel("Energy use (kg of oil equivalent per capita)")
plt.xlabel("Years")
plt.legend(loc = 'upper left')
plt.title("Energy use over time, \n1990 to 2010")

plt.figure()
plt.plot(yearsgdp['Nepal'].iloc[12:33], color='Red', label='Nepal')
plt.plot(yearsgdp['Japan'].iloc[12:33], color = 'Green', label='Japan')
plt.plot(yearsgdp['Madagascar'].iloc[12:33], color='Blue', label='Madagascar')
plt.plot(yearsgdp['Australia'].iloc[12:33], color = 'Black', label='Australia')
plt.plot(Moving_averagegdp.iloc[12:33], color='goldenrod', label='Moving Average')
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22])
plt.yticks([1000,2000,3000,4000,5000,6000,7000,8000,9000])
plt.ylim(0, 9550)
plt.grid()
plt.ylabel("Energy use (kg of oil equivalent per capita)")
plt.xlabel("Years")
plt.legend(loc = 'upper left')
plt.title("Energy use over time,\n2002 to 2022")

# %%

def bootstrap_i(frame):
    Firstdiff = (frame['1994'] - frame['1990']) / (1994-1990)
    Seconddiff = (frame['1998'] - frame['1994']) / (1998-1994)
    Thirddiff = (frame['2002'] - frame['1998']) / (2002-1998)
    Fourthdiff = (frame['2006'] - frame['2002']) / (2006-2002)
    Fifthdiff = (frame['2010'] - frame['2006']) / (2010-2006)
    
    return Firstdiff, Seconddiff, Thirddiff, Fourthdiff, Fifthdiff

def bootstrap_r(frame):
    Sixthdiff = (frame['2006'] - frame['2002']) / (2006-2002)
    Seventhdiff = (frame['2010'] - frame['2006']) / (2010-2006)
    Eigthdiff = (frame['2014'] - frame['2010']) / (2014-2010)
    Ninethdiff = (frame['2018'] - frame['2014']) / (2018-2014)
    Tenthdiff = (frame['2022'] - frame['2018']) / (2022-2018)
    
    return Sixthdiff, Seventhdiff, Eigthdiff, Ninethdiff, Tenthdiff

# Recieving values for bookstrapping for the first 20 years, 1990 to 2010
AUSdiff_one, AUSdiff_two, AUSdiff_thr, AUSdiff_for, AUSdiff_fiv = bootstrap_i(yearsgdp["Australia"])

print(AUSdiff_one, AUSdiff_two, AUSdiff_thr, AUSdiff_for, AUSdiff_fiv)
print(np.mean([AUSdiff_one, AUSdiff_two, AUSdiff_thr, AUSdiff_for, AUSdiff_fiv]))

JPNdiff_one, JPNdiff_two, JPNdiff_thr, JPNdiff_for, JPNdiff_fiv = bootstrap_i(yearsgdp["Japan"])

print(JPNdiff_one, JPNdiff_two, JPNdiff_thr, JPNdiff_for, JPNdiff_fiv)
print(np.mean([JPNdiff_one, JPNdiff_two, JPNdiff_thr, JPNdiff_for, JPNdiff_fiv]))

MDGdiff_one, MDGdiff_two, MDGdiff_thr, MDGdiff_for, MDGdiff_fiv = bootstrap_i(yearsgdp["Madagascar"])

print(MDGdiff_one, MDGdiff_two, MDGdiff_thr, MDGdiff_for, MDGdiff_fiv)
print(np.mean([MDGdiff_one, MDGdiff_two, MDGdiff_thr, MDGdiff_for, MDGdiff_fiv]))

NPLdiff_one, NPLdiff_two, NPLdiff_thr, NPLdiff_for, NPLdiff_fiv = bootstrap_i(yearsgdp["Nepal"])

print(NPLdiff_one, NPLdiff_two, NPLdiff_thr, NPLdiff_for, NPLdiff_fiv)
print(np.mean([NPLdiff_one, NPLdiff_two, NPLdiff_thr, NPLdiff_for, NPLdiff_fiv]))

# Recieving values for bookstrapping for the latter 20 years, 2002 to 2022
AUSdiff_six, AUSdiff_sev, AUSdiff_egt, AUSdiff_nin, AUSdiff_ten = bootstrap_r(yearsgdp["Australia"])

print(AUSdiff_six, AUSdiff_sev, AUSdiff_egt, AUSdiff_nin, AUSdiff_ten)
print(np.mean([AUSdiff_six, AUSdiff_sev, AUSdiff_egt, AUSdiff_nin, AUSdiff_ten]))

JPNdiff_six, JPNdiff_sev, JPNdiff_egt, JPNdiff_nin, JPNdiff_ten = bootstrap_r(yearsgdp["Japan"])

print(JPNdiff_six, JPNdiff_sev, JPNdiff_egt, JPNdiff_nin, JPNdiff_ten)
print(np.mean([JPNdiff_six, JPNdiff_sev, JPNdiff_egt, JPNdiff_nin, JPNdiff_ten]))

MDGdiff_six, MDGdiff_sev, MDGdiff_egt, MDGdiff_nin, MDGdiff_ten = bootstrap_r(yearsgdp["Madagascar"])

print(MDGdiff_six, MDGdiff_sev, MDGdiff_egt, MDGdiff_nin, MDGdiff_ten)
print(np.mean([MDGdiff_six, MDGdiff_sev, MDGdiff_egt, MDGdiff_nin, MDGdiff_ten]))

NPLdiff_six, NPLdiff_sev, NPLdiff_egt, NPLdiff_nin, NPLdiff_ten = bootstrap_r(yearsgdp["Nepal"])
print(NPLdiff_six, NPLdiff_sev, NPLdiff_egt, NPLdiff_nin, NPLdiff_ten)
print(np.mean([NPLdiff_six, NPLdiff_sev, NPLdiff_egt, NPLdiff_nin, NPLdiff_ten]))

print(np.mean([AUSdiff_one, AUSdiff_two, AUSdiff_thr, AUSdiff_for, AUSdiff_fiv, AUSdiff_six, AUSdiff_sev, AUSdiff_egt, AUSdiff_nin, AUSdiff_ten]))
print(np.mean([JPNdiff_one, JPNdiff_two, JPNdiff_thr, JPNdiff_for, JPNdiff_fiv, JPNdiff_six, JPNdiff_sev, JPNdiff_egt, JPNdiff_nin, JPNdiff_ten]))
print(np.mean([MDGdiff_one, MDGdiff_two, MDGdiff_thr, MDGdiff_for, MDGdiff_fiv, MDGdiff_six, MDGdiff_sev, MDGdiff_egt, MDGdiff_nin, MDGdiff_ten]))
print(np.mean([NPLdiff_one, NPLdiff_two, NPLdiff_thr, NPLdiff_for, NPLdiff_fiv, NPLdiff_six, NPLdiff_sev, NPLdiff_egt, NPLdiff_nin, NPLdiff_ten]))

AUS = np.array([AUSdiff_one, AUSdiff_two, AUSdiff_thr, AUSdiff_for, AUSdiff_fiv, AUSdiff_six, AUSdiff_sev, AUSdiff_egt, AUSdiff_nin, AUSdiff_ten])
JPN = np.array([JPNdiff_one, JPNdiff_two, JPNdiff_thr, JPNdiff_for, JPNdiff_fiv, JPNdiff_six, JPNdiff_sev, JPNdiff_egt, JPNdiff_nin, JPNdiff_ten])
MDG = np.array([MDGdiff_one, MDGdiff_two, MDGdiff_thr, MDGdiff_for, MDGdiff_fiv, MDGdiff_six, MDGdiff_sev, MDGdiff_egt, MDGdiff_nin, MDGdiff_ten])
NPL = np.array([NPLdiff_one, NPLdiff_two, NPLdiff_thr, NPLdiff_for, NPLdiff_fiv, NPLdiff_six, NPLdiff_sev, NPLdiff_egt, NPLdiff_nin, NPLdiff_ten])

high_income_arr = [AUS, JPN]
low_income_arr = [MDG, NPL]
print(high_income_arr)
print(np.mean([np.abs(high_income_arr)]))

AUS_mean = np.mean([AUSdiff_one, AUSdiff_two, AUSdiff_thr, AUSdiff_for, AUSdiff_fiv, AUSdiff_six, AUSdiff_sev, AUSdiff_egt, AUSdiff_nin, AUSdiff_ten])
JPN_mean = np.mean([JPNdiff_one, JPNdiff_two, JPNdiff_thr, JPNdiff_for, JPNdiff_fiv, JPNdiff_six, JPNdiff_sev, JPNdiff_egt, JPNdiff_nin, JPNdiff_ten])
MDG_mean = np.mean([MDGdiff_one, MDGdiff_two, MDGdiff_thr, MDGdiff_for, MDGdiff_fiv, MDGdiff_six, MDGdiff_sev, MDGdiff_egt, MDGdiff_nin, MDGdiff_ten])
NPL_mean = np.mean([NPLdiff_one, NPLdiff_two, NPLdiff_thr, NPLdiff_for, NPLdiff_fiv, NPLdiff_six, NPLdiff_sev, NPLdiff_egt, NPLdiff_nin, NPLdiff_ten])

print(np.mean([AUS_mean, np.abs(JPN_mean)]))
print(AUS_mean)
print(JPN_mean)

def group_mean_distance(countries):
    country_means = [abs(np.mean(country)) for country in countries]
    return np.mean(country_means)

observed_high = group_mean_distance(high_income_arr)
observed_low = group_mean_distance(low_income_arr)
observed_diff = observed_high - observed_low

np.random.seed(56)
samples = 10000
boot_diffs = np.zeros(samples)

for i in range(samples):
    high_boot = [np.random.choice(country, size=len(country), replace=True)
                 for country in high_income_arr]
    
    low_boot = [np.random.choice(country, size=len(country), replace=True)
                for country in low_income_arr]
    
    high_stat = group_mean_distance(high_boot)
    low_stat = group_mean_distance(low_boot)
    
    boot_diffs[i] = high_stat - low_stat
    
ci_lower, ci_upper = np.percentile(boot_diffs, [2.5, 97.5])

print(high_boot)
print(low_boot)
print(high_stat)
print(low_stat)

plt.hist(boot_diffs, bins=40, edgecolor='black')
plt.axvline(observed_diff, color='red', linewidth=2, label='Observed difference')
plt.xlabel('Bootstrap difference (High - Low)')
plt.ylabel('Frequency')
plt.title('Bootstrap Distribution of Group Difference')
plt.legend()
plt.show()

sampleB = 10000
boot_high = np.zeros(sampleB)
boot_low = np.zeros(sampleB)

for i in range(sampleB):
    high_boot2 = [np.random.choice(country, size=len(country), replace=True)
                  for country in high_income_arr]
    
    low_boot2 = [np.random.choice(country, size=len(country), replace=True)
                 for country in low_income_arr]
    
    boot_high[i] = group_mean_distance(high_boot2)
    boot_low[i] = group_mean_distance(low_boot2)
    
plt.figure(figsize=(12,5))
plt.title("Bootstrap Distributions for high income countries and low income countries")
plt.subplot(1,2,1)
plt.hist(boot_high, bins=40, edgecolor="black")
plt.axvline(observed_high, color="red", linewidth=2, label="Observed")
plt.xlabel("Mean distance from 0 \nHigh income countries)")
plt.ylabel("Frequency")
plt.legend()

plt.subplot(1,2,2)
plt.hist(boot_low, bins=40, edgecolor="black")
plt.axvline(observed_low, color="red", linewidth=2, label="Observed")
plt.xlabel("Mean distance from 0\n(Low income countries)")
plt.ylabel("Frequency")
plt.legend()

plt.tight_layout()
plt.show()