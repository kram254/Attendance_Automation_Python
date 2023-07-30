import cv2
import numpy as np
import Automated_Attendance_System
import os
from datetime import datetime

# Configuration
PATH_IMAGES = 'path/to/images'
CSV_FILE = 'Attendance.csv'
RECOGNITION_THRESHOLD = 0.6  # Adjust the threshold for face recognition accuracy

def load_images(path):
    images = []
    person_names = []
    for img_name in os.listdir(path):
        img_path = os.path.join(path, img_name)
        current_img = cv2.imread(img_path)
        images.append(current_img)
        person_names.append(os.path.splitext(img_name)[0])
    return images, person_names

def face_encodings(images):
    encode_list = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = Automated_Attendance_System.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list

def attendance(name):
    with open(CSV_FILE, 'r+') as f:
        my_data_list = f.readlines()
        name_list = [line.split(',')[0].strip() for line in my_data_list]

        if name not in name_list:
            time_now = datetime.now()
            t_str = time_now.strftime('%H:%M:%S')
            d_str = time_now.strftime('%d/%m/%Y')
            f.write(f'{name}, {t_str}, {d_str}\n')

def main():
    images, person_names = load_images(PATH_IMAGES)
    encode_list_known = face_encodings(images)
    print("All Encoding Complete!!!!!")

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

        faces_current_frame = Automated_Attendance_System.face_locations(faces)
        encodes_current_frame = Automated_Attendance_System.face_encodings(faces, faces_current_frame)

        for encode_face, face_loc in zip(encodes_current_frame, faces_current_frame):
            matches = Automated_Attendance_System.compare_faces(encode_list_known, encode_face, tolerance=RECOGNITION_THRESHOLD)
            face_distances = Automated_Attendance_System.face_distance(encode_list_known, encode_face)
            match_index = np.argmin(face_distances)

            if matches[match_index]:
                name = person_names[match_index].upper()
                y1, x2, y2, x1 = [loc * 4 for loc in face_loc]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                attendance(name)

        cv2.imshow("Camera", frame)

        if cv2.waitKey(10) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    
    
    
      
# import Automated_Attendance_System
# import numpy as np
# import cv2
# import os
# from datetime import datetime

# imagespath = 'images'
# myList = os.listdir(imagespath)
# images = []
# personName = []



# print(myList)

# for cu_img in myList:
#     current_Img = cv2.imread(f'{imagespath} / {cu_img}')
#     images.append(current_Img)
#     personName.append(os.path.splitext(cu_img)[0])

# print(personName)


# def faceEncodings(images):
#     encodeList = []

#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = Automated_Attendance_System.face_encodings(img)[0]
#         encodeList.append(encode)

#     return encodeList


# encodeListKnown = (faceEncodings(images))
# print("All Encoding Complete!!!!!")


# def attendance(name):
#     with open('Attendance.csv', 'r+') as f:
#         myDataList = f.readlines()
#         nameList = []
#         for line in myDataList:
#             entry = line.split(',')
#             nameList.append(entry[0])

#         if name not in nameList:
#             time_now = datetime.now()
#             tStr = time_now.strftime('%H:%M:%S')
#             dStr = time_now.strftime('%d/%m/%Y')
#             f.writelines(f'{name}, {tStr}, {dStr}')


# cap = cv2.VideoCapture(0)

# while True:

#     ret, frame = cap.read()
#     faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
#     faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

#     facesCurrentFrame = Automated_Attendance_System.face_locations(faces)
#     encodesCurrentFrame = Automated_Attendance_System.face_encodings(faces, facesCurrentFrame)

#     for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
#         matches = Automated_Attendance_System.compare_faces(encodeListKnown, encodeFace)
#         faceDis = Automated_Attendance_System.face_distance(encodeListKnown, encodeFace)

#         matchIndex = np.argmin(faceDis)

#         if matches[matchIndex]:
#             name = personName[matchIndex].upper()

#             y1, x2, y2, x1 = faceLoc

#             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#             cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
#             attendance(name)
#     cv2.imshow("Camera", frame)

#     if cv2.waitKey(10) == 13:
#         break

# cap.release()

# cv2.destroyAllWindows()
