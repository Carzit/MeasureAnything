import cv2

img_show = cv2.imread('r1.png') # the raw image
img_read = cv2.imread('d1.png') # the depth image

def mouse_click(event, x, y, flags, para):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',' ,y ,',', img_read[y, x][0])

if __name__ == '__main__':
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("img", mouse_click)
    while True:
        cv2.imshow('img', img_show)
        if cv2.waitKey() == ord('q'): # press 'q' to quit
            break
    cv2.destroyAllWindows()