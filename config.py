# -*-coding:utf-8-*-
import warnings


class Config(object):
    def __init__(self):
        """
        初始化系列参数方便修改
        """
        # 这一部分设置数据导入导出路径
        self.trainFolder = 'dataReader/readyTrain/'  # 训练图像路径
        self.testFolder = 'dataReader/test/'  # 测试图像路径
        self.modelPath = 'snapshots/res18.pth'  # 模型存储路径
        self.queryFolder = 'dataReader/query/'  # 查询图像路径
        # 这一部分设置模型基本参数
        self.lr = 1e-3
        self.weightDecay = 1e-3
        self.batchSize = 90
        self.maxEpoch = 100
        self.lrDecay = 0.1  # 学习率下降率
        self.lrDecayRate = 40  # 每隔那么多次，学习率就下降一下
        self.minLR = 1e-8  # 学习率最小值
        self.numClass = 702
        self.lossFunc = 'CrossEntropyLoss'  # 对应的损失函数
        self.trainRate = 0.98  # 用于训练的图像比例
        # 这一部分设置模型训练中其余的参数
        self.printFreq = 60  # 隔60次打印一下
        self.useGpu = True  # 要不要GPU
        self.model = 'resnet18'  # 模型名字
        self.numWorker = 4  # 线程数
        self.snapFreq = 10  # 每过这么多轮保存一下快照
        self.isPreTrain = True  # 是否使用预训练模型
        self.topN = 6  # 计算CMC曲线排名前几

    def parse(self, **kwargs):
        # 按照用户配置更新参数
        for k, v in kwargs.items():
            if not getattr(self, k):
                warnings.warn("no %s found" % k)
            setattr(self, k, v)
        print('user config:')
        for k, v in vars(self).items():
            if not k.startswith('__'):
                # 非内部构建的函数
                print(k, v)


opt = Config()  # 实例化一个对象好导出
