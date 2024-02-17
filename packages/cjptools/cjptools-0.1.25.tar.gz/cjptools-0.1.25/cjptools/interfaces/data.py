from cjptools import checkNorm
def display_data_details(data_loader):
    # 获取数据集的长度
    res = ''
    dataset_size = len(data_loader.dataset)
    res += f"数据集大小：{dataset_size}\n"
    # 获取每个batch的大小
    batch_size = data_loader.batch_size
    res += f"每个批次大小：{batch_size}\n"
    # 计算总共有多少个批次
    num_batches = len(data_loader)
    res += f"总批次数：{num_batches}\n"
    # 获取第一个批次的数据
    batch = data_loader.dataset.__getitem__(0)
    # 获取批次中的输入和标签
    inputs, labels = batch
    # 打印输入张量的形状
    res += f"输入形状（单样本）：{inputs.shape}，数据类别：{inputs.dtype}。\n"
    # 打印标签张量的形状
    res += f"标签"
    if hasattr(labels,'shape'):
        res += f"形状（单样本）：{labels.shape}，"
    if hasattr(labels,'dtype'):
        res += f"数据类别：{labels.dtype}。\n"
    else:
        res += f"数据类别：{type(labels)}。\n"
    # 打印输入和标签的摘要信息
    res += f"第一个样本的输入范数为：{checkNorm(inputs)}\n"
    # res += str(inputs).replace('\n\n', '\n')  # 打印前五个样本的输入
    res += f"第一个样本的输出：{labels}"
    # res += str(labels)  # 打印前五个样本的标签
    return res


class DataLoader(object):
    def __init__(self, localTrains=None, localVals=None, localTests=None, globalTrain=None, globalVal=None,
                 globalTest=None):
        self._localTrains = localTrains
        self._localVals = localVals
        self._localTests = localTests
        self._globalTrain = globalTrain
        self._globalVal = globalVal
        self._globalTest = globalTest

    @property
    def localTrains(self):
        return self._localTrains

    @property
    def localVals(self):
        return self._localVals

    @property
    def localTests(self):
        return self._localTests

    @property
    def globalTrain(self):
        return self._globalTrain

    @property
    def globalVal(self):
        return self._globalVal

    @property
    def globalTest(self):
        return self._globalTest

    def __str__(self):
        res = ""
        if self.localTrains:
            res += "\n====================本地训练数据集===================="
            for (i, dataloader) in enumerate(self.localTrains):
                if dataloader:
                    res += f"\n> [本地训练数据集 {i}]\n"
                    res += display_data_details(dataloader)
                else:
                    res += f"\n> [warning] 本地训练数据集 {i} 不存在！"
        if self.localVals:
            res += "\n====================本地验证数据集===================="
            for (i, dataloader) in enumerate(self.localVals):
                if dataloader:
                    res += f"\n> [本地验证数据集 {i}]\n"
                    res += display_data_details(dataloader)
                else:
                    res += f"\n> [warning] 本地验证数据集 {i} 不存在！"
        if self.localTests:
            res += "\n====================本地测试数据集===================="
            for (i, dataloader) in enumerate(self.localTests):
                if dataloader:
                    res += f"\n> [本地测试数据集 {i}]\n"
                    res += display_data_details(dataloader)
                else:
                    res += f"\n> [warning] 本地测试数据集 {i} 不存在！"
        if self.globalTrain:
            res += "\n====================全局训练数据集====================\n"
            res += display_data_details(self.globalTrain)
        if self.globalVal:
            res += "\n====================全局验证数据集====================\n"
            res += display_data_details(self.globalVal)
        if self.globalTest:
            res += "\n====================全局测试数据集====================\n"
            res += display_data_details(self.globalTest)

        return res[1:] if len(res) > 0 else "[warning] 未包含任何有效数据！"
