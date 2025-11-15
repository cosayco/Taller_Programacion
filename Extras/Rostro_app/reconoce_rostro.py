import cv2
import os
import urllib.request

# Archivos del modelo DNN
modelFile = "res10_300x300_ssd_iter_140000.caffemodel"
configFile = "deploy.prototxt"

# URLs oficiales de OpenCV
modelURL = "https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel"
configURL = "https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt"

# Descargar archivos si no existen
def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Descargando {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"{filename} descargado correctamente.")

print("Verificando archivos del modelo...")
download_file(modelURL, modelFile)
download_file(configURL, configFile)

# Cargar el modelo DNN
net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

# Clasificadores Haar para ojos y sonrisas
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Iniciar cámara
cap = cv2.VideoCapture(0)
smile_count = 0

print("Iniciando detección en tiempo real. Presiona 'q' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    # Preparar blob para DNN
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                                 (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * [w, h, w, h]
            (x, y, x2, y2) = box.astype("int")

            (frame, (x, y), (x2, y2), (255, 0, 0), 2)

            roi_gray = cv2.cvtColor(frame[y:y2, x:x2], cv2.COLOR_BGR2GRAY)
            roi_color = frame[y:y2, x:x2]

            # Detectar ojos
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            # Detectar sonrisas
            smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22)
            if len(smiles) > 0:
                smile_count += 1
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)

    # Mostrar contador
    cv2.putText(frame, f"Sonrisas detectadas: {smile_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Detección DNN + Ojos + Sonrisas", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): #Presionar 'q' para salir
        break

cap.release()
cv2.destroyAllWindows()
print("Aplicación finalizada.")