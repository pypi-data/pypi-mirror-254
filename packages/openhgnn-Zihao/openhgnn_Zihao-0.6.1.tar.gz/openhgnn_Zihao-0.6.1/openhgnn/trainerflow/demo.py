import copy
import dgl
import numpy as np
import torch as th
from tqdm import tqdm
import torch.nn as nn
import torch
import torch.nn.functional as F
from . import BaseFlow, register_flow
from ..tasks import build_task
from ..utils import extract_embed, get_nodes_dict
from collections.abc import Mapping
from ..models import build_model


@register_flow("demo")  # 这是一个trainer
class Demo(BaseFlow):
    """Demo flows."""

    def __init__(self, args):  # 这个args 就是最外层config（包括config.ini中的内容和 model,dataset
                                                        #  task,gpu,seed,logger等
        super(Demo, self).__init__(args)

#########           修改处,例如模型是GGNN,任务是link_prediction
#   我们把model和task组合到一起，作为一个新的task，用这个新的task注册

        args.task = args.model +"_" +args.task # task: GGNN_link_prediction


        self.args = args
        self.model_name = args.model
        self.device = args.device

#      在task对象的init函数中，会build_dataset下载原始数据，把原始数据处理成 异质图hg
        
        self.task = build_task(args) # args 就是 最开始的config
        self.hg = self.task.get_graph().to(self.device)


#     我希望在task中的build_dataset中，dataset只负责下载原始数据，然后返回一个raw_dir目录，存放原始数据
#     然后再flow(trainer)中对原始数据做处理，生成hg。
######     修改处       #################        
        self.raw_dir = self.task.raw_dir
        self.process_dir = self.task.raw_dir


        self.model = build_model(self.model).build_model_from_args(self.args, self.hg)
        self.model = self.model.to(self.device)
    def preprocess(self):

        return

    def train(self):
        pass

    def _mini_train_step(self,):
        pass

    def loss_calculation(self, positive_graph, negative_graph, embedding):
        pass

    def _full_train_setp(self):
        pass

    def _test_step(self, split=None, logits=None):
        pass