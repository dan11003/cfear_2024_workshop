import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from pandas.api.types import CategoricalDtype
import glob
import os
from tabulate import tabulate

sns.set_theme(style="ticks", color_codes=True)
sns.set(style="ticks")

def LoadData(base_dir):
    search_string="/*/*.csv"
    dfs = []
    print("Loading:")
    for filename in glob.glob(base_dir+search_string, recursive=True):
        print(filename)
        df = pd.read_csv(filename, index_col=None, header=0, skipinitialspace=True)
        dfs.append(df)
    df = pd.concat(dfs, axis=0, ignore_index=True)
    return df

def main():

    evaluation='eval_train_set'
    
    df=LoadData(evaluation)

    print("\n---------------------- EVALUATION " + evaluation +" ----------------------")
    
    datasets=df['dataset'].unique()
    for dataset in datasets:
        for seq in df[df['dataset']==dataset]['sequence'].unique():
            print(dataset + " - " + seq)
      
    print("\nCFEAR configurations: ")
    methods = df['method'].unique()
    methods.sort()
    print(methods)

	
    for dataset in datasets:
        print("\nDataset: " + dataset)
        dataset_results = []
        dataset_rates   = []        

        for method in methods:
            dfm=df[ (df["method"]==method) & (df["dataset"]==dataset)]
            g = sns.catplot(x="sequence", y="Trans.err.(%)",
                        data=dfm, saturation=.5,
                        kind="bar",  aspect=1)
            g.set_xticklabels(rotation=90)
            plt.savefig("./output/" + dataset + "_" + method + "_drift.pdf", bbox_inches='tight', format='pdf')


            #print("\t" + method)
            if(dfm.shape[0]>0):
                trans_mean = "{:2.2f}".format(dfm["Trans.err.(%)"].mean())
                rot_mean = "{:2.2f}".format(dfm["Rot.err.(deg/100m)"].mean())
                estimation_time = "{:2.2f}ms".format(dfm["full-est avg"].mean())
                filtering_time = "{:2.2f}ms".format(dfm["Filtering - filtering avg"].mean())
                total = "{:2.1f}ms".format(dfm["Filtering - filtering avg"].mean() + dfm["full-est avg"].mean())
                framerate = "{:2.1f}".format(1000.0/(dfm["Filtering - filtering avg"].mean() + dfm["full-est avg"].mean()))
                
                #print(method + ": Drift (transl[%] / rot[deg/100m]): (" + trans_mean + "/" + rot_mean + "), time per frame: " + total + ", framerate: " + framerate+ "Hz" )
                #print("\t\tMean: & " +  trans_mean + " & " + rot_mean + " & " + framerate + "\\\\") 
                result_string = "(" + trans_mean + "/" + rot_mean + ") & "
                dataset_results.append(result_string)
                dataset_rates.append(framerate)
            plt.close()
            """
            for seq in dfm['sequence'].unique():
                dfms=dfm[dfm['sequence']==seq]
                trans_mean = "{:2.2f}".format(dfms["Trans.err.(%)"].mean())
                rot_mean = "{:2.2f}".format(dfms["Rot.err.(deg/100m)"].mean())
                print("\t\t" +  seq + " & (" + trans_mean + " & " + rot_mean + ")")
                #print( seq + " & " + method + " & " + dataset + " & odom training")
            """
        # insert into latex table
        df_result = pd.DataFrame({'CFEAR Configuration': methods, 'Results (transl. err [%] / Rot. err [deg/100m]': dataset_results, 'Frame Rate [Hz]': dataset_rates})
        print(tabulate(df_result, headers='keys', tablefmt='pretty', showindex=False))
        print("\nLatex:")
        print(" &\t".join(methods) + "\\\\") 
        print(" &\t".join(dataset_results) + "\\\\")
        print(" &\t".join(dataset_rates) + "\\\\")
        print("\n\n")
        

if __name__ == "__main__":
    main()
    
