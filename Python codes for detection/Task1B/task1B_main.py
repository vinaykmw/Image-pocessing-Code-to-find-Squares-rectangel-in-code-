#classes and subclasses to import
import cv2
import numpy as np
import os
listdir='C:/Users/smart/Desktop/New Folder'
global shape
i=0
css=cls=csc=clc=csr=clr=cst=clt=cms=cmr=cmc=cmt=0
#################################################################################################
# DO NOT EDIT!!!
#################################################################################################
#subroutine to write rerults to a csv
def writecsv(color,shape,size,count):
    #open csv file in append mode
    filep = open('results1B_1228.csv','a')
    # create string data to write per image
    datastr = "," + color + "-" + shape + "-" + size + "-" + str(count)
    #write to csv
    filep.write(datastr)

def main(path):
    
    global i
    i=i+1
    global css,cls,csc,clc,csr,clr,cst,clt,cms,cmr,cmc,cmt
    ss=ls=sc=lc=sr=lr=st=lt=ms=mr=mc=mt=0
    css=cls=csc=clc=csr=clr=cst=clt=cms=cmr=cmc=cmt=0
    
        
#####################################################################################################
    #Write your code here!!!
#####################################################################################################
    def figure_size(shape,c):
        global ss,ls,sc,lc,sr,lr,st,lt,ms,mr,mc,mt
        global css,cls,csc,clc,csr,clr,cst,clt,cms,cmr,cmc,cmt
       
        area=cv2.contourArea(c)
        
    
        if(shape=="triangle"):
            if(area<=1532.0):
            #st+=1
                size="small"
                cst=cst+1
                print cst
            elif(area>=5560.5):
                #lt+=1
                size="large"
                clt=clt+1
                print clt
            else:
                #mt+=1
                size="medium"
                cmt=cmt+1
            
        if(shape=="square"):
            if(area<=2913.0):
           # ss+=1
                size="small"
                css=css+1
            elif(area>=10609.0):
                #ls+=1
                size="large"
                cls=cls+1
            else:
                #ms+=1
                size="medium"
                cms=cms+1

        if(shape=="circle"):
            if(area<=2203.5):
                #sc+=1
                size="small"
                csc=csc+1
            elif(area>=8331.0):
               # lc+=1
                size="large"
                clc=clc+1
            else:
            
                size="medium"
                cmc=cmc+1


        if(shape=="rectangle"):
            if(area<=1532.0):
            
                size="small"
                csr=csr+1
            elif(area>=20909):
        
                size="large"
                clr=clr+1
                print clr
            else:
            
                size="medium"
                cmr=cmr+1
                print cmr

        return str(size)
###############################

    npe=nc=nt=ns=nr=0
    b=[]
    c=[]
    list=[]
##### GREEN ###################################3
    print css,cls,csc,clc,csr,clr,cst,clt,cms,cmr,cmc,cmt
    image = cv2.imread(path, 1)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    final_image=image
    lower_range = np.array([50, 100, 100], dtype=np.uint8)
    upper_range = np.array([70, 255, 255], dtype=np.uint8)
    mask1 = cv2.inRange(hsv, lower_range, upper_range)
    color="green"

    black= np.zeros((image.shape[0],image.shape[1],3)) # making a black image of same size of imported image
    ret , thresh=cv2.threshold(mask1,200,255,cv2.THRESH_BINARY) # thresholding to make clear contrast between shapes and background
# we can use canny edges too

    thresh2=thresh
