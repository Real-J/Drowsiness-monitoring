import cv2
import dlib
from scipy.spatial import distance as dist

# Load Dlib's face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/Users/mathew/Downloads/shape_predictor_68_face_landmarks.dat")

# Define constants for EAR threshold and consecutive frames
EAR_THRESHOLD = 0.25
CONSECUTIVE_FRAMES = 15
MAR_THRESHOLD = 0.75

# Initialize counters
blink_counter = 0
yawn_counter = 0
drowsy_counter = 0
alert_counter = 0

# Eye Aspect Ratio (EAR) calculation
def calculate_ear(eye):
    # Compute the distances between the two sets of vertical eye landmarks
    vertical_1 = dist.euclidean(eye[1], eye[5])
    vertical_2 = dist.euclidean(eye[2], eye[4])

    # Compute the distance between the horizontal eye landmarks
    horizontal = dist.euclidean(eye[0], eye[3])

    # Compute the EAR
    ear = (vertical_1 + vertical_2) / (2.0 * horizontal)
    return ear

# Mouth Aspect Ratio (MAR) calculation
def calculate_mar(mouth):
    # Compute the distances between the vertical mouth landmarks
    vertical = dist.euclidean(mouth[2], mouth[10])
    horizontal = dist.euclidean(mouth[0], mouth[6])

    # Compute the MAR
    mar = vertical / horizontal
    return mar

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = detector(gray)

    for face in faces:
        # Get facial landmarks
        landmarks = predictor(gray, face)

        # Extract eye and mouth landmarks
        left_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)]
        right_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)]
        mouth = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(48, 68)]

        # Calculate EAR for both eyes
        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)
        ear = (left_ear + right_ear) / 2.0

        # Calculate MAR for the mouth
        mar = calculate_mar(mouth)

        # Draw landmarks for visualization
        for point in left_eye + right_eye + mouth:
            cv2.circle(frame, point, 2, (0, 255, 0), -1)

        # Check if EAR is below the threshold
        if ear < EAR_THRESHOLD:
            blink_counter += 1
        else:
            blink_counter = 0

        # Check if MAR is above the threshold (indicating yawning)
        if mar > MAR_THRESHOLD:
            yawn_counter += 1
        else:
            yawn_counter = 0

        # If drowsiness is detected for a sustained duration
        if blink_counter >= CONSECUTIVE_FRAMES or yawn_counter >= CONSECUTIVE_FRAMES:
            drowsy_counter += 1
            alert_counter = 0
            cv2.putText(frame, "DROWSINESS DETECTED", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            alert_counter += 1
            drowsy_counter = 0

        # Display EAR and MAR values on the screen
        cv2.putText(frame, f"EAR: {ear:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        cv2.putText(frame, f"MAR: {mar:.2f}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    # Display the frame
    cv2.imshow("Drowsiness Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
