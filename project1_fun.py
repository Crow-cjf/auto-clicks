# coding=gbk
# ����
from time import sleep
import pyautogui as gui
import cv2
import pyscreeze 


def rapid_clicks(targets,text=None):
    """
    �Զ����targets,�ڶ�Ӧ������������ı�text
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
    ������ȡͼ����������Զ���ȡͼ�겢����ͼ����б�
    '''
    # ������ͼ��
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
    ����ͼ�꣬��λ�����
    '''
    # ��¼Ѱ���Ƿ�ɹ�
    result=0
    
    location=gui.locateOnScreen(target,grayscale=True,confidence=.9)
    if location:
        gui.click(gui.center(location),button='left')
        result=1
        
    return result

def clicks(targets,time=5):
    
    number=len(targets)
    #ѭ�����
    for value in range(time):
        
        print(str(value+1)+' Time:')
        #��¼һ���гɹ�����Ĵ���
        success=0       

        #һ���Զ����
        for num in range(number):
            #��¼���ĳ��ͼ��ʧ�ܵĴ���
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

    # ѭ�����
    for value in range(time):
        print(str(value+1)+' Time:')
        
        # ��¼�ɹ��������
        success=0
        #һ��ѭ��
        for num in range(number):
            fault=0
            while True:
                # ����
                screenshot=pyscreeze.screenshot('my_screenshot.png')
                temp=cv2.imread(r'my_screenshot.png',cv2.IMREAD_GRAYSCALE)
                
                # ��ȡ���ͼ�꼰�������
                theight,twidth=targets[num].shape[:2]
                tempheight,tempwidth=temp.shape[:2]
                
                # ����ϵͳ�ع��������
                scaletemp=cv2.resize(temp,(int(tempwidth/screenScale),int(tempheight/screenScale)))
                
                # �ڽ�����ƥ��ͼ��λ��
                res=cv2.matchTemplate(scaletemp,targets[num],cv2.TM_CCOEFF_NORMED)
                min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
                
                # �ɹ��ҵ�ͼ�꣬ȷ��ͼ�����Ĳ����һ��,������һ��ͼ��ĵ��
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
                    
                    # ���ʧ�ܵ����һͼ�꣬��������
                elif fault==90:
                    print('No found target '+str(num))
                    break
                # Ѱ��ʧ�ܣ���ֹͣһ��ʱ����ٴν�����ƥ��ͼ��
                fault +=1
                sleep(1)
        
        if success==number:
            print('Succeed!')

    print('Finished '+str(time)+' Time.')
                