# making copy of thresholded image
    res,contours,hirachy=cv2.findContours(thresh2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# finding contours in image
    cv2.drawContours(black,contours,-1,(255,255,255),3)

# loop to detect the images 

    for c in contours:
    
    
        approx=cv2.approxPolyDP(c,0.03*cv2.arcLength(c,True),True)
        a=len(approx)
            #cv2.drawContours(image,[approx],0,(255,0,0),1)
            #cv2.imshow('appeoximaed ',image)
    #print approx  ## approx has coordinates of contours
    #print len(approx)


### triangle
        if a==3:
            nt=nt+1
            M=cv2.moments(c)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            shape="triangle"
            cv2.drawContours(final_image,[c],0,(0,0,0),2)
            figure_size("triangle",[c])
        
## square and rectangle
        if a==4:
        
            x,y,w,h =cv2.boundingRect(c)
       
            M=cv2.moments(c)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            if abs(w-h)<=4:
                ns=ns+1
                shape="square"
                cv2.drawContours(final_image,[c],0,(0,0,0),2)
                figure_size("square",c)
            

            else :
                shape="rectangle"
                cv2.drawContours(final_image,[c],0,(0,0,0),2)
                nr=nr+1
                figure_size("rectangle",c)
            

         
# evertything more than 6 will be take as circle
        if a>=6:
         
             M=cv2.moments(c)
             cx=int(M['m10']/M['m00'])
             cy=int(M['m01']/M['m00'])
             shape="circle"
             cv2.drawContours(final_image,[c],0,(0,0,0),2)
             nc=nc+1
             figure_size("circle",c)
         
        cv2.putText(final_image,str(color)+str('-')+str(shape),(cx-50,cy),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0),2)
        
        list.append(str('[')+shape+str('-')+color+str(']'))
    ##data writing calling write csv
    if css > 0:
        writecsv('green','square','small',css)
        print css,cls,csc,clc,csr,clr,cst,clt,cms,cmr,cmc,cmt
        
    if cls >0:
        writecsv('green','square','large',cls)
    if clc > 0:
        writecsv('green','circle','large',clc)
        print css,cls,csc,clc,csr,clr,cst,clt,cms,cmr,cmc,cmt
    if csr > 0:
        writecsv('green','rectangle','small',csr)
    if clr > 0:
        writecsv('green','rectangle','large',clr)
    if cst > 0:
        writecsv('green','triangle','small',cst)
    if clt > 0:
        writecsv('green','triangle','large',clt)
    if cms > 0:
        writecsv('green','square','medium',cms)
    if cmr > 0:
        writecsv('green','rectangle','medium',cmr)
    if cmc > 0:
        writecsv('green','circle','medim',cmc)
    if cmt > 0:
        writecsv('green','triangle','medium',cmt)
    if csc>0:
        writecsv('green','circle','small',csc)

##BLUE COLOR DETECTION WITH SHAPE    
  
    css=cls=csc=clc=csr=clr=cst=clt=cms=cmr=cmc=cmt=0
    lower_range = np.array([110, 100, 100], dtype=np.uint8)
    upper_range = np.array([130, 255, 255], dtype=np.uint8)
    mask2 = cv2.inRange(hsv, lower_range, upper_range)
    color="blue"

    black= np.zeros((image.shape[0],image.shape[1],3)) # making a black image of same size of imported image
    ret , thresh=cv2.threshold(mask2,200,255,cv2.THRESH_BINARY) # thresholding to make clear contrast between shapes and background
    # we can use canny edges too

    thresh2=thresh
