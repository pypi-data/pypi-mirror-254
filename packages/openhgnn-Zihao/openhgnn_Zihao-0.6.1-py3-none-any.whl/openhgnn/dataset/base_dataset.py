from abc import ABC, ABCMeta, abstractmethod
from dgl.data.utils import load_graphs


class BaseDataset(ABC):  # 这个基类本身没啥用，主要看子类的成员
    def __init__(self, *args, **kwargs):
        super(BaseDataset, self).__init__()
        self.logger = kwargs['logger']  #  上层传过来的时候，logger也可以是None
        self.g = None
        self.meta_paths = None
        self.meta_paths_dict = None

    def load_graph_from_disk(self, file_path):  #  一般不用这个函数
        """
        load graph from disk and the file path of graph is generally stored in ``./openhgnn/dataset/``.

        Parameters
        ----------
        file_path: the file path storing the graph.bin

        Returns
        -------
        g: dgl.DGLHetrograph
        """
        g, _ = load_graphs(file_path)
        return g[0]

