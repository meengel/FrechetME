### Michael Engel ### 2023-12-22 ### src.py ###
import numpy as np
import torch

# main functionality
def getFrechetMean(
        points,
        distance,
        startpoint = None,
        threshold = 1e-3,
        threshold_order = 1,
        optimizer = None,
        optimizerkwargs = {"lr":1e-2, "weight_decay":0},
        maxiter = 100,
        logger = print,
):
    points = np.array(points, ndmin=2)
    Nsamples, dim = points.shape
    
    points_torch = torch.tensor(points, requires_grad=False)
    if not np.all(startpoint):
        center = np.mean(points, axis=0, keepdims=True)
        C = torch.tensor(center, dtype=float, requires_grad=True)
    else:
        C = torch.tensor(startpoint, dtype=float, requires_grad=True)
        
    if not optimizer:
        optimizer = torch.optim.Adam([C], **optimizerkwargs)
    else:
        optimizer = optimizer([C], **optimizerkwargs)
      
    loss_old = torch.inf
    for i in range(maxiter):
        optimizer.zero_grad(set_to_none=True)
                
        loss = distance(C, points_torch)
        loss.backward()
        
        optimizer.step()

        if torch.norm(loss_old-loss.detach(), p=threshold_order)<threshold:
            logger(f"getFrechetMean: converged in {i+1} steps!")
            return C.detach().numpy()
        
        loss_old = loss.detach()
        
    logger(f"getFrechetMean: did not converge in {maxiter} steps!")
    logger(f"getFrechetMean: {i+1}/{maxiter}: {loss:.6e}: {C}: {C.grad}")
    return C.detach().numpy()

# distance measures
def eulerian(C, points):
    return torch.mean(torch.norm(C-points,dim=1,p=2)**2)

def geodesicMeanCartesian(C, points):
    return torch.mean(torch.arccos(torch.multiply(C,points)))

def geodesicMeanLonLat(C, points, R=1):
    dLat = points[:,[1]] * torch.pi / 180 - C[:,[1]] * torch.pi / 180
    dLon = points[:,[0]] * torch.pi / 180 - C[:,[0]] * torch.pi / 180
    a = torch.sin(dLat/2) * torch.sin(dLat/2) + torch.cos(points[:,[1]] * torch.pi / 180) * torch.cos(C[:,[1]] * torch.pi / 180) * torch.sin(dLon/2) * torch.sin(dLon/2)
    return torch.mean(2 * torch.arctan2(torch.sqrt(a), torch.sqrt(1-a)) * R)