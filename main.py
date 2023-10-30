import cv2


def sample():
    #reading the image saved in the folder and printing
    img=cv2.imread("dog.jpeg",1)
    print(img)

    #showing the image
    cv2.imshow('dog_img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #writing the image
    cv2.imwrite('dog.png',img)

def advanced():
    #if the image is closed or esc key is pressed, the windows will be closed, 

    #if the s key is pressed before closing the image then it will write the img and then windows
    #will be closed
    
    img=cv2.imread('dog.jpeg',0)

    cv2.imshow('dog_img',img)
    k=cv2.waitKey(0)

    if k==27:
        cv2.destroyAllWindows()
    elif k==ord('s'):
        cv2.imwrite('dog.png',img)
        cv2.destroyAllWindows()

advanced()