# making copy of thresholded image
    res,contours,hirachy=cv2.findContours(thresh2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# finding contours in image
    cv2.drawContours(black,contours,-1,(255,255,255),3)
# draw contours in black image

# loop to detect the images 

    for c in contours:
    
        approx=cv2.approxPolyDP(c,0.03*cv2.arcLength(c,True),True)
        a=len(approx)
### triangle
        if a==3:
            nt=nt+1
            M=cv2.moments(c)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            shape="triangle"
            cv2.drawContours(final_image,[c],0,(0,0,0),2)
            figure_size("triangle",c)
        
## square and rectangle
        if a==4:
        
            x,y,w,h =cv2.boundingRect(c)
       
            M=cv2.moments(c)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            if abs(w-h)<=4:
                ns=ns+1
                shape="square"
                cv2.drawContours(final_image,[c],0,(0,0,0),2)
                figure_size("square",c)
            

            else :
                shape="rectangle"
                cv2.drawContours(final_image,[c],0,(0,0,0),2)
                nr=nr+1
                figure_size("rectangle",c)
            

         
# evertything more than 6 will be take as circle
        if a>=6:
         
             M=cv2.moments(c)
             cx=int(M['m10']/M['m00'])
             cy=int(M['m01']/M['m00'])
             shape="circle"
             cv2.drawContours(final_image,[c],0,(0,0,0),2)
             nc=nc+1
             figure_size("circle",c)
         
        cv2.putText(final_image,str(color)+str('-')+str(shape),(cx-50,cy),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0),2)
        
        list.append(str('[')+shape+str('-')+color+str(']'))

    ##data writing calling write csv
    if css > 0:
        writecsv('blue','sqare','small',css)
        print css,cls,csc,clc,csr,clr,cst,clt,cms,cmr,cmc,cmt
        
    if cls >0:
        writecsv('blue','square','large',cls)
    if clc > 0:
        writecsv('blue','circle','large',clc)
        print css,cls,csc,clc,csr,clr,cst,clt,cms,cmr,cmc,cmt
    if csr > 0:
        writecsv('blue','rectangle','small',csr)
    if clr > 0:
        writecsv('blue','rectangle','large',clr)
    if cst > 0:
        writecsv('blue','triangle','small',cst)
    if clt > 0:
        writecsv('blue','triangle','large',clt)
    if cms > 0:
        writecsv('blue','square','medium',cms)
    if cmr > 0:
        writecsv('blue','rectangle','medium',cmr)
    if cmc > 0:
        writecsv('blue','circle','medim',cmc)
    if cmt > 0:
        writecsv('blue','triangle','medium',cmt)
    if csc>0:
        writecsv('blue','circle','small',csc)
    
##RED COLOR DETECTION WITH SHAPE
    css=cls=csc=clc=csr=clr=cst=clt=cms=cmr=cmc=cmt=0
    lower_range = np.array([0, 100, 100], dtype=np.uint8)
    upper_range = np.array([10, 255, 255], dtype=np.uint8)
    mask3 = cv2.inRange(hsv, lower_range, upper_range)
    color="red"

    black= np.zeros((image.shape[0],image.shape[1],3)) # making a black image of same size of imported image
    ret , thresh=cv2.threshold(mask3,200,255,cv2.THRESH_BINARY) # thresholding to make clear contrast between shapes and background
# we can use canny edges too

    thresh2=thresh
# making copy of thresholded image


    res,contours,hirachy=cv2.findContours(thresh2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# finding contours in image
    cv2.drawContours(black,contours,-1,(255,255,255),3)

# loop to detect the images 

    for c in contours:
    
    
        approx=cv2.approxPolyDP(c,0.03*cv2.arcLength(c,True),True)
        a=len(approx)


### triangle
        if a==3:
            nt=nt+1
            M=cv2.moments(c)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            shape="triangle"
            cv2.drawContours(final_image,[c],0,(0,0,0),2)
            figure_size("triangle",c)
        
## square and rectangle
        if a==4:
        
            x,y,w,h =cv2.boundingRect(c)
       
            M=cv2.moments(c)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            if abs(w-h)<=4:
                ns=ns+1
                shape="square"
                cv2.drawContours(final_image,[c],0,(0,0,0),2)
                figure_size("square",c)
            

            else :
                shape="rectangle"
                cv2.drawContours(final_image,[c],0,(0,0,0),2)
                nr=nr+1
                figure_size("rectangle",c)
            

         
# evertything more than 6 will be take as circle
        if a>=6:
         
             M=cv2.moments(c)
             cx=int(M['m10']/M['m00'])
             cy=int(M['m01']/M['m00'])
             shape="circle"
             cv2.drawContours(final_image,[c],0,(0,0,0),2)
             nc=nc+1
             figure_size("circle",c)
         
        cv2.putText(final_image,str(color)+str('-')+str(shape),(cx-50,cy),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0),2)
        
        list.append(str('[')+shape+str('-')+color+str(']'))

    ##data writing calling write csv
    if css > 0:
        writecsv('red','sqare','small',css)
        print css,cls,csc,clc,csr,clr,cst,clt,cms,cmr,cmc,cmt
        
    if cls >0:
        writecsv('red','square','large',cls)
    if clc > 0:
        writecsv('red','circle','large',clc)
        
    if csr > 0:
        writecsv('red','rectangle','small',csr)
    if clr > 0:
        writecsv('red','rectangle','large',clr)
    if cst > 0:
        writecsv('red','triangle','small',cst)
    if clt > 0:
        writecsv('red','triangle','large',clt)
    if cms > 0:
        writecsv('red','square','medium',cms)
    if cmr > 0:
        writecsv('red','rectangle','medium',cmr)
    if cmc > 0:
        writecsv('red','circle','medim',cmc)
    if cmt > 0:
        writecsv('red','triangle','medium',cmt)
    if csc>0:
        writecsv('red','circle','small',csc)

