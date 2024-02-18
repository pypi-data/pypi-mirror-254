import os
from dgl.data.utils import download, extract_archive
from dgl.data import DGLDataset
from dgl.data.utils import load_graphs
from dgl.heterograph import DGLGraph
import dgl



# 从云盘直接获取graph.pkl
class IMDB4MAGNN_Dataset(DGLDataset):

    def __init__(self, name, raw_dir=None, force_reload=False, verbose=True):
        assert name in ['imdb4MAGNN', ]


 #     _download(),precess(),save()
        super(IMDB4MAGNN_Dataset, self).__init__(name=name,
                                        url=None,
                                        raw_dir=None, # save_dir默认等于raw_dir
                                        force_reload=force_reload,
                                        verbose=verbose)

    def download(self):
        from gdbi import NodeExportConfig, EdgeExportConfig, Neo4jInterface, NebulaInterface

        node_export_config = [
            NodeExportConfig('A', ['attribute'] ),
            NodeExportConfig('M', ['attribute'], ['label']), 
            NodeExportConfig('D', ['attribute'])  
        ]


        edge_export_config = [
            EdgeExportConfig('A_M', ('A','M')),
            EdgeExportConfig('M_A', ('M','A')),
            EdgeExportConfig('M_D', ('M','D')),
            EdgeExportConfig('D_M', ('D','M'))    
        ]

        # # neo4j 
        # graph_database = Neo4jInterface()

        # nebula 
        graph_database = NebulaInterface()


        graph_address = ''
        user_name = ''
        password = ''
        conn = graph_database.GraphDBConnection(graph_address, user_name, password)
        self.graph = graph_database.get_graph(conn, 'imdb4MAGNN', node_export_config, edge_export_config)


        pass

    def process(self):

        graph = self.graph
#######     graph是标准图字典,imdb4MAGNN有A,D,M三类节点，A-M,D-M,M-A,M-D四类边，其中M类节点有label和mask
        cano_edges = {}
        for edge_type in graph['edge_index_dict'].keys():  # 'A_M'
            src_type = edge_type[0] # A
            dst_type = edge_type[-1]    # M
            edge_type_2 = src_type + '-' + dst_type # A-M
            
            cano_edge_type = (src_type,edge_type_2,dst_type)  # ('A','A-M','M')
            u,v = graph['edge_index_dict'][edge_type][0] ,graph['edge_index_dict'][edge_type][1]  # 边中的源点id，目点id

            cano_edges[cano_edge_type] = (u,v)



        hg = dgl.heterograph(cano_edges)

        for node_type in graph['X_dict'].keys() :  # 所有节点类型 
            hg.nodes[node_type].data['h'] = graph['X_dict'][node_type]  # node_type类节点的特征 h
            if node_type == 'M':
                hg.nodes[node_type].data['labels'] = graph['Y_dict'][node_type]  # node_type类节点的label 

        import torch

#########           构造train_mask,val_mask,test_mask
        # 设置节点数量
        num_nodes = 4278
        # 生成随机的节点索引
        random_indices = torch.randperm(num_nodes)
        # 设置训练、验证和测试集的大小
        num_train = 400
        num_val = 400
        num_test = 3478
        # 构造 train_mask
        train_mask = torch.zeros(num_nodes, dtype=torch.int)
        train_mask[random_indices[:num_train]] = 1
        # 构造 val_mask
        val_mask = torch.zeros(num_nodes, dtype=torch.int)
        val_mask[random_indices[num_train:num_train+num_val]] = 1

        # 构造 test_mask
        test_mask = torch.zeros(num_nodes, dtype=torch.int)
        test_mask[random_indices[num_train+num_val:]] = 1

        # 检查是否有交叉
        assert torch.sum(train_mask * val_mask) == 0
        assert torch.sum(train_mask * test_mask) == 0
        assert torch.sum(val_mask * test_mask) == 0


        hg.nodes['M'].data['train_mask'] = train_mask
        hg.nodes['M'].data['val_mask'] = val_mask
        hg.nodes['M'].data['test_mask'] = test_mask



