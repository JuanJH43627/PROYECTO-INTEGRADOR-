import cv2
import mediapipe as mp
import tkinter as tk
from PIL import Image, ImageTk


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

# --- Interfaz Tkinter ---
ventana = tk.Tk()
ventana.title("Detección de Manos")
ventana.geometry("800x650")
ventana.configure(background="#800040")
ventana.iconwindow()

# --frame para los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)

boton1 = tk.Button(frame_botones, text="Abecedario",bg="#8D9FA0")
boton1.pack(side="left",padx=20)

boton2 = tk.Button(frame_botones, text="Completar Palabras",bg="#8D9FA0")
boton2.pack(side="left", padx=20)

lbl_video = tk.Label(ventana)
lbl_video.pack(pady=20)


def actualizar_video():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)  # espejo para vista más natural

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )

        # Marco verde
        h, w, _ = frame.shape
        cv2.rectangle(frame, (20, 20), (w - 20, h - 20), (0, 255, 0), 2)

        

        # Contador de manos
        num_manos = len(result.multi_hand_landmarks) if result.multi_hand_landmarks else 0
        lbl_manos.config(text=f"manos detectadas: {num_manos}")
        #cv2.putText(frame, f"Manos detectadas: {num_manos}",
         #           (40, h - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        # Convertir para Tkinter
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=im_pil)

        lbl_video.imgtk = imgtk
        lbl_video.configure(image=imgtk)

    lbl_video.after(10, actualizar_video)

lbl_manos = tk.Label(ventana, text="manos detectadas : 0", font=("Arial",14),bg="#3CDB2A", fg="#000000") 
lbl_manos.pack()


actualizar_video()


ventana.mainloop()

cap.release()
hands.close()
cv2.destroyAllWindows()
