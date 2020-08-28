# suraj_vel_plt.py redshift(z) lower_limit(X1) upper_limit(X2) 'input_name' numner_of_columns_to_plot(c1) 'output_name'
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['text.usetex'] = True
lambda_rest=[933.376, 944.525, 963.9903, 976.4481, 977.0201, 989.799, 1004.6676, 1012.495, 1020.6989, 1025.7616, 1025.9681, 1026.1134, 1031.9265, 1036.3367, 1037.018, 1037.6155, \
       1039.2304, 1048.2199, 1062.671, 1063.1764, 1066.6598, 1071.0358, 1081.8748, 1083.9937, 1088.0589, 1096.8769, 1112.0480, 1117.9774, 1122.524, 1125.4477, 1128.0078, 1129.195, 1129.3175, \
       1143.2260, 1144.9379, 1152.8180, 1163.326, 1164.208, 1164.272, 1164.8672, 1188.7742, 1190.203, 1190.4158, 1193.2897, 1194.5002, 1197.184, 1197.3938, 1199.391, \
       1199.5496, 1200.2233, 1200.7098, 1201.118, 1206.500, 1215.6700, 1235.8380, 1237.0589, 1238.821, 1239.9253, 1240.3947, 1242.804, 1250.578, 1253.805, 1259.518, 1260.4221, \
       1260.533, 1264.7377, 1265.0020, 1277.2452, 1277.2827, 1295.6531, 1296.1739, 1298.697, 1301.8743, 1302.1685, 1304.3702, 1304.8576, 1309.2757, 1317.217, 1328.8333, \
       1329.0849, 1334.5323, 1334.8132, 1335.7077, 1347.2396, 1355.5977, 1358.7730, 1362.460, 1367.9509, 1370.132, 1393.7602, 1402.7729, 1414.402, 1466.2110, 1526.7070, 1533.4316, 1548.204, \
       1550.781, 1560.3092, 1560.6820, 1574.5508, 1602.4863, 1608.4511, 1611.2005, 1656.2672, 1656.9284, 1670.7886, 1709.6042, 1741.5531, 1751.9157, 1808.0129, 1816.9285, 1854.7184, \
       1862.7910, 1910.6123, 1910.9538, 2026.1370, 2026.269, 2026.4122, 2026.4768, 2056.2569, 2059.4756, 2062.2361, 2062.6604, 2066.1640, 2167.4534, 2249.8768, 2260.7805, \
       2264.1647, 2290.6934, 2311.6723, 2320.7468, 2344.2139, 2346.2616, 2367.7750, 2374.4612, 2382.7652, 2484.0209, 2576.877, 2586.6500, 2594.499, 2600.1729, 2606.462, 2683.887, \
       2796.3543, 2803.5315, 2852.9631, 2853.649, 3066.3467, 3072.9704, 3229.1899, 3242.9184, 3248.4739, 3274.8980, 3302.3641, 3302.3703, 3302.9738, \
       3302.9804, 3303.319, 3303.929, 3342.834, 3370.5336, 3384.7304, 3392.0165, 3441.5918,5889.9509,7664.911]

line_ID=['SVI933', 'SVI945', 'NI964', 'OI976', 'CIII977', 'NIII990', 'ClI1005', 'SIII1012', 'SiII1021', 'OI1025.8', 'MgII1026', 'MgII1026p1', 'OVI1032', 'CII1036', 'CII*1037', 'OVI1038', \
   'OI1039', 'ArI1048', 'SIV1063', 'FeII1063', 'ArI1067', 'ClII1071', 'FeII1082', 'NII1084', 'ClI1088', 'FeII1097', 'FeII1112', 'PV1118', 'FeIII1123', 'FeII1125', 'PV1128', 'CI1129.2', 'CI1129.3', \
   'FeII1143', 'FeII1145', 'PII1153', 'MnII1163', 'MnII1164.2', 'GeII1164.3', 'KrI1165', 'ClI1189', 'SIII1190.2', 'SiII1190.4', 'SiII1193', 'SiII*1195', 'MnII1197.2', 'SiII*1197.4', 'MnII1199.4', \
   'NI1199.6', 'NI1200.2', 'NI1200.8', 'MnII1201', 'SiIII1207', 'HI1216', 'KrI1236', 'GeII1237', 'NV1239', 'MgII1239.9', 'MgII1240.4', 'NV1243', 'SII1251', 'SII1254', 'SII1260', 'SiII1260.4', \
   'FeII1260.5', 'SiII*1264.7', 'SiII*1265', 'CI1277.2', 'CI*1277.3', 'SI1295.7', 'SI1296.2', 'TiIII1299', 'PII1301.9', 'OI1302.2', 'SiII1304.4', 'OI*1304.9', 'SiII*1309', 'NiII1317', 'CI1328.8', \
   'CI*1329.1', 'CII1334.5', 'PIII1334.8', 'CII*1336', 'ClI1347','OI1356', 'CuII1359', 'BII1362', 'CuII1368', 'NiII1370', 'SiIV1394', 'SiIV1403', 'GaII1414', 'CoII1466', 'SiII1527', 'SiII*1533', 'CIV1548', \
   'CIV1551', 'CI1560.3', 'CI*1560.7', 'CoII1575', 'GeII1602', 'FeII1608', 'FeII1611', 'CI*1656.3', 'CI1657', 'AlII1671', 'NiII1710', 'NiII1742', 'NiII1752', 'SiII1808', 'SiII*1816.9', 'AlIII1855', \
   'AlIII1863', 'TiII1910.6', 'TiII1911', 'ZnII2026.1', 'CrII2026.3', 'CoII2026.4', 'MgI2026.5', 'CrII2056', 'CoII2059', 'CrII2062.2', 'ZnII2062.7', 'CrII2066', 'FeI2167', 'FeII2250', 'FeII2261', \
   'AlI2264', 'NiI2291', 'NiI2312', 'NiI2321', 'FeII2344', 'NiI2346', 'AlI2368', 'FeII2374', 'FeII2383', 'FeI2484', 'MnII2577', 'FeII2587', 'MnII2595', 'FeII2600', 'MnII2607', 'VII2684', \
   'MgII2796', 'MgII2804', 'MgI2853', 'NaI2853.7', 'TiII3066', 'TiII3073', 'TiII3229', 'TiII3242', 'CuI3248', 'CuI3274', 'NaI3302.36', 'NaI3302.37', 'NaI3302.97', \
  'NaI3302.98', 'NaI3303.3', 'NaI3303.9', 'TiI3342', 'NiI3370', 'TiII3384', 'NiI3392', 'FeI3441', 'NaI5889.9509(gal)','KI7664.911(gal)']

