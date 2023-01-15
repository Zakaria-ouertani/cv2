import cv2


def detect_stains(existing_image, camera_index):
    # Capture video input from the camera
    cap = cv2.VideoCapture(camera_index)

    # Read the first frame
    existing_image = cv2.imread(existing_image, cv2.IMREAD_GRAYSCALE)
    while True:
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Load the existing image of the face

        # Use the matchTemplate function to compare the current frame to the existing image
        result = cv2.matchTemplate(gray, existing_image, cv2.TM_CCOEFF_NORMED)

        # Use the minMaxLoc function to find the coordinates of the best match
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Define a threshold value for the match
        threshold = 0.8

        # Check if the match exceeds the threshold
        if max_val > threshold:
            # Draw a rectangle around the area of the best match
            top_left = max_loc
            bottom_right = (top_left[0] + existing_image.shape[1], top_left[1] + existing_image.shape[0])
            cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)

            # Display the frame with the rectangle
            cv2.imshow("Stain Detection", frame)

        else:
            print("No stains detected.")
        if cv.waitKey(20) & 0xFF == ord(" "):
            break
    cv2.waitKey(0)
    # Release the camera
    cap.release()

    # Close all windows
    cv2.destroyAllWindows()


detect_stains("pic.jpeg", 0)