#ORANGE COLOR DETECTION
    css=cls=csc=clc=csr=clr=cst=clt=cms=cmr=cmc=cmt=0
    lower_range = np.array([6, 100, 100], dtype=np.uint8)
    upper_range = np.array([26, 255, 255], dtype=np.uint8)
    mask2 = cv2.inRange(hsv, lower_range, upper_range)
    color="orange"

    black= np.zeros((image.shape[0],image.shape[1],3)) # making a black image of same size of imported image
    ret , thresh=cv2.threshold(mask2,200,255,cv2.THRESH_BINARY) # thresholding to make clear contrast between shapes and background
    # we can use canny edges too

    thresh2=thresh
# making copy of thresholded image
    res,contours,hirachy=cv2.findContours(thresh2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# finding contours in image
    cv2.drawContours(black,contours,-1,(255,255,255),3)
# loop to detect the images 

    for c in contours:
    
    
        approx=cv2.approxPolyDP(c,0.03*cv2.arcLength(c,True),True)
        a=len(approx)
            


### triangle
        if a==3:
            nt=nt+1
            M=cv2.moments(c)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            shape="triangle"
            cv2.drawContours(final_image,[c],0,(0,0,0),2)
            figure_size("triangle",c)
        
## square and rectangle
        if a==4:
        
            x,y,w,h =cv2.boundingRect(c)
       
            M=cv2.moments(c)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            if abs(w-h)<=4:
                ns=ns+1
                shape="square"
                cv2.drawContours(final_image,[c],0,(0,0,0),2)
                figure_size("square",c)
            

            else :
                shape="rectangle"
                cv2.drawContours(final_image,[c],0,(0,0,0),2)
                nr=nr+1
                figure_size("rectangle",c)
            

         
# evertything more than 6 will be take as circle
        if a>=6:
         
             M=cv2.moments(c)
             cx=int(M['m10']/M['m00'])
             cy=int(M['m01']/M['m00'])
             shape="circle"
             cv2.drawContours(final_image,[c],0,(0,0,0),2)
             nc=nc+1
             figure_size("circle",c)
         
        cv2.putText(final_image,str(color)+str('-')+str(shape),(cx-50,cy),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0),2)
        
        list.append(str('[')+shape+str('-')+color+str(']'))

    ##data writing calling write csv
    if css > 0:
        writecsv(color,'sqare','small',css)
        print css,cls,csc,clc,csr,clr,cst,clt,cms,cmr,cmc,cmt
        
    if cls >0:
        writecsv(color,'square','large',cls)
    if clc > 0:
        writecsv(color,'circle','large',clc)
        print css,cls,csc,clc,csr,clr,cst,clt,cms,cmr,cmc,cmt
    if csr > 0:
        writecsv(color,'rectangle','small',csr)
    if clr > 0:
        writecsv(color,'rectangle','large',clr)
    if cst > 0:
        writecsv(color,'triangle','small',cst)
    if clt > 0:
        writecsv(color,'triangle','large',clt)
    if cms > 0:
        writecsv(color,'square','medium',cms)
    if cmr > 0:
        writecsv(color,'rectangle','medium',cmr)
    if cmc > 0:
        writecsv(color,'circle','medim',cmc)
    if cmt > 0:
        writecsv(color,'triangle','medium',cmt)
    if csc>0:
        writecsv(color,'circle','small',csc)

