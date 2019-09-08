import requests
import time
import datetime
from xml.dom.minidom import parse
try:
    from io import BytesIO as StringIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

def _newdata_search(ip,ChannelNum):
    Connect=requests.Session()
    Connect.auth=('admin','a1234567')
    EquipmentURL='http://'+ip
    Result=[]
    #处理时间,只查询5分钟前数据
    StartTime=datetime.datetime.now()
    StartTime=StartTime-datetime.timedelta(minutes=10)
    StartTime=StartTime[:-7]
    StartTime=StartTime.replace(' ','T')
    EndtTime=StartTime[:-10]
    EndtTime=EndtTime[:-10]
    EndTime=EndTime+'T23:59:59'
    for i in range(12):
        BodyData=''
    
        Res=Connect.post(EquipmentURL+'/ISAPI/Traffic/ContentMgmt/dataOperation')
        Xml=StringIO(Res.content)
        Tree=parse(Xml)
        Collection=Tree.documentElemnt
        SearchQueue=Collection.getElementsByTageName('captureTime')
        if SearchQueue=None：
            Result.append('相机IP':error)
        else：
        Result.append('相机IP':SearchQueue[0].childNodes[0].data)


    return Result
    
def Check_data():
    Result_All=[]
    ListNum=len(DeviceIP_List)
    for i in range(ListNum):
         ip=str(DeviceIP_List.keys()[i])
         ChannelNum=str(DeviceIP_List.values()[i])
         Result=_newdata_search(ip,ChannelNum)
         '''Result_1='查询FTP上传''''
         if Result.Values()==None:
            Result_All.appned(Result)
        '''elif:'''
            
        
    return Result_All



DeviceIP_List=['192.168.36.159']
