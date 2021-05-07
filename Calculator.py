from PyQt5 import QtCore, QtWidgets
class Ui_Form(object):
    def setupUi(self, Form):
        form_w=348
        form_h=337
        Form.setObjectName("self.Form")
        Form.resize(form_w, form_h)
        Form.setWindowTitle("裝備效益計算機(V1.2) 作者：牡羊")
        
        self.Calculator = QtWidgets.QTabWidget(Form)
        self.Calculator.setGeometry(QtCore.QRect(5, 5, form_w-10, form_h-10))
        self.Calculator.setObjectName("Calculator")
        
        page=[]
        page_name=["UI","數值","星力 / 卷軸","星火","其他"]
        for i in range(len(page_name)):
            page.append(QtWidgets.QWidget())
            page[i].setObjectName("page"+str(i))
            self.Calculator.addTab(page[i], "")
            self.Calculator.setTabText(self.Calculator.indexOf(page[i]),page_name[i])
        
        self.designPage0(page[0])
        self.designPage1(page[1])
        self.designPage2(page[2])
        self.designPage3(page[3])
        self.Description(page[4])
        
        self.Calculator.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def designPage0(self,page):
        label_name=["等級","楓祝前主屬","楓祝後主屬","傑諾前副屬","傑諾後副屬","最高表攻","傷害%","最終傷害%","BOSS傷害%","無視防禦%"
                   ,"爆擊傷害%","攻擊力%","武器係數","ARC","楓祝%數","角色卡主屬","角色卡副屬","極限主屬","極限副屬","怪物防禦%"]
        self.page0_data=[]
        empty=[10,68,78,10,11,48,0,0,0,0,0,0,0,0,0,0,0,0,0,300]
        for i in range(2):
            for j in range(10):
                curIndex=j+i*10
                self.makelabel(page, 15+i*158, 15+j*25, 72, 20,label_name[curIndex])
                
                self.page0_data.append(QtWidgets.QLineEdit(page))
                self.page0_data[curIndex].setGeometry(QtCore.QRect(93+i*158, 15+j*25, 67, 20))
                self.page0_data[curIndex].setObjectName("page0_data"+str(curIndex))
                self.page0_data[curIndex].setText(str(empty[curIndex]))
                #self.page0_data[curIndex].setText(str(curIndex))
        
        self.page0_data[12].setEnabled(False)
        self.page0_data[14].setEnabled(False)
        self.page0_data[12]=QtWidgets.QComboBox(page)
        self.page0_data[12].setGeometry(QtCore.QRect(93+1*158, 15+2*25, 67, 20))
        self.page0_data[12].setObjectName("page0_data30")
        self.page0_data[12].addItems(["1","1.2","1.25","1.3","1.34","1.35","1.44","1.49","1.5","1.7","1.75"])
        self.page0_data[14]=QtWidgets.QComboBox(page)
        self.page0_data[14].setGeometry(QtCore.QRect(93+1*158, 15+4*25, 67, 20))
        self.page0_data[14].setObjectName("page0_data30")
        self.page0_data[14].addItems(["15","16"])
        
        self.page0_btn=[]
        btn_name=["確定","儲存檔案","選擇檔案"]
        for i in range(3):
            self.page0_btn.append(QtWidgets.QPushButton(page))
            self.page0_btn[i].setGeometry(QtCore.QRect(221-i*105, 267, 98, 25))
            self.page0_btn[i].setObjectName("submit_ui")
            self.page0_btn[i].setText(btn_name[i])
            
    def designPage1(self,page):
        self.page1_btn=[]
        page1_data_type=[QtWidgets.QLineEdit(page),QtWidgets.QComboBox(page)]
        for i in range(2):
            self.page1_btn.append(page1_data_type[i])
            self.page1_btn[i].setGeometry(QtCore.QRect(15+i*103,15, 99, 20))
            self.page1_btn[i].setObjectName("page1_btn"+str(i))
            
        self.page1_btn[0].setText("1")
        self.page1_btn[1].addItems(["主屬     相當於","% 主屬 相當於","副屬     相當於","% 副屬 相當於","攻擊     相當於","% 攻     相當於","% 總傷 相當於","% 爆傷 相當於","% 全屬 相當於"])
        
        self.page1_data=[]
        label_name=["主屬","%主","副屬","%副","攻擊","%攻","%總","%爆"]
        for i in range(2):
            for j in range(4):
                curIndex=j+i*4
                self.page1_data.append(QtWidgets.QLineEdit(page))
                self.page1_data[curIndex].setGeometry(QtCore.QRect(15+j*78,40+i*25, 70, 20))
                self.page1_data[curIndex].setEnabled(False)
                self.page1_data[curIndex]=QtWidgets.QLabel(page)
                self.page1_data[curIndex].setGeometry(QtCore.QRect(60+j*78,43+i*25, 36, 20))
                self.page1_data[curIndex].setText(label_name[curIndex])
                self.page1_data[curIndex].setEnabled(False)
                self.page1_data[curIndex]=QtWidgets.QLabel(page)
                self.page1_data[curIndex].setGeometry(QtCore.QRect(18+j*78,40+i*25, 64, 20))
                self.page1_data[curIndex].setObjectName("page1_data"+str(curIndex))
                self.page1_data[curIndex].setText("0")
        
        self.page1_data.append(QtWidgets.QLineEdit(page))
        self.page1_data[8].setGeometry(QtCore.QRect(15+3*78,15, 70, 20))
        self.page1_data[8].setEnabled(False)
        self.page1_data[8]=QtWidgets.QLabel(page)
        self.page1_data[8].setGeometry(QtCore.QRect(60+3*78,18, 36, 20))
        self.page1_data[8].setText("%全")
        self.page1_data[8].setEnabled(False)
        self.page1_data[8]=QtWidgets.QLabel(page)
        self.page1_data[8].setGeometry(QtCore.QRect(18+3*78,15, 64, 20))
        self.page1_data[8].setObjectName("page1_data8")
        self.page1_data[8].setText("0")
                
        self.page1_data1=[]
        label_name=[["增加"],["主屬","主屬%","副屬","副屬%","攻擊","攻擊%","總傷%","爆傷%","無視%"],["0","增幅 0.0%"]]
        for i in range(2):
            for j in range(9):
                curIndex=j+i*9
                self.makelabel(page, 57-i*40, 95+j*23, 36, 18,label_name[i][j*i])
                
                if i==0:
                    self.page1_data1.append(QtWidgets.QLineEdit(page))
                else:
                    self.page1_data1.append(QtWidgets.QLabel(page))
                self.page1_data1[curIndex].setGeometry(QtCore.QRect(85+i*45, 95+j*23, 40+i*26, 18))
                self.page1_data1[curIndex].setObjectName("page1_data1"+str(curIndex))
                self.page1_data1[curIndex].setText(label_name[2][i])
            
        self.page1_data1.append(QtWidgets.QLabel(page))
        self.page1_data1[18].setGeometry(QtCore.QRect(203, 279, 114, 18))
        self.page1_data1[18].setObjectName("page1_data1")
        self.page1_data1[18].setText("總共 0%")
        
        self.page1_data2=[]
        label_name=["主屬","主屬%","副屬","副屬%","攻擊","攻擊%","總傷%","爆傷%","無視%"]
        for i in range(9):
            label=QtWidgets.QLineEdit(page)
            label.setGeometry(QtCore.QRect(199, 92+i*20, 120, 21))
            label.setEnabled(False)
            self.makelabel(page, 203, 95+i*20, 36, 16,label_name[i])
            
            self.page1_data2.append(QtWidgets.QLabel(page))
            self.page1_data2[i].setGeometry(QtCore.QRect(250, 95+i*20, 67, 16))
            self.page1_data2[i].setObjectName("page1_data2"+str(i))
            self.page1_data2[i].setText("0")
                
        for i in self.page1_btn:
            i.setEnabled(False)
        for i in self.page1_data1:
            i.setEnabled(False)

    def designPage2(self,page):
        label_name=["150級裝備","160級裝備","200級裝備"]
        for i in range(3):
            self.makelabel(page, 70+i*86, 15, 86, 12,label_name[i])
        
        for i in range(7):
            self.makelabel(page, 18, 31+i*22, 30, 20,str(i+16)+"星")
        
        self.page2_data=[]
        for i in range(3):
            self.page2_data.append([])
            for j in range(7):
                self.page2_data[i].append(QtWidgets.QLineEdit(page))
                self.page2_data[i][j].setGeometry(QtCore.QRect(60+i*86, 30+j*22, 78, 20))
                self.page2_data[i][j].setObjectName("page2_data"+str(i))
                self.page2_data[i][j].setText("0")
        
        label=[0,0,0,0]
        self.page2_data1=[0,0,0,0]
        label_name=["卷軸","換成"]
        for i in range(2):
            self.makelabel(page, 19, 189+i*22, 30, 20,label_name[i])
            
            self.page2_data1[i]=QtWidgets.QComboBox(page)
            self.page2_data1[i].setGeometry(QtCore.QRect(60, 188+i*22, 78, 20))
            self.page2_data1[i].addItems(["無","極電","RED","X","V","B飾","B防"])
            self.page2_data1[i].setObjectName("page2_data1"+str(i))
            self.page2_data1[i+2]=QtWidgets.QLineEdit(page)
            self.page2_data1[i+2].setGeometry(QtCore.QRect(146, 188+i*22, 78, 20))
            self.page2_data1[i+2].setObjectName("page2_data1"+str(i+2))
            self.page2_data1[i+2].setText("0")
            
            self.makelabel(page, 232, 189+i*22, 15, 20,"張")
                    
        self.page2_btn=[]
        self.page2_btn.append(QtWidgets.QPushButton(page))
        self.page2_btn[0].setGeometry(QtCore.QRect(15, 235, 297, 25))
        self.page2_btn[0].setObjectName("check_btn")
        self.page2_btn[0].setText("確定")
        
        self.page2_data2=[]
        star_improve_name=["屬性增加 0","攻擊增加 0","總增幅 0.0%"]
        for i in range(3):
            self.page2_data2.append(QtWidgets.QLabel(page))
            self.page2_data2[i].setGeometry(QtCore.QRect(20+i*103, 270, 99, 16))
            self.page2_data2[i].setObjectName("page2_data2"+str(i))
            self.page2_data2[i].setText(star_improve_name[i])
        
        for i in self.page2_data:
            for j in i:
                j.setEnabled(False)
        for i in self.page2_data1:
            i.setEnabled(False)
        for i in self.page2_btn:
            i.setEnabled(False)
    
    def designPage3(self,page):
        self.makelabel(page, 15, 15+25*0, 50, 20,"裝備等級")
            
        self.level=QtWidgets.QComboBox(page)
        self.level.setGeometry(QtCore.QRect(68, 15+25*0, 50, 20))
        self.level.setObjectName("level")
        self.level.addItems(["100","110","120","130","140","150","160","170","200"])
        self.level.setEnabled(False)
        
        self.page3_data=[]
        label_name=["屬性最高","ＨＰ最高","攻擊最高"]
        data_name=["45","900","12%"]
        for i in range(len(label_name)):
            self.makelabel(page, 15, 40+25*i, 50, 20,label_name[i])
            
            self.page3_data.append(QtWidgets.QLabel(page))
            self.page3_data[i].setGeometry(QtCore.QRect(68, 40+25*i, 48, 20))
            self.page3_data[i].setObjectName("page3_data"+str(i))
            self.page3_data[i].setText("+ "+data_name[i])
        
        self.page3_data1=[]
        label_name=["主屬","副屬","%全屬","攻擊","總傷","B傷"]
        for i in range(2):
            for j in range(3):
                curIndex=j+i*3
                self.page3_data1.append(QtWidgets.QLineEdit(page))
                self.page3_data1[curIndex].setGeometry(QtCore.QRect(140+90*i, 15+25*j, 48, 20))
                self.page3_data1[curIndex].setObjectName("page3_data"+str(i))
                self.page3_data1[curIndex].setText("0")
                self.page3_data1[curIndex].setEnabled(False)
                
                self.makelabel(page, 191+90*i, 15+25*j, 36, 20,label_name[curIndex])
            
        self.page3_data1.append(QtWidgets.QLabel(page))
        self.page3_data1[6].setGeometry(QtCore.QRect(142, 90, 200, 20))
        self.page3_data1[6].setObjectName("page3_data"+str(i))
        self.page3_data1[6].setText("= 0 主屬 或 0 攻擊")# 增幅：0%")

    def Description(self,page):
        label=[]
        label_name=["問題回報"
                   ,""
                   ,"1. 快速設定武器係數、%攻(仍須加上 武器 以及 萌獸)"
                   ,""
                   ,"2. BOSS傷害 與 總傷 相同(合併計算)"
                   ,"3. 傑諾，惡復不適用"
                   ,"4. 雙副屬職業請將副屬相加( 誤差較大 )"
                   ,"5. 星火攻擊指武器白值，防具飾品最高皆為3"]
                   
        for i in range(len(label_name)):
            self.makelabel(page, 15, 15+i*25, 303, 20, label_name[i])
        
        self.connection=QtWidgets.QComboBox(page)
        self.connection.setGeometry(QtCore.QRect(68, 15+25*0, 60, 20))
        self.connection.setObjectName("setup_class")
        self.connection.addItems(["巴哈","信箱"])
        
        self.report=QtWidgets.QLineEdit(page)
        self.report.setGeometry(QtCore.QRect(15, 15+25*1, 300, 20))
        self.report.setObjectName("home_data")
        self.report.setText("home.gamer.com.tw/homeindex.php?owner=leehosen")
        
        self.setup_class=QtWidgets.QComboBox(page)
        self.setup_class.setGeometry(QtCore.QRect(15, 15+25*3, 120, 20))
        self.setup_class.setObjectName("setup_class")
        self.setup_class.addItems(["箭神","神射手","開拓者","狂豹獵人","破風使者","精靈遊俠","火毒","冰雷","主教","凱內西斯","煉獄巫師","烈焰巫師","夜光","龍魔導士","伊利恩","幻獸師(熊)","幻獸師(豹)","幻獸師(鷹)","幻獸師(貓)","陰陽師","英雄(單)","英雄(雙)","聖騎士(單)","聖騎士(雙)","黑騎士","凱撒","惡魔殺手","爆拳槍神","米哈逸","聖魂劍士(單)","聖魂劍士(雙)","狂狼勇士","神之子(琉)","神之子(璃)","劍豪","劍豪(拔刀)","夜使者","暗影神偷","影武者","暗夜行者","幻影俠盜","卡蒂娜","虎影","拳霸","槍神","重砲指揮官","天使破壞者","機甲戰神","閃雷悍將","隱月","亞克","蒼龍俠客"])
        
        
    def makelabel(self,page,x=10,y=10,w=10,h=20,text="",s=True):
        self.label=QtWidgets.QLabel(page)
        self.label.setGeometry(QtCore.QRect(x, y, w, h))
        self.label.setObjectName("label")
        self.label.setText(text)
        self.label.setEnabled(s)