import cv2
import numpy as np
import time
import imutils
import math

def detections (net,image, confidence_setting, H, W):
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843,(300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()
    boxes = []
    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
    for i in range(0, detections.shape[2]):

        confidence = detections[0, 0, i, 2]

        if confidence > confidence_setting:
            idx = int(detections[0, 0, i, 1])
            if CLASSES[idx] == 'car' or CLASSES[idx] == 'bus':
                box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                (startX, startY, endX, endY) = box.astype("int")
                box = [startX, startY, endX - startX, endY - startY]
                boxes.append(box)

    return image, boxes 

if __name__ == '__main__':
    #load model to detect object
    #model_url ='E:/ML/ObectTracking/Caffe/res10_300x300_ssd_iter_140000.caffemodel'
    #prototype_url = 'E:/ML/ObectTracking/Caffe/deploy.prototxt'
    
    prototype_url = 'E:/ML/ObectTracking/Caffe/MobileNetSSD_deploy.prototxt'
    model_url ='E:/ML/ObectTracking/Caffe/MobileNetSSD_deploy.caffemodel'

    confidence_setting = 0.75
    maxdistence = 50 #max distence to define a new object

    net = cv2.dnn.readNetFromCaffe(prototype_url, model_url)
    #dnn.readNetFromCaffe(prototype_url, model_url)

    trackers = []
    url_path = 'test_video.mp4'
    #path = 'E:/ML/ObectTracking/video/test_video_result_2.avi'
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    
    cap = cv2.VideoCapture(url_path)
    #out = cv2.VideoWriter(path,fourcc, 20, (460,360))

    #define a box of Roid
    frame_number = 0
    car_counting = 0
    objectID = 0
   
    while (cap.isOpened()):
        start_time = time.time()
        ret_val, frame = cap.read()
        boxes = []
        if frame is None:
            break

        frame = cv2.resize(frame,(460,360))
        dt_frame = frame.copy()
        (H, W) = (360,460)
        Counter_point = H- 115
        i = 0
        listtrackers = trackers
        trackers = []
        for obj in listtrackers:
         
            tracker = obj['tracker']
            car_speed = obj.get("speed", 0)
            first_position = obj.get('firstposition')
            (success, box) = tracker.update(frame)
            boxes.append(box)

            objectdata = dict()
            objectdata['ID'] = obj['ID']
            objectdata['tracker'] = tracker
            objectdata['firstposition'] = obj['firstposition']
            objectdata['speed'] = obj['speed']
            
            
            (x, y, w, h) = [int(v) for v in box]
            cXd = int((x + (x + w)) / 2.0)
            cYd = int((y + (y + h)) / 2.0)
            
            #calculate speed
            if frame_number%60 == 0:
                objectdata['firstposition'] = box
                (xl, yl, wl, hl) = [int(v) for v in first_position]
                cXl = int((xl + (xl + wl)) / 2.0)
                cYl = int((yl + (yl + hl)) / 2.0)

                car_speed = math.sqrt((cXl-cXd)**2 + (cYl-cYd)**2)
                objectdata['speed'] = car_speed
            #end
            
            
            text = "Km/s: {:.2f}".format(car_speed)
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, (cXd, cYd), 4, (0, 255, 0), -1)
            y = y - 10 if y - 10 > 10 else y + 10
            cv2.putText(frame, text, (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            location_y = int((y + (y + h)) / 2.0)
            if location_y > Counter_point: # counting
                car_counting += 1  
            else:
                trackers.append(objectdata)                  
            i += 1
       
        
        if frame_number%3 == 0:
            frame, boxes_detected = detections(net,frame, confidence_setting, H, W)
            for box_dt in boxes_detected:
               
                IsExsitedObject = 0   
                (xd, yd, wd, hd) = [int(v) for v in box_dt]
                cXd = int((xd + (xd + wd)) / 2.0)
                cYd = int((yd + (yd + hd)) / 2.0)
                if cYd <= Counter_point-50: 
                               
                    for box_tracker in boxes: 
                        (xt, yt, wt, ht) = [int(c) for c in box_tracker]
                        cXt = int((xt + (xt + wt)) / 2.0)
                        cYt = int((yt + (yt + ht)) / 2.0)
                        distence = math.sqrt((cXt-cXd)**2 + (cYt-cYd)**2)
                        
                        if distence < maxdistence:
                            IsExsitedObject = 1
                            break
                    if IsExsitedObject == 0:
                        cv2.rectangle(frame, (xd, yd), ((xd + wd), (yd + hd)),(0, 0, 255), 2)
                        tracker = cv2.TrackerKCF_create()
                        objectID += 1
                        objectdata = dict()
                        tracker.init(frame, tuple(box_dt)) 
                        objectdata['ID'] = objectID
                        objectdata['speed'] = 0
                        objectdata['tracker'] = tracker
                        objectdata['firstposition'] = tuple(box_dt)
                        trackers.append(objectdata)
                 
       
        frame_number += 1
        end_time = time.time()
        text = "FPS: " +"{:.1f}".format(1/(end_time-start_time))
        text += " Total: " +"{:.2f}".format(car_counting)
        cv2.putText(frame, text, (10, H - ((1 * 20) + 300)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        cv2.line(frame, (0, Counter_point), (W, Counter_point), (0,255,0), 2)

        cv2.imshow("Frame", frame)
        out.write(frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    cap.release()
    # out.release()
    cv2.destroyAllWindows