#       如果要链接图数据库的话
        self._g = hg

 


    def __getitem__(self, idx):
        # get one example by index
        assert idx == 0, "This dataset has only one graph" 
        return self._g

    def __len__(self):
        return 1


    def save(self):
        pass

    def load(self):
        pass

    def has_cache(self):
        pass






# 从云盘直接获取graph.pkl
class IMDB4MAGNN_Dataset(DGLDataset):

#   在init函数之前的成员，会默认有一个self前缀
    _prefix = 'https://s3.cn-north-1.amazonaws.com.cn/dgl-data/'


    def __init__(self, name, raw_dir=None, force_reload=False, verbose=True):
        assert name in ['imdb4MAGNN', ]
        
        self._urls = {
       'imdb4MAGNN': 'dataset/openhgnn/{}_std.zip'.format(name),
}


        raw_dir = './openhgnn/dataset'        

        # 本地zip文件（的本地存放路径）  
        self.data_path = './openhgnn/dataset/'+ name +'_std.zip'  #  。openhgnn/dataset/    +  imdb4MAGNN_std.zip
        # name:imdb4MAGNN   # 云盘zip文件 imdb4MAGNN_std.zip    

        # 解压出来的文件imdb4MAGNN_std.pkl
#   这是标准的graph.pkl文件                 imdbMAGNN 目录
        self.g_path = './openhgnn/dataset/' + name + '/{}_std.pkl'.format(name)   



        url = self._prefix + self._urls[name]  # https://s3.cn-north-1.amazonaws.com.cn/dgl-data/ +  dataset/imdb4MAGNN_std.zip
 

 #     调用DGLDataset的初始化函数，会依次执行_download(),precess(),save()
        super(IMDB4MAGNN_Dataset, self).__init__(name=name,
                                        url=url,
                                        raw_dir=raw_dir, # save_dir默认等于raw_dir
                                        force_reload=force_reload,
                                        verbose=verbose)

    def download(self):
        # download raw data to local disk
        # path to store the file
        if os.path.exists(self.data_path):  # data_path是本地zip文件
           # data_path指的是zip文件，已经有了的话，那就不需要下载和解压
           pass
        else:
            #                        raw_dir目录
            download(self.url, 
                     path=os.path.join(self.raw_dir))   #  在raw_dir目录内，下载一个zip文件

        #  本地zip文件就是data_path，             raw_dir / name  这个是目录
        extract_archive(self.data_path, os.path.join(self.raw_dir, self.name))  # 解压之后的就是name_std.pkl

    def process(self):

        import dgl
        import pickle
        # 打开pickle文件并加载数据
        with open(self.g_path, 'rb') as file: # self.g_path就是pkl文件
            graph = pickle.load(file)

#######     graph是标准图字典,imdb4MAGNN有A,D,M三类节点，A-M,D-M,M-A,M-D四类边，其中M类节点有label和mask
        cano_edges = {}
        for edge_type in graph['edge_index_dict'].keys():  # 'A_M'
            src_type = edge_type[0] # A
            dst_type = edge_type[-1]    # M
            edge_type_2 = src_type + '-' + dst_type # A-M
            
            cano_edge_type = (src_type,edge_type_2,dst_type)  # ('A','A-M','M')
            u,v = graph['edge_index_dict'][edge_type][0] ,graph['edge_index_dict'][edge_type][1]  # 边中的源点id，目点id

            cano_edges[cano_edge_type] = (u,v)



        hg = dgl.heterograph(cano_edges)

        for node_type in graph['X_dict'].keys() :  # 所有节点类型 
            hg.nodes[node_type].data['h'] = graph['X_dict'][node_type]  # node_type类节点的特征 h
            if node_type == 'M':
                hg.nodes[node_type].data['labels'] = graph['Y_dict'][node_type]  # node_type类节点的label 

        import torch

