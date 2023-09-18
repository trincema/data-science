import cv2


class FaceDetection:
    imageInPath = 'faces-in-a-crowd.jpg'
    imageOutPath = imageInPath.replace('.', '-processed.')

    def __init__(self) -> None:
        # Load the Classifier
        self.face_classifier = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

    def load_image(self, path):
        """
        To improve computational efficiency, we first need to convert this image to grayscale before performing face detection.
        """
        self.img = cv2.imread(path)
        self.gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
    
    def perform_face_detection(self, gray = True):
        img = self.gray_img
        if not gray:
            img = self.img
        self.face = self.face_classifier.detectMultiScale(
            img, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
        )
        # create a bounding box around those faces
        for (x, y, w, h) in self.face:
            cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), 4)

    def save_image(self, path):
        cv2.imwrite(path, self.img)
