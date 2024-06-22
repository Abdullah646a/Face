# import tkinter as tk
# import subprocess
#
# def run_command():
#     command = "python ./face_recognition_demo.py ^m_fd ./models\face-detection-retail-0044\face-detection-retail-0044.xml ^ m_lm ./models\landmarks-regression-retail-0009\FP16\landmarks-regression-retail-0009.xml -m_reid ./models\face-reidentification-retail-0095\FP16\face-reidentification-retail-0095.xml ^--verbose ^-fg "/face_database" --input 0"  # Replace "dir" with your desired command
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     output, error = process.communicate()
#     if error:
#         print(f"Error running command: {error.decode('utf-8')}")
#     else:
#         print(output.decode('utf-8'))
#
# ##GUI
# root = tk.Tk()
# root.title("FACE")
#
# button = tk.Button(root, text="Send Command", command=run_command)
# button.pack(padx=50, pady=50)
#
# root.mainloop()
import tkinter as tk
import subprocess

def run_command():
    command = 'python ./face_recognition_demo.py ^m_fd ./models\face-detection-retail-0044\face-detection-retail-0044.xml ^ m_lm ./models\landmarks-regression-retail-0009\FP16\landmarks-regression-retail-0009.xml -m_reid ./models\face-reidentification-retail-0095\FP16\face-reidentification-retail-0095.xml ^--verbose ^-fg "/face_databas/" --input 0'  # Replace "dir" with your desired command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if error:
        print(f"Error running command: {error.decode('utf-8')}")
    else:
        print(output.decode('utf-8'))

##GUI
root = tk.Tk()
root.title("FACE")

button = tk.Button(root, text="Send Command", command=run_command)
button.pack(padx=50, pady=50)

root.mainloop()