lambda_observed=[]
import sys
if len(sys.argv) == 7:
    z=float(sys.argv[1])
    X1=int(sys.argv[2])
    X2=int(sys.argv[3])
    input_name=sys.argv[4]
    c1=int(sys.argv[5])
    output_name=sys.argv[6]
#z=input("Enter the redshift of the absorber, z :")
#[X1,X2]=input("Give the velocity range:")
#c1=input("Number of Columns to plot:")
#output_name=input("Give the output name to save your plot:")
n=len(lambda_rest)
for m in range(n):
   s=(1+z)*lambda_rest[m]
   lambda_observed.append(s)
import os
#from urlparse import urlparse
#import glob
#list=[]
#for fo in glob.glob('*.txt'):
#    list.append(fo)
with open(input_name) as fl:
    lines = fl.readlines()
list = [line.rstrip('\n') for line in open(input_name)]
print list
n=len(list)
print(n)
#print len(line_ID)
line_ID_1=[]
for l in line_ID:
     r=l.replace(".", "p")+".txt"
     line_ID_1.append(r)
#print line_ID_1 
#print len(line_ID_1)
k=0
while k<n:
  for fn in list:
    for j in line_ID_1:
       if fn == j:
            print ('got text file', fn)
            data=np.loadtxt(fn,unpack=True)
            xk=data[0]
            yk=data[1] 
            y_err=data[2]
            y_fit=data[3]
            xc = lambda_observed[line_ID_1.index(j)]
            print ('at wavelength', xc)
            vel_plt=[]         
            for i in xk:
              p=((i-xc)/xc)*300000
              vel_plt.append(p) 
            if c1==2:   
               ax=plt.subplot(n/2,c1,k+1)
            if c1==1:   
               ax=plt.subplot(n,c1,k+1)   
            #ax.plot(vel_plt,yk,'g',label=os.path.splitext(fn)[0].replace("p","."))
            ax.step(vel_plt,yk,linewidth=0.8,color='k')
            ax.plot([],[],' ',label=os.path.splitext(fn)[0].replace("p","."),color='r')
            ax.plot(vel_plt,y_fit,linewidth=0.5,color='b')
            plt.xlim(X1,X2)
            if min(yk)>0.5:
                plt.ylim(0.5, 1.5)
                ax.plot(vel_plt,y_err+0.5,linewidth=0.6,color='g',linestyle='--')
            else:
                plt.ylim(0, 1.5)
                ax.plot(vel_plt,y_err,linewidth=0.6,color='g',linestyle='--')
            plt.axhline(y=1.0, linewidth=0.6, color = 'r', linestyle='--')
            plt.axvline(x=0.0, linewidth=0.5, color='c', linestyle='--')
            #xcoords = [0,-2370, -1570,-1240,-1030,-730,-475,-530,-140,-265,150,780,1500]
            #for xi in xcoords:
            # plt.axvline(x=xi, linewidth=0.5, color='g', linestyle='--')
            plt.locator_params(axis='y', nbins=4)
            plt.legend(frameon=False)
            plt.subplots_adjust(wspace=0.16,hspace=0.16)
            vel_plt = np.array(vel_plt)
            yk=np.array(yk)
            leg = plt.legend(framealpha = 0, loc = 'upper left')
            for text in leg.get_texts():
                plt.setp(text, color = 'r')
            #ax.set_aspect('auto')
