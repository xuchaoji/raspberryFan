# raspberryFan
## 图片说明
使用的三极管型号为S8550，三极管的引脚图见S8550-pinout.png

![image](https://github.com/xuchaoji/raspberryFan/blob/master/S8550-pinout.png)

接线图见pi_fan.jpg

![image](https://github.com/xuchaoji/raspberryFan/blob/master/pi_fan.jpg)

树莓派GPIO引脚图见PiGPIO.png

![image](https://github.com/xuchaoji/raspberryFan/blob/master/PiGPIO.png)

## 脚本说明
将项目clone到本地后，在目录中python fan.py即可运行脚本。
建议配合screen使用，步骤如下：
创建screen： screen -S fan
启动脚本：python fan.py
断开screen：Ctrl+A+D
恢复screen：screen -r fan

## 脚本开机启动
编辑/etc/rc.local 在其中加入如下命令:

screen -dmS fan sh\n
screen -S fan -X stuff "bash\n
"\n
screen -S fan -X stuff "cd /root/onBoot\n
"\n
screen -S fan -X stuff "python /root/onBoot/fan.py\n
"\n


**其中的/root/onBoot为fan.py的存放目录，右引号必须换行，否则想当于输入命令没回车，传入screen的命令不能执行**
