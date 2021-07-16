import subprocess

class SearchAndConnect:
    def __init__(self):
        self.defaultSSID = "THORBELL"
        self.defaultPASS = "applica07"

    def search(self):
        command = "nmcli device wifi list"
        list=subprocess.run(command,capture_output=True, text=True, shell=True)     #Obtiene una lista de redes
        self.connected=False                #Asume que no está conectada a ninguna
        for item in list.stdout:            #Y busca, si alguna figura
            if(item.startswith("*"):        #que comienza con un asterisco "*"
                self.connected=True         #Es porque está conectada a ésa
        
        return self.connected

    def createHotspot(self):
        command=f"nmcli device wifi hotspot ssid {self.defaultSSID} password {self.defaultPASS}"
        return=subprocess.run(command,capture_output=True, text=True, shell=True)
    
