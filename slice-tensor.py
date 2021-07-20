# The data changes [4, 161, 325] → [4, 161, 324] by removing the first element in the 3rd dimension
import torch

# ver 1
a = torch.randn(4, 161, 325)
b = a[:, :, 1:]
b.shape
# ver 2
a = torch.rand(4,161,325)
b = a[..., 1:]            # or t = t[Ellipsis, 1:] Here, Ellipsis indicate rest of dims
b.shape
