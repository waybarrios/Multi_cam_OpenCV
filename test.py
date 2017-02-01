import cv2
def show_camera():
  mirror=False
  #Setting up cameras
  cam0 = cv2.VideoCapture(0)
  cam1 = cv2.VideoCapture(1)
  cam2 = cv2.VideoCapture(2)
  cam3 = cv2.VideoCapture(3)
  cam4 = cv2.VideoCapture(4)
  while True:
	#Getting imgs from cameras 
	ret_val0, img0 = cam0.read()
	ret_val1, img1 = cam1.read()
	ret_val2, img2 = cam2.read()
	ret_val3, img3 = cam3.read()
	ret_val4, img4 = cam4.read()
	
        cv2.imshow('webcam0',img0)
	cv2.imshow('webcam1',img1)
	cv2.imshow('webcam2',img2)
	cv2.imshow('webcam3',img3)
	cv2.imshow('webcam4',img4)
	#quit
        if cv2.waitKey(1) & 0XFF==ord('q'):
		break
  cv2.destroyAllWindows()
  
def main():
	show_camera()

if __name__=='__main__':
	main()
		
		
