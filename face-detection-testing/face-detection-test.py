from face_detection import FaceDetection

def basic_test():
    face_detect = FaceDetection()
    face_detect.load_image('faces-in-a-crowd.jpg')
    face_detect.perform_face_detection()
    face_detect.save_image('out.jpg')