#########           构造train_mask,val_mask,test_mask
        # 设置节点数量
        num_nodes = 4278
        # 生成随机的节点索引
        random_indices = torch.randperm(num_nodes)
        # 设置训练、验证和测试集的大小
        num_train = 400
        num_val = 400
        num_test = 3478
        # 构造 train_mask
        train_mask = torch.zeros(num_nodes, dtype=torch.int)
        train_mask[random_indices[:num_train]] = 1
        # 构造 val_mask
        val_mask = torch.zeros(num_nodes, dtype=torch.int)
        val_mask[random_indices[num_train:num_train+num_val]] = 1

        # 构造 test_mask
        test_mask = torch.zeros(num_nodes, dtype=torch.int)
        test_mask[random_indices[num_train+num_val:]] = 1

        # 检查是否有交叉
        assert torch.sum(train_mask * val_mask) == 0
        assert torch.sum(train_mask * test_mask) == 0
        assert torch.sum(val_mask * test_mask) == 0


        hg.nodes['M'].data['train_mask'] = train_mask
        hg.nodes['M'].data['val_mask'] = val_mask
        hg.nodes['M'].data['test_mask'] = test_mask



#       如果要链接图数据库的话
        self._g = hg

 

#  getitem和len都没啥用，因为这是全图训练，相当于一共只有一个数据（整张图）
    def __getitem__(self, idx):
        # get one example by index
        assert idx == 0, "This dataset has only one graph"  #  大部分GNN都是全图训练，所以不会minibatch，不需要划分子图
        return self._g

    def __len__(self):
        # number of data examples
        return 1

#  不需要把graph保存到本地，留在程序中即可
    def save(self):
        # save processed data to directory `self.save_path`
        pass

    def load(self):
        # load processed data from directory `self.save_path`
        pass

    def has_cache(self):
        # check whether there are processed data in `self.save_path`
        pass




# 模板，很适合处理各种数据集，这是模板更新后的代码
class DBLP4MAGNN_Dataset(DGLDataset):

#   在init函数之前的成员，会默认有一个self前缀
    _prefix = 'https://s3.cn-north-1.amazonaws.com.cn/dgl-data/'
    _urls = {
        'dblp4MAGNN': 'dataset/openhgnn/dblp4MAGNN_std.zip',
}

    def __init__(self, name, raw_dir=None, force_reload=False, verbose=True):
        assert name in [
                        'dblp4MAGNN', 
                        ]
        
        
        raw_dir = './openhgnn/dataset'        

        
        # 这是从云盘上下载下来的  本地zip文件（的本地存放路径）  
        self.data_path = './openhgnn/dataset/'+ name +'_std.zip'  #  。openhgnn/dataset/    +  dblp4MAGNN_std.zip
        # name:dblp4MAGNN_std   # 云端压缩文件 dblp4MAGNN_std.zip    # 解压出来的文件dblp.pkl
        
