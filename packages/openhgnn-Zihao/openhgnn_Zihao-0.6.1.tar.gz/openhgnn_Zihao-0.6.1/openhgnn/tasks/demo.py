import torch.nn.functional as F

from . import BaseTask, register_task
from ..dataset import build_dataset
from ..utils import Evaluator


@register_task("demo")  
class Demo(BaseTask):
    """Demo task."""
    def __init__(self, args):
        super(Demo, self).__init__()
        self.n_dataset = args.dataset
        self.dataset = build_dataset(args.dataset, 'demo')
        # self.evaluator = Evaluator()
        self.evaluator = Evaluator(args.seed)

    def get_graph(self):
        return getattr(self.dataset, 'g', self.dataset[0])

    def get_loss_fn(self):
        return F.binary_cross_entropy_with_logits

    def get_evaluator(self, name):
        if name == 'acc':
            return self.evaluator.author_link_prediction
        elif name == 'mrr':
            return self.evaluator.mrr_
        elif name == 'academic_lp':
            return self.evaluator.author_link_prediction

    def evaluate(self, y_true, y_score, name):
        if name == 'ndcg':
            return self.evaluator.ndcg(y_true, y_score)
        

##########################################################
#        下面是一个简单模板，可以根据这个来改


# trainer中build_task(args)就是返回一下下面的实例

@register_task("GGNN_link_prediction")
class DisenKGAT_LinkPrediction(BaseTask):
    r"""
    Link prediction tasks for DisenKGAT

    """
#                       args就是最外层的config
    def __init__(self,   args  )  :
        super(DisenKGAT_LinkPrediction, self).__init__()
        self.logger = None
        # dataset = 'DisenKGAT_WN18RR' 或者 'DisenKGAT_FB15k-237'      
        self.dataset = build_dataset(dataset = args.dataset, task='link_prediction', # 只有前两个参数是必传的，后面的都是可传可不传
                                     args=args) # 传入args，就是最初的config
        self.raw_dir = self.dataset.raw_dir
        self.processed_dir = self.dataset.processed_dir

    def evaluate(self):
        return None
    





