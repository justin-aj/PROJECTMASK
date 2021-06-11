# PROJECTMASK
Mask Detector using MobileNet Architecture and face recognition with a fining system on any Database.
The steps of the method are as follows,
First Phase: We have used MobileNet, a class of light weight deep convolutional neural networks that are vastly smaller in size and faster in performance than many other popular models, in order to classify if a person are using a mask or not. We have used MobileNet implemented in TensorFlow’s Keras API.
And in order to find faces in a frame/image and then identify if the person is wearing a mask or not, we have used CascadeClassifier, already included in the OpenCV library. In general, this training method uses an .xml file, which is also already included in the package, to train a model that recognizes faces in a generic way, using the Viola-Jones and AdaBoost method to improve performance. 


Second Phase: If the person is identified not wearing , his image is captured and the face encoding of the face on the image is generated.
A face encoding is basically a way to represent the face using a set of 128 computer-generated measurements. Two different pictures of the same person would have similar encoding and two different people would have totally different encoding. So the images from the database will be compared with the image captured not wearing a mask. Inorder to perform these operations, we use face_recogniton package which is library Built using dlib’s state-of-the-art face recognition built with deep learning.
Third Phase: As the face is recognized from the database, the identified user details like mobile number is extracted from the database and a message his sent to him using twilio which is a web application programming interface (API) that software developers can use to add communications such as phone calling, messaging, video and two-factor authentication into their Python applications.

dataset link:
RUN detect_mask_video for output