#   这是标准的graph.pkl文件               dblp4MAGNN
        self.g_path = './openhgnn/dataset/' + name + '/dblp.pkl'   # 解压出来的文件：dblp.pkl



        url = self._prefix + self._urls[name]  # https://s3.cn-north-1.amazonaws.com.cn/dgl-data/ +  dataset/dblp4MAGNN_std.zip
 

 #     调用DGLDataset的初始化函数，会依次执行_download(),precess(),save()
        super(DBLP4MAGNN_Dataset, self).__init__(name=name,
                                        url=url,
                                        raw_dir=raw_dir, # save_dir默认等于raw_dir
                                        force_reload=force_reload,
                                        verbose=verbose)

    def download(self):
        # download raw data to local disk
        # path to store the file
        if os.path.exists(self.data_path):  # data_path是zip文件
           # data_path指的是zip文件，已经有了的话，那就不需要下载和解压
           pass
        else:
            #                        raw_dir目录
            download(self.url, 
                     path=os.path.join(self.raw_dir))   #  在raw_dir目录内，下载一个zip文件

        #  正常来说下载的zip文件就是data_path，             raw_dir / name  这个是目录
        extract_archive(self.data_path, os.path.join(self.raw_dir, self.name))  # 解压之后的就是dblp.pkl

    def process(self):

        import dgl
        import pickle
        # 打开pickle文件并加载数据
        with open(self.g_path, 'rb') as file:
            graph = pickle.load(file)

        cano_edges = {}
        for edge_type in graph['edge_index_dict'].keys():  # 'A_P'
            src_type = edge_type[0] # A
            dst_type = edge_type[-1]    # P
            edge_type_2 = src_type + '-'+dst_type # A-P
            
            cano_edge_type = (src_type,edge_type_2,dst_type)  # ('A','A-P','P')
            u,v = graph['edge_index_dict'][edge_type][0] ,graph['edge_index_dict'][edge_type][1]  # 边中的源点id，目点id

            cano_edges[cano_edge_type] = (u,v)



        hg = dgl.heterograph(cano_edges)

        for node_type in graph['X_dict'].keys() :  # 所有节点类型 
            hg.nodes[node_type].data['h'] = graph['X_dict'][node_type]  # node_type类节点的特征h
            if node_type == 'A':
                hg.nodes[node_type].data['labels'] = graph['Y_dict'][node_type]  # node_type类节点的label 

        import torch

        # 设置节点数量
        num_nodes = 4057

        # 生成随机的节点索引
        random_indices = torch.randperm(num_nodes)

        # 设置训练、验证和测试集的大小
        num_train = 400
        num_val = 400
        num_test = 3257

        # 构造 train_mask
        train_mask = torch.zeros(num_nodes, dtype=torch.int)
        train_mask[random_indices[:num_train]] = 1

        # 构造 val_mask
        val_mask = torch.zeros(num_nodes, dtype=torch.int)
        val_mask[random_indices[num_train:num_train+num_val]] = 1

        # 构造 test_mask
        test_mask = torch.zeros(num_nodes, dtype=torch.int)
        test_mask[random_indices[num_train+num_val:]] = 1

        # 检查是否有交叉
        assert torch.sum(train_mask * val_mask) == 0
        assert torch.sum(train_mask * test_mask) == 0
        assert torch.sum(val_mask * test_mask) == 0


        hg.nodes['A'].data['train_mask'] = train_mask
        hg.nodes['A'].data['val_mask'] = val_mask
        hg.nodes['A'].data['test_mask'] = test_mask



#       如果要链接图数据库的话
        self._g = hg

####################################    这些是我自己加的内容 ##############################################



 


#  getitem和len都没啥用，因为这是全图训练，相当于一共只有一个数据（整张图）
    def __getitem__(self, idx):
        # get one example by index
        assert idx == 0, "This dataset has only one graph"  #  大部分GNN都是全图训练，所以不会minibatch，不需要划分子图
        return self._g

    def __len__(self):
        # number of data examples
        return 1

#  不需要把graph保存到本地，留在程序中即可
    def save(self):
        # save processed data to directory `self.save_path`
        pass

    def load(self):
        # load processed data from directory `self.save_path`
        pass

    def has_cache(self):
        # check whether there are processed data in `self.save_path`
        pass





#   这是模板的原始代码  ,   生成csv文件
    
class AcademicDataset(DGLDataset):

#   在init函数之前的成员，会默认有一个self前缀
    _prefix = 'https://s3.cn-north-1.amazonaws.com.cn/dgl-data/'
    _urls = {
        'academic4HetGNN': 'dataset/academic4HetGNN.zip',
        'acm4GTN': 'dataset/acm4GTN.zip',
        'acm4NSHE': 'dataset/acm4NSHE.zip',
        'acm4NARS': 'dataset/acm4NARS.zip',
        'acm4HeCo': 'dataset/acm4HeCo.zip',
        'imdb4MAGNN': 'dataset/imdb4MAGNN.zip',
        'imdb4GTN': 'dataset/imdb4GTN.zip',
        'DoubanMovie': 'dataset/DoubanMovie.zip',

#############################################################
        'dblp4MAGNN': 'dataset/dblp4MAGNN.zip',
##################################################################
        'yelp4HeGAN': 'dataset/yelp4HeGAN.zip',
        'yelp4rec': 'dataset/yelp4rec.zip',
        'HNE-PubMed': 'dataset/HNE-PubMed.zip',
        'MTWM': 'dataset/MTWM.zip',
        'amazon4SLICE': 'dataset/amazon4SLICE.zip'
    }

    def __init__(self, name, raw_dir=None, force_reload=False, verbose=True):
        assert name in ['acm4GTN', 'acm4NSHE', 'academic4HetGNN', 'imdb4MAGNN', 'imdb4GTN', 'HNE-PubMed', 'MTWM',
                        'DoubanMovie', 'dblp4MAGNN', 'acm4NARS', 'acm4HeCo', 'yelp4rec', 'yelp4HeGAN', 'amazon4SLICE']
        
        # 这是从云盘上下载下来的zip文件（的本地存放路径）
        self.data_path = './openhgnn/' + self._urls[name]  #  。openhgnn/ +    dataset/dblp4MAGNN.zip

