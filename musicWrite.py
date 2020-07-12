import wave
import struct
import math
import sys
 
def write_frame(time,freq,framerate,file,wave=0.8,sampwidth=2):
    #time 持续时间 freq 音频频率 framerate采样频率 file 音频文件 wave 音量 sampwidth 采样深度
    t=0#时刻
    step=1.0/framerate #每帧间隔时长
    fw=2.0*math.pi*freq #频率控制参数
    wave=wave*(math.pow(2,sampwidth*8-1)-1)#音量控制
    while t<=time:
        v=int(math.sin(t*fw)*wave)#对波采样  math.sin(t*fw)产生freq频率的正弦波
        t+=step#更新时刻
        #最后这里是与sampwidth的值有关的，下面语句当前仅当sampwidth=2时成立，详细信息参考struct.pack()
        file.writeframesraw(struct.pack("h",v))#写入文件  struct.pack("h",v)将有符号整数v转化成16比特2进制
    
def init(path="./test.wav"):
    music_file=wave.open(path,"w")         #打开或创建wav文件

    # 依据C.wav等对应的getparam设置
    music_file.setnchannels(1)             #设置声道数 1 单声道
    music_file.setframerate(44100)         #设置帧率 44.1kHz
    music_file.setsampwidth(2)             #设置采样宽度2B 16bit
    
    # 读取每个音符
    c_data = wave.open("source/C.wav","r")
    d_data = wave.open("source/D.wav","r")
    e_data = wave.open("source/E.wav","r")
    f_data = wave.open("source/F.wav","r")
    g_data = wave.open("source/G.wav","r")
    a_data = wave.open("source/A.wav","r")
    b_data = wave.open("source/B.wav","r")
    c__data = wave.open("source/C_.wav","r")
    o_data = wave.open("source/O.wav","r")
    # 音符最短长度
    n_frame = min(a_data.getnframes(),b_data.getnframes(),c_data.getnframes(),c__data.getnframes(),\
        d_data.getnframes(),e_data.getnframes(),f_data.getnframes(),g_data.getnframes())
    # 音符裁剪至相同长度
    c = c_data.readframes(n_frame)
    d = d_data.readframes(n_frame)
    e = e_data.readframes(n_frame)
    f = f_data.readframes(n_frame)
    g = g_data.readframes(n_frame)
    a = a_data.readframes(n_frame)
    b = b_data.readframes(n_frame)
    c_ = c__data.readframes(n_frame)
    o = o_data.readframes(n_frame)

    # 读取每个音符
    c2_data = wave.open("source/Cx2.wav","r")
    d2_data = wave.open("source/Dx2.wav","r")
    e2_data = wave.open("source/Ex2.wav","r")
    f2_data = wave.open("source/Fx2.wav","r")
    g2_data = wave.open("source/Gx2.wav","r")
    a2_data = wave.open("source/Ax2.wav","r")
    b2_data = wave.open("source/Bx2.wav","r")
    c2__data = wave.open("source/C_x2.wav","r")
    o2_data = wave.open("source/Ox2.wav","r")
    # 音符最短长度
    n_frame = min(a2_data.getnframes(),b2_data.getnframes(),c2_data.getnframes(),c2__data.getnframes(),\
        d2_data.getnframes(),e2_data.getnframes(),f2_data.getnframes(),g2_data.getnframes())
    # 音符裁剪至相同长度
    cx2 = c2_data.readframes(n_frame)
    dx2 = d2_data.readframes(n_frame)
    ex2 = e2_data.readframes(n_frame)
    fx2 = f2_data.readframes(n_frame)
    gx2 = g2_data.readframes(n_frame)
    ax2 = a2_data.readframes(n_frame)
    bx2 = b2_data.readframes(n_frame)
    cx2_ = c2__data.readframes(n_frame)
    ox2 = o2_data.readframes(n_frame)

    return n_frame,music_file,a,b,c,c_,d,e,f,g,o,ax2,bx2,cx2,cx2_,dx2,ex2,fx2,gx2,ox2

def write_music_box(path,filename):
    #############################################
    # 使用八个音阶写入 不能变调只能变速（全音+半音）#
    #############################################
    n_frame,music_file,a,b,c,c_,d,e,f,g,o,ax2,bx2,cx2,cx2_,dx2,ex2,fx2,gx2,ox2 = init(path)
    
    music_map = {'1':c,'2':d,'3':e,'4':f,'5':g,'6':a,'7':b,'8':c_,'0':o,
                 '11':cx2,'22':dx2,'33':ex2,'44':fx2,'55':gx2,'66':ax2,'77':bx2,'88':cx2_,'00':ox2}
    fp = open(filename).readlines()
    
    for line in fp[1:]:
        for i in line.split( ):#直接 不会有\n 使用' '会将'1 2 3'分成'1''2''3\n'
            if(len(i)==2):
                if(i[0]==i[1]):
                    music_file.writeframes(music_map[i[0]*2])
                else:
                    music_file.writeframes(music_map[i[0]*2])
                    music_file.writeframes(music_map[i[1]*2])
            else:
                music_file.writeframes(music_map[i])

    music_file.close()

