import numpy as np 
import torch 


list = [1,2,3]
tensor = torch.tensor([0, 1])
ndarray = np.array([1,2,3])  

# list to torch.Tensor
tensor=torch.Tensor(list)
# list to numpy
ndarray = np.array(list)

# torch.Tensor to numpy
ndarray = tensor.numpy()
# torch.Tensor to list
list = tensor.numpy().tolist() # 先转 numpy，后转 list

# numpy to torch.Tensor
tensor = torch.from_numpy(ndarray) 
# numpy to list
list = ndarray.tolist()
