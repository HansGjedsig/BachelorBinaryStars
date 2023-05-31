import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import cm
import matplotlib as mlt
import pandas as pd
import statistics as stat
import scipy.stats as SciStat
from BinaryStarFunctions import*
from LoadbarFunc import progress_bar


importdata=True

plot =True

plotKickAng=False & plot #True if scatterplot of kick angles
plotHistSim=True & plot #True i histograms are wanted of simulated variables
plotHist=True & plot #True if histograms of other data i wanted 
plotConstraints=True & plot #True if distribution of constricted data is wanted
SavePlots= False & plot #True if plots wanted saved as png

name = 'SGR 0755-2933' #folder of same name is needed
plotname = 'SGR 0755-2933'

if importdata:
    df = pd.read_csv(name+'/'+name+'.csv')
    cols = df.columns[:]

file1 = open(name+'/'+name+'.txt', 'r')
Lines = file1.readlines()
for i in range(6,12):
    exec(Lines[i])
for i in range(14,19):
    exec(Lines[i])


alpha_ej = df.loc[:,cols[17]]

##################################################################################

post_SN_variable_logic = [(M_NS_max-M_NS_min)!=0,
                           (w_max-w_min)!=0,
                           (M1_max-M1_min)!=0,
                           (M2_max-M2_min)!=0,
                           (p_orb_max-p_orb_min)!=0]

post_SN_variable_all = [['Mass of newborn NS',M_NS_min, M_NS_max,'M$_{\odot}$'],
                        ['Kick velocity',w_min, w_max,'km/s'],
                        ['Mass of the progenitor star',np.round(M1_min,2), M1_max,'M$_{\odot}$'],
                        ['Mass of the companion star',M2_min, M2_max,'M$_{\odot}$'],
                        ['Pre-SN orbital period',p_orb_min, p_orb_max,'d']]

constraints_logic = [np.isfinite(v_sys_min) & np.isfinite(v_sys_max),
                     np.isfinite(misAng_min) & np.isfinite(misAng_max),
                     np.isfinite(e_min) & np.isfinite(e_max),
                     np.isfinite(p_orbf_min) & np.isfinite(p_orbf_max),
                     np.isfinite(alpha_ej_min) & np.isfinite(alpha_ej_max)]
constraints_all = [['Systemic recoil velocity',v_sys_min,v_sys_max, 'km/s'],
                   ['Misalignment angle',misAng_min,misAng_max, 'Degree'],
                   ['Eccentricity',e_min,e_max,' '],
                   ['Orbital period',p_orbf_min,p_orbf_max,'d'],
                   ['Asymmetry parameter',alpha_ej_min,alpha_ej_max,' ']]


PreHist=[df.loc[:,cols[6]],df.loc[:,cols[1]],df.loc[:,cols[4]],df.loc[:,cols[5]],df.loc[:,cols[8]]]
postHist= [df.loc[:,cols[13]],df.loc[:,cols[16]],df.loc[:,cols[10]],df.loc[:,cols[9]],df.loc[:,cols[17]]]
phi_sys, theta_sys = df.loc[:,cols[3]],df.loc[:,cols[2]]

colors=['b','g','r','c','deeppink','y','orange','purple','steelblue']
# latex text format
plt.rcParams.update({"text.usetex": True, "font.family": "Sarif"})

if plotKickAng:
    print('\n'+'Generating kick angle plot')
    fig, ax = plt.subplots(figsize=(14, 10))

    ax.scatter(phi_sys,theta_sys,s=min(10000/len(phi_sys),20))
    plt.ylim([0, 180])
    plt.xlim([0,360])
    plt.grid(which='both',linestyle=':')
    ax.tick_params(axis='both', which='major', labelsize=40)
    plt.xlabel('Kick angle $\phi$',size=40)
    plt.ylabel('Kick angle $\\theta$',size=40)
    ax.minorticks_on()
    ax.tick_params(which='minor', length=7)
    ax.tick_params(which='major', length=10)
    if SavePlots==True:
        fig.savefig(name+'/'+plotname+'KickScatter.png',bbox_inches='tight',dpi=200)
    plt.show()
