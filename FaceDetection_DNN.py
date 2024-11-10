import cv2

# Load the DNN model
model_path = "./Res10_300x300_ssd_iter_140000.caffemodel"
config_path = "./deploy.prototxt"
net = cv2.dnn.readNetFromCaffe(config_path, model_path)

# real-time detection
# use the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    (h, w) = frame.shape[:2]
    
    # Prepare the input for the DNN network
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    # Draw a rectangle on the identified faces
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        
        if confidence > 0.5:  
            box = detections[0, 0, i, 3:7] * [w, h, w, h]
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(frame, (startX, startY), (endX, endY), (255, 0, 0), 2)
    
    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
