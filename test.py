from ultralytics import YOLO
import cv2 as cv

#load model
model=YOLO(r"weights/best.pt")

#load test image
image_path=r"assets/test2.jpg"
image=cv.imread(image_path)

#model's guess
results=model(image_path)

#drawing square
for box in results[0].boxes:
    
    #coordinates
    x1, y1, x2, y2 = map(int,box.xyxy[0]) 
    cls_id=int(box.cls[0]) #classification id
    confidence=float(box.conf[0]) #confidence score
    label= f"{model.names[cls_id].upper()}, conf: {confidence:.2f}" #label detection

    #putting square with coordinates
    cv.rectangle(image,(x1,y1) , (x2,y2) , (0,255,0) , 2)
    
    #put label on image
    cv.putText(image,label,(x1,y1-10),cv.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)

#show the image
cv.namedWindow("PREDICTION")
cv.imshow("PREDICTION",image)
cv.waitKey(0)
cv.destroyAllWindows()

#save the prediction
cv.imwrite("prediction-result-2.jpg",image)