
# UVD [Youtueb Video Downloder]

**Description**

This Projects is all about Downloading YouTube Video Using Python.
How you Can Use Python3 & a Python Library PyTube to Download YouTube Videos.👨‍💻

**Why You Want This?**

 1.You Want to Download Movie From YouTube ( Pirated 💀 ).

 2.You Want to Download YouTube Video For Your Video ( Maybe For Rosting 🤬 ).

 3.You Want to Download for Fun Only.

 4.You Want to Add this Project in Your Resume ( You Thief 🤨 ) 
 Just Kidding You Can Surely rebuild this Project and in Your Resume or 
 just Copy Paste as We Always Do. 
 
**Requirements**
    
 1.Python3 
 
 2.PyTube
 
    pip install pytube
## The Code

**Import PyTube**

```python
    import pytube   
```
**Import YouTube from PyTube**
```python
    from pytube import YouTube 
```
**Getting URL from the User**
```python
    video_url = input("Enter The Url of Video You Want To Download") 
```
**Getting Video Using PyTube**
```python
    youtube = pytube.YouTube(video_url)  
    video = youtube.streams.first() 
```
**Downloading Video to Downloading Folder( Remember to Change the Path Here :)**
```python
    youtube = pytube.YouTube(video_url)  
    video = youtube.streams.first() 
```
**Print the Info About Dowloading Status**
```python
    print("Downloding....")   
    print("Downloding...")   
    print("Downloding....")   
    print("Downloding...")   
    print("Downloding..")   
    print("Downloding.")
    print("Done Video Downloaded Successfully")
```  
