import pandas as pd
import matplotlib.pyplot as plt

def limpia_dataset(df_, test_):
   df = df_.copy()
   test =test_.copy()
   y_train = df.SeriousDlqin2yrs
   index_train = df['Unnamed: 0']
   y_test = test.SeriousDlqin2yrs
   index_test = df['Unnamed: 0']
   del df.SeriousDlqin2yrs
   del df['Unnamed: 0']
   df.RevolvingUtilizationOfUnsecuredLines[
   df.RevolvingUtilizationOfUnsecuredLines > 3]=3
   test.RevolvingUtilizationOfUnsecuredLines[
   test.RevolvingUtilizationOfUnsecuredLines > 3]=3

   df.edad[df.edad < 0] = df.edad.median()
   test.edad[test.edad < 0] =df.edad.median()

   df.numero_fallos_bajo['numero_fallos_bajo'] = 0
   df.numero_fallos_bajo[(df['NumberOfTime30-59DaysPastDueNotWorse'] == 1) |
           (df['NumberOfTime30-59DaysPastDueNotWorse'] == 2)] = 1
   df.numero_fallos_bajo[(df['NumberOfTime30-59DaysPastDueNotWorse'] == 3) |
           (df['NumberOfTime30-59DaysPastDueNotWorse'] == 4)] = 2
   df.numero_fallos_bajo[(df['NumberOfTime30-59DaysPastDueNotWorse'] >= 5) &
                         (df['NumberOfTime30-59DaysPastDueNotWorse'] <= 6)] = 3
   df.numero_fallos_bajo[df['NumberOfTime30-59DaysPastDueNotWorse'] > 6] = 4
   
   test.numero_fallos_bajo['numero_fallos_bajo'] = 0
   test.numero_fallos_bajo[(test['NumberOfTime30-59DaysPastDueNotWorse'] == 1) |
           (test['NumberOfTime30-59DaysPastDueNotWorse'] == 2)] = 1
   test.numero_fallos_bajo[(test['NumberOfTime30-59DaysPastDueNotWorse'] == 3) |
           (test['NumberOfTime30-59DaysPastDueNotWorse'] == 4)] = 2
   test.numero_fallos_bajo[(test['NumberOfTime30-59DaysPastDueNotWorse'] >= 5) &
                           (test['NumberOfTime30-59DaysPastDueNotWorse'] <= 6)] = 3
   test.numero_fallos_bajo[test['NumberOfTime30-59DaysPastDueNotWorse'] > 6] = 4

   df['numero_fallos_intermedio'] = 0
   df.numero_fallos_intermedio[(df['NumberOfTime60-89DaysPastDueNotWorse'] == 1) |
           (df['NumberOfTime60-89DaysPastDueNotWorse'] == 2)] = 1
   df.numero_fallos_intermedio[(df['NumberOfTime60-89DaysPastDueNotWorse'] == 3) |
           (df['NumberOfTime60-89DaysPastDueNotWorse'] == 4)] = 2
   df.numero_fallos_intermedio[(df['NumberOfTime60-89DaysPastDueNotWorse'] >= 5) &
                               (df['NumberOfTime60-89DaysPastDueNotWorse'] <= 6)] = 3
   df.numero_fallos_intermedio[df['NumberOfTime60-89DaysPastDueNotWorse'] > 6] = 4

   test.numero_fallos_intermedio['numero_fallos_intermedio'] = 0
   test.numero_fallos_intermedio[(test['NumberOfTime60-89DaysPastDueNotWorse'] == 1) |
           (test['NumberOfTime60-89DaysPastDueNotWorse'] == 2)] = 1
   test.numero_fallos_intermedio[(test['NumberOfTime60-89DaysPastDueNotWorse'] == 3) |
           (test['NumberOfTime60-89DaysPastDueNotWorse'] == 4)] = 2
   test.numero_fallos_intermedio[(test['NumberOfTime60-89DaysPastDueNotWorse'] >= 5) &
                                 (test['NumberOfTime60-89DaysPastDueNotWorse'] <= 6)] = 3
   test.numero_fallos_intermedio[test['NumberOfTime60-89DaysPastDueNotWorse'] > 6] = 4
   
   df['numero_fallos_altos'] = 0
   df.numero_fallos_altos[(df['NumberOfTimes90DaysLate'] == 1) |
           (df['NumberOfTimes90DaysLate'] == 2)] = 1
   df.numero_fallos_altos[(df['NumberOfTimes90DaysLate'] == 3) |
           (df['NumberOfTimes90DaysLate'] == 4)] = 2
   df.numero_fallos_altos[(df['NumberOfTimes90DaysLate'] >= 5) &
                          (df['NumberOfTimes90DaysLate'] <= 6)] = 3
   df.numero_fallos_altos[df['NumberOfTimes90DaysLate'] > 6] = 4

   test['numero_fallos_altos'] = 0
   test.numero_fallos_altos[(test['NumberOfTimes90DaysLate'] == 1) | (test['NumberOfTimes90DaysLate'] == 2)] = 1
   test.numero_fallos_altos[(test['NumberOfTimes90DaysLate'] == 3) | (test['NumberOfTimes90DaysLate'] == 4)] = 2
   test.numero_fallos_altos[(test['NumberOfTimes90DaysLate'] >= 5) & (test['NumberOfTimes90DaysLate'] <= 6)] = 3
   test.numero_fallos_altos[test['NumberOfTimes90DaysLate'] > 6] = 4

   ingresos_medianos = df.MonthlyIncome.median()
   df.MonthlyIncome[df.MonthlyIncome >= 20000] = 20000
   test.MonthlyIncome[test.MonthlyIncome >= 20000] = 20000
   df.MonthlyIncome.fillna(ingresos_medianos)
   test.MonthlyIncome.fillna(ingresos_medianos)

   df.NumberOfOpenCreditLinesAndLoans[df.NumberOfOpenCreditLinesAndLoans >= 25] = 25
   test.NumberOfOpenCreditLinesAndLoans[test.NumberOfOpenCreditLinesAndLoans >= 25] = 25

   df.NumberRealEstateLoansOrLines[df.NumberRealEstateLoansOrLines >= 7] = 7
   test.NumberRealEstateLoansOrLines[test.NumberRealEstateLoansOrLines >= 7] = 7

   dependientes_medianos = df.NumberOfDependendants.median()
   df.NumberOfDependendants[df.NumberOfDependendants >= 6] = 6
   test.NumberOfDependendants[test.NumberOfDependendants >= 6] = 6
   df.NumberOfDependendants.fillna(dependientes_medianos)
   test.NumberOfDependendants.fillna(NumberOfDependendants)

   df['deudas'] = 0
   df.deudas[(df['DebtRatio'] > 0) &   (df['DebtRatio'] <= 0.15)] = 1
   df.deudas[(df['DebtRatio'] > 0.15) &   (df['DebtRatio'] <= 0.4)] = 2
   df.deudas[(df['DebtRatio'] > 0.4) &  (df['DebtRatio'] <= 0.6)] = 3
   df.deudas[(df['DebtRatio'] > 0.6) &  (df['DebtRatio'] <= 1)] = 4
   df.deudas[(df['DebtRatio'] > 1) &  (df['DebtRatio'] <= 10)] = 5
   df.deudas[(df['DebtRatio'] > 10) &  (df['DebtRatio'] <= 100)] = 6
   df.deudas[df['DebtRatio'] > 100] = 7

   test['deudas'] = 0
   test.deudas[(test['DebtRatio'] > 0) &   (test['DebtRatio'] <= 0.15)] = 1
   test.deudas[(test['DebtRatio'] > 0.15) &   (test['DebtRatio'] <= 0.4)] = 2
   test.deudas[(test['DebtRatio'] > 0.4) &  (test['DebtRatio'] <= 0.6)] = 3
   test.deudas[(test['DebtRatio'] > 0.6) &  (test['DebtRatio'] <= 1)] = 4
   test.deudas[(test['DebtRatio'] > 1) &  (test['DebtRatio'] <= 10)] = 5
   test.deudas[(test['DebtRatio'] > 10) &  (test['DebtRatio'] <= 100)] = 6
   test.deudas[test['DebtRatio'] > 100] = 7
            
   df['prop_impago_credito'] = df['NumberOfTime60-89DaysPastDueNotWorse']/df['NumberOfOpenCreditLinesAndLoans']
   test['prop_impago_credito'] = test['NumberOfTime60-89DaysPastDueNotWorse']/test['NumberOfOpenCreditLinesAndLoans']

   df['prop_impago_hipoteca'] = df['NumberOfTime60-89DaysPastDueNotWorse']/df['NumberRealEstateLoansOrLines']
   test['prop_impago_hipoteca'] = test['NumberOfTime60-89DaysPastDueNotWorse']/test['NumberRealEstateLoansOrLines']
   
   df['prop_deuda'] = df['DebtRatio']/df['RevolvingUtilizationOfUnsecuredLines']
   test['prop_deuda'] = test['DebtRatio']/test['RevolvingUtilizationOfUnsecuredLines']

   return df, y_train, index_train, test, y_test, index_test

train_df = pd.read_csv('data/cs-training.csv')
test_df = pd.read_csv('data/cs-training.csv')

X_train, y_train, i_train, X_testm, y_test, i_test = limpia_dataset(train_df,test_df)
print('He acabado')
'''
Nombres de las variables
Index(['Unnamed: 0', 'SeriousDlqin2yrs',
       'RevolvingUtilizationOfUnsecuredLines', 'age',
       'NumberOfTime30-59DaysPastDueNotWorse', 'DebtRatio', 'MonthlyIncome',
       'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate',
       'NumberRealEstateLoansOrLines', 'NumberOfTime60-89DaysPastDueNotWorse',
       'NumberOfDependents'],
      dtype='object')
'''


