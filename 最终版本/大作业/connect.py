import socket
import threading
import json  # json.dumps(some)打包   json.loads(some)解包
import tkinter
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText  # 导入多行文本框用到的包

IP = ''         # 公共IP
PORT = ''       # 公共port
user = ''       # 公共user
users = []      # 用户列表
chat = '已连接'  # 设置给已经连接的用户发消息

# 登陆窗口
loginRoot = tkinter.Tk()           # 建立主窗口
loginRoot.title('选择作为哪一端：')   # 标题为“选择作为哪一端（服务器/客户端）
loginRoot['height'] = 110          # 窗口高度
loginRoot['width'] = 270           # 窗口宽度
loginRoot.resizable(0, 0)          # 限制窗口大小，这里面是布尔值

IP1 = tkinter.StringVar()          # 把获取的值以字符串输出
IP1.set('127.0.0.1:8888')          # 默认显示的ip和端口
User = tkinter.StringVar()         # 把获取的值以字符串输出
User.set('')                       # 输入昵称（服务器/客户端）

# 地址端口标签
labelIP = tkinter.Label(loginRoot, text='地址:端口')
labelIP.place(x=20, y=10, width=100, height=20)

entryIP = tkinter.Entry(loginRoot, width=80, textvariable=IP1)
entryIP.place(x=120, y=10, width=130, height=20)

# 用户名标签
labelUser = tkinter.Label(loginRoot, text='昵称')
labelUser.place(x=30, y=40, width=80, height=20)

entryUser = tkinter.Entry(loginRoot, width=80, textvariable=User)
entryUser.place(x=120, y=40, width=130, height=20)


# 登录按钮
def login(*args):
    global IP, PORT, user
    IP, PORT = entryIP.get().split(':')     # 获取IP和端口号
    PORT = int(PORT)                        # 端口号需要为int类型
    user = entryUser.get()
    if not user:                            # 如果没有输入就点登录
        tkinter.messagebox.showerror('温馨提示', message='请输入任意的用户名！')
    else:
        loginRoot.destroy()                 # 关闭窗口


loginRoot.bind('<Return>', login)           # 回车绑定登录功能
but = tkinter.Button(loginRoot, text='登录', command=login)
but.place(x=100, y=70, width=70, height=30)

loginRoot.mainloop()                        # 调用tk的主循环

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
if user:
    s.send(user.encode())                   # 发送用户名
else:
    s.send('no'.encode())                   # 没有输入用户名则标记no

# 如果没有用户名则将ip和端口号设置为用户名
addr = s.getsockname()                      # 获取ip和端口号
addr = addr[0] + ':' + str(addr[1])         # 把地址转为字符串后赋值给addr
if user == '':
    user = addr

# 聊天窗口
# 创建图形界面
root = tkinter.Tk()                         # 建立主界面
root.title(user)                            # 窗口命名为用户名
root['height'] = 400                        # 界面高度
root['width'] = 580                         # 界面宽度
root.resizable(0, 0)                        # 限制窗口大小，两个值都是布尔值

# 创建多行文本框
listbox = ScrolledText(root)
listbox.place(x=5, y=0, width=570, height=320)
# 文本框使用的字体颜色
listbox.tag_config('red', foreground='red')      # 红色
listbox.tag_config('blue', foreground='blue')    # 蓝色
listbox.insert(tkinter.END, '连接成功！', 'blue')  # 开始连接时发送连接成功

# 表情功能代码部分
# 创建按钮, 使用全局变量, 方便创建和销毁
b1 = ''
b2 = ''
b3 = ''
b4 = ''
b5 = ''
b6 = ''
b7 = ''
b8 = ''

# 将图片打开存入变量中
p1 = tkinter.PhotoImage(file='./emoji/facepalm.png')
p2 = tkinter.PhotoImage(file='./emoji/smirk.png')
p3 = tkinter.PhotoImage(file='./emoji/ebgy.png')
p4 = tkinter.PhotoImage(file='./emoji/smart.png')
p5 = tkinter.PhotoImage(file='./emoji/bear.png')
p6 = tkinter.PhotoImage(file='./emoji/shy.png')
p7 = tkinter.PhotoImage(file='./emoji/surprise.png')
p8 = tkinter.PhotoImage(file='./emoji/cat.png')

# 用字典将标记与表情图片一一对应, 用于后面接收标记判断表情贴图
dic = {'aa**': p1, 'bb**': p2, 'cc**': p3, 'dd**': p4, 'ff**': p5, 'gg**': p6, 'hh**': p7, 'ii**': p8}
ee = 0  # 判断表情面板开关的标志


# 发送表情图标记的函数, 在按钮点击事件中调用
def mark(exp):  # 参数是发的表情图标记, 发送后将按钮销毁
    global ee
    mes = exp + ':;' + user + ':;' + chat
    s.send(mes.encode())
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    b5.destroy()
    b6.destroy()
    b7.destroy()
    b8.destroy()
    ee = 0


