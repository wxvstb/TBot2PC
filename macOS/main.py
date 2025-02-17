import rumps
import sys, subprocess
import psutil
import json

     
with open('resources/api.json', 'r') as file:
              data = json.load(file)
pid1 = data["pid"]
     

class MyApp(rumps.App):
    def __init__(self):
        super(MyApp, self).__init__("TBot2PC", icon="resources/icon5.png")
        if psutil.pid_exists(pid1):
           self.icon = "resources/icon_on.png"
        else:
            print(f"Процес з PID {pid1} не знайдено.")
        
        
    
    

    
    @rumps.clicked("Start")
    def on_start(self, _):
        with open('resources/api.json', 'r') as file:
              data = json.load(file)
        pid = data["pid"]
        api = data["api"]
        if pid == -1 and api != "":
            self.icon = "resources/icon_on.png"
            subprocess.Popen([sys.executable, 'tel.py'])
        
        
    @rumps.clicked("Stop")
    def on_stop(self, _):
        with open('resources/api.json', 'r') as file:
             data = json.load(file)
        pid = data["pid"]
        p = psutil.Process(pid)
        p.terminate()
        data["pid"] = -1
        with open('resources/api.json', "w", encoding="utf-8") as file:
                 json.dump(data, file, ensure_ascii=False, indent=4)
        self.icon = "resources/icon5.png"
    
    @rumps.clicked("Setting")
    def on_hello(self, _):
        subprocess.Popen([sys.executable, 'py.py'])
        with open('resources/api.json', 'r') as file:
              data = json.load(file)
        pid = data["pid"]
        if pid == -1:
            self.icon = "resources/icon5.png"
        else:
            self.icon = "resources/icon_on.png"
        
    
        

if __name__ == "__main__":
    app = MyApp()
    app.run()

