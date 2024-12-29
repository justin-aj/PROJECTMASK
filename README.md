# **ProjectMASK: Mask Detector with Face Recognition and Fining System**

## **Overview**

ProjectMASK is a robust application designed to detect whether individuals are wearing masks and, if not, identify them using face recognition. Upon identification, the system sends a notification message to the person through their registered mobile number, using Twilio API. The project integrates **MobileNet**, **OpenCV**, and **face_recognition** libraries to achieve real-time detection and recognition with high efficiency.

---

## **Features**
1. **Mask Detection**:
   - Utilizes **MobileNet**, a lightweight deep convolutional neural network, to classify whether a person is wearing a mask or not.
   - Implements OpenCV's **CascadeClassifier** for face detection.

2. **Face Recognition**:
   - Encodes the face of individuals without masks using **dlib**'s face recognition model.
   - Compares the captured face with an existing database to identify the person.

3. **Notification System**:
   - Extracts user details (e.g., mobile number) from a database upon recognition.
   - Sends an alert message to the person using the **Twilio API**.

---

## **Methodology**

### **Phase 1: Mask Detection**
- **MobileNet Architecture**:
  - A pre-trained MobileNet model implemented in TensorFlow’s Keras API classifies mask usage.
  - Lightweight and efficient for real-time applications.
- **Face Detection**:
  - OpenCV’s **CascadeClassifier** is used to detect faces within an image or frame.
  - The Viola-Jones and AdaBoost methods enhance face detection performance.

### **Phase 2: Face Recognition**
- If a person is identified as not wearing a mask:
  1. **Image Capture**:
     - Captures the face of the person not wearing a mask.
  2. **Face Encoding**:
     - Generates a 128-dimensional face encoding for the captured image using the **face_recognition** library.
  3. **Database Matching**:
     - Compares the encoding with stored images in the database to identify the person.

### **Phase 3: Notification and Fining System**
- Once identified:
  - Extracts user information (e.g., mobile number) from the database.
  - Sends a warning message using the **Twilio API**.
  - The system can be extended to implement a fining mechanism.

---

## **Dataset**
- The dataset for training and testing the mask detection model is available at the following link:  
  [Dataset Link](https://drive.google.com/drive/folders/1pUbDu1sgcWpwvdJl3cXUoPcaIk1CNLJe?usp=sharing)

---

## **Installation and Setup**

### **Prerequisites**
- Python 3.7 or higher
- Required libraries: TensorFlow, Keras, OpenCV, dlib, face_recognition, Twilio
- Twilio account for messaging (create your own account to avoid exposing credentials)

### **Steps to Set Up**
1. **Clone the Repository**:
   ```
   git clone https://github.com/your-repository/ProjectMASK.git
   cd ProjectMASK
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Set Up Twilio**:
   - Sign up for a Twilio account at [Twilio](https://www.twilio.com).
   - Obtain your **Account SID**, **Auth Token**, and **Twilio Phone Number**.
   - Update the `twilio_config.py` file with your credentials.

4. **Run the Application**:
   ```
   python main.py
   ```

---

## **Usage**

1. **Mask Detection**:
   - The system detects faces in real-time using your webcam or pre-recorded videos.
   - Classifies whether the person is wearing a mask.

2. **Face Recognition**:
   - If a mask is not detected, the system captures the face and compares it with the database.
   - Identifies the individual based on stored face encodings.

3. **Notification System**:
   - Sends an SMS alert to the identified person using Twilio.

---

## **Project Structure**
```
ProjectMASK/
├── dataset/                   # Folder for training and testing datasets
├── models/                    # Pre-trained MobileNet model and weights
├── scripts/                   # Python scripts for mask detection and face recognition
├── twilio_config.py           # Twilio configuration file (Update with your credentials)
├── requirements.txt           # List of dependencies
├── main.py                    # Main program entry point
├── README.md                  # Project documentation
```

---

## **Future Enhancements**
- Integrate real-time video feed from CCTV cameras.
- Add a feature for automated fine deduction from a wallet system.
- Improve the system to detect improper mask usage (e.g., masks below the nose).
- Extend the notification system to send email alerts.

---

## **Disclaimer**
This project uses sensitive personal data (e.g., face encodings and contact details). Ensure compliance with privacy regulations such as **GDPR** when deploying in a real-world environment.

---

## **References**
- [MobileNet Paper](https://arxiv.org/abs/1704.04861)
- [OpenCV Documentation](https://docs.opencv.org)
- [Twilio API Documentation](https://www.twilio.com/docs/usage/api)

---

## **License**
This project is licensed under the MIT License.
