import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import csv
import math
from pandas.api.types import CategoricalDtype
import glob
import os

sns.set_theme(style="ticks", color_codes=True)
sns.set(style="ticks")

def LoadData(base_dir):
    search_string="/*/*.csv"
    dfs = []
    for filename in glob.glob(base_dir+search_string, recursive=True):
        print(filename)
        df = pd.read_csv(filename, index_col=None, header=0, skipinitialspace=True)
        dfs.append(df)
    df = pd.concat(dfs, axis=0, ignore_index=True)
    return df

def main():

    evaluation='training_verification'
    df=LoadData(evaluation)

    print("---------------------- EVALUATION " + evaluation +" ----------------------")
    methods=df['method'].unique()
    print("Evaluation of the following methods: ")
    print(methods)
    print("\nSequences: ")
    print(df['sequence'].unique())
    print("-----------------------------------------------\n")

    print("-----------------RESULTS (Latex) -----------------")
    print("Method & Tuned & Seq.  & Transl (\%) & Rot &   Rate [Hz]  \\\\")
    for method in methods:
        dfm=df[df["method"]==method]
        g = sns.catplot(x="sequence", y="Trans.err.(%)",
                    data=dfm, saturation=.5,
                    kind="bar",  aspect=1)
        g.set_xticklabels(rotation=90)
        #plt.show()
        #save figure
        plt.savefig(method+"_drift.pdf", bbox_inches='tight', format='pdf')


        if(dfm.shape[0]>0):
            trans_mean = "{:2.2f}".format(dfm["Trans.err.(%)"].mean())
            rot_mean = "{:2.2f}".format(dfm["Rot.err.(deg/100m)"].mean())
            estimation_time = "{:2.2f}ms".format(dfm["full-est avg"].mean())
            filtering_time = "{:2.2f}ms".format(dfm["Filtering - filtering avg"].mean())
            total = "{:2.1f}ms".format(dfm["Filtering - filtering avg"].mean() + dfm["full-est avg"].mean())
            framerate = "{:2.1f}".format(1000.0/(dfm["Filtering - filtering avg"].mean() + dfm["full-est avg"].mean()))
            #print(method + ": Drift (transl[%] / rot[deg/100m]): (" + trans_mean + "/" + rot_mean + "), time per frame: " + total + ", framerate: " + framerate+ "Hz" )
            print(method + " & Oxford & odom training & " + trans_mean + " & " + rot_mean + " & " + framerate + "\\\\") 
    print("\n-----------------------------------------------\n")

if __name__ == "__main__":
    main()
    
