import cv2

#to capture the video and show it
def main():
    cam = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

    while True:
        ret,frame = cam.read()
        if ret:
            cv2.imshow('img',frame)
            out.write(frame)
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
    cam.release()
    out.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()