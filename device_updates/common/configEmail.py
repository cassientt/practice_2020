import os 
import win32com.client as win32
import datatime
import readConfig
import getpathInfo


read_conf = readConfig.ReadConfig()
subject = read_conf.get_email('subject')#从配置文件中读取邮件主题
app = str(read_conf.get_email('app'))#从配置文件中读取邮件类型
addresses = read_conf.get_email('addressee')#读取收件人
cc = read_conf.get_email('cc')#读取抄送人

mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')
class send_email():
    def wangyi_Email():
        wangyi =win32.Dispatch("%s.Application" % app)
        mail = wangyi.CreateItem(win32.costants.wyMailItem)
        mail.To = addresses
        mail.CC = cc
        mail.subject = str (datatime.datetime.now())[0:19]  +'%s' %subject
        mail.Attachments.Add(mail_path, 1, 1, "myFile" )
        content = """ 24
                测试执行中···
                测试已完成！！！
                生成报告中···
                报告已生成···
                报告已邮件发送！！
             """
        mail.Body = content
        mail.Send()

if __name__ == '__main__':
    print(subject)
    send_email().wangyi_Email()
    print("send email ok !!!!")