#   这是处理之后的graph文件（的位置）          dblp4MAGNN
        self.g_path = './openhgnn/dataset/' + name + '/graph.bin'  

        raw_dir = './openhgnn/dataset'

        url = self._prefix + self._urls[name]  # https://s3.cn-north-1.amazonaws.com.cn/dgl-data/ +  dataset/dblp4MAGNN.zip
 

 #     调用DGLDataset的初始化函数，会依次执行_download(),precess(),save()
        super(AcademicDataset, self).__init__(name=name,
                                        url=url,
                                        raw_dir=raw_dir, # save_dir默认等于raw_dir
                                        force_reload=force_reload,
                                        verbose=verbose)

    def download(self):
        # download raw data to local disk
        # path to store the file
        if os.path.exists(self.data_path):  # data_path是zip文件
           # data_path指的是zip文件，已经有了的话，那就不需要下载和解压
           pass
        else:
            file_path = os.path.join(self.raw_dir)
            #                        raw_dir目录
            download(self.url, path=file_path)   #  在raw_dir目录内，下载一个zip文件

        #  正常来说下载的zip文件就是data_path，             raw_dir / name  这个是目录
        extract_archive(self.data_path, os.path.join(self.raw_dir, self.name))  # 解压之后的就是graph.bin

    def process(self):
        # process raw data to graphs, labels, splitting masks
        g, _ = load_graphs(self.g_path)  # g_path就是解压之后的graph.bin。
        #  g是一个list，只有一个元素g[0]:dgl.heterograph.DGLgraph

#       self._g就是一个DGLGraph
        self._g = g[0]

####################################    这些是我自己加的内容 ##############################################
     #以下内容的作用是，根据DGLGraph，得到对应的节点和边的csv文件，这些csv文件用于向图数据库上传

        node_dir = os.path.join(self.raw_dir,   #  dblp数据集的 节点数据目录，目录下存放的是 每个类型节点 的特征和label
                                self.name,
                                'node_dir')
        if not os.path.exists(node_dir):   # 如果 节点目录不存在，则创建目录
            os.makedirs(node_dir)

        import csv
        for node_type in self._g.ntypes:  #  ['A','P','T','V']
            # print(self._g.nodes['A'].data['h'])             # 节点数4057 * 特征长度300
            # print(self._g.nodes['A'].data['lables'])        #  节点数
            # print(self._g.nodes['A'].data['train_mask'])    #  节点数
            # 只有A节点有labels，和train_mask,test_mask,valid_mask

            #   当前节点类型 ,所有类型节点 都有特征 h
            node_ids = self._g.nodes(node_type)  # 全部节点id
            h_feat = self._g.nodes[node_type].data['h']  #  节点特征

           # dblp只有A类节点有Label和mask，imdb只有M类节点     
            if node_type == 'M':
                labels =self._g.nodes[node_type].data['labels'] # 某类节点才有label
                data = list(zip(node_ids.tolist(), labels.tolist(), h_feat.tolist()))
            else: # 其他类节点没有label
                data = list(zip(node_ids.tolist(),h_feat.tolist()))
            
