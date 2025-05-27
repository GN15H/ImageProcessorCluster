from tkinter import filedialog
import connection_handler
import image_handler

NODES_AMOUNT = 2
print("Seleccionar archivo")
file_path = filedialog.askopenfilename(initialdir="./")
img_arr = image_handler.read_image(file_path)
img_segments = image_handler.get_image_segments(img_arr, NODES_AMOUNT)
a = connection_handler.Connection_Handler(NODES_AMOUNT)
print("Obteniendo nodos...")
a.get_nodes()
print("Enviando datos")
a.send_data(img_segments)
print("Recibiendo Datos")
a.receive_segments()
a.join_img(img_arr)