# fill the region between two radial velocities for the corresponding ion. Can be used multiple times for multiple regions and mutiple ions.            
            if list[k] == 'OI1302p2.txt':
                     ax.fill_between(vel_plt, 1, yk, where=(vel_plt<400) & (vel_plt>25),interpolate=True, facecolor='gray')
                     ax.fill_between(vel_plt, 1, yk, where=(vel_plt<-25) & (vel_plt>-300),interpolate=True, facecolor='gray')
            if list[k] == 'SII1260.txt':
                     ax.fill_between(vel_plt, 1, yk, where=(vel_plt<-20) & (vel_plt>-300),interpolate=True, facecolor='gray')
                     ax.fill_between(vel_plt, 1, yk, where=(vel_plt<400) & (vel_plt>20),interpolate=True, facecolor='gray')
            if list[k] == 'SII1254.txt':
                     ax.fill_between(vel_plt, 1, yk, where=(vel_plt<-20) & (vel_plt>-200),interpolate=True, facecolor='gray')
                     ax.fill_between(vel_plt, 1, yk, where=(vel_plt<150) & (vel_plt>20),interpolate=True, facecolor='gray')
# remove all the tick labels but the last one 
            if c1==2:
              if k<(n-2):
                 ax.axes.xaxis.set_ticklabels([])
            if c1==1:
              if k<(n-1):
                 ax.axes.xaxis.set_ticklabels([])    
            if c1==2:   
               if k>(n-3):   
                  ax.set_xlabel(r"Radial Velocity (km s$^{-1}$)",fontsize=16)
            k=k+1
            if fn=='SiII1527.txt':
                xcoords = [5549.30114,5550.23519,5547.23409,5552.25357,5553.03596,5554.78980,5554.09697,5547.70591,5551.33168]
                for xi in xcoords:
                  plt.axvline(x=(xi-xc)/xc*300000, linewidth=0.5, color='g', linestyle='--')
            if fn=='AlII1671.txt':
                xcoords = [6073.01152,6074.03372,6070.74940,6076.24259,6077.09881,6079.01817,6078.25995,6071.26575,6075.23370]
                for xi in xcoords:
                  plt.axvline(x=(xi-xc)/xc*300000, linewidth=0.5, color='g', linestyle='--')
            if fn=='OI1302p2.txt':
                xcoords = [4733.14476]
                for xi in xcoords:
                  plt.axvline(x=(xi-xc)/xc*300000, linewidth=0.5, color='g', linestyle='--')
            if fn=='SII1260.txt':
                xcoords = [4578.12161]
                for xi in xcoords:
                  plt.axvline(x=(xi-xc)/xc*300000, linewidth=0.5, color='g', linestyle='--')
            
            if fn=='FeII1608.txt':
                xcoords = [5846.42518,5849.53570]
                for xi in xcoords:
                    plt.axvline(x=(xi-xc)/xc*300000, linewidth=0.5, color='g', linestyle='--')
            if fn=='FeII2374.txt':
                xcoords = [8630.72978,8635.32166]
                for xi in xcoords:
                    plt.axvline(x=(xi-xc)/xc*300000, linewidth=0.5, color='g', linestyle='--')
            if fn=='ZnII2026p1.txt':
                xcoords = [7364.63840,7368.55667]
                for xi in xcoords:
                    plt.axvline(x=(xi-xc)/xc*300000, linewidth=0.5, color='g', linestyle='--')
            if fn=='ZnII2062p7.txt':
                xcoords = [7497.39415,7501.38304]
                for xi in xcoords:
                    plt.axvline(x=(xi-xc)/xc*300000, linewidth=0.5, color='g', linestyle='--')

            if fn=='SII1260.txt':
                          plt.ylim(0.5, 1.25)
                          ax.plot(vel_plt,y_err+0.5,linewidth=0.6,color='g',linestyle='--')
            if fn=='ZnII2026p1.txt':
                          plt.ylim(0.5, 1.25)
                          ax.plot(vel_plt,y_err+0.5,linewidth=0.6,color='g',linestyle='--')
            if fn=='ZnII2062p7.txt':
                          plt.ylim(0.5, 1.25)
                          ax.plot(vel_plt,y_err+0.5,linewidth=0.6,color='g',linestyle='--')


            #ax.set_ylabel(r"Normalized Flux",fontsize=18)
#plt.figure(figsize = (1,1))
if c1==2:
   ax.text(3*X1-250, (1.5)*n/5, r"Normalized Flux", va='center', rotation='vertical',fontsize=16)
if c1==1:
   ax.text(X1-90, (1.5)*n/3, r"Normalized Flux", va='center', rotation='vertical',fontsize=16)
if c1==1:
   ax.set_xlabel(r"Radial Velocity (km s$^{-1}$)",fontsize=16)
plt.savefig(output_name, format='eps', dpi=1000)
plt.show()