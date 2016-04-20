# -*- coding: utf-8 -*-
"""

@author: Vishal Narote
"""
'''
import selenium
import time

from selenium import webdriver
driver = webdriver.Firefox() ## Opening Firefox
driver.get("http://cpcb.nic.in/agra_data.php") ## Opening website
time.sleep(10) ## Allowing time to open
driver.find_element_by_xpath("""/html/body/table/tbody/tr[9]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[3]/td/table/tbody/tr[12]/td[1]/div/a""").click()
posts = driver.find_element_by_xpath("""/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[51]""")
print posts  ## Copy data value

driver.find_elements_by_id("download").click() ##Downloads Pdf data file'''
 
#    
#from cStringIO import StringIO
#from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
#from pdfminer.converter import TextConverter
#from pdfminer.layout import LAParams
#from pdfminer.pdfpage import PDFPage
#
#def convert(fname, pages=None):
#    if not pages:
#        pagenums = set()
#    else:
#        pagenums = set(pages)
#
#    output = StringIO()
#    manager = PDFResourceManager()
#    converter = TextConverter(manager, output, laparams=LAParams())
#    interpreter = PDFPageInterpreter(manager, converter)
#
#    infile = file(fname, 'rb')
#    for page in PDFPage.get_pages(infile, pagenums):
#        interpreter.process_page(page)
#    infile.close()
#    converter.close()
#    text = output.getvalue()
#    output.close
#    return text 
#    

import numpy
import pylab

import pylab
import numpy as np
import matplotlib.pyplot as plt
import scipy



B=0
SO2=range(4)
NO2=range(4)
RSPM=range(4)
SPM=range(4)

#Taj Mahal
SO2[0]=np.array([0,4,0, 0,05,8,4,0,0,0,0 ,6,4,0,4,0,0,0, 3,0,0,0,4,4,3 ,2 ,0,0,06,5,6,6])
NO2[0]=np.array([33,23,13,15 ,18,16,12,20,18,24,20 ,0,11,20,24,B,16,11,10 ,11,19,0,0,28,14 ,15 ,11,20,15,18,15,34])
RSPM[0]=np.array([225,225,245,225,200 ,128,95,109,134,146,177,130 ,93,111,125,145,171,138,139 ,140,167,148,158,151,140 ,130 ,112,130,156,184,196,260])
SPM[0]=np.array([416,386,465, 430,318,176,197,269,275,306,200 ,235,226,282,251,276,331,275 ,286,356,324,452,285,300 ,245 ,315,235,313,362,372,390,391])

#Itmad-ud-daulah and March 2016
SO2[1]=np.array([0,0 ,0 ,8 ,0,9,8 ,0 ,0,0, 0,0,0 ,0 ,0,0 ,4 ,0,5 ,7 ,0,0 ,0 ,4,5 ,5 ,5,0 ,0 ,4,4 ,4 ])
NO2[1]=np.array([41,44,45 ,51 ,28 ,32,15 ,16 ,17,13 ,33 ,14,36 ,24 ,20,21 ,50 ,24,23 ,22 ,20,31 ,33 ,40,45 ,17 ,27,32 ,19 ,20,22 ,28 ])
RSPM[1]=np.array([261,262,369 ,258 , 147,154,103 , 111,144,175 ,188 ,131,198 ,138 ,150,149 ,164 ,189, 143, 187,188,165 ,144 ,239,135 ,156 ,134,178 ,154 ,298, 154, 262])
SPM[1]=np.array([575, 265,656 ,351 ,390,351 ,546 ,263,326 ,325 ,338,485 ,354 ,353,555 ,532 ,381,355 ,354 ,409, 154, 431,367,354 ,304,303 ,329,135 ,315 ,408, 513,454 ])

#Rambagh
SO2[2]=np.array([6,5 ,4,6 ,1 ,4, 5, 4,0,7 ,7 ,0,0 ,0 ,7,0 ,0 ,0,0 ,0,4, 10,9 ,8 ,5, 4,3 ,0,7,4 ,4 ,10])
NO2[2]=np.array([42,41,54 ,42,21 ,29,65 ,84 ,22 ,54 ,35,32 , 84,24,65 ,25 ,23,65 ,46 ,21, 54, 44,11,21 ,45 ,65 ,21 ,41 ,16,54 ,84 ,52])
RSPM[2]=np.array([322,388,322,268 ,287,178 ,165 ,119,168 ,265 ,191,199 ,187 ,169,178 ,198 ,213,256 ,265 ,210,165 ,125 ,266,245 ,254 ,244 , 285, 265,193, 164, 154,160])
SPM[2]=np.array([484 ,523,468 ,655,648 ,546 ,245, 684,684 ,396,268 ,685 ,258, 844,648 ,310,484 ,245 ,316,245, 285,645 ,430,615 ,645 ,645, 648,267 ,288 ,294,268 ,444])

