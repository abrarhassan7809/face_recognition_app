# =======take a picture=======
# import cv2
# import os
# import tkinter as tk
# from PIL import ImageTk, Image
# import random
#
# # Create a tkinter window
# window = tk.Tk()
# window.title("Take Picture")
#
# # Create a label to display the video feed
# video_label = tk.Label(window)
# video_label.pack()
#
# # Initialize video capture
# video_capture = cv2.VideoCapture(0)
#
#
# def take_picture():
#     image_counter = str(random.randint(1000, 9999))
#     # Capture a frame
#     ret, frame = video_capture.read()
#
#     # Convert the frame to RGB format
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
#     # Convert the frame to PIL format
#     img = Image.fromarray(rgb_frame)
#
#     # Display the image in the tkinter window
#     img_tk = ImageTk.PhotoImage(image=img)
#     video_label.configure(image=img_tk)
#     video_label.image = img_tk
#
#     # Save the image in the folder
#     folder_name = "captured_images"
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)
#     img_path = os.path.join(folder_name, f"captured_image_{image_counter}.jpg")
#     img.save(img_path)
#     print(f"Image saved: {img_path}")
#
#
# def update_frame():
#     # Capture video frame-by-frame
#     ret, frame = video_capture.read()
#
#     # Convert the frame to RGB format
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
#     # Convert the frame to PIL format
#     img = Image.fromarray(rgb_frame)
#
#     # Display the image in the tkinter window
#     img_tk = ImageTk.PhotoImage(image=img)
#     video_label.configure(image=img_tk)
#     video_label.image = img_tk
#
#     # Schedule the next frame update
#     window.after(10, update_frame)
#
#
# # Create a button to take a picture
# picture_button = tk.Button(window, text="Take Picture", command=take_picture)
# picture_button.pack()
#
# # Start updating the frames
# update_frame()
#
# # Start the tkinter event loop
# window.mainloop()
#
# # Release the video capture
# video_capture.release()
# cv2.destroyAllWindows()

# ======match faces with input===but face matching function is not work properly===
# import cv2
# import os
# import tkinter as tk
# from tkinter import simpledialog
# from PIL import ImageTk, Image
# import face_recognition
# import random
#
# # Create a tkinter window
# window = tk.Tk()
# window.title("Take Picture")
#
# # Create a label to display the video feed
# video_label = tk.Label(window)
# video_label.pack()
#
# # Initialize video capture
# video_capture = cv2.VideoCapture(0)
#
# # Load known face encodings from the captured_images folder
# known_encodings = []
# known_names = []
# folder_name = "captured_images"
# for file_name in os.listdir(folder_name):
#     image_path = os.path.join(folder_name, file_name)
#     if os.path.isdir(image_path):
#         continue
#     image = face_recognition.load_image_file(image_path)
#     encoding = face_recognition.face_encodings(image)[0]
#     known_encodings.append(encoding)
#     known_names.append(file_name.split(".")[0])
#
#
# def take_picture():
#     # Prompt user for name only once
#     if not known_names:
#         name = simpledialog.askstring("Input", "Enter your name:", parent=window)
#         if name:
#             known_names.append(name)
#
#     # Capture a frame
#     ret, frame = video_capture.read()
#
#     # Convert the frame to RGB format
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
#     # Convert the frame to PIL format
#     img = Image.fromarray(rgb_frame)
#
#     # Display the image in the tkinter window
#     img_tk = ImageTk.PhotoImage(image=img)
#     video_label.configure(image=img_tk)
#     video_label.image = img_tk
#
#     # Save the image in the user's folder
#     image_counter = str(random.randint(1000, 9999))
#     folder_path = os.path.join(folder_name, known_names[0])
#     image_path = os.path.join(folder_path, f"name_{image_counter}.jpg")
#     os.makedirs(folder_path, exist_ok=True)  # Create the user's folder if it doesn't exist
#     img.save(image_path)
#     print(f"Image saved: {image_path}")
#
#
# def match_face():
#     # Capture a frame
#     ret, frame = video_capture.read()
#
#     # Convert the frame to RGB format
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
#     # Find faces in the frame
#     face_locations = face_recognition.face_locations(rgb_frame)
#     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
#
#     for face_encoding in face_encodings:
#         # Compare face encoding with known encodings
#         matches = face_recognition.compare_faces(known_encodings, face_encoding)
#         if True in matches:
#             matched_index = matches.index(True)
#             name = known_names[matched_index]
#             print(f"Face Match: {name}")
#         else:
#             print("No match found")
#
#
# def update_frame():
#     # Capture video frame-by-frame
#     ret, frame = video_capture.read()
#
#     # Convert the frame to RGB format
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
#     # Convert the frame to PIL format
#     img = Image.fromarray(rgb_frame)
#
#     # Display the image in the tkinter window
#     img_tk = ImageTk.PhotoImage(image=img)
#     video_label.configure(image=img_tk)
#     video_label.image = img_tk
#
#     # Schedule the next frame update
#     window.after(10, update_frame)
#
#
# # Create a button to take a picture
# picture_button = tk.Button(window, text="Take Picture", command=take_picture)
# picture_button.pack()
#
# # Create a button to match the captured face
# match_button = tk.Button(window, text="Match Face", command=match_face)
# match_button.pack()
#
# # Start updating the frames
# update_frame()
#
# # Start the tkinter event loop
# window.mainloop()
#
# # Release the video capture
# video_capture.release()
# cv2.destroyAllWindows()

