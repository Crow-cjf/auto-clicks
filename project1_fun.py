# coding=gbk
# 导入
from time import sleep
import pyautogui as gui
import cv2
import pyscreeze 


def rapid_clicks(targets,text=None):
    """
    自动点击targets,在对应点击次数输入文本text
    """
    if text:
        orders=text.keys()
        texts=list(text.values())
        for num in range(len(targets)):
            while True:
                if locate_click(targets[num]):
                    if num+1 in orders:
                        gui.write(texts.pop(0))
                    break
    else:
        for num in range(len(targets)):
            while True:
                if locate_click(targets[num]):
                    break


def images_read(number=30):
    '''
    给出读取图标的数量，自动读取图标并返回图标的列表
    '''
    # 读入点击图标
    targets=[]
    for value in range(number):
        target=r'target'+str(value+1)+'.png'
        
        image=cv2.imread(target,cv2.IMREAD_GRAYSCALE)
        if image is None:
            break
        else:
            targets.append(image)
            
    return targets
    
def locate_click(target):
    '''
    输入图标，定位并点击
    '''
    # 记录寻标是否成功
    result=0
    
    location=gui.locateOnScreen(target,grayscale=True,confidence=.9)
    if location:
        gui.click(gui.center(location),button='left')
        result=1
        
    return result

def clicks(targets,time=5):
    
    number=len(targets)
    #循环点击
    for value in range(time):
        
        print(str(value+1)+' Time:')
        #记录一趟中成功点击的次数
        success=0       

        #一趟自动点击
        for num in range(number):
            #记录点击某个图标失败的次数
            fault=0
            while True:
                if locate_click:
                    success+=1
                    sleep(0.5)
                    break
                
                elif fault == 60:
                    print('No found target '+str(num+1)+'!')
                    break
                    
                fault+=1
                sleep(1)
                
        if success==number:
            print('Succeed!')
            
def cycle_clicks(targets,time=5):
    
    screenScale=1
    number=len(targets)

    # 循环点击
    for value in range(time):
        print(str(value+1)+' Time:')
        
        # 记录成功点击次数
        success=0
        #一次循环
        for num in range(number):
            fault=0
            while True:
                # 截屏
                screenshot=pyscreeze.screenshot('my_screenshot.png')
                temp=cv2.imread(r'my_screenshot.png',cv2.IMREAD_GRAYSCALE)
                
                # 读取点击图标及截屏宽高
                theight,twidth=targets[num].shape[:2]
                tempheight,tempwidth=temp.shape[:2]
                
                # 根据系统重构截屏宽高
                scaletemp=cv2.resize(temp,(int(tempwidth/screenScale),int(tempheight/screenScale)))
                
                # 在截屏中匹配图标位置
                res=cv2.matchTemplate(scaletemp,targets[num],cv2.TM_CCOEFF_NORMED)
                min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
                
                # 成功找到图标，确定图标中心并点击一下,进行下一个图标的点击
                if(max_val>=0.9):
                    top_left=max_loc
                    tagHalfW=int(twidth/2)
                    tagHalfH=int(theight/2)
                    tagCenterX=top_left[0]+tagHalfW
                    tagCenterY=top_left[1]+tagHalfH
                    pyautogui.click(tagCenterX,tagCenterY,button='left') 
                    success+=1
                    sleep(0.5)
                    break
                    
                    # 多次失败点击下一图标，避免死锁
                elif fault==90:
                    print('No found target '+str(num))
                    break
                # 寻找失败，在停止一段时间后，再次截屏，匹配图标
                fault +=1
                sleep(1)
        
        if success==number:
            print('Succeed!')

    print('Finished '+str(time)+' Time.')
                
