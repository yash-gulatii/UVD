import pytube  
from pytube import YouTube  
video_url = input("Enter The Url of Video You Want To Download")
youtube = pytube.YouTube(video_url)  
video = youtube.streams.first()  
video.download('C:\Users\yashg\Downloads')
print("Downloding....")   
print("Downloding...")   
print("Downloding....")   
print("Downloding...")   
print("Downloding..")   
print("Downloding.")
print("Done Video Downloaded Successfully")   