k=0
if plotHistSim:
    print('\n'+'Generating histograms for simulated random values')
    for i in range(len(post_SN_variable_logic)):
        if post_SN_variable_logic[i]==True:
            fig, ax = plt.subplots(figsize=(10, 10))
            
            ax.hist(PreHist[i],min(int(np.sqrt(len(PreHist[i]))),100),edgecolor='black',color=colors[k])
            ax.tick_params(axis='both', which='major', labelsize=40)
            plt.xlabel(post_SN_variable_all[i][0]+'  ['+post_SN_variable_all[i][3]+']', size = 40)
            if post_SN_variable_all[i][3]==' ':
                plt.xlabel(post_SN_variable_all[i][0], size = 40)
            plt.ylabel('Counts', size=40)
            plt.xlim([post_SN_variable_all[i][1],post_SN_variable_all[i][2]])
            ax.minorticks_on()
            ax.tick_params(which='minor', length=7)
            ax.tick_params(which='major', length=10)
            
            plt.text(1.02, 0.95, '$\\textbf{Sim range:}$',
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.05, 0.9,str(post_SN_variable_all[i][1]) +' -- '+str(post_SN_variable_all[i][2]),
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.02, 0.8, '$\\textbf{Data range:}$',
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.05, 0.75,str(round(min(PreHist[i]),3))+"--"+str(round(max(PreHist[i]),3)),
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.02, 0.65, '$\\textbf{Mean:}$ ',
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.05, 0.6,str(round(np.mean(PreHist[i]),3)),
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.02, 0.5, '$\\textbf{Median:}$ ',
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.05, 0.45,str(round(stat.median(PreHist[i]),3)),
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.02, 0.35, '$\\textbf{Std:} $',
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.05, 0.3,str(round(stat.stdev(PreHist[i]),3)),
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.02, 0.20, '$\\textbf{Bin width:}$',
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.05, 0.15,str("{:.3E}".format((max(PreHist[i])-min(PreHist[i]))/(min(int(np.sqrt(len(PreHist[i]))),100)))),
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.4, 0.05, plotname,
                     size=28,
                 horizontalalignment='right',
                 verticalalignment='center',
                 transform = ax.transAxes)
            rect = patches.Rectangle((1, 0), 0.42, 1, linewidth=1, edgecolor='black', facecolor='none',transform = ax.transAxes,clip_on=False)
            ax.add_patch(rect)
            
            k=k+1
            if SavePlots==True:
                fig.savefig(name+'/'+plotname+'-Sim-'+post_SN_variable_all[i][0]+'.png',bbox_inches='tight',dpi=200)
            plt.show()
if plotHist:
    print('\n'+'Generating histograms of non-Constricted data')
    for i in range(len(constraints_logic)):
        if constraints_logic[i]==False:
            fig, ax = plt.subplots(figsize=(10, 10))
            if constraints_all[i][0]=='Systemic recoil velocity':
                ax.hist(postHist[i],min(int(np.sqrt(len(postHist[i]))),100),edgecolor='black',color=colors[k])
                ax.minorticks_on()
                ax.set_xlim(left=min(postHist[i])-0.01*(max(postHist[i])-min(postHist[i])))
                ax.set_xlim(right=max(postHist[i])+0.01*(max(postHist[i])-min(postHist[i])))
            
            if constraints_all[i][0]!='Systemic recoil velocity':
                ax.hist(postHist[i][postHist[i]<np.percentile(postHist[i], 95)],min(int(np.sqrt(len(postHist[i][postHist[i]<np.percentile(postHist[i], 95)]))),100),edgecolor='black',color=colors[k])
                ax.minorticks_on()
                ax.set_xlim(left=min(postHist[i][postHist[i]<np.percentile(postHist[i], 95)])-0.01*(max(postHist[i][postHist[i]<np.percentile(postHist[i], 95)])-min(postHist[i][postHist[i]<np.percentile(postHist[i], 95)])))
                ax.set_xlim(right=max(postHist[i][postHist[i]<np.percentile(postHist[i], 95)])+0.01*(max(postHist[i][postHist[i]<np.percentile(postHist[i], 95)])-min(postHist[i][postHist[i]<np.percentile(postHist[i], 95)])))
                
            ax.tick_params(axis='both', which='major', labelsize=40)
            plt.xlabel(constraints_all[i][0]+'  ['+constraints_all[i][3]+']', size = 40)
            if constraints_all[i][3]==' ':
                plt.xlabel(constraints_all[i][0], size = 40)
            plt.ylabel('Counts', size=40)
            ax.tick_params(which='minor', length=7)
            ax.tick_params(which='major', length=10)
            plt.text(1.02, 0.8, '$\\textbf{Data range:}$',
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.05, 0.75,str(round(min(postHist[i]),3))+"--"+str(round(max(postHist[i]),3)),
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.02, 0.65, '$\\textbf{Mean: }$',
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.05, 0.60,str(round(np.mean(postHist[i]),3)),
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.02, 0.50, '$\\textbf{Median:}$ ',
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.05, 0.45,str(round(stat.median(postHist[i]),3)),
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.02, 0.35, '$\\textbf{Std: }$',
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.05, 0.3,str(round(stat.stdev(postHist[i]),3)),
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.02, 0.2, '$\\textbf{Bin width:}$',
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.05, 0.15,str("{:.3E}".format((max(postHist[i])-min(postHist[i]))/(min(int(np.sqrt(len(postHist[i]))),100)))),
                     size=28,
                 horizontalalignment='left',
                 verticalalignment='center',
                 transform = ax.transAxes)
            plt.text(1.4, 0.05, plotname,
                     size=28,
                 horizontalalignment='right',
                 verticalalignment='center',
                 transform = ax.transAxes)
            rect = patches.Rectangle((1, 0), 0.42, 1, linewidth=1, edgecolor='black', facecolor='none',transform = ax.transAxes,clip_on=False)
            ax.add_patch(rect)
            k=k+1
            if SavePlots==True:
                fig.savefig(name+'/'+plotname+'-nonRan-'+constraints_all[i][0]+'.png',bbox_inches='tight',dpi=200)
            plt.show()