#Nunhai
SO2[3]=np.array([0,0 ,11,10 ,6 ,0,5, 7,8 ,6,8 , 8,9, 0, 0,0,0 , 0,0,6,3 ,5, 6,6 ,4, B,8 ,0,0 ,9 ,8,9 ])
NO2[3]=np.array([42, 45 ,55 ,50,23 ,55 ,37,54 ,58 ,45, 32,62 ,15,23 ,21 ,41,35 ,51 ,46,32 ,25 ,38,24 ,32 ,25 ,35 ,40 ,28,12 ,24 ,30,25 ])
RSPM[3]=np.array([135,352 ,135 ,249,315 ,155 ,98,352 ,315 ,179,161 ,153 ,132,152 ,222 ,227,178 ,146 ,149,146 ,164 ,231,132 ,151 ,151 ,135 ,165 ,171, 152 , 261,267 , 261])
SPM[3]=np.array([ 651,616,529,651 ,615 ,240,511 ,846 ,489,615 , 654,476,651 , 351,366, 216,645 ,333,845 ,765 ,769, 765, 618,612 , 761, 351,341,387,515 , 351,684,513])

"""
for i in range(4):
    SO2[i]=SO2[i]
    NO2[i]=NO2[i]
    RSPM[i]=RSPM[i]
    SPM[i]=SPM[i]
"""
#Making 4 by 4 array/matrix
arr=np.array([[SO2[0],NO2[0],RSPM[0],SPM[0]],[SO2[1],NO2[1],RSPM[1],SPM[1]],[SO2[2],NO2[2],RSPM[2],SPM[2]],[SO2[3],NO2[3],RSPM[3],SPM[3]]])
pylab.figure(2) 

pylab.plot(range(32),RSPM[0])
for i in range(32):
    pylab.figure(3)
    
### Selecting type of Plot    
    img=arr[:,:,i]
    imgplot=pylab.imshow(img,cmap='Paired',interpolation="kaiser")
    
### Dividing the Chart Area for Locations and Pollutants    
    plt.axvline(x=2.5,color='white')
    plt.axvline(x=0.5,color='white')
    plt.axvline(x=1.5,color='white')
    plt.axhline(y=0.5,color="white")
    plt.axhline(y=1.5,color="white")
    plt.axhline(y=2.5,color="white")
    
    pylab.xticks([0,1,2,3],["NO2","SO2","RSPM","SPM"])                   #X axis labels
    pylab.yticks([0,1,2,3],["Taj Mahal","Itmad","Rambagh","Nunhari"])    #Y axis labels
    if i==0:
        cbar=pylab.colorbar(imgplot,orientation='horizontal')
        cbar.set_label("Concentration in PPM")                      #Colourbar Label
    pylab.pause(2)


    
pylab.colorbar(imgplot,orientation='horizontal',label="In PPM")
pylab.show()

#days=range(32)
#print len(SO2)
#pylab.plot(days,SO2)
#pylab.show()
#import visual, math
#ball1 = visual.sphere()
#ball2=visual.sphere(pos=[0,-4,0])
#box = visual.box(pos=[0,-1, 0], width=2, length=2, height=0.5)
#box2=visual.box(pos=[0, -4, 0], width =2, length=2,height=0.5)
#trace1 = visual.curve(radius=0.2, color=visual.color.green)
#trace2 = visual.curve(radius=0.2, color=visual.color.blue)
#for i in  range(32):
#    t = i
#    y1 = SO2[i]
#    y2 = NO2[i]
#    #update  the  ball's position
#    ball1.pos = [t, y1, 0]
#    ball2.pos = [t, y2, 0]
#    trace1.append(ball1.pos)
#    trace2.append(ball2.pos)
#    #ensure  we have  only 24  frames  per  second
#    visual.rate(10)
