from statsmodels.tsa.stattools import adfuller

class time_series_models:
    def __init__(self):
        pass


    def arima_stationarity_test(self, df,column):
        pre_result = adfuller(df[column].dropna())
        k = pre_result[2]
        if pre_result[1] >= 0.05:
            significant_list = {}
            for i in range(1,k): 
                df['Seasonal First Difference'] = df[column] - df[column].shift(i)
                result=adfuller(df['Seasonal First Difference'].dropna())        
                if result[1] < 0.05:
                    significant_list[i] = result[1]
            if significant_list != {}:
                best_key = min(significant_list, key=significant_list.get)
                print(significant_list)
                df['Seasonal First Difference'] = df[column] - df[column].shift(best_key)
                results=adfuller(df['Seasonal First Difference'].dropna()) 
                labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations']
                for value,label in zip(results,labels):
                    print(label+' : '+str(value))
                print("Best shift happened at : {}".format(best_key))
                print()
                df['Seasonal First Difference'].plot(x=df['Month_x'], y=df[column])
                print()
            else:
                print()
                print("Seasonality couldn't be removed with the given parameters...")
                print()
        else:
            print("There is no trend or seasonality found in this dataset...")
            print()