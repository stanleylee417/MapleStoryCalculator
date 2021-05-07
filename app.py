import sys
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from Calculator import Ui_Form


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #page0
        self.ui.page0_btn[0].clicked.connect(self.submit_ui)
        self.ui.page0_btn[1].clicked.connect(self.save_data)
        self.ui.page0_btn[2].clicked.connect(self.read_data)
        #page1
        self.ui.page1_btn[0].textChanged.connect(self.equivalent)
        self.ui.page1_btn[1].activated.connect(self.equivalent)
        for i in range(9):
            self.ui.page1_data1[i].textChanged.connect(self.improve)
        #page2
        self.ui.page2_btn[0].clicked.connect(self.star)
        #page3
        self.ui.level.activated.connect(self.setlevel)
        for i in range(6):
            self.ui.page3_data1[i].textChanged.connect(self.StarFire)
        #Description
        self.ui.connection.activated.connect(self.connection)
        self.ui.setup_class.activated.connect(self.setup_class)
        
        self.move(20,20)
        self.show()
    
    def submit_ui(self):
        empty=[10,68,78.2,10,11,48.57,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.page0_data=[]
        for i in range(len(self.ui.page0_data)):    #取得並檢查UI能力值
            try:
                if (i==12) or (i==14):
                    num=float(self.ui.page0_data[i].currentText())
                else:
                    num=float(self.ui.page0_data[i].text())
                    if num<empty[i]:
                        num=empty[i]
            except Exception:
                num=empty[i]
                pass
            if (i!=9) and (i!=12) and (i!=14):
                self.ui.page0_data[i].setText(str(int(num)))
            self.page0_data.append(num)

        try:    #計算屬性
            self.ui_set()
            self.equivalent()
            self.improve()
            self.star()
            self.StarFire()
            #啟用增幅設定
            for i in self.ui.page1_btn:
                i.setEnabled(True)
            for i in self.ui.page1_data1:
                i.setEnabled(True)
            for i in self.ui.page2_data:
                for j in i:
                    j.setEnabled(True)
            for i in self.ui.page2_data1:
                i.setEnabled(True)
            for i in self.ui.page2_btn:
                i.setEnabled(True)
            self.ui.level.setEnabled(True)
            for i in self.ui.page3_data1:
                i.setEnabled(True)
        except Exception:   #重設UI
            for i in range(20):
                if (i!=12) and (i!=14):
                    self.ui.page0_data[i].setText(str(empty[i]))
            self.submit_ui()
            pass
        
    def ui_set(self):
        setPER=[6,7,8,9,10,11,14,19]
        for i in setPER:
            self.page0_data[i]/=100
        #攻擊力
        self.att = self.page0_data[5] / ((4*self.page0_data[2]+self.page0_data[4])*(1+self.page0_data[11])*(1+self.page0_data[6])*(1+self.page0_data[7])*0.01*self.page0_data[12])
        #不吃%主屬
        self.nm  = self.page0_data[15]+self.page0_data[17]+self.page0_data[13]*10
        #不吃%副屬
        self.ns  = self.page0_data[16]+self.page0_data[18]
        #主屬%
        self.mp  = round((self.page0_data[2]-self.page0_data[1]) / ((self.page0_data[0]*5+18)*self.page0_data[14]),2)-1
        self.mp  = (self.page0_data[2]-self.page0_data[1]) / ((self.page0_data[0]*5+18)*self.page0_data[14])-1
        #吃%的主屬
        self.ym  = (self.page0_data[2]-self.nm) / (1+self.mp) - (self.page0_data[0]*5+18)*(1+self.page0_data[14])
        #吃%的副屬
        self.ys  = (self.page0_data[4]-self.page0_data[3]) / 0.1
        #副屬%
        self.sp  = ((self.page0_data[4]-self.ns) / self.ys) -1
        
    def save_data(self):
        try:
            self.submit_ui()
            fileName,filetype=QFileDialog.getSaveFileName(self,"另存新檔","./","aries (*.aries)")
            data=open(fileName,"w")
            data_save=[]
            for i in range(len(self.ui.page0_data)):
                if (i==12) or (i==14):
                    data_save.append(str(self.ui.page0_data[i].currentIndex())+"\n")
                else:
                    data_save.append(str(int(self.ui.page0_data[i].text()))+"\n")
            data.writelines(data_save)
            data.close()
        except Exception:
            pass
    
    def read_data(self):
        try:
            fileName, filetype = QFileDialog.getOpenFileName(self,"選擇檔案","./","aries (*.aries)")
            data=open(fileName,"r")
            data_save=[]
            for i in iter(data):
                i=i.replace("\n","")
                data_save.append(i)
            for i in range(len(self.ui.page0_data)):
                if (i==12) or (i==14):
                    self.ui.page0_data[i].setCurrentIndex(int(data_save[i]))
                else:
                    self.ui.page0_data[i].setText(str(data_save[i]))
            data.close()
            self.submit_ui()
        except Exception:
            pass

    def equivalent(self):
        try:
            input=float(self.ui.page1_btn[0].text())
        except Exception:
            input=1
            self.ui.page1_btn[0].setText(str(input))
            pass
        curIndex=self.ui.page1_btn[1].currentIndex()
        if curIndex==8:
            curIndex=9
        
        data=self.calc()
        page1_data=[]
        for i in range(8):
            page1_data.append((data[curIndex]-1)/(data[i]-1))
        
        page1_data.append((data[curIndex]-1)/(data[9]-1))
        for i in range(9):
            self.ui.page1_data[i].setText(str(round(page1_data[i]*input,2)))
        
    def improve(self):
        input=[]
        for i in range(9):
            if i==7:
                try:
                    num=float(self.ui.page1_data1[i].text())
                except Exception:
                    num=0
                    self.ui.page1_data1[i].setText(str(num))
                    pass
            else:
                try:
                    num=int(float(self.ui.page1_data1[i].text()))
                except Exception:
                    num=0
                    pass
                self.ui.page1_data1[i].setText(str(num))
            input.append(num)
        
        data=self.calc(input[0],input[1],input[2],input[3],input[4],input[5],input[6],input[7],input[8])
        for i in range(9):
            self.ui.page1_data1[i+9].setText("增幅 "+str(round((data[i]-1)*100,2))+"%")
        self.ui.page1_data1[18].setText("總共 "+str(round((data[10]-1)*100,2))+"%")
        
        setPER=[1,3,5,6,7,8]
        for i in setPER:
            input[i]/=100
        text=[0,0,0,0,0,0,0,0,0]
        text[0]=(self.ym+input[0]+(self.page0_data[0]*5+18)*(1+self.page0_data[14]))*(1+self.mp+input[1])+self.nm   #主屬
        text[1]=self.mp+input[1]  #主屬%
        text[2]=(self.ys+input[2])*(1+self.sp+input[3])+self.ns #副屬
        text[3]=self.sp+input[3]  #副屬%
        text[4]=self.att+input[4] #攻擊
        text[5]=self.page0_data[11]+input[5]  #攻擊%
        text[6]=self.page0_data[6]+input[6]+self.page0_data[8]    #總傷+B傷
        text[7]=self.page0_data[10]+input[7]  #爆傷
        text[8]=1-(1-self.page0_data[9])*(1-input[8]) #無視
        for i in setPER:
            text[i]*=100
        for i in range(9):
            if i>=7:
                self.ui.page1_data2[i].setText(str(round(text[i],3)))
            else:
                self.ui.page1_data2[i].setText(str(round(text[i])))
        self.ui.page1_data2[4].setText(str(text[4]))
    
    def star(self):
        page2_data=[]
        for i in range(3):
            page2_data.append([])
            for j in range(7):
                try:
                    num=int(self.ui.page2_data[i][j].text())
                except Exception:
                    num=0
                    pass
                self.ui.page2_data[i][j].setText(str(int(num)))
                page2_data[i].append(num)
        page2_data1=[0,0,0,0]
        for i in range(2):
            page2_data1[i]=self.ui.page2_data1[i].currentIndex()
            try:
                num=int(self.ui.page2_data1[i+2].text())
            except Exception:
                num=0
                pass
            self.ui.page2_data1[i+2]
            page2_data1[i+2]=num
        
        page2_data2=[0,0,0]
        for i in range(7):
            page2_data2[0]+=page2_data[0][i]*11
            page2_data2[0]+=page2_data[1][i]*13
            page2_data2[0]+=page2_data[2][i]*15
            page2_data2[1]+=page2_data[0][i]*(9+i)
            page2_data2[1]+=page2_data[1][i]*(10+i)
            page2_data2[1]+=page2_data[2][i]*(12+i)
        page2_data2[1]+=page2_data[0][6]
        page2_data2[1]+=page2_data[1][6]
        page2_data2[1]+=page2_data[2][6]
        
        if page2_data1[0]==6:
            page2_data2[0]-=page2_data1[2]*2
        if page2_data1[1]==6:
            page2_data2[0]+=page2_data1[3]*2
        
        set_reel=[0,4,5,7,8,9,9]
        page2_data2[1]-=set_reel[page2_data1[0]]*page2_data1[2]
        page2_data2[1]+=set_reel[page2_data1[1]]*page2_data1[3]
        
        data=self.calc(page2_data2[0],0,page2_data2[0],0,page2_data2[1],0,0,0,0)
        
        self.ui.page2_data2[0].setText("屬性增加 "+str(page2_data2[0]))
        self.ui.page2_data2[1].setText("攻擊增加 "+str(page2_data2[1]))
        self.ui.page2_data2[2].setText("總增幅 "+str(round((data[10]-1)*100,2))+"%")

    def setlevel(self):
        index=self.ui.level.currentIndex()
        a  =["45" ,"45" ,"57" ,"57" ,"60" ,"60" ,"72" ,"72" ,"87"]
        att=["12%","12%","12%","12%","12%","12%","15%","15%","18%"]
        hp =["900","990","1080","1170","1260","1350","1440","1530","1800"]
        self.ui.page3_data[0].setText("+ "+a[index])
        self.ui.page3_data[1].setText("+ "+hp[index])
        self.ui.page3_data[2].setText("+ "+att[index])

    def StarFire(self):
        page3_data1=[]
        for i in range(6):
            try:
                input=int(float(self.ui.page3_data1[i].text()))
            except Exception:
                input=0
                pass
            page3_data1.append(input)
            self.ui.page3_data1[i].setText(str(input))
        data=self.calc(page3_data1[0],page3_data1[2],page3_data1[1],page3_data1[2],page3_data1[3],0,page3_data1[4]+page3_data1[5],0,0)
        basic=self.calc()
        a=(data[10]-1)/(basic[0]-1)
        b=(data[10]-1)/(basic[4]-1)

        self.ui.page3_data1[6].setText("= "+str(round(a,2))+" 主屬 或 " +str(round(b,2))+ "攻擊")# 增幅："+str(round((data[10]-1)*100,2))+"%")

    def calc(self,m=1,mp=1,s=1,sp=1,att=1,attp=1,dmg=1,strike=1,ignore=1):
        mp/=100
        sp/=100
        attp/=100
        dmg/=100
        strike/=100
        ignore/=100
        
        data=[0,0,0,0,0,0,0,0,0,0,0]
        x=(self.ym+m+(self.page0_data[0]*5+18)*(1+self.page0_data[14]))*(1+self.mp)+self.nm
        data[0]=(4*x+self.page0_data[4])/(4*self.page0_data[2]+self.page0_data[4])#主屬
        x=(self.ym+(self.page0_data[0]*5+18)*(1+self.page0_data[14]))*(1+self.mp+mp)+self.nm
        data[1]=(4*x+self.page0_data[4])/(4*self.page0_data[2]+self.page0_data[4])#主屬%
        x=(self.ys+s)*(1+self.sp)+self.ns
        data[2]=(4*self.page0_data[2]+x)/(4*self.page0_data[2]+self.page0_data[4])#副屬
        x=(self.ys)*(1+self.sp+sp)+self.ns
        data[3]=(4*self.page0_data[2]+x)/(4*self.page0_data[2]+self.page0_data[4])#副屬%
        data[4]=(self.att+att)/self.att#攻擊
        data[5]=(1+self.page0_data[11]+attp)/(1+self.page0_data[11])#攻擊%
        data[6]=(1+self.page0_data[6]+self.page0_data[8]+dmg)/(1+self.page0_data[6]+self.page0_data[8])#總傷+B傷
        data[7]=(1.35+self.page0_data[10]+strike)/(1.35+self.page0_data[10])#爆傷(1.2~1.5平均值)
        x=1-(1-self.page0_data[9])*(1-ignore)
        x=1-(self.page0_data[19]*(1-x))
        y=1-(self.page0_data[19]*(1-self.page0_data[9]))
        if x<0:
            data[8]=1
        elif y<0:
            data[8]=101
        else:
            data[8]=x/y#無視
        
        data[9]=data[1]*data[3]#全屬%
        data[10]=1#總增幅
        for i in range(9):
            data[10]*=data[i]
        return data
    
    def connection(self):
        address=["home.gamer.com.tw/homeindex.php?owner=leehosen"
                ,"stanleylee417@gmail.com"]
        self.ui.report.setText(address[self.ui.connection.currentIndex()])
    
    def setup_class(self):
        curIndex=self.ui.setup_class.currentIndex()
        page0_data11_set=[25,0,20,35,20,30,0,0,0,10,40,10,0,35,10,15,11,5,11,0,0,0,0,0,0,34,0,15,10,10,10,0,4,4,8,0,0,0,0,10,0,0,10,34,20,0,0,0,10,4,0,25]
        page0_data12_set=[3,5,3,5,3,3,1,1,1,0,0,1,1,0,1,4,4,4,4,5,3,6,1,4,7,4,1,9,1,1,4,7,7,4,2,2,10,3,3,10,3,3,3,9,8,8,9,8,9,9,9,8]
        self.ui.page0_data[11].setText(str(page0_data11_set[curIndex]))
        self.ui.page0_data[12].setCurrentIndex(page0_data12_set[curIndex])
    
app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())