# 四个对应的函数，调用进行销毁
def bb1():
    mark('aa**')


def bb2():
    mark('bb**')


def bb3():
    mark('cc**')


def bb4():
    mark('dd**')


def bb5():
    mark('ff**')


def bb6():
    mark('gg**')


def bb7():
    mark('hh**')


def bb8():
    mark('ii**')


def express():  # 创建表情的点击按钮
    global b1, b2, b3, b4, b5, b6, b7, b8, ee
    if ee == 0:
        ee = 1
        b1 = tkinter.Button(root, command=bb1, image=p1,
                            relief=tkinter.FLAT, bd=0)
        b2 = tkinter.Button(root, command=bb2, image=p2,
                            relief=tkinter.FLAT, bd=0)
        b3 = tkinter.Button(root, command=bb3, image=p3,
                            relief=tkinter.FLAT, bd=0)
        b4 = tkinter.Button(root, command=bb4, image=p4,
                            relief=tkinter.FLAT, bd=0)
        b5 = tkinter.Button(root, command=bb5, image=p5,
                            relief=tkinter.FLAT, bd=0)
        b6 = tkinter.Button(root, command=bb6, image=p6,
                            relief=tkinter.FLAT, bd=0)
        b7 = tkinter.Button(root, command=bb7, image=p7,
                            relief=tkinter.FLAT, bd=0)
        b8 = tkinter.Button(root, command=bb8, image=p8,
                            relief=tkinter.FLAT, bd=0)
        b1.place(x=5, y=248)
        b2.place(x=75, y=248)
        b3.place(x=145, y=248)
        b4.place(x=215, y=248)
        b5.place(x=285, y=248)
        b6.place(x=355, y=248)
        b7.place(x=425, y=248)
        b8.place(x=495, y=248)
    else:
        ee = 0
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()
        b7.destroy()
        b8.destroy()


# 创建表情按钮
eBut = tkinter.Button(root, text='表情', command=express)
eBut.place(x=5, y=320, width=60, height=30)

# 创建输入文本框和关联变量
a = tkinter.StringVar()
a.set('')
entry = tkinter.Entry(root, width=120, textvariable=a)
entry.place(x=5, y=350, width=570, height=40)


def send(*args):
    # 没有添加的话发送信息时会提示没有聊天对象
    users.append('已连接')
    print(chat)
    if chat not in users:
        tkinter.messagebox.showerror('温馨提示', message='没有聊天对象!')
        return
    mes = entry.get() + ':;' + user + ':;' + chat  # 添加聊天对象标记
    s.send(mes.encode())
    a.set('')                                      # 发送后清空文本框


# 创建发送按钮
button = tkinter.Button(root, text='发送', command=send)
button.place(x=515, y=353, width=60, height=30)
root.bind('<Return>', send)                       # 绑定回车发送信息


# 用于时刻接收服务端发送的信息并打印
def recv():
    global users
    while True:
        data = s.recv(1024)
        data = data.decode()
        # 没有捕获到异常则表示接收到的是在线用户列表
        try:
            data = json.loads(data)
            users = data
        except:
            data = data.split(':;')
            data1 = data[0].strip()            # 消息
            data2 = data[1]                    # 发送信息的用户名
            data3 = data[2]                    # 聊天对象
            markk = data1.split('：')[1]
            # 判断是不是图片
            pic = markk.split('#')
            # 判断是不是表情
            # 如果字典里有则贴图
            if (markk in dic) or pic[0] == '``':
                data4 = '\n' + data2 + '：'  # 例:名字-> \n名字：
                if data3 == chat:
                    if data2 == user:       # 如果是自己则将则字体变为红色
                        listbox.insert(tkinter.END, data4, 'red')
                        listbox.image_create(tkinter.END, image=dic[markk])
                    else:
                        listbox.insert(tkinter.END, data4, 'blue')  # END将信息加在最后一行
                        listbox.image_create(tkinter.END, image=dic[markk])

            else:
                data1 = '\n' + data1
                if data3 == chat:
                    if data2 == user:  # 如果是自己则将则字体变为红色
                        listbox.insert(tkinter.END, data1, 'red')
                    else:
                        listbox.insert(tkinter.END, data1, 'blue')  # END将信息加在最后一行

            listbox.see(tkinter.END)                                # 显示在最后


def break_to_server():                                              # 断开连接
    s.close()


button = tkinter.Button(root, text='离开', command=break_to_server)
button.place(x=315, y=353, width=60, height=30)


def clear_to_data():                                               # 清空输入框
    a.set('')


button = tkinter.Button(root, text='清空', command=clear_to_data)
button.place(x=415, y=353, width=60, height=30)

r = threading.Thread(target=recv)
r.start()  # 开始线程接收信息

root.mainloop()  # tk循环
s.close()  # 关闭图形界面后关闭TCP连接
