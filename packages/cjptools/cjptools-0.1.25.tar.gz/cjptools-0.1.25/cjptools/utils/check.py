from numpy import linalg as LA
import torch
import torch.nn.functional as F
import copy

modelHolder = {}


def addModel(name, model):
    modelHolder[name] = copy.deepcopy(model)


def getModel(name):
    return modelHolder[name]


def checkNorm(ts):
    if isinstance(ts, torch.Tensor):
        with torch.no_grad():
            res = torch.norm(ts).item();
            return res
    return LA.norm(ts)


def modelCosSimilarity(model1, model2):
    param1 = torch.cat([param.view(-1) for param in model1.parameters()])
    param2 = torch.cat([param.view(-1) for param in model2.parameters()])
    cosine_sim = F.cosine_similarity(param1, param2, dim=0)
    return cosine_sim.item()


def modelNormSimilarity(model1, model2):
    param1 = torch.cat([param.view(-1) for param in model1.parameters()])
    param2 = torch.cat([param.view(-1) for param in model2.parameters()])
    euclidean_dist = torch.norm(param1 - param2)
    return euclidean_dist.item()


def modelNorm(model):
    param1 = torch.cat([param.view(-1) for param in model.parameters()])
    euclidean_dist = torch.norm(param1)
    return euclidean_dist.item()
