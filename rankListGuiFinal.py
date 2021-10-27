from threading import Thread
import ffmpeg
import time

class rankList:    
    import threading
    from pathlib import Path
    from tkinter import font
    from tkvideo import tkvideo
    from io import BytesIO, TextIOWrapper
    from simple_image_download import simple_image_download as simpl
    from os import terminal_size
    import os, shutil, ssl, PIL, urllib, tkinter, requests, magic, sys, threading
    from tkinter import ttk
    import tkinter.scrolledtext as st
    from PIL import Image, ImageDraw, ImageFont, ImageEnhance
    from tkinter import Label
    from urllib.parse import quote


    response = simpl.simple_image_download()
    root = tkinter.Tk()
    root.title("Rank List")
    keyword = tkinter.StringVar()
    limit = tkinter.IntVar()
    progress = 0
    imgFrameLimit = 100
    imgList = []
    urlList = []
    global vid
    global numExecuted
    


    ssl._create_default_https_context = ssl._create_unverified_context

    def __init__(self):
    
        if(self.os.path.exists(str(self.Path().absolute()) + '/tmp')):
            self.shutil.rmtree(str(self.Path().absolute()) + "/tmp")
        if(not(self.os.path.exists(str(self.Path().absolute()) + '/tmp'))):
            self.os.makedirs(str(self.Path().absolute()) + '/tmp')
            
        self.root.bind_all("<Return>", self.handler)

        self.numExecuted = 0
        keywordLabel = self.ttk.Label(self.root, text="Enter a keyword", font=("Times New Roman", 15), width=20); keywordLabel.grid(row=0, column=0)
        limitLabel = self.ttk.Label(self.root, text="Enter a limit", font=("Times New Roman", 15), width=20,); limitLabel.grid(row=0, column=1)
        keywordEntry = self.ttk.Entry(self.root, width=20, textvariable=self.keyword); keywordEntry.grid(row=1, column=0)
        limitEntry = self.ttk.Entry(self.root, width=20, textvariable=self.limit); limitEntry.grid(row=1, column=1)
        self.vid = self.ttk.Label(self.root, width=40); self.vid.grid(row=2, column=0, columnspan=2)
        player = self.tkvideo(str(self.Path().absolute()) + "/placeholder3.mp4", self.vid, loop = 1, size = (854, 480))
        vidThread = self.threading.Thread(target=player.play)
        vidThread.start()
        #progressBar = self.ttk.Progressbar(orient="horizontal", width=40, mode="determinate", maximum=self.limit * 2, variable=self.progress); progressBar.grid(row=3, column=0)
        self.root.mainloop()

    def handler(self, event):
        startUrls = time.time()
        #print("Keyword = " + self.keyword.get() + " Limit  = " + str(self.limit.get()))
        #urlThread = self.threading.Thread(target=self.response.urls, args=(self.keyword.get, self.limit.get))
        urlList = self.response.urls(self.keyword.get(), self.limit.get())

        start = time.time()
        titleThread = Thread(target=self.titleImage, args=(self.keyword.get(), self.limit.get()))
        titleThread.start()
        titleThread.join()
        #self.titleImage(self.keyword.get(), self.limit.get())

        imgThreadList = []
        for i in range(len(urlList)):
            #print(urlList[i] + "at position " + str(i))
            imgThreadList.append(Thread(target=self.imgWText, args=(i, urlList)))
            imgThreadList[i].start()
            imgThreadList[i].join()
            #self.imgWText(i, urlList)
        #for thread in imgThreadList:
        #    thread.join()
        #for img in self.imgList:
            #print(img + str(self.imgList.index(img)))
        #ffmpegThread = self.threading.Thread(target=self.ffmpegRun)
        #ffmpegThread.daemon = 1
        #ffmpegThread.start()
        self.ffmpegRun()
        end = time.time()
        print(f"Runtime of the urls method is {start - startUrls}")
        print(f"Runtime of the program is {end - start}")
            
    def ffmpegRun(self):
        try:
            process = ffmpeg.input('pipe:', r='60', f='jpeg_pipe').output(str(self.Path().absolute()) + '/tmp/test.mp4', vcodec='libx264').overwrite_output().run_async(pipe_stdin=True)
            for image in self.imgList:
                with open("./tmp/" + image, "rb") as img:
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    if not("mid") in image:
                        f = img.read()
                        b = bytearray(f)
                        process.stdin.write(f)
                    else:
                        f = img.read()
                        b = bytearray(f)
                        for j in range(self.imgFrameLimit - 10):
                            process.stdin.write(f)

            process.stdin.close()
            process.wait()
        except ffmpeg.Error as e:
            print('stderr:', e.stderr.decode('utf8'))
            raise e
        try:
            self.vid.destroy()
            self.vid = self.ttk.Label(self.root); self.vid.grid(row=2, column=0, columnspan=2)
            player = self.tkvideo(str(self.Path().absolute()) +  "/tmp/test.mp4", self.vid, loop = 1, size = (854, 480))
            player.play()
        except Exception as e:
            print(e)

        #print("video")

    def titleImage(self, keyword, limit):
        img = self.Image.new('RGB', (854, 480), (0, 0, 255))
        d1 = self.ImageDraw.Draw(img)
        fnt = self.ImageFont.truetype(str(self.Path().absolute()) + '/comic.ttf', 100)
        d1.text((100, 100), "Top " + str(limit) + " " + keyword, font = fnt, fill = (255, 255, 255))
        enhancer = self.ImageEnhance.Brightness(img)
        for a in range(22):
            if(0 <= a <= 10):
                temp = enhancer.enhance(a / 10)
                self.imgList.insert(a, "temp" + str(0) + "-" + str(a) + ".jpg")
                #print(str(a / 10) + " at position + " + str(a))
                temp.save(str(str(self.Path().absolute()) + "/tmp/temp" + str(0) + "-" + str(a) + ".jpg"))
                #print(a)
            elif(12 <= a <= 22):
                temp = enhancer.enhance(abs(22 - a) / 10)
                self.imgList.insert(a ,"temp" + str(0) + "-" + str(a) + ".jpg")
                #print(str(abs(22 - a) / 10) + " at position + " + str(a))
                temp.save(str(str(self.Path().absolute()) + "/tmp/temp" + str(0) + "-" + str(a) + ".jpg"))
                #print(a)
            else:
                #print("1 at position + " + str(a))
                self.imgList.insert(11, "temp" + str(0) + "-" + str(11) + "mid.jpg")    
                img.save(str(str(self.Path().absolute()) + "/tmp/temp" + str(0) + "-" + str(11) + "mid.jpg"))
                #print(11)

        
    def imgWText(self, num, urlList):
        img = self.Image.new('RGB', (854, 480), (0, 0, 255))
        d1 = self.ImageDraw.Draw(img)
        fnt = self.ImageFont.truetype(str(self.Path().absolute()) + '/comic.ttf', 100)
        d1.text((200, 200), "Number " + str(num + 1), font = fnt, fill = (255, 255, 255))
        enhancer = self.ImageEnhance.Brightness(img)
        for i in range(22):
            if(0 <= i <= 10):
                temp = enhancer.enhance(i / 10)
                #print(str(i / 10) + " at position + " + str(i))
                self.imgList.insert(((self.numExecuted + 1 )*22) + i, "temp" + str(num + 1) + "-" + str(i) + ".jpg")
                #print(str((self.numExecuted + 1 )*22 + i))
                temp.save(str(self.Path().absolute()) + "/tmp/temp" + str(num + 1) + "-" + str(i) + ".jpg")
                
                
            elif(12 <= i <= 22):
                #print(str(abs(22 - i) / 10) + " at position + " + str(i))
                temp = enhancer.enhance(abs(22 - i) / 10)
                self.imgList.insert(((self.numExecuted + 1 )*22) + i, "temp" + str(num + 1) + "-" + str(i) + ".jpg")
                #print(str((self.numExecuted + 1 )*22 + i))
                temp.save(str(self.Path().absolute()) + "/tmp/temp" + str(num + 1) + "-" + str(i) + ".jpg")
                

            else:
                #print("1 at position + " + str(i))
                temp = enhancer.enhance(1)
                self.imgList.insert(((self.numExecuted + 1 )*22) + i, "temp" + str(num + 1) + "-" + str(11) + "mid.jpg")
                #print(str((self.numExecuted + 1 )*22 + i))
                temp.save(str(self.Path().absolute()) + "/tmp/temp" + str(num + 1) + "-" + str(11) + "mid.jpg")
                

        img = self.downloadPage(urlList[num])
        
        if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
        enhancer = self.ImageEnhance.Brightness(img)
        
        for i in range(22):
            if(0 <= i <= 10):
                temp = enhancer.enhance(i / 10)
                #print(str(i / 10) + " at position + " + str(i))
                temp.resize((854, 480))
                self.imgList.insert(((self.numExecuted + 1 )*44) + i, "temp" + str(num + 1) + "-" + str(i + 22) + ".jpg")
                temp.save(str(self.Path().absolute()) + "/tmp/temp" + str(num + 1) + "-" + str(i + 22) + ".jpg")
                #print(((self.numExecuted + 1 )*44) + i)

            elif(12 <= i <= 22):
                temp = enhancer.enhance(abs(22 - i) / 10)
                #print(str(abs(22 - i) / 10) + " at position + " + str(i))
                temp.resize((854, 480))
                self.imgList.insert(((self.numExecuted + 1 )*44) + i, "temp" + str(num + 1) + "-" + str(i + 22) + ".jpg")
                temp.save(str(self.Path().absolute()) + "/tmp/temp" + str(num + 1) + "-" + str(i + 22) + ".jpg")
                #print(((self.numExecuted + 1 )*44) + i)

            else:
                temp = enhancer.enhance(1)
                #print("1 at position + " + str(i))
                temp.resize((854, 480))
                self.imgList.insert(((self.numExecuted + 1 )*44) + i, "temp" + str(num + 1) + "-" + str(32) + "mid.jpg")
                #print(((self.numExecuted + 1 )*44) + i)
                img.save(str(self.Path().absolute()) + "/tmp/temp" + str(num + 1) + "-" + str(32) + "mid.jpg")
            self.numExecuted += 1
            
                
                
    def urls(self, keyword, limit):
        links = []
        linkThreads = []

        url = 'https://www.google.com/search?q=' + self.quote(
            keyword.encode(
                'utf-8')) + '&biw=1536&bih=674&tbm=isch&sxsrf=ACYBGNSXXpS6YmAKUiLKKBs6xWb4uUY5gA:1581168823770&source=lnms&sa=X&ved=0ahUKEwioj8jwiMLnAhW9AhAIHbXTBMMQ_AUI3QUoAQ'
        raw_html = self.downloadPage(url)

        end_object = -1
        google_image_seen = False
        j = 0

        while j < limit:
            linkThreads.append(self.Thread(target=self.subUrl, args=(j, end_object, google_image_seen, raw_html)))
            #self.subUrl(j, end_object, google_image_seen, raw_html)
        return(links)
    
    def subUrl(self, links, j, end_object, google_image_seen, raw_html, extensions={'.jpg', '.png', '.ico', '.gif', '.jpeg'}):
        while (True):
            try:
                new_line = raw_html.find('"https://', end_object + 1)
                end_object = raw_html.find('"', new_line + 1)

                buffor = raw_html.find('\\', new_line + 1, end_object)
                if buffor != -1:
                    object_raw = (raw_html[new_line + 1:buffor])
                else:
                    object_raw = (raw_html[new_line + 1:end_object])

                if any(extension in object_raw for extension in extensions):
                    break

            except Exception as e:
                break

        try:
            r = self.requests.get(object_raw, allow_redirects=True, timeout=1)
            if('html' not in str(r.content)):
                mime = self.magic.Magic(mime=True)
                file_type = mime.from_buffer(r.content)
                file_extension = f'.{file_type.split("/")[1]}'
                if file_extension == '.png' and not google_image_seen:
                    google_image_seen = True
                    raise ValueError()
                links(object_raw)
                
            else:
                j -= 1
        except Exception as e:
            j -= 1
        j += 1

    def downloadPage(self, url):
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
            req = self.urllib.request.Request(url, headers=headers)
            resp = self.PIL.Image.open(self.urllib.request.urlopen(req))
            return resp

        except Exception as e:
            print(e)
rankList()