def write_music_freq(path,filename):
    ############################################
    # 直接写入每个音阶的频率，见"two_tigers.wav" #
    ############################################

    tw=wave.open(path,"w")
    framerate = 44100
    tw.setnchannels(1)            
    tw.setframerate(framerate)        
    tw.setsampwidth(2)            

    # C5 - C6对应音频
    C  = 523.25
    D  = 587.33
    E  = 659.25
    F  = 698.46
    G  = 783.99
    A  = 880.00
    B  = 987.77
    C_ = 1046.50
    O  = 0

    music_map = {'1':C,'2':D,'3':E,'4':F,'5':G,'6':A,'7':B,'8':C_,'0':O}
    fp = open(filename).readlines()
    info = fp[0].split( )# 获取简谱信息：节拍和每分钟拍数
    b1,b2 = info[0].split(':')[1].split('-')# b1表示几分音符为一拍 b2表示一节几拍
    if len(info) == 1:# 默认每拍0.5s 四分音符一拍
        time = 0.5 * int(b1) / 4
    else:# 依据每分钟拍数计算每拍时长
        bpm = info[1].split(':')[1]
        time = 60.0 / int(bpm)
    for line in fp[1:]:
        for i in line.split( ):#直接 不会有\n 使用' '会将'1 2 3'分成'1''2''3\n'
            #只处理全音和半音，最复杂情况如1+5-6-，其他情况12 1- 12+ 1+2 1-2- 1+22 332-
            if(len(i)==1):
                write_frame(time=time,freq=music_map[i],framerate=framerate,file=tw)
            elif(len(i)==2):
                if(i.isdigit()):
                    if(i[0]==i[1]):
                        write_frame(time=time,freq=music_map[i[0]],framerate=framerate,file=tw)
                    else:
                        write_frame(time=time/2,freq=music_map[i[0]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[1]],framerate=framerate,file=tw)
                else:
                    if(i[1]=='+'):
                        write_frame(time=time,freq=music_map[i[0]]*2,framerate=framerate,file=tw)
                    elif(i[1]=='-'):
                        write_frame(time=time,freq=music_map[i[0]]/2,framerate=framerate,file=tw)
                    else:
                        print('error!')
                        exit()
            elif(len(i)==3):
                if(i.isdigit()):
                    if(i[0]==i[1]):
                        write_frame(time=time,freq=music_map[i[0]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[2]],framerate=framerate,file=tw)
                    elif(i[1]==i[2]):
                        write_frame(time=time/2,freq=music_map[i[0]],framerate=framerate,file=tw)
                        write_frame(time=time,freq=music_map[i[1]],framerate=framerate,file=tw)
                    else:
                        write_frame(time=time/2,freq=music_map[i[0]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[1]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[2]],framerate=framerate,file=tw)
                else:
                    if(i[1]=='+'):
                        write_frame(time=time/2,freq=music_map[i[0]]*2,framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[2]],framerate=framerate,file=tw)
                    elif(i[1]=='-'):
                        write_frame(time=time/2,freq=music_map[i[0]]/2,framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[2]],framerate=framerate,file=tw)
                    elif(i[2]=='+'):
                        write_frame(time=time/2,freq=music_map[i[0]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[1]]*2,framerate=framerate,file=tw)
                    elif(i[2]=='-'):
                        write_frame(time=time/2,freq=music_map[i[0]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[1]]/2,framerate=framerate,file=tw)
                    else:
                        print('error!')
                        exit()
            elif(len(i)==6):
                if(i[0]==i[2]):
                    if(i[1]=='+'):
                        write_frame(time=time,freq=music_map[i[0]]*2,framerate=framerate,file=tw)
                    elif(i[1]=='-'):
                        write_frame(time=time,freq=music_map[i[0]]/2,framerate=framerate,file=tw)
                    else:
                        print('error!')
                        exit()
                    if(i[5]=='+'):
                        write_frame(time=time/2,freq=music_map[i[4]]*2,framerate=framerate,file=tw)
                    elif(i[5]=='-'):
                        write_frame(time=time/2,freq=music_map[i[4]]/2,framerate=framerate,file=tw)
                    else:
                        print('error!')
                        exit()
                elif(i[2]==i[4]):
                    if(i[1]=='+'):
                        write_frame(time=time/2,freq=music_map[i[0]]*2,framerate=framerate,file=tw)
                    elif(i[1]=='-'):
                        write_frame(time=time/2,freq=music_map[i[0]]/2,framerate=framerate,file=tw)
                    else:
                        print('error!')
                        exit()
                    if(i[5]=='+'):
                        write_frame(time=time,freq=music_map[i[4]]*2,framerate=framerate,file=tw)
                    elif(i[5]=='-'):
                        write_frame(time=time,freq=music_map[i[4]]/2,framerate=framerate,file=tw)
                    else:
                        print('error!')
                        exit()
                else:
                    if(i[1]=='+'):
                        write_frame(time=time/2,freq=music_map[i[0]]*2,framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[2]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[4]],framerate=framerate,file=tw)
                    elif(i[1]=='-'):
                        write_frame(time=time/2,freq=music_map[i[0]]/2,framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[2]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[4]],framerate=framerate,file=tw)
                    elif(i[3]=='+'):
                        write_frame(time=time/2,freq=music_map[i[0]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[2]]*2,framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[4]],framerate=framerate,file=tw)
                    elif(i[3]=='-'):
                        write_frame(time=time/2,freq=music_map[i[0]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[2]]/2,framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[4]],framerate=framerate,file=tw)
                    elif(i[5]=='+'):
                        write_frame(time=time/2,freq=music_map[i[0]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[2]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[4]]*2,framerate=framerate,file=tw)
                    elif(i[5]=='-'):
                        write_frame(time=time/2,freq=music_map[i[0]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[2]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[4]]/2,framerate=framerate,file=tw)
                    else:
                        print('error!')
                        exit()
            else:#len(i)==4
                if(i[1].isdigit()):
                    if(i[0]==i[1]):
                        write_frame(time=time,freq=music_map[i[0]],framerate=framerate,file=tw)
                    else:
                        write_frame(time=time/2,freq=music_map[i[0]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[1]],framerate=framerate,file=tw)
                    if(i[3]=='+'):
                        write_frame(time=time/2,freq=music_map[i[2]]*2,framerate=framerate,file=tw)
                    elif(i[3]=='-'):
                        write_frame(time=time/2,freq=music_map[i[2]]/2,framerate=framerate,file=tw)
                elif(i[3].isdigit()):
                    if(i[1]=='+'):
                        write_frame(time=time/2,freq=music_map[i[0]]*2,framerate=framerate,file=tw)
                    elif(i[1]=='-'):
                        write_frame(time=time/2,freq=music_map[i[0]]/2,framerate=framerate,file=tw) 
                    if(i[2]==i[3]):
                        write_frame(time=time,freq=music_map[i[2]],framerate=framerate,file=tw)
                    else:
                        write_frame(time=time/2,freq=music_map[i[2]],framerate=framerate,file=tw)
                        write_frame(time=time/2,freq=music_map[i[3]],framerate=framerate,file=tw)
                else:
                    if(i[1]=='+'):
                        write_frame(time=time/2,freq=music_map[i[0]]*2,framerate=framerate,file=tw)
                    elif(i[1]=='-'):
                        write_frame(time=time/2,freq=music_map[i[0]]/2,framerate=framerate,file=tw)
                    else:
                        print('error!')
                        exit()
                    if(i[3]=='+'):
                        write_frame(time=time/2,freq=music_map[i[2]]*2,framerate=framerate,file=tw)
                    elif(i[3]=='-'):
                        write_frame(time=time/2,freq=music_map[i[2]]/2,framerate=framerate,file=tw)
                    else:
                        print('error!')
                        exit()
               
    '''

    #56 54 3 1 56 54 3 1 
    write_frame(time=0.25, freq=G,   framerate=44100, file=tw)
    write_frame(time=0.25, freq=A,   framerate=44100, file=tw)
    write_frame(time=0.25, freq=G,   framerate=44100, file=tw)
    write_frame(time=0.25, freq=F,   framerate=44100, file=tw)
    write_frame(time=0.5,  freq=E,   framerate=44100, file=tw)
    write_frame(time=0.5,  freq=C,   framerate=44100, file=tw)
    write_frame(time=0.25, freq=G,   framerate=44100, file=tw)
    write_frame(time=0.25, freq=A,   framerate=44100, file=tw)
    write_frame(time=0.25, freq=G,   framerate=44100, file=tw)
    write_frame(time=0.25, freq=F,   framerate=44100, file=tw)
    write_frame(time=0.5,  freq=E,   framerate=44100, file=tw)
    write_frame(time=0.5,  freq=C,   framerate=44100, file=tw)
    
    #2 6（低音） 1 - 2 6（低音） 1 -
    write_frame(time=0.5, freq=D,    framerate=44100, file=tw)
    write_frame(time=0.5, freq=A/2,  framerate=44100, file=tw)
    write_frame(time=0.5, freq=C,    framerate=44100, file=tw)
    write_frame(time=0.5, freq=0,    framerate=44100, file=tw)
    write_frame(time=0.5, freq=D,    framerate=44100, file=tw)
    write_frame(time=0.5, freq=A/2,  framerate=44100, file=tw)
    write_frame(time=0.5, freq=C,    framerate=44100, file=tw)
    write_frame(time=0.5, freq=0,    framerate=44100, file=tw)
    '''
    
    tw.close()
 
    # C 1 do
    # D 2 re
    # E 3 mi
    # F 4 fa
    # G 5 so 
    # A 6 la
    # B 7 si

    # A4 = 440
    # 中央C是C4
    # 每隔一个8度翻倍
    # 音符频率对照https://pages.mtu.edu/~suits/notefreqs.html

def main():
    filename = sys.argv[1]
    music_type = sys.argv[2] # 0 -> box , 1 -> freq
    path = filename.replace('txt','wav')

    if music_type == '0':
        write_music_box(path,filename)
    elif music_type == '1':
        write_music_freq(path,filename)
    print(path+' has been writen...')
main()
