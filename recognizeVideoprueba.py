import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cam.isOpened():
    print("No se pudo acceder a la cámara.")
else:
    while True:
        ret, frame = cam.read()
        if not ret:
            print("No se pudo obtener la imagen de la cámara.")
            break

        cv2.imshow("Camara", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
cam.release()