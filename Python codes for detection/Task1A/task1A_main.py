#classes and subclasses to import
import cv2
import numpy as np
import os
listdir='C:/Users/smart/Desktop/New Folder'
global shape
i=0
#################################################################################################
# DO NOT EDIT!!!
#################################################################################################
#subroutine to write rerults to a csv
def writecsv(color,shape):
    #open csv file in append mode
    filep = open('results1A_1228.csv','a')
    # create string data to write per image
    datastr = "," + color + "-" + shape
    #write to csv
    filep.write(datastr)

def main(path):
#####################################################################################################
    #Write your code here!!!
#####################################################################################################
    global i
    i=i+1
    npe=nc=nt=ns=nr=0
    b=[]
    c=[]

    
    #for i in range(1,6):
    

        

    list=[]

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
# draw contours in black image



# biinding rectangle
###################
#for c in contours:
#    x,y,w,h =cv2.boundingRect(c) # gives initial coordinates and lwngth and wif=dth of rectangle
#
#    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)
#    cv2.imshow('bounding rectangle',image)
#################



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
            

            else :
                shape="rectangle"
                cv2.drawContours(final_image,[c],0,(0,0,0),2)
                nr=nr+1
            
#pentagon
        if a==5:
         
             M=cv2.moments(c)
             cx=int(M['m10']/M['m00'])
             cy=int(M['m01']/M['m00'])
             shape="pentagon"
             cv2.drawContours(final_image,[c],0,(0,0,0),2)
             npe=npe+1
         
# evertything more than 6 will be take as circle
        if a>=6:
         
             M=cv2.moments(c)
             cx=int(M['m10']/M['m00'])
             cy=int(M['m01']/M['m00'])
             shape="circle"
             cv2.drawContours(final_image,[c],0,(0,0,0),2)
             nc=nc+1
         
        cv2.putText(final_image,str(color) + str('-')+str(shape),(cx-50,cy),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0),2)
        writecsv(color,shape)
        list.append(str('[')+shape+str('-')+color+str(']'))
##BLUE COLOR DETECTION WITH SHAPE    

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
            

            else :
                shape="rectangle"
            
                cv2.drawContours(final_image,[c],0,(0,0,0),2)
                nr=nr+1
            
#pentagon
        if a==5:
         
             M=cv2.moments(c)
             cx=int(M['m10']/M['m00'])
             cy=int(M['m01']/M['m00'])
             shape="pentagon"
             
             cv2.drawContours(final_image,[c],0,(0,0,0),2)
             npe=npe+1
         
# evertything more than 6 will be take as circle
        if a>=6:
         
             M=cv2.moments(c)
             cx=int(M['m10']/M['m00'])
             cy=int(M['m01']/M['m00'])
             shape="circle"
            
             cv2.drawContours(final_image,[c],0,(0,0,0),2)
             nc=nc+1
         
        cv2.putText(final_image,str(color) + str('-') + str(shape),(cx-50,cy),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0),2)
        writecsv(color,shape)
        list.append(str('[')+shape+str('-')+color+str(']'))

##RED COLOR DETECTION WITH SHAPE

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
# draw contours in black image



# biinding rectangle
###################
#for c in contours:
#    x,y,w,h =cv2.boundingRect(c) # gives initial coordinates and lwngth and wif=dth of rectangle
#
#    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)
#    cv2.imshow('bounding rectangle',image)
#################



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
            

            else :
               shape="rectangle"
               cv2.drawContours(final_image,[c],0,(0,0,0),2)
               nr=nr+1
          
#pentagon
        if a==5:
         
             M=cv2.moments(c)
             cx=int(M['m10']/M['m00'])
             cy=int(M['m01']/M['m00'])
             shape="pentagon"
    
             cv2.drawContours(final_image,[c],0,(0,0,0),2)
             npe=npe+1
         
# evertything more than 6 will be take as circle
        if a>=6:
         
             M=cv2.moments(c)
             cx=int(M['m10']/M['m00'])
             cy=int(M['m01']/M['m00'])
             shape="circle"
             
             cv2.drawContours(final_image,[c],0,(0,0,0),2)
             nc=nc+1
         
        cv2.putText(final_image,str(color)+str('-')+str(shape),(cx-50,cy),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0),2)
        writecsv(color,shape)
        list.append(str('[')+shape+str('-')+color+str(']'))
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
        filep = open('results1A_1228.csv','a')
        #this csv will later be used to save processed data, thus write the file name of the image 
        filep.write(fp)
        #close the file so that it can be reopened again later
        filep.close()
        #process the image
        data = main(fp)
        print data
        #open the csv
        filep = open('results1A_1228.csv','a')
        #make a newline entry so that the next image data is written on a newline
        filep.write('\n')
        
        #close the file
        filep.close()
