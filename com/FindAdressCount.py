import GetAdressFromCsv
from collections import Counter
import csvRead
import re,os
class FindAdressCount():
    def setdict(self):
        dict = GetAdressFromCsv.GetAdressFromCsv().GetDetailAdress()
        set_dict = {}
        for key, value in dict.items():
            set_dict[key] = list(set(value))
        return set_dict

    def getres(self):
        #获取未去重的列表
        dict = GetAdressFromCsv.GetAdressFromCsv().GetDetailAdress()
        original_valuelist=[]
        for key, value in dict.items():
            original_valuelist.append(value)

        appear_time=0
        valuelist = []
        keylist=[]
        Detail_result=[]
        Detail_result_adress=[]
        total_result=[]
        #获取去重的列表进行并集
        for key,value in self.setdict().items():
            valuelist.append(value)
            keylist.append(key)
        union = set(valuelist[0])
        for i in valuelist[1:]:
            union=union | set(i)
        # print(union)

        #得到value列表的并集，去之前去重的字典里循环遍历
        for val in union:
            count=0
            for singlevaluelistindex in range(len(original_valuelist)):
                if val in original_valuelist[singlevaluelistindex]:
                    val_index = original_valuelist[singlevaluelistindex].index(val)
                    count+=1
                    per = val_index/len(original_valuelist[singlevaluelistindex])*100
                    Detail_result_adress.append(val)
                    #只要出现不管几次，默认记为1次
                    Detail_result.append(str(val+':  '+'出现在'+keylist[singlevaluelistindex]+',  最早的是第'+
                                             str(val_index+1)+'笔交易,  '+keylist[singlevaluelistindex]+'共有'+str(len(original_valuelist[singlevaluelistindex]))+'笔交易,  交易前'
                                             +"{:.1f}%".format(per)))

            total_result.append(val+'  :出现  '+str(count)+'次')
        if not os.path.exists("AdressFile"):
            os.makedirs("AdressFile")
        detail_file = open('AdressFile/'+'detail_adress_result.txt', 'w')
        total_file = open('AdressFile/'+'total_adress_result.txt', 'w')
        for item in Detail_result:
            detail_file.write("%s\n" % item)
        for item in total_result:
            total_file.write("%s\n" % item)
        detail_file.close()
        total_file.close()

        return [Detail_result,total_result,Detail_result_adress]

    def SavefilesSeparately(self,count):
        list = self.getres()
        count_adress=[]
        count_adress_dict={}
        for TraRecord  in list[1]:
            appear_time = TraRecord[-2]
            if int(appear_time)==count:
                count_adress.append(TraRecord)
    #根据地址从detail_result中拿出地址所有的记录
        for i in count_adress:
            eth_adress = i[0:42]
            eth_adress_index_in_Detail_result_adress = list[2].index(eth_adress)
            ThisAdresslist = list[0][eth_adress_index_in_Detail_result_adress:eth_adress_index_in_Detail_result_adress+count]
            count_adress_dict[eth_adress]=ThisAdresslist

        #写入文件
        if not os.path.exists("AdressFile/AppearTimeFile"):
            os.makedirs("AdressFile/AppearTimeFile")
        # count_file = open('AdressFile/AppearTimeFile/'+str(count)+'_time_appear_adress.txt', 'w')
        count_adress_file = open('AdressFile/AppearTimeFile/'+str(count)+'_time_appear_adress.txt', 'w')

        # count_adress_file.write(str(count_adress_dict))
        for key, value in count_adress_dict.items():
            count_adress_file.write('{'+key+":\n"+'['+"\n")
            for item in value:
                count_adress_file.write(item +','+"\n")
            count_adress_file.write(']'+"\n")
        count_adress_file.close()


# if __name__ == '__main__':
#     findAdressCount =FindAdressCount()
#     # findAdressCount.getres()
#     findAdressCount.SavefilesSeparately(6)
















