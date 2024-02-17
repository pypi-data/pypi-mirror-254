import numpy as np
import torch
import subprocess
import random


# 轮盘赌算法
def rws(fitness_scores, population=None):
    total_fitness = sum(fitness_scores)
    selection_probs = [fitness / total_fitness for fitness in fitness_scores]

    # 使用轮盘赌算法选择个体
    selected_index = None
    rand_num = random.uniform(0, 1)
    cumulative_prob = 0

    for i, prob in enumerate(selection_probs):
        cumulative_prob += prob
        if rand_num <= cumulative_prob:
            selected_index = i
            break
    if population is not None:
        selected_individual = population[selected_index]
    else:
        selected_individual = selected_index
    return selected_individual


class GpuMemory(object):
    def __init__(self):
        pass

    def getInfo(self):
        res = {}
        res['torchVersion'] = torch.__version__
        cuda_available = torch.cuda.is_available()
        res['cudaAvailable'] = cuda_available
        if cuda_available:
            # 获取GPU设备数量
            num_gpu = torch.cuda.device_count()
            res['gpuNum'] = num_gpu
            res['gpuInfo'] = []

            command = 'nvidia-smi --query-gpu=memory.total --format=csv'
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            output = result.stdout.strip().split('\n')[1:]  # 删除标题行
            total_memory = [float(line.split(',')[0].strip().split(' ')[0].strip()) for line in output]
            command = 'nvidia-smi --query-gpu=memory.used --format=csv'
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            output = result.stdout.strip().split('\n')[1:]  # 删除标题行
            used_memory = [float(line.split(',')[0].strip().split(' ')[0].strip()) for line in output]
            command = 'nvidia-smi --query-gpu=memory.free --format=csv'
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            output = result.stdout.strip().split('\n')[1:]  # 删除标题行
            free_memory = [float(line.split(',')[0].strip().split(' ')[0].strip()) for line in output]

            for current_gpu_index in range(num_gpu):
                # 获取当前GPU的名称
                info = {}
                info['name'] = torch.cuda.get_device_name(current_gpu_index)

                # 获取GPU显存的总量和已使用量
                info['totalMemory'] = total_memory[current_gpu_index] / 1024.0  # 显存总量(GB)
                info['usedMemory'] = used_memory[current_gpu_index] / 1024.0  # 已使用显存(GB)
                info['freeMemory'] = free_memory[current_gpu_index] / 1024.0  # 剩余显存(GB)
                res['gpuInfo'].append(info)
        return res;

    def __str__(self):
        res = self.getInfo()
        ss = ''
        ss += f"PyTorch版本：{res['torchVersion']}\n"
        if res['cudaAvailable']:
            ss += f"CUDA可用，共有 {res['gpuNum']} 个GPU设备可用。\n"
            for current_gpu_index, info in enumerate(res['gpuInfo']):
                ss += f"第{current_gpu_index}块显卡信息如下：\n"
                ss += f"\tGPU设备名称：{info['name']}\n"
                ss += f"\tGPU显存总量：{info['totalMemory']:.2f} GB\n"
                ss += f"\t已使用的GPU显存：{info['usedMemory']:.2f} GB\n"
                ss += f"\t剩余GPU显存：{info['freeMemory']:.2f} GB\n"
        else:
            ss = "CUDA不可用。\n"
        return ss

    def gpuIdWithMaxFree(self):
        res = self.getInfo()
        ind = -1;
        freeMemory = 0
        name = ''
        for current_gpu_index, info in enumerate(res['gpuInfo']):
            if info['freeMemory'] > freeMemory:
                freeMemory = info['freeMemory']
                ind = current_gpu_index
                name = info['name']
        return ind, freeMemory, name

    def gpuIdWithRws(self, sharp=2.0):
        if sharp == np.inf:
            return self.gpuIdWithMaxFree()
        res = self.getInfo()
        fitness_scores = [info['freeMemory'] ** sharp for info in res['gpuInfo']]
        maxScore = max(fitness_scores)
        fitness_scores = [score / maxScore for score in fitness_scores]
        ind = rws(fitness_scores)
        freeMemory = res['gpuInfo'][ind]['freeMemory']
        name = res['gpuInfo'][ind]['name']
        return ind, freeMemory, name


if __name__ == "__main__":
    mem = GpuMemory()
    print(mem.gpuIdWithRws(sharp=np.inf))
