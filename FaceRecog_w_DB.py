import face_recognition
import pickle
import time
import cv2
import os
import numpy as np
import mysql.connector
from mysql.connector import Error
import base64
from PIL import Image
import io
from twilio.rest import Client

def face_recog_w_db(img_name):
    print("Start")

    all_face_encodings = {}

    connection = mysql.connector.connect(host='localhost',
                                         database='STUDENTImage',
                                         user='root',
                                         password='')





    if connection.is_connected():
        print("loop 1")

        cursor = connection.cursor()
        '''
        
        file = open("ajin.jpg", 'rb').read()
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        file = base64.b64encode(file)
        
        nameofstd=input("Enter Name of Student:")
        srn=input("Enter Unique srn of student")
        mobileno=input("Enter Mobile No of Student:")
        # print(file)
        args = (file, "ajin.jpg",nameofstd,srn,"0",mobileno)
        query = 'INSERT INTO STUDENTImage.PBL VALUES(%s, %s,%s,%s,%d,%d)'
        cursor.execute(query, args)
        connection.commit()
       
        query = 'SELECT Image_Path  FROM PBL'
        cursor.execute(query)
        data = cursor.fetchall()
    
        for row in data:
            image = data[0][0]
    
            binary_data = base64.b64decode(image)
    
            image = Image.open(io.BytesIO(binary_data))
        
        '''
        query = 'SELECT FileName  FROM PBL'
        cursor.execute(query)
        file = cursor.fetchall()
        que = 'SELECT Name  FROM PBL '
        cursor.execute(que)
        fil = cursor.fetchall()
        print(fil)
        print(file)


        for ro,oro in zip(file,fil):


            ro=ro[0]
            oro=oro[0]
            img1 = face_recognition.load_image_file(ro)
            all_face_encodings[oro] = face_recognition.face_encodings(img1)[0]
            print("loop 2")


        # find path of xml file containing haarcascade file
            cascPathface = os.path.dirname(
                cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
            # load the harcaascade in the cascade classifier

            faceCascade = cv2.CascadeClassifier(cascPathface)

            # load the known faces and embeddings saved in last file
            # data = pickle.loads(open('face_enc.csv', "rb").read())
            with open('dataset_faces.dat', 'wb') as f:
                pickle.dump(all_face_encodings, f)
            with open('dataset_faces.dat', 'rb') as f:
                data = pickle.load(f)

            face_names = list(data.keys())
            face_encodings = np.array(list(data.values()))

            # Find path to the image you want to detect face and pass it here
            image = cv2.imread(img_name)

            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # convert image to Greyscale for haarcascade
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray,
                                                 scaleFactor=1.1,
                                                 minNeighbors=5,
                                                 minSize=(60, 60),
                                                 flags=cv2.CASCADE_SCALE_IMAGE)

            # the facial embeddings for face in input
            encodings = face_recognition.face_encodings(rgb)
            names = []
            # loop over the facial embeddings incase
            # we have multiple embeddings for multiple fcaes
            for encoding in encodings:
                print("loop 3")
                # Compare encodings with encodings in data["encodings"]
                # Matches contain array with boolean values and True for the embeddings it matches closely
                # and False for rest
                matches = face_recognition.compare_faces(face_encodings,
                                                         encoding)
                # set name =inknown if no encoding matches
                name = "Unknown"
                # check to see if we have found a match
                if True in matches:
                    print("loop 4")
                    # Find positions at which we get True and store them
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}
                    # loop over the matched indexes and maintain a count for
                    # each recognized face face
                    for i in matchedIdxs:
                        print("loop 5")
                        # Check the names at respective indexes we stored in matchedIdxs
                        name = face_names[i]
                        print(name)

                        # increase count for the name we got
                        counts[name] = counts.get(name, 0) + 1
                        # set name which has highest count
                        name = max(counts, key=counts.get)

                    # update the list of names
                    names.append(name)
                    # loop over the recognized faces
                    for ((x, y, w, h), name) in zip(faces, names):
                        print("loop 6")
                        # rescale the face coordinates
                        # draw the predicted face name on the image

                        query = 'SELECT MobileNo  FROM PBL where Name=%s'
                        cursor.execute(query,(name,))
                        file = cursor.fetchall()
                        print(file)

                        file = file[0]
                        file = file[0]
                        print(file)
                        fullfile=("+91")+file
                        print(fullfile)
                        print(file)
    
                        print(name)
                        account_sid = ''
                        auth_token = ''
                        client = Client(account_sid, auth_token)
                        count = 1
                        message = client.messages \
                            .create(
                            body='Warning {} Wear Your Mask'.format(count),
                            from_='',
                            to=fullfile
                        )
    
                        print(message.sid)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(image, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.75, (0, 255, 0), 2)
                        exit()
                else:
                    break