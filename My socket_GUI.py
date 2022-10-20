import tkinter as tk
import socket
import tkinter
import tkinter.messagebox
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd1 = "GET"
cmd2 = " "
# cmd3 ="http://data.pr4e.org/romeo.txt"
cmd4 = " "
cmd5 = "HTTP/1.0\r\n\r\n"

list = {}

root = tk.Tk()
root.title("My socket_GUI")
root.geometry("500x250")
# root---界面（需要放在那个界面），show----输入的字符显示为*，可以设置成show=none
e = tk.Entry(root)

e.pack()


def insert_point():
    cmd3 = str(e.get())
    cmd = cmd1 + cmd2 + cmd3 + cmd4 + cmd5
    cmd = cmd.encode()
    mysock.send(cmd)
    if len(cmd3)!=0:
     while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode(), end='')
        t1.insert('insert', data)
    else :
        tkinter.messagebox.showerror('错误','请输入地址')
    mysock.close()




# root---界面（需要放在那个界面），text----显示文本
# width----宽度   height----高度  command----命令（执行哪个函数）
b1 = tk.Button(root, text=" 访问地址", width=15, height=2, command=insert_point)
b1.pack()

# root---界面（需要放在那个界面），height ----文本框宽度
t1 = tk.Text(root)
t1.pack(fill="x")

root.mainloop()
