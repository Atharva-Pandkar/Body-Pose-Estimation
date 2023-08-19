import os 


print(os.getcwd())
print(os.getcwd()+"/Files")
print(os.getcwd()+"/Files/Image")
print(os.getcwd()+"/Files/Live-Stream")
print(os.getcwd()+"/Files/Video")
print(os.path.exists(os.getcwd()+"/Files/Image/pose.py"))
print(os.path.exists(os.getcwd()+"/Files/Live-Stream/pose_video.py"))
print(os.path.exists(os.getcwd()+"/Files/Video/pose_video.py"))
print(os.getcwd()+"/Videos/Live-Stream")
print(os.getcwd()+"/Files/Videos/Pre-Existing-Videos")
print(os.getcwd()+"/Images")
print (os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
/home/atharva/Downloads/sample_video.mp4