if plotConstraints:
    print('\n'+'Generating histograms of constricted data')
    for i in range(len(constraints_logic)):
        if constraints_logic[i]==True:
           fig, ax = plt.subplots(figsize=(10, 10))
           
           ax.hist(postHist[i],min(int(np.sqrt(len(postHist[i]))),100),edgecolor='black',color=colors[k])
           ax.tick_params(axis='both', which='major', labelsize=40)
           plt.xlabel(constraints_all[i][0]+'  ['+constraints_all[i][3]+']', size = 40)
           if constraints_all[i][3]==' ':
               plt.xlabel(constraints_all[i][0], size = 40)
           plt.ylabel('Counts', size=40)
           plt.xlim([constraints_all[i][1],constraints_all[i][2]])
           ax.minorticks_on()
           ax.tick_params(which='minor', length=7)
           ax.tick_params(which='major', length=10)
           plt.text(1.02, 0.8, '$\\textbf{Data range:}$',
                    size=28,
                horizontalalignment='left',
                verticalalignment='center',
                transform = ax.transAxes)
           plt.text(1.05, 0.75,str(round(min(postHist[i]),3))+"--"+str(round(max(postHist[i]),3)),
                    size=28,
                horizontalalignment='left',
                verticalalignment='center',
                transform = ax.transAxes)
           plt.text(1.02, 0.65, '$\\textbf{Mean: }$',
                    size=28,
                horizontalalignment='left',
                verticalalignment='center',
                transform = ax.transAxes)
           plt.text(1.05, 0.60,str(round(np.mean(postHist[i]),3)),
                    size=28,
                horizontalalignment='left',
                verticalalignment='center',
                transform = ax.transAxes)
           plt.text(1.02, 0.50, '$\\textbf{Median:}$ ',
                    size=28,
                horizontalalignment='left',
                verticalalignment='center',
                transform = ax.transAxes)
           plt.text(1.05, 0.45,str(round(stat.median(postHist[i]),3)),
                    size=28,
                horizontalalignment='left',
                verticalalignment='center',
                transform = ax.transAxes)
           plt.text(1.02, 0.35, '$\\textbf{Std: }$',
                    size=28,
                horizontalalignment='left',
                verticalalignment='center',
                transform = ax.transAxes)
           plt.text(1.05, 0.3,str(round(stat.stdev(postHist[i]),3)),
                    size=28,
                horizontalalignment='left',
                verticalalignment='center',
                transform = ax.transAxes)
           plt.text(1.02, 0.2, '$\\textbf{Bin width:}$',
                    size=28,
                horizontalalignment='left',
                verticalalignment='center',
                transform = ax.transAxes)
           plt.text(1.05, 0.15,str("{:.3E}".format((max(postHist[i])-min(postHist[i]))/(min(int(np.sqrt(len(postHist[i]))),100)))),
                    size=28,
                horizontalalignment='left',
                verticalalignment='center',
                transform = ax.transAxes)
           plt.text(1.4, 0.05, plotname,
                    size=28,
                horizontalalignment='right',
                verticalalignment='center',
                transform = ax.transAxes)
           rect = patches.Rectangle((1, 0), 0.42, 1, linewidth=1, edgecolor='black', facecolor='none',transform = ax.transAxes,clip_on=False)
           ax.add_patch(rect)
           k=k+1
           if SavePlots==True:
               fig.savefig(name+'/'+plotname+'-Constrict-'+constraints_all[i][0]+'.png',bbox_inches='tight',dpi=200)
           plt.show()

print('\n'+'Done! YaY')