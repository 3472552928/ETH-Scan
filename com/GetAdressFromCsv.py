import AdressList
import csvRead
import re,os
class GetAdressFromCsv():

    def GetEveryAdress(self):
        coinname = []
        res = []
        pattern = r'---(.+)\.csv'
        for i in AdressList.adresslist:
            result = re.search(pattern, i)
            coinname.append(result.group(1))
            res.append(csvRead.ReadCsv(i).readALL(end=5002,start=1))
        return [res,coinname]

    def GetDetailAdress(self):
        coinname_dict = {}
        coinname_dict_file = {}
        count=0
        for coinname in self.GetEveryAdress()[1]:
            coinname_dict[coinname] = []
            coinname_dict_file[coinname] = []
            for Singcoindata in self.GetEveryAdress()[0][count]:
                coinname_dict[coinname].append(Singcoindata[4])
                coinname_dict_file[coinname].append(Singcoindata[4])

            if not os.path.exists("AdressFile"):
                os.makedirs("AdressFile")
            file = open('AdressFile/'+coinname+'_coin_match_adress.txt', 'w')
            file.write(str(coinname_dict_file))
            file.close()
            count+=1
            coinname_dict_file={}
        file = open('AdressFile/' + '_coin_match_adress.txt', 'w')
        file.write(str(coinname_dict))
        file.close()
        return coinname_dict

# if __name__ == '__main__':
#     GetAdressFromCsv().GetDetailAdress()











