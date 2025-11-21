import cv2
import os
import time
import sys

def capture_and_recognize():
    print("Initializing webcam...")
    # Try different camera indices if default (0) doesn't work
    for i in range(0, 3):  # Try first 3 camera indices
        cap = cv2.VideoCapture(i)  # No CAP_DSHOW for Linux compatibility
        if cap.isOpened():
            print(f"Successfully opened camera at index {i}")
            break
    
    if not cap.isOpened():
        print("Error: Could not open any webcam. Please check your camera connection.")
        print("Troubleshooting tips:")
        print("1. Make sure the camera is properly connected")
        print("2. Check if another application is using the camera")
        print("3. Try a different USB port if using an external camera")
        return
    
    print("\nFace Recognition System")
    print("----------------------")
    print("1. Make sure you can see yourself in the camera window")
    print("2. Press 'c' to capture an image")
    print("3. Press 'q' to quit")
    print("----------------------")
    
    try:
        while True:
            # Try to read a frame multiple times if needed
            for attempt in range(3):
                ret, frame = cap.read()
                if ret:
                    break
                time.sleep(0.1)  # Small delay between attempts
                
            if not ret:
                print("\nError: Failed to grab frame from webcam")
                print("1. Make sure the camera is not being used by another application")
                print("2. Try unplugging and reconnecting the camera")
                print("3. Check your system's camera permissions")
                continue
                
            # Display the current frame
            cv2.imshow('Face Recognition (c: capture, q: quit)', frame)
            
            # Check for key press
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('c'):
                # Save the captured image with timestamp
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                temp_img = f'temp_capture_{timestamp}.jpg'
                
                try:
                    cv2.imwrite(temp_img, frame)
                    if not os.path.exists(temp_img):
                        raise Exception("Failed to save captured image")
                    print(f"\n✅ Image captured and saved as {temp_img}")
                    print("Processing image...")
                except Exception as e:
                    print(f"\n❌ Error saving image: {str(e)}")
                    print("Please check write permissions in the current directory.")
                    continue
                
                # Display the captured image
                cv2.imshow('Captured Image', frame)
                cv2.waitKey(1000)  # Show for 1 second
                cv2.destroyWindow('Captured Image')
                
                # Try to find a match in the database
                try:
                    print("Searching database for a match...")
                    
                    # Simple check if db directory exists and has files
                    if not os.path.exists('db') or not os.listdir('db'):
                        print("Error: No database found or database is empty.")
                        print("Please add reference images to the 'db' folder.")
                        continue
                    
                    # Import DeepFace here to handle the TensorFlow warnings better
                    from deepface import DeepFace
                    
                    start_time = time.time()
                    
                    # Find the best match in the database
                    dfs = DeepFace.find(
                        img_path=temp_img,
                        db_path="./db",
                        enforce_detection=False,
                        silent=True
                    )
                    
                    if dfs and not dfs[0].empty:
                        # Get the best match
                        best_match = dfs[0].iloc[0]
                        identity = best_match['identity']
                        distance = best_match['distance']
                        
                        # Extract name from the path
                        name = os.path.splitext(os.path.basename(identity))[0]
                        print(f"\n✅ Match found: {name}")
                        print(f"Similarity: {1 - distance:.2f}")
                        print(f"Time taken: {time.time() - start_time:.2f} seconds")
                        
                        # Show the matched image
                        matched_img = cv2.imread(identity)
                        if matched_img is not None:
                            cv2.imshow('Matched: ' + name, matched_img)
                            cv2.waitKey(3000)
                            cv2.destroyWindow('Matched: ' + name)
                    else:
                        print("\n❌ No match found in the database.")
                    
                    print("\nPress 'c' to try again or 'q' to quit")
                    
                except Exception as e:
                    print(f"\n❌ Error during face recognition: {str(e)}")
                finally:
                    # Clean up
                    if os.path.exists(temp_img):
                        os.remove(temp_img)
            
            elif key == ord('q'):
                print("\nExiting...")
                break
    
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    
    finally:
        # Clean up
        if 'cap' in locals() and cap.isOpened():
            cap.release()
        cv2.destroyAllWindows()
        print("Program ended.")

if __name__ == "__main__":
    capture_and_recognize()