#############################       节点数据直接写到 csv   ##########################################################
            print("生成当前类型节点的 csv文件:",node_type)
            node_file = os.path.join(node_dir,
                                    node_type + '.csv')

            if not os.path.exists(node_file):
                # 创建 节点txt文件  ，并写入内容
                with open(node_file, 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)

                # dblp只有A类节点有Label和mask，imdb只有M类节点
                # 先写第一行，ID,label,attribute
                    if node_type == 'M':  
                        csv_writer.writerow(['ID', 'label', 'attribute']) # 列名
                    else:
                        csv_writer.writerow(['ID', 'attribute']) # 列名

                # 再把全部节点数据写入
                    # for now_id,now_label,now_feat in data:
                    #     csv_writer.writerow([now_id, now_label, now_feat])
                    csv_writer.writerows(data) # 把data中全部行都写入




#########################    版本1，先写txt(这个版本弃置)
            # print("生成当前类型节点的 txt文件:",node_type)
            # node_file = os.path.join(node_dir,
            #                         node_type + '.txt')
            # if not os.path.exists(node_file):
            #     # 创建 节点txt文件  ，并写入内容
            #     with open(node_file, 'w') as file:
            #         for now_id, now_label,now_feat in list(     zip(node_ids.tolist(), labels.tolist(),h_feat.tolist())     ):
            #             # 将每个节点的信息写入文件
            #             # print(now_id.item())  # now_id是Tensor，它的item就是把Tensor中的数字返回，但是只适合只有一个元素的Tensor
            #             # print(now_label.item())
            #             # print(now_feat.numpy())

            #             file.write(f"{now_id},{now_label},{now_feat}\n")  #  在txt文件中，我用逗号 , 分隔源点ID和目点ID

###################################################################################



# 单独看一下  A类型  节点 的特征、标签和tvt划分
        # print(self._g.nodes['A'].data['h'])             # 节点数 * 特征长度
        # print(self._g.nodes['A'].data['labels'])        #  节点数*1
        # print(self._g.nodes['A'].data['train_mask'])    #  节点数*1

#  单独看一下，A-P这类边
        # src_id , dst_id = self._g.all_edges(etype = ('A','A-P','P'))  # 取出所有类型为'A-P'的边，src_id是源节点id，dst_id是目的节点id，他们的维度都是边的数量
                    

        edge_dir = os.path.join(self.raw_dir,   #  dblp数据集的 边目录，目录下存放每个规范边的txt文件
                                self.name,
                                'edge_dir')
        if not os.path.exists(edge_dir):   # 如果 边目录不存在，则创建目录
            os.makedirs(edge_dir)


        for src_type, edge_type, dst_type in self._g.canonical_etypes:  # 遍历每一种边类型（相当于每一个边子图）

            print("生成当前的边子图txt文件:",src_type, "_",edge_type,"_", dst_type)
            src_id  , dst_id = self._g.all_edges(etype = (src_type,edge_type,dst_type))  #  返回这种边子图 中的源节点id和目的节点id
            edge_file = os.path.join(edge_dir,
                                    src_type + '_'+edge_type +'_'+ dst_type + '.txt')
            
            if not os.path.exists(edge_file):
                # 创建 边txt文件  ，并写入内容
                with open(edge_file, 'w') as file:
                    for now_src_id, now_dst_id in zip(src_id, dst_id):
                        # 将每条边的信息写入文件
                        file.write(f"{now_src_id.item()},{now_dst_id.item()}\n")  #  在txt文件中，我用逗号 , 分隔源点ID和目点ID

            #  因为txt文件中就是用逗号分隔，因此只需要改个后缀，就能变成csv文件
                csv_file = os.path.splitext(edge_file)[0] + '.csv'
                os.rename(edge_file, csv_file)            

        


#  getitem和len都没啥用，因为这是全图训练，相当于一共只有一个数据（整张图）
    def __getitem__(self, idx):
        # get one example by index
        assert idx == 0, "This dataset has only one graph"  #  大部分GNN都是全图训练，所以不会minibatch，不需要划分子图
        return self._g

    def __len__(self):
        # number of data examples
        return 1

#  不需要把graph保存到本地，留在程序中即可
    def save(self):
        # save processed data to directory `self.save_path`
        pass

    def load(self):
        # load processed data from directory `self.save_path`
        pass

    def has_cache(self):
        # check whether there are processed data in `self.save_path`
        pass


