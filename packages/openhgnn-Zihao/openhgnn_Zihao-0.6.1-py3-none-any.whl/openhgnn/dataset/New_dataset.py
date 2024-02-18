import os
import requests
import zipfile
import io
from ordered_set import OrderedSet
from collections import defaultdict as ddict
from torch.utils.data import DataLoader


# 这里是model+task对应的数据集,
# build_dataset 函数调用
# return DATASET_REGISTRY[_dataset](dataset,args = kwargs.get('args')) 
# 最终会调用下面的对象的初始化函数，返回一个实例

@register_dataset('GGNN_link_prediction')
class DisenKGAT_LinkPrediction(LinkPredictionDataset):
    r"""
    """
    def __init__(self, dataset ,*args, **kwargs): # dataset "DisenKGAT"

        #   额外关键字参数中有args
        self.args = kwargs.get("args")

        # 获取当前文件所在的  文件夹路径
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        # 数据集名称，作为文件夹名称即  DisenKGAT_WN18RR
        self.dataset_name = dataset
                                    # openhgnn/dataset  # DisenKGAT_WN18RR/
        self.raw_dir = os.path.join(self.current_dir, self.dataset_name ,"raw_dir" ) 
        self.processed_dir = os.path.join(self.current_dir, self.dataset_name ,"processed_dir" ) 


        if not os.path.exists(self.raw_dir):
            os.makedirs(self.raw_dir) # 创建raw_dir文件夹即  openhgnn/dataset/DisenKGAT_WN18RR/raw
            print(f"已创建新文件夹：{self.raw_dir}")
            self.download()
        else:
            print("raw_dir文件夹已经存在")

        

    def download(self): # 下载原始数据

        url = "https://s3.cn-north-1.amazonaws.com.cn/dgl-data/dataset/openhgnn/{}.zip".format(self.dataset_name)
        
        #   把压缩文件zip直接解压缩到self_rawdir文件夹中，不会把zip文件下载到文件夹中
        response = requests.get(url)
        with zipfile.ZipFile(io.BytesIO(response.content)) as myzip:
            myzip.extractall(self.raw_dir) # 把压缩文件解压到raw_dir文件夹中,
            #zip解压后，直接在raw_dir中直接生成3个txt (而不是再生产一个文件夹)
        print("---  download   finished---")

        # 实例初始化过程包括了download和process，process之后会在这个对象中生成一些成员，
                                                                    #比如self.dataiter或者self.hg，之后task中会把这些成员拿出来用
        




