#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def kalman(A,B,F,C,Q,R,xk,Pk,uk,yk):
    #Correction
    # TODO
    #Prediction
    #TODO
    return xk1,Pk1

def node():
   A=np.matrix('1.6551, -0.7408;1,0')
   B=np.matrix('0.25;0')
   C=np.matrix('0.1799, 0.1628')
   T, tf = 0.01, 0.8
   kf, n = int(tf/T), A.shape[0]
   xk, xn = np.matrix(np.zeros((n,1))), np.matrix(np.zeros((n,1)))
   yg, y, yn, t = np.zeros((kf)), np.zeros((kf)), np.zeros((kf)), np.zeros((kf))
   Q, R = 0.05, 0.5
   xg = np.matrix('0;0') # First State Estimation
   Pk = B*Q*B.T          # Estimation covariance
   for k in range(kf):
      t[k] = k*T
      wk, vk = np.random.normal(0, Q, 1), np.random.normal(0, R, 1)
      uk = 1 if (k*T < 0.4) else 2
      # -- nominal --
      yn[k] = C*xn
      xn = A*xn + B*uk
      # -- Noisy --
      y[k] = C*xk + vk
      xk = A*xk + B*uk + B*wk
      # -- Filtered from noisy --
      xg,Pk = kalman(A,B,B,C,Q,R,xg,Pk,uk,y[k])
      yg[k] = C*xg
   plt.plot(t,y,'r',t,yg,'b',t,yn,'g')
   plt.legend(['Noisy','Kalman','Nominal'])
   plt.axis([0,tf,-1,3])
   plt.xlabel('time [sec]')
   plt.ylabel('C voltage [V]')
   plt.title('Kalman behavior')
   plt.show()


if __name__ == '__main__':
    node()
