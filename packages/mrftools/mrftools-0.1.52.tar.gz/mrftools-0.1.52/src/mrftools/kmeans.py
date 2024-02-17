from mrftools import KMeansModes

import math
import torch
from time import time
import numpy as np

class KMeans:
  def __init__(self, n_clusters, max_iter=100, tol=0.0001, verbose=0, mode=KMeansModes.EUCLIDEAN, minibatch=None, random_state=1234):
    self.n_clusters = n_clusters
    self.max_iter = max_iter
    self.tol = tol
    self.verbose = verbose
    self.mode = mode
    self.minibatch = minibatch
    self._loop = False
    self._show = False
    self.centroids = None
    self.random_state=random_state

  @staticmethod
  def cos_sim(a, b):
    a_norm = a.norm(dim=-1, keepdim=True)
    b_norm = b.norm(dim=-1, keepdim=True)
    a = a / (a_norm + 1e-8)
    b = b / (b_norm + 1e-8)
    return a @ b.transpose(-2, -1)

  @staticmethod
  def euc_sim(a, b):
    return 2 * a @ b.transpose(-2, -1) -(a**2).sum(dim=1)[..., :, None] - (b**2).sum(dim=1)[..., None, :]

  def max_sim(self, a, b):
    device = a.device.type
    batch_size = a.shape[0]
    if self.mode == KMeansModes.COSINE:
      sim_func = self.cos_sim
    elif self.mode == KMeansModes.EUCLIDEAN:
      sim_func = self.euc_sim

    if device == 'cpu':
      sim = sim_func(a, b)
      max_sim_v, max_sim_i = sim.max(dim=-1)
      return max_sim_v, max_sim_i
    else:
      if a.dtype == torch.double:
        expected = a.shape[0] * a.shape[1] * b.shape[0] * 8
      if a.dtype == torch.float:
        expected = a.shape[0] * a.shape[1] * b.shape[0] * 4
      elif a.dtype == torch.half:
        expected = a.shape[0] * a.shape[1] * b.shape[0] * 2
      ratio = math.ceil(expected / self.remaining_memory())
      subbatch_size = math.ceil(batch_size / ratio)
      msv, msi = [], []
      for i in range(ratio):
        if i*subbatch_size >= batch_size:
          continue
        sub_x = a[i*subbatch_size: (i+1)*subbatch_size]
        sub_sim = sim_func(sub_x, b)
        sub_max_sim_v, sub_max_sim_i = sub_sim.max(dim=-1)
        del sub_sim
        msv.append(sub_max_sim_v)
        msi.append(sub_max_sim_i)
      if ratio == 1:
        max_sim_v, max_sim_i = msv[0], msi[0]
      else:
        max_sim_v = torch.cat(msv, dim=0)
        max_sim_i = torch.cat(msi, dim=0)
      return max_sim_v, max_sim_i

  def fit_predict(self, X, centroids=None):
    np.random.seed(self.random_state) 
    batch_size, emb_dim = X.shape
    device = X.device.type
    start_time = time()
    if centroids is None:
      self.centroids = X[np.random.choice(batch_size, size=[self.n_clusters], replace=False)]
    else:
      self.centroids = centroids
    num_points_in_clusters = torch.ones(self.n_clusters, device=device)
    closest = None
    for i in range(self.max_iter):
      iter_time = time()
      if self.minibatch is not None:
        x = X[np.random.choice(batch_size, size=[self.minibatch], replace=False)]
      else:
        x = X
      closest = self.max_sim(a=x, b=self.centroids)[1]
      matched_clusters, counts = closest.unique(return_counts=True)

      c_grad = torch.zeros_like(self.centroids)
      if self._loop:
        for j, count in zip(matched_clusters, counts):
          c_grad[j] = x[closest==j].sum(dim=0) / count
      else:
        if self.minibatch is None:
          expanded_closest = closest[None].expand(self.n_clusters, -1)
          mask = (expanded_closest==torch.arange(self.n_clusters, device=device)[:, None]).to(X.dtype)
          c_grad = mask @ x / mask.sum(-1)[..., :, None]
          c_grad[c_grad!=c_grad] = 0 # remove NaNs
        else:
          expanded_closest = closest[None].expand(len(matched_clusters), -1)
          mask = (expanded_closest==matched_clusters[:, None]).to(X.dtype)
          c_grad[matched_clusters] = mask @ x / mask.sum(-1)[..., :, None]
      error = (c_grad - self.centroids).pow(2).sum()
      if self.minibatch is not None:
        lr = 1/num_points_in_clusters[:,None] * 0.9 + 0.1
      else:
        lr = 1
      num_points_in_clusters[matched_clusters] += counts
      self.centroids = self.centroids * (1-lr) + c_grad * lr
      if self.verbose >= 2:
        print('iter:', i, 'error:', error.item(), 'time spent:', round(time()-iter_time, 4))
      if error <= self.tol:
        break
    if self.verbose >= 1:
      print(f'used {i+1} iterations ({round(time()-start_time, 4)}s) to cluster {batch_size} items into {self.n_clusters} clusters')
    return closest

  def predict(self, X):
    return self.max_sim(a=torch.tensor(X), b=self.centroids)[1]

  def fit(self, X, centroids=None):
    return self.fit_predict(torch.tensor(X), centroids)