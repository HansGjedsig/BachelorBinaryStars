import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import cm
import matplotlib.ticker as ticker
import matplotlib as mlt
import pandas as pd
import statistics as stat
from BinaryStarFunctions import*
from LoadbarFunc import progress_bar


importdata=True
SavePlots=True

name = 'SGR 0755-2933-test' #folder of same name is needed
plotname = 'SGR 0755-2933-test'

if importdata:
    df = pd.read_csv(name+'/'+name+'.csv')
    cols = df.columns[:]

file1 = open(name+'/'+name+'.txt', 'r')
Lines = file1.readlines()
for i in range(6,12):
    exec(Lines[i])
for i in range(14,18):
    exec(Lines[i])
    
phi_sys, theta_sys = df.loc[:,cols[3]],df.loc[:,cols[2]]

crit_ang =df.loc[:,cols[15]]
e = df.loc[:,cols[10]]
pf = df.loc[:,cols[9]]
ratio = df.loc[:,cols[1]]/df.loc[:,cols[14]]
test2 =ratio[crit_ang==-1]
MASS = df.loc[:,cols[4]]


m_prog = 5
m_c = 18
m_ns = 1.44
qf = m_c/m_ns
qi = m_c/m_prog
deltaM = m_prog-m_ns
mi = m_prog+m_c

r_ratio = (m_ns/m_prog)**(2/3)*(0.6*qf**(2/3)+np.log(1+qf**(1/3)))/(0.6*qi**(2/3)+np.log(1+qi**(1/3)))

x = np.linspace(0, 2,1000)
thetay = np.arccos(((1-deltaM/mi)/r_ratio-1+2*deltaM/mi+x**2)/(-2*x))*180/np.pi

plt.rcParams.update({"text.usetex": True, "font.family": "Sarif"})
fig, ax = plt.subplots(figsize=(14, 10))
var=0.1
im=ax.hexbin(phi_sys,theta_sys,gridsize=(360,180),mincnt=1,cmap='turbo',vmax=79)

test = im.get_array()
print(max(test))

cbar = fig.colorbar(im)
cbar.ax.tick_params(labelsize=40)
ax.yaxis.set_major_locator(ticker.MultipleLocator(30))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.xaxis.set_major_locator(ticker.MultipleLocator(90))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))

deltaMmin = 1.55-1.44
Mmin = 1.55+18
deltaMax = 5-1.44
Mmax = 5+18


cbar.set_label(label='Counts',size=40)
plt.ylim([0, 180])
plt.xlim([0,360])
plt.grid(which='both',linestyle=':')
ax.tick_params(axis='both', which='major', labelsize=40)
plt.xlabel('Kick angle $\\varphi$',size=40)
plt.ylabel('Kick angle $\\theta$',size=40)
ax.tick_params(which='minor', length=7)
ax.tick_params(which='major', length=10)
plt.show()
if SavePlots==True:
    fig.savefig(name+'/'+plotname+'KickScatterHeat.png',bbox_inches='tight',dpi=200)

fig, ax = plt.subplots(figsize=(14, 10))
var=0.1
im=ax.hexbin(phi_sys[crit_ang==-1],theta_sys[crit_ang==-1],gridsize=(360,180),mincnt=1,cmap='turbo',vmax=79)
#plt.plot(x, thetay,color='black')
cbar = fig.colorbar(im)
cbar.ax.tick_params(labelsize=40)
ax.yaxis.set_major_locator(ticker.MultipleLocator(30))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.xaxis.set_major_locator(ticker.MultipleLocator(90))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))

deltaMmin = 1.55-1.44
Mmin = 1.55+18
deltaMax = 5-1.44
Mmax = 5+18


cbar.set_label(label='Counts',size=40)
plt.ylim([0, 180])
plt.xlim([0,360])
plt.grid(which='both',linestyle=':')
ax.tick_params(axis='both', which='major', labelsize=40)
plt.xlabel('Kick angle $\\varphi$',size=40)
plt.ylabel('Kick angle $\\theta$',size=40)
ax.tick_params(which='minor', length=7)
ax.tick_params(which='major', length=10)
plt.show()
if SavePlots==True:
    fig.savefig(name+'/'+plotname+'KickScatterHeatMinusCrit.png',bbox_inches='tight',dpi=200)

fig, ax = plt.subplots(figsize=(14, 10))
var=0.1
im=ax.hexbin(phi_sys[crit_ang>-1],theta_sys[crit_ang>-1],gridsize=(360,180),mincnt=1,cmap='turbo',vmax=79)
#plt.plot(x, thetay,color='black')
cbar = fig.colorbar(im)
cbar.ax.tick_params(labelsize=40)
ax.yaxis.set_major_locator(ticker.MultipleLocator(30))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.xaxis.set_major_locator(ticker.MultipleLocator(90))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))

deltaMmin = 1.55-1.44
Mmin = 1.55+18
deltaMax = 5-1.44
Mmax = 5+18


cbar.set_label(label='Counts',size=40)
plt.ylim([0, 180])
plt.xlim([0,360])
plt.grid(which='both',linestyle=':')
ax.tick_params(axis='both', which='major', labelsize=40)
plt.xlabel('Kick angle $\\varphi$',size=40)
plt.ylabel('Kick angle $\\theta$',size=40)
ax.tick_params(which='minor', length=7)
ax.tick_params(which='major', length=10)
plt.show()
if SavePlots==True:
    fig.savefig(name+'/'+plotname+'KickScatterHeatPlusCrit.png',bbox_inches='tight',dpi=200)










