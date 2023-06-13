import time
from tkinter import messagebox


print("enterを押したらstartされますもう一度enterを押したらstopされます")
input()
print("Started")
count = 1
start_time = time.time()
input()
print("Stopped")
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time, "seconds")