# =======face match with folder name===face match properly with database======
import cv2
import os
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import ImageTk, Image
import face_recognition
import numpy as np
import sqlite3
import datetime

window = tk.Tk()
window.title("Take Picture")

video_label = tk.Label(window)
video_label.pack()

video_capture = cv2.VideoCapture(0)

known_encodings = []
known_names = []
folder_name = "captured_images"
for dir_name, _, file_names in os.walk(folder_name):
    encodings = []
    for file_name in file_names:
        image_path = os.path.join(dir_name, file_name)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        encodings.append(encoding)
    if encodings:
        known_encodings.append(np.array(encodings))
        known_names.append(os.path.basename(dir_name))


# Connect to the SQLite database
conn = sqlite3.connect("face_database.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS matches (name TEXT, class_name TEXT, time TEXT, status TEXT)")


def take_picture():
    name = simpledialog.askstring("Input", "Enter your name:", parent=window)
    if name:
        known_names.append(name)
        folder_path = os.path.join(folder_name, name)
        os.makedirs(folder_path, exist_ok=True)

        ret, frame = video_capture.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the frame to PIL format
        img = Image.fromarray(rgb_frame)

        img_tk = ImageTk.PhotoImage(image=img)
        video_label.configure(image=img_tk)
        video_label.image = img_tk

        image_counter = len(os.listdir(folder_path)) + 1
        image_path = os.path.join(folder_path, f"image_{image_counter}.jpg")
        img.save(image_path)
        print(f"Image saved: {image_path}")


def match_face():
    ret, frame = video_capture.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    matched_names = []
    for face_encoding in face_encodings:
        for i, encodings in enumerate(known_encodings):
            matches = face_recognition.compare_faces(encodings, face_encoding)
            if True in matches:
                matched_names.append(known_names[i])

    if matched_names:
        print(f"Face Match: {', '.join(matched_names)}")
        class_name = simpledialog.askstring("Input", "Enter your class name:", parent=window)
        if class_name:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for name in matched_names:
                # Get the folder name
                folder_path = os.path.join(folder_name, name)
                if os.path.exists(folder_path):
                    status = "present"
                else:
                    status = "face does not match"

                cursor.execute("INSERT INTO matches (name, class_name, time, status) VALUES (?, ?, ?, ?)",
                               (name, class_name, current_time, status))

            conn.commit()
            messagebox.showinfo("Face Matched", f"{name}: Present")
        else:
            messagebox.showerror("Error", "Please enter your class name.")
    else:
        print("No match found")
        messagebox.showinfo("Face Not Matched", "Face does not match.")


def update_frame():
    ret, frame = video_capture.read()

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb_frame)

    img_tk = ImageTk.PhotoImage(image=img)
    video_label.configure(image=img_tk)
    video_label.image = img_tk

    window.after(10, update_frame)


picture_button = tk.Button(window, text="Take Picture", command=take_picture)
picture_button.pack(pady=(20, 0))

match_button = tk.Button(window, text="Match Face", command=match_face)
match_button.pack(pady=(10, 0))

update_frame()
window.mainloop()

video_capture.release()
cv2.destroyAllWindows()

cursor.close()
conn.close()