#YELLOW COLOR DETECTION
    css=cls=csc=clc=csr=clr=cst=clt=cms=cmr=cmc=cmt=0
    lower_range = np.array([20, 100, 100], dtype=np.uint8)
    upper_range = np.array([40, 255, 255], dtype=np.uint8)
    mask2 = cv2.inRange(hsv, lower_range, upper_range)
    color="yellow"

    black= np.zeros((image.shape[0],image.shape[1],3)) # making a black image of same size of imported image
    ret , thresh=cv2.threshold(mask2,200,255,cv2.THRESH_BINARY) # thresholding to make clear contrast between shapes and background
    # we can use canny edges too

    thresh2=thresh
# making copy of thresholded image


    res,contours,hirachy=cv2.findContours(thresh2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# finding contours in image
    cv2.drawContours(black,contours,-1,(255,255,255),3)
# draw contours in black image

# loop to detect the images 

    for c in contours:
    
    
        approx=cv2.approxPolyDP(c,0.03*cv2.arcLength(c,True),True)
        a=len(approx)
            


### triangle
        if a==3:
            nt=nt+1
            M=cv2.moments(c)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            shape="triangle"
            cv2.drawContours(final_image,[c],0,(0,0,0),2)
            figure_size("triangle",c)
        
## square and rectangle
        if a==4:
        
            x,y,w,h =cv2.boundingRect(c)
       
            M=cv2.moments(c)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            if abs(w-h)<=4:
                ns=ns+1
                shape="square"
                cv2.drawContours(final_image,[c],0,(0,0,0),2)
                figure_size("square",c)
            

            else :
                shape="rectangle"
                cv2.drawContours(final_image,[c],0,(0,0,0),2)
                nr=nr+1
                figure_size("rectangle",c)
            

         
# evertything more than 6 will be take as circle
        if a>=6:
         
             M=cv2.moments(c)
             cx=int(M['m10']/M['m00'])
             cy=int(M['m01']/M['m00'])
             shape="circle"
             cv2.drawContours(final_image,[c],0,(0,0,0),2)
             nc=nc+1
             figure_size("circle",c)
         
        cv2.putText(final_image,str(color)+str('-')+str(shape),(cx-50,cy),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0),2)
        
        list.append(str('[')+shape+str('-')+color+str(']'))

    ##data writing calling write csv
    if css > 0:
        writecsv('blue','sqare','small',css)
        print css,cls,csc,clc,csr,clr,cst,clt,cms,cmr,cmc,cmt
        
    if cls >0:
        writecsv(color,'square','large',cls)
    if clc > 0:
        writecsv(color,'circle','large',clc)
        print css,cls,csc,clc,csr,clr,cst,clt,cms,cmr,cmc,cmt
    if csr > 0:
        writecsv(color,'rectangle','small',csr)
    if clr > 0:
        writecsv(color,'rectangle','large',clr)
    if cst > 0:
        writecsv(color,'triangle','small',cst)
    if clt > 0:
        writecsv(color,'triangle','large',clt)
    if cms > 0:
        writecsv(color,'square','medium',cms)
    if cmr > 0:
        writecsv(color,'rectangle','medium',cmr)
    if cmc > 0:
        writecsv(color,'circle','medim',cmc)
    if cmt > 0:
        writecsv(color,'triangle','medium',cmt)
    if csc>0:
        writecsv(color,'circle','small',csc)
    
    cv2.imshow('output'+str(path),final_image)
    cv2.imwrite('output'+str(i)+'.png',final_image) 
    cv2.waitKey(0)
    b=['output'+str(path),list]
    print b
    
    cv2.waitKey()
    cv2.destroyAllWindows()
#################################################################################################
# DO NOT EDIT!!!
#################################################################################################
#main where the path is set for the directory containing the test images
if __name__ == "__main__":
    mypath = '.'
    #getting all files in the directory
    onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if f.endswith(".png")]
    #iterate over each file in the directory
    for fp in onlyfiles[:]:
        
        #Open the csv to write in append mode
        filep = open('results1B_1228.csv','a')
        #this csv will later be used to save processed data, thus write the file name of the image 
        filep.write(fp)
        #close the file so that it can be reopened again later
        filep.close()
        #process the image
        data = main(fp)
        print data
        #open the csv
        filep = open('results1B_1228.csv','a')
        #make a newline entry so that the next image data is written on a newline
        filep.write('\n')
        
        #close the file
        filep.close()
