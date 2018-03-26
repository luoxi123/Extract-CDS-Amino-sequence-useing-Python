import numpy as np
class Turn_Cds_Amino():
    def __init__(self,cds_sequence):
        self.cds_sequence=cds_sequence
        
    def turn_cds_to_amino(self):
        cds1=self.cds_sequence
        self.qq=[]
        self.coding_se={'gct':'A',
        'gcc':'A',
        'gca':'A',
        'gcg':'A',
           'tgt':'C',
           'tgc':'C',
           'gat':'D',
           'gac':'D',
           'gaa':'E',
           'gag':'E',
           'ttt':'F',
           'ttc':'F',
           'ggt':'G',
           'ggc':'G',
           'ggg':'G',
           'gga':'G',
           'cat':'H',
           'cac':'H',
           'att':'I',
           'atc':'I',
           'ata':'I',
           'aaa':'K',
           'aag':'K',
           'tta':'L',
           'ttg':'L',
           'ctt':'L',
           'ctc':'L',
           'cta':'L',
           'ctg':'L',
           'atg':'M',
           'aat':'N',
           'aac':'N',
           'cct':'P',
           'ccc':'P',
           'cca':'P',
           'ccg':'P',
           'caa':'Q',
           'cag':'Q',
           'cgt':'R',
           'cgc':'R',
           'cga':'R',
           'cgg':'R',
           'aga':'R',
           'agg':'R',
           'tct':'S',
           'tcc':'S',
           'tca':'S',
           'tcg':'S',
           'agt':'S',
           'agc':'S',
           'act':'T',
           'acc':'T',
           'aca':'T',
           'acg':'T',
           'gtt':'V',
           'gtc':'V',
           'gta':'V',
           'gtg':'V',
           'tgg':'W',
           'tat':'Y',
           'tac':'Y',
           'taa':'X',
           'tag':'X',
           'tga':'X'}
        coding_se1=self.coding_se
        """初始化"""
        s,ad,coding1=[],[],[]
        window=3
        """将列表中多个元素合成一个元素；如：列表中为a=【‘a’，‘t’，‘c’】，合并为a=atc"""
        aa=''.join(map(str,cds1)) 
        """将合并好的元素加入新列表，这时该列表只有一个元素：ad【0】"""
        for i in range(0,len(aa)):
            ad.append(aa[i])
            #print(ad)
            """将列表转化成array数组，并进行变形：密码子变形为3xn的矩阵"""
        s=np.array(ad)
        ss=s.reshape(int(len(cds1)/window),window)
        """将3xn维矩阵中的每一行进行合并，既是将每一行合并成一个密码子"""
        for j in range(0,len(ss)):
            #print(ss[j])
            q=''.join(map(str,ss[j]))
            self.qq.append(q)
        #print(self.qq)
        """循环遍历密码子列表和氨基酸字典，输出密码子对应的氨基酸简写"""
        for k in range(0,len(self.qq)):
            #print('k',str(k))
            for n,v in coding_se1.items():
                if self.qq[k]==n:
                    bb=v
                    coding1.append(bb)
                else:
                    pass
        self.amino=''.join(map(str,coding1))
        temp_amino=self.amino
        return temp_amino
    
    """计算每一种密码子出现的次数"""
    def number_coding_use(self):
        """调用上一函数的中间变量"""
        cs=self.qq
        cs1={}
        count=0
        for n,v in self.coding_se.items():
            for k in range(0,len(cs)):
                if cs[k] in n:
                    count+=1
                    cs1[cs[k]]=count
                #elif cs[k] not in n:
                    #cs1[cs[k]]=0
                #else:
                    #print('\t\t\t***********')
            count=0
        #print(qq)
        """计算出每一种密码子出现的次数，并返回字典值"""
        return cs1
    
    """计算出每一种密码子出现的频率"""
    def frequency_coding_use(self):
        cs2=self.qq
        cs3={}
        count2=0
        for n,v in self.coding_se.items():
            for k in range(0,len(cs2)):
                if cs2[k] in n:
                    count2+=1
                    cs3[cs2[k]]=(count2/(len(cs2)-1))*100
                #else:
                    #print('\t\t\t... ... ... ... ...')
            count2=0
        #print(qq)
        """计算出每一种密码子出现的频率，并返回字典值"""
        return cs3
    
    