from numba import jit 
from numba import njit
import numpy as np 
import random as rd 
@njit()
def check_la_phom(arr):
    k = []
    for i in arr: 
      if check_ca(i,arr[arr!=i]) == True :
          k.append(i)
    return k 

@njit()
def LongestConseqSubseq(arr, l):
    val = []
    c = 0
    for i in range(l):
        n = 1
        while arr[i] + n in arr:
            c += 1
            n += 1
        val.append(c + 1)
        c = 0
    return max(val)
@njit()

def check_u_khan(k):
  arr1 = k[np.where(k%4 == 0)[0]]//4
  arr2 = k[np.where(k%4 == 1)[0]]//4
  arr3 = k[np.where(k%4 == 2)[0]]//4
  arr4 = k[np.where(k%4 == 3)[0]]//4
  if len(arr1)> 0 :
    if LongestConseqSubseq(arr1,len(arr1)) > 1 :
      return False 
  if len(arr2)>0:
    if LongestConseqSubseq(arr2,len(arr2)) > 1 :
      return False 
  if len(arr3)>0 :
    if LongestConseqSubseq(arr3,len(arr3)) >1 :
      return False  
  if len(arr4)>0:
    if LongestConseqSubseq(arr4,len(arr4)) >1 :
      return False
  for i in range(0,13):
    if len(k[np.where(k//4 == i)[0]]) > 1 :
       return False
  return True

@njit()
def check_ca(a,arr):
    a1 = a%4
    arr1= arr[arr%4==a1]
    a2 = a//4
    arr3 = arr[arr//4==a2]
    if len(arr3)>=2:
      return True
    arr2 = arr1//4
    if a2+1 in arr2 and a2+2 in arr2:
      return True 
    elif a2-1 in arr2 and a2-2 in arr2:
      return True
    elif a2-1 in arr2 and a2+1 in arr2 :
      return True
    return False 

@njit()
def tim_diem_toi_uu(pt,py):
  k = []
  for i in pt: 
    if check_ca(i,pt[pt!=i]) == True :
        k.append(i)
  k = np.array(k)
  l =[]
  du_0 = k[np.where(k%4 == 0)[0]]
  du_1 = k[np.where(k%4 == 1)[0]]
  du_2 = k[np.where(k%4 == 2)[0]]
  du_3 = k[np.where(k%4 == 3)[0]]
  if len(du_0) >= 3:
    l0 = []
    for i in range(len(du_0)):
        if du_0[i] == du_0[i - 1] + 4:
            if du_0[i-1] not in l0:
              l0.append(du_0[i-1])
            if du_0[i] not in l0:
              l0.append(du_0[i])
    if len(l0)>2 :
      l0 = np.array(l0)
      l.append(l0)
  if len(du_1) >= 3:
    l1 = []
    for i in range(len(du_1)):
        if du_1[i] == du_1[i - 1] + 4:
            if du_1[i-1] not in l1:
              l1.append(du_1[i-1])
            if du_1[i] not in l1:
              l1.append(du_1[i])
    if len(l1)>2 :
      l1 =  np.array(l1)
      l.append(l1)  
  if len(du_2) >= 3:
    l2 = []
    for i in range(len(du_2)):
        if du_2[i] == du_2[i - 1] + 4:
            if du_2[i-1] not in l2:
              l2.append(du_2[i-1])
            if du_2[i] not in l2:
              l2.append(du_2[i])
    if len(l2)>2 :
      l2 =  np.array(l2)
      l.append(l2)
  if len(du_3) >= 3:
    l3 = []
    for i in range(len(du_3)):
        if du_3[i] == du_3[i - 1] + 4:
            if du_3[i-1] not in l3:
              l3.append(du_3[i-1])
            if du_3[i] not in l3:
              l3.append(du_3[i])
    if len(l3)>2 :
      l3 = np.array(l3)
      l.append(l3)
  arr1 = k//4
  l1 = []
  for i in range(0,13):
    l1.append(np.count_nonzero(arr1 == i))
  for i in np.where(np.array(l1)>=3)[0]:
    l.append(k[np.where(arr1==i)])

  y = []
  for i in l:
    if i  is not None :
      if len(i)>=4 :
        for j in range(3,len(i)+1):
          for k in range(0,len(i)-j+1):
              y.append(i[k:k+j])
      else: 
        y.append(i)

  lx = []
  r = []
  u = []
  for i in range(len(y)):
    for j in range(len(y)):
      if len(np.intersect1d(y[i],y[j]))  == 0 and i != j:
          t = np.sum(py)-(np.sum(y[i])+np.sum(y[j]))
          lx.append(t)
          r.append(np.append(y[i],y[j]))
  for i in range(len(y)):
      lx.append(np.sum(py)-np.sum(y[i]))
      r.append((y[i])) 

  scoreArr = np.array(lx)
  minScore = np.min(scoreArr)
  minId = np.where(scoreArr==minScore)[0]  
  for v in minId:
    u.append(r[v])
  return u[0]

@njit()
def tim_diem_toi_uu_co_phom(pt,py,s):
  k = []
  for i in pt: 
    if check_ca(i,pt[pt!=i]) == True :
        k.append(i)
  k = np.array(k)
  l =[]
  du_0 = k[np.where(k%4 == 0)[0]]
  du_1 = k[np.where(k%4 == 1)[0]]
  du_2 = k[np.where(k%4 == 2)[0]]
  du_3 = k[np.where(k%4 == 3)[0]]
  if len(du_0) >= 3:
    l0 = []
    n = len(du_0)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if du_0[j] > du_0[j + 1]:
                du_0[j], du_0[j + 1] = du_0[j + 1], du_0[j]
                already_sorted = False
        if already_sorted:
            break
    for i in range(len(du_0)):

        if du_0[i] == du_0[i - 1] + 4:
            if du_0[i-1] not in l0:
              l0.append(du_0[i-1])
            if du_0[i] not in l0:
              l0.append(du_0[i])
    if len(l0)>2 :
      l0 = np.array(l0)
      l.append(l0)

  if len(du_1) >= 3:
    l1 = []
    n = len(du_1)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if du_1[j] > du_1[j + 1]:
                du_1[j], du_1[j + 1] = du_1[j + 1], du_1[j]
                already_sorted = False
        if already_sorted:
            break
    for i in range(len(du_1)):
        if du_1[i] == du_1[i - 1] + 4:
            if du_1[i-1] not in l1:
              l1.append(du_1[i-1])
            if du_1[i] not in l1:
              l1.append(du_1[i])
    if len(l1)>2 :
      l1 =  np.array(l1)
      l.append(l1)  

  if len(du_2) >= 3:
    l2 = []
    n = len(du_2)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if du_2[j] > du_2[j + 1]:
                du_2[j], du_2[j + 1] = du_2[j + 1], du_2[j]
                already_sorted = False
        if already_sorted:
            break
    for i in range(len(du_2)):
        if du_2[i] == du_2[i - 1] + 4:
            if du_2[i-1] not in l2:
              l2.append(du_2[i-1])
            if du_2[i] not in l2:
              l2.append(du_2[i])
    if len(l2)>2 :
      l2 =  np.array(l2)
      l.append(l2)

  if len(du_3) >= 3:
    l3 = []
    n = len(du_3)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if du_3[j] > du_3[j + 1]:
                du_3[j], du_3[j + 1] = du_3[j + 1], du_3[j]
                already_sorted = False
        if already_sorted:
            break
    for i in range(len(du_3)):
        if du_3[i] == du_3[i - 1] + 4:
            if du_3[i-1] not in l3:
              l3.append(du_3[i-1])
            if du_3[i] not in l3:
              l3.append(du_3[i])
    if len(l3)>2 :
      l3 = np.array(l3)
      l.append(l3)
  arr1 = k//4
  l1 = []
  for i in range(0,13):
    l1.append(np.count_nonzero(arr1 == i))
  for i in np.where(np.array(l1)>=3)[0]:
    l.append(k[np.where(arr1==i)])
  y = []
  for i in l:
    if i  is not None :
      if len(i)>=4 :
        for j in range(3,len(i)+1):
          for k in range(0,len(i)-j+1):
              y.append(i[k:k+j])
      else: 
        y.append(i)
  lx = []
  r = []
  u = []
  for i in range(len(y)):
    for j in range(len(y)):
      if len(np.intersect1d(y[i],y[j]))  == 0 and i != j:
          r.append(np.append(y[i],y[j]))
  for i in range(len(y)):
      r.append((y[i])) 

  b = []
  if len(s)==1  :
    for i in range(len(r)) :
      if len(np.intersect1d(s,r[i])) ==1 :
        b.append(r[i])
        lx.append(np.sum(py)-np.sum(r[i]))

  else :
    for i in range(len(r)) :
      if len(np.intersect1d(s[0],r[i]))==1:
        for j in range(len(r)):
          if j != i :
            if len(np.intersect1d(s[1],r[j]))==1:
              b.append(np.append(r[i],r[j]))
              lx.append(np.sum(py)-np.sum(r[i])-np.sum(r[j]))

  scoreArr = np.array(lx)
  minScore = np.min(scoreArr)
  minId = np.where(scoreArr==minScore)[0] 

  for i in minId:
    u.append(b[i]) 
  return u[0]

@njit()
def check_so_ca(a,arr):
    a1 = a%4
    arr1= arr[arr%4==a1]
    a2 = a//4
    arr3 = arr[arr//4==a2]
    l = 0 
    k = []
    if len(arr3)>=2:
        l += 1
        k.append(arr3)
    arr2 = arr1//4

    if a2+1 in arr2 and a2+2 in arr2:
        l += 1
        k.append(np.array([(a2+1)*4+a1,(a2+2)*4+a1]))

    elif a2-1 in arr2 and a2-2 in arr2:
        l += 1
        k.append(np.array([(a2-1)*4+a1,(a2-2)*4+a1]))
    elif a2-1 in arr2 and a2+1 in arr2 :
        l += 1
        k.append(np.array([(a2-1)*4+a1,(a2+1)*4+a1]))
    return l,k

@njit()
def getValidActions(p_state):
  vi_tri = np.where(p_state[416:420]==1)[0][0] 
  phase = p_state[420:423]
  validActions = np.full(54, 0,dtype = np.float64)
  temp = p_state[0:52]
  la_bai_truoc= p_state[52:104]
  t = np.where(temp==1)[0]
  if phase[0] == 1:
    validActions[1] = 1 #bốc bài 
    if len(np.where(la_bai_truoc ==1)[0]) != 0:# có lá bài của người đi trước 
        if check_ca(np.where(la_bai_truoc ==1)[0][0],t) == True :
          if len(np.where(p_state[104+52+52:104+52+52+52]==1)[0]) <1 : # có cạ trong bộ và có lá bài của người đi trước và chưa ăn phỏm nào 
            validActions[0] = 1 # Ăn bài 
          elif len(np.where(p_state[104+52+52:104+52+52+52]==1)[0]) == 1  : # có cạ trong bộ và có lá bài của người đi trước và đã ăn 1 phỏm 
            l1,r1 = check_so_ca(np.where(p_state[104+52+52:104+52+52+52]==1)[0][0],t)
            l2,r2 = check_so_ca(np.where(la_bai_truoc ==1)[0][0],t)
            if (l1 == l2) and l1 == 1:
              if (r1[0][0]== r2[0][0]) and (r1[0][1]== r2[0][1]) :
                 validActions[0] = 0
            # elif (l1 == l2) and l1 == 2:
            #   if (r1[0] == r2[0]).all() and (r1[1]==r2[1]).all():
            #      validActions[0] = 0
            # elif (l1 == l2) and l1 == 2:
            else:
              validActions[0] = 1 # Ăn bài 
          elif  len(np.where(p_state[104+52+52:104+52+52+52]==1)[0]) == 2  : # có cạ trong bộ và có lá bài của người đi trước và đã ăn 2 phỏm 
              l1,r1 = check_so_ca(np.where(p_state[104+52+52:104+52+52+52]==1)[0][0],t)
              l2,r2 = check_so_ca(np.where(p_state[104+52+52:104+52+52+52]==1)[0][1],t)
              l3,r3 = check_so_ca(np.where(la_bai_truoc ==1)[0][0],t)
              if l1 == 1 and l2 == 1 and l3 == 1 :
                if (r1[0][0] == r3[0][1]) or (r3[0][1]== r2[0][1]):
                  validActions[0] = 0
              # elif l1 == 2 and l2 ==1 and l3 == 1:
              #      validActions[0] = 0
              # elif l1 == 1 and l2 ==2 and l3 ==1 :
              #      validActions[0] = 0
              else :
                  validActions[0] = 1 # Ăn bài 
  elif phase[1] == 1:
    #check cạ 
    if len(np.where(p_state[104+52+52:104+52+52+52]==1)[0]) == 1 :
      validActions[t+2] = 1
      l,r = check_so_ca(np.where(p_state[104+52+52:104+52+52+52]==1)[0][0],t)

      if l == 1:
        r1 = r[0][0]
        r2 = r[0][1]
        # khoa cac la bai lai 
        validActions[t[np.where((t==r1))[0]]+2] = 0

        validActions[t[np.where((t==r2))[0]]+2] = 0
    elif len(np.where(p_state[104+52+52:104+52+52+52]==1)[0]) == 2 :
      l1,r1 = check_so_ca(np.where(p_state[104+52+52:104+52+52+52]==1)[0][0],t)
      l2,r2 = check_so_ca(np.where(p_state[104+52+52:104+52+52+52]==1)[0][1],t)
      if l1 == 1 and l2 ==1  :
        r11 = r1[0][0]
        r12 = r1[0][1]
        r21 = r2[0][0]
        r22 = r2[0][1]
         # khoa cac la bai t1,t2
        validActions[t[np.where((t!=r11) & (t!= r12) & (t!= r22) & (t!= r21))[0]]+2] = 1
      elif (l1 == 1 and l2 >2)  :
        # t[r# khoa cac la bai t1
        r11 = r1[0][0]
        r12 = r1[0][1]
        validActions[t[(t!=r11) & (t!= r12)]+2] = 1
      elif (l1> 2 and l2 == 1):
        # khoa cac la bai t2
        r11 = r2[0][0]
        r12 = r2[0][1]
        validActions[t[(t!=r11) & (t!= r12) ]+2] = 1

      elif (l1 == 1 and l2 == 2)  :
        # t[r# khoa cac la bai t1
        r11 = r1[0][0]
        r12 = r1[0][1]

        r21 = r2[0][0]
        r22 = r2[0][1]
        r23 = r2[1][0]
        r24 = r2[1][1]
        if (r21 == r11 and r12 == r22) :
            validActions[t[(t!=r11) & (t!= r12) & (t!= r23) & (t!= r24)]+2] = 1
        elif (r23 == r11 and r24 == r12):
            validActions[t[(t!=r11) & (t!= r12) & (t!= r21) & (t!= r22)]+2] = 1
        else :
            validActions[t[(t!=r11) & (t!= r12)]+2] = 1
      elif (l1 == 2 and l2 == 1):
        # khoa cac la bai t2
        r21 = r2[0][0]
        r22 = r2[0][1]

        r11 = r1[0][0]
        r12 = r1[0][1]
        r13 = r1[1][0]
        r14 = r1[1][1]
        if (r21 == r11 and r12 == r22) :
            validActions[t[(t!=r21) & (t!= r22) & (t!= r13) & (t!= r14)]+2] = 1
        elif (r13 == r21 and r14 == r22):
            validActions[t[(t!=r11) & (t!= r12) & (t!= r21) & (t!= r22)]+2] = 1
        else :
            validActions[t[(t!=r21) & (t!= r22)]+2] = 1  
      elif l1 == 2 and l2 ==2 :
        r11 = r1[0][0]
        r12 = r1[0][1]
        r13 = r1[1][0]
        r14 = r1[1][1]

        r21 = r2[0][0]
        r22 = r2[0][1]
        r23 = r2[1][0]
        r24 = r2[1][1]
        if (r21 == r11 and r12 == r22) and  (r23 == r13 and r14 == r24):
            validActions[t[(t!=r21) & (t!= r22) & (t!= r13) & (t!= r14)]+2] = 1
        else:
            validActions[t+2] = 1
    else :
        validActions[t+2] = 1
  return validActions
@njit()
def stepEnv(action,env):
  temp = env[0:52]
  phase = env[53] 
  turn = env[52] 
  pIdx = turn % 4
  if phase == 0 : 
    if action == 0: # Ăn bài 
       temp[env[54]] = pIdx + 9
       env[53] = 1

    if action == 1 : # không ăn bài 
       id = np.random.choice(np.where(temp==4)[0])
       temp[id] = pIdx
       env[53] = 1
  elif phase == 1 :
    if len(temp[temp == pIdx +5])+1 < 4: # đánh bài 
       temp[action-2] = pIdx+5
       env[54] = action-2
       env[55:55+52][np.where(temp ==pIdx)[0]]= pIdx   

    elif len(temp[temp == pIdx +5])+1 >= 4:# đánh bài 
       temp[action-2] = pIdx+5
       env[55:55+52][np.where(temp ==pIdx)[0]]=pIdx
       if len(temp[temp == pIdx +9]) == 0:
        temp[action-2] = pIdx+5
        env[55:55+52][np.where(temp ==pIdx)[0]]=pIdx
      
        if len(check_la_phom(np.where(temp ==pIdx)[0])) >= 3 :
            temp[action-2] = pIdx+5
            env[54] = action-2
            r = tim_diem_toi_uu(np.where(temp ==pIdx)[0],np.where(temp ==pIdx)[0])
            env[55+52:55+52+52][r]= pIdx
            env[55:55+52][r] = -1
            env[55:55+52][np.where(temp ==pIdx)[0]]=pIdx
       elif len(temp[temp == pIdx +9]) > 0:
      
        k = np.append(np.where(temp ==pIdx)[0],np.where(temp==pIdx +9)[0])
        r = tim_diem_toi_uu_co_phom(k,k,np.where(temp==pIdx +9)[0])
        env[55+52:55+52+52][r]= pIdx   
        env[55:55+52][r] = -1
            
       
       env[54] = action-2
    env[55:55+52][action-2] = -1
    env[53] = 0   
    env[52] += 1

       # hạ phỏm 

@njit() 
def initEnv():
    temp = np.arange(52) #số lá bài 
    np.random.shuffle(temp)
    env = np.full(159, 0)
    for i in range(5):
      if i != 4 :
        env[temp[9*i:9*(i+1)]]= i
      else: 
        env[temp[36:]]=i
    env[52] = 0 # Turn
    env[53] = 0 # Phase 
    #5,6,7,8 lá bài rác của từng người 
    #9,10,11,12 lá bài đã ăn  và các lá phỏm đã hạ 
    env[54] = -1 # lá thằng trc đánh 
    env[55:55+52] = -1 # các lá còn lại để hạ 
    env[55+52:55+52+52] = -1
    #0,1,2,3 các lá còn lại  của từng player 
    return env

@njit()
def getActionSize():
    return 54
@njit()
def getAgentSize():
    return 4

@njit()
def getStateSize():
    return 633



@njit()
def getAgentState(e_state):
    p_state = np.full(633,0,dtype = np.float64)
    temp = e_state[0:52]
    pIdx = e_state[52] % 4 
    # 0 -> 51: Index các lá bài. 1 Là trên tay,  0 là của người chơi khác hoặc chưa bốc, -1 là các lá đã đánh hoặc bị đã ăn
    p_state[0:52] = e_state[0:52]
    p_state[np.where(e_state[0:52] == pIdx)[0]] = 1
    p_state[np.where((e_state[0:52] != pIdx))[0]] = 0
    # 'la bai',np.where(p_state[0:52] == 1)[0])
    # lá bài thằng trước đánh cho mình 
    if e_state[54] > 0:
        p_state[52:104][e_state[54]] = 1 
    # bài rác của người tiếp theo 
    if pIdx!= 3 :
      p_state[104:104+52][(np.where(temp == pIdx+6)[0])] = 1
    else :
      p_state[104:104+52][(np.where(temp == 5)[0])]= 1  
    #  bài rác của mình và người khác 
    if pIdx!= 3 :
      p_state[104+52:104+52+52][np.where((temp>4) & (temp<= 8) & (temp != pIdx+6))[0]]= 1    
    else :
      p_state[104+52:104+52+52][np.where((temp>4) & (temp<= 8) & (temp != 5))[0]]= 1       
    # số phỏm của bản thân 
    p_state[104+52+52:104+52+52+52][np.where(temp == pIdx+9)[0]] = 1
    # số phỏm của 3 người khác 
    if pIdx == 0  :
      p_state[104+52+52+52:104+52+52+52+52][np.where(temp == 10)[0]] = 1
      p_state[104+52+52+52+52:104+52+52+52+52+52][np.where(temp == 11)[0]] = 1
      p_state[104+52+52+52+52+52:104+52+52+52+52+52+52][np.where(temp == 12)[0]] = 1
    elif pIdx == 3:
      p_state[104+52+52+52:104+52+52+52+52][np.where(temp == 9)[0]] = 1
      p_state[104+52+52+52+52:104+52+52+52+52+52][np.where(temp == 10 )[0]] = 1
      p_state[104+52+52+52+52+52:104+52+52+52+52+52+52][np.where(temp == 11)[0]] = 1
    elif pIdx == 1 :
      p_state[104+52+52+52:104+52+52+52+52][np.where(temp == 11)[0]] = 1
      p_state[104+52+52+52+52:104+52+52+52+52+52][np.where(temp == 12 )[0]] = 1
      p_state[104+52+52+52+52+52:104+52+52+52+52+52+52][np.where(temp == 9)[0]] = 1
    elif pIdx == 2 :
      p_state[104+52+52+52:104+52+52+52+52][np.where(temp == 12)[0]] = 1
      p_state[104+52+52+52+52:104+52+52+52+52+52][np.where(temp == 9 )[0]] = 1
      p_state[104+52+52+52+52+52:104+52+52+52+52+52+52][np.where(temp == 10)[0]] = 1
    # vị tri của bản thân 
    p_state[416:420][pIdx] = 1
    #Phase 
    p_state[420:423][e_state[53]] = 1
    # các lá bài của người chơi khác khi hạ phỏm 
    p_state[423:423+52][np.where(e_state[55:55+52]== pIdx)[0]] = 1
    if pIdx == 0  :
      p_state[423+52:423+52+52][np.where(e_state[55:55+52]== 1)[0]] = 1
      p_state[423+52+52:423+52+52+52][np.where(e_state[55:55+52]== 2)[0]] = 1
      p_state[423+52+52+52:423+52+52+52+52][np.where(e_state[55:55+52]== 3)[0]] = 1
    elif pIdx == 3:
      p_state[423+52:423+52+52][np.where(e_state[55:55+52]== 0)[0]] = 1
      p_state[423+52+52:423+52+52+52][np.where(e_state[55:55+52]== 1)[0]] = 1
      p_state[423+52+52+52:423+52+52+52+52][np.where(e_state[55:55+52]== 2)[0]] = 1
    elif pIdx == 1 :
      p_state[423+52:423+52+52][np.where(e_state[55:55+52]== 2)[0]] = 1
      p_state[423+52+52:423+52+52+52][np.where(e_state[55:55+52]== 3)[0]] = 1
      p_state[423+52+52+52:423+52+52+52+52][np.where(e_state[55:55+52]== 0)[0]] = 1
    elif pIdx == 2 :
      p_state[423+52:423+52+52][np.where(e_state[55:55+52]== 3)[0]] = 1
      p_state[423+52+52:423+52+52+52][np.where(e_state[55:55+52]== 0)[0]] = 1
      p_state[423+52+52+52:423+52+52+52+52][np.where(e_state[55:55+52]== 1)[0]] = 1
    m = checkEnded(e_state)
    # Đã kết thúc game chưa 
    if m == -1:
      p_state[631] = 1 
    else :
      p_state[631] = 0 
    # Check xem có thắng hay không
    if m == pIdx+1 :
      p_state[632] = 1
    else:
      p_state[632] = 0 
 
    return p_state

@njit()
def checkEnded(env):
    la_bai_da_hai = env[55:55+52]
    la_phom = env[0:52]     
    scoreArr = np.array([sum(np.where(la_bai_da_hai==0)[0]),sum(np.where(la_bai_da_hai==1)[0]),sum(np.where(la_bai_da_hai==2)[0]), sum(np.where(la_bai_da_hai==3)[0])])
    scorephom = np.array([len(np.where(la_phom==9)[0]), len(np.where(la_phom==10)[0]),len(np.where(la_phom==11)[0]), len(np.where(la_phom==12)[0])])
    if len(np.where(env[0:52]==5)[0])+len(np.where(env[0:52]==6)[0])+len(np.where(env[0:52]==7)[0])+len(np.where(env[0:52]==8)[0]) < 16 :
      if len(np.where(la_phom ==9)[0]) == 3 or len(np.where(la_phom ==10)[0]) == 3 or len(np.where(la_phom ==11)[0]) == 3 or len(np.where(la_phom ==12)[0]) == 3:
          maxScorePlayers = np.where(scorephom==3)[0]
          return maxScorePlayers[0]   
      else:
          return -1  
    elif len(np.where(env[0:52]==5)[0])+len(np.where(env[0:52]==6)[0])+len(np.where(env[0:52]==7)[0])+len(np.where(env[0:52]==8)[0]) == 16:
      if len(np.where(env[55+52:55+52+52]==0)[0]) == 0  :
        scoreArr[0]+= 999
      if len(np.where(env[55+52:55+52+52]==1)[0]) == 0  :
        scoreArr[1]+= 999
      if len(np.where(env[55+52:55+52+52]==2)[0]) == 0  :
        scoreArr[2]+= 999
      if len(np.where(env[55+52:55+52+52]==3)[0]) == 0  :
        scoreArr[3]+= 999      
      minScore = np.min(scoreArr)
      minScorePlayers = np.where(scoreArr==minScore)[0]
      if minScore > 999:
        return 0
      else:
        return np.min(minScorePlayers)
@njit()
def getReward(state):
    if state[631] == 1 :
        return -1
    else:
       if state[632] == 1:
          return 1
       else:
          return 0

      
from numba.typed import List

def one_game_normal(p0,  list_other, per_player, per1, per2, per3, p1, p2, p3):
    env= initEnv()
    if check_u_khan(np.where(env[0:52]==0)[0]) == True  or check_u_khan(np.where(env[0:52]==1)[0]) == True or check_u_khan(np.where(env[0:52]==2)[0]) == True or check_u_khan(np.where(env[0:52]==3)[0]) == True :
        env = initEnv()
    tempData = []
    for _ in range(4):
        dataOnePlayer = List()
        dataOnePlayer.append(np.array([[0.]]))
        tempData.append(dataOnePlayer)

    while True:
        pIdx = env[52] % 4

        if list_other[pIdx] == -1:
            action,  per_player = p0(getAgentState(env), per_player)
        elif list_other[pIdx] == 1:
            action,  per1 = p1(getAgentState(env),  per1)
        elif list_other[pIdx] == 2:
            action,  per2 = p2(getAgentState(env),  per2)
        elif list_other[pIdx] == 3:
            action,  per3 = p3(getAgentState(env),  per3)
        stepEnv(action, env)
        if checkEnded(env) != -1:
            break
    for pIdx in range(4):
        env[52] = pIdx
        if list_other[pIdx] == -1:
            action,  per_player = p0(getAgentState(env),  per_player)
        elif list_other[pIdx] == 1:
            action,  per1 = p1(getAgentState(env),  per1)
        elif list_other[pIdx] == 2:
            action,  per2 = p2(getAgentState(env),  per2)
        elif list_other[pIdx] == 3:
            action,  per3 = p3(getAgentState(env),  per3)
    winner = False
    if np.where(list_other == -1)[0] == (checkEnded(env) - 1): 
        winner = True
    else: 
        winner = False
    return winner, per_player

@njit()
def one_game_numba(p0,  list_other, per_player, per1, per2, per3, p1, p2, p3):
    env= initEnv()
    if check_u_khan(np.where(env[0:52]==0)[0]) == True  or check_u_khan(np.where(env[0:52]==1)[0]) == True or check_u_khan(np.where(env[0:52]==2)[0]) == True or check_u_khan(np.where(env[0:52]==3)[0]) == True :
        env = initEnv()
    tempData = []
    for _ in range(4):
        dataOnePlayer = List()
        dataOnePlayer.append(np.array([[0.]]))
        tempData.append(dataOnePlayer)

    while True:
        pIdx = env[52] % 4

        if list_other[pIdx] == -1:
            action,  per_player = p0(getAgentState(env), per_player)
            validActions = getValidActions(getAgentState(env))
            if validActions[action] != 1:
              raise Exception('Action không hợp lệ.')
        elif list_other[pIdx] == 1:
            action,  per1 = p1(getAgentState(env),  per1)
        elif list_other[pIdx] == 2:
            action,  per2 = p2(getAgentState(env),  per2)
        elif list_other[pIdx] == 3:
            action,  per3 = p3(getAgentState(env),  per3)
        stepEnv(action, env)
        if checkEnded(env) != -1:
            break
    for pIdx in range(4):
        env[52] = pIdx
        if list_other[pIdx] == -1:
            action,  per_player = p0(getAgentState(env),  per_player)
        elif list_other[pIdx] == 1:
            action,  per1 = p1(getAgentState(env),  per1)
        elif list_other[pIdx] == 2:
            action,  per2 = p2(getAgentState(env),  per2)
        elif list_other[pIdx] == 3:
            action,  per3 = p3(getAgentState(env),  per3)
        else:
          raise Exception('Sai list_other.')
    winner = False
    if np.where(list_other == -1)[0] == (checkEnded(env) - 1): 
        winner = True
    else: 
        winner = False
    return winner, per_player
@njit()
def random_Env(p_state, per):
    arr_action = getValidActions(p_state)
    arr_action = np.where(arr_action == 1)[0]
    act_idx = np.random.randint(0, len(arr_action))
    return arr_action[act_idx], per

def n_games_normal(p0, num_game, per_player, list_other, per1, per2, per3, p1, p2,p3):
    win = 0
    for _n in range(num_game):
        np.random.shuffle(list_other)
        winner,per_player = one_game_normal(p0, list_other, per_player, per1,per2, per3, p1, p2, p3)
        win += winner
    return win, per_player

@njit()
def n_games_numba(p0, num_game, per_player, list_other, per1, per2, per3, p1, p2,p3):
    win = 0
    for _n in range(num_game):
        np.random.shuffle(list_other)
        winner,per_player = one_game_numba(p0, list_other, per_player, per1,per2, per3, p1, p2, p3)
        win += winner
    return win, per_player

import importlib.util, json, sys
try:
    from setup import SHORT_PATH
except:
    pass
def load_module_player(player, game_name = None):
    if game_name == None:
        spec = importlib.util.spec_from_file_location('Agent_player', f"{SHORT_PATH}Agent/{player}/Agent_player.py")
    else:
        spec = importlib.util.spec_from_file_location('Agent_player', f"{SHORT_PATH}Agent/ifelse/{game_name}/{player}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@njit()
def check_run_under_njit(agent, perData):
    return True
@njit()
def bot_lv0(state, perData):
    validActions = getValidActions(state)
    arr_action = np.where(validActions==1)[0]
    idx = np.random.randint(0, arr_action.shape[0])
    return arr_action[idx], perData

def numba_main_2(p0, num_game, per_player, level, *args):
    num_bot = getAgentSize() - 1
    list_other = np.array([-1] + [i+1 for i in range(num_bot)])
    try: check_njit = check_run_under_njit(p0, per_player)
    except: check_njit = False

    if "_level_" not in globals():
        global _level_
        _level_ = level
        init = True
    else:
        if _level_ != level:
            _level_ = level
            init = True
        else:
            init = False

    if init:
        global _list_per_level_
        global _list_bot_level_
        _list_per_level_ = []
        _list_bot_level_ = []

        if _level_ == 0:
            _list_per_level_ = [np.array([[0.]], dtype=np.float64) for _ in range(num_bot)]
            _list_bot_level_ = [bot_lv0 for _ in range(num_bot)]
        else:
            env_name = sys.argv[1]
            if len(args) > 0:
                dict_level = json.load(open(f'{SHORT_PATH}Log/check_system_about_level.json'))
            else:
                dict_level = json.load(open(f'{SHORT_PATH}Log/level_game.json'))

            if str(_level_) not in dict_level[env_name]:
                raise Exception('Hiện tại không có level này')

            lst_agent_level = dict_level[env_name][str(level)][2]

            for i in range(num_bot):
                if level == -1:
                    module_agent = load_module_player(lst_agent_level[i], game_name = env_name)
                    _list_per_level_.append(module_agent.DataAgent())
                else:
                    data_agent_level = np.load(f'{SHORT_PATH}Agent/{lst_agent_level[i]}/Data/{env_name}_{level}/Train.npy',allow_pickle=True)
                    module_agent = load_module_player(lst_agent_level[i])
                    _list_per_level_.append(module_agent.convert_to_test(data_agent_level))
                _list_bot_level_.append(module_agent.Test)

    if check_njit:
        return n_games_numba(p0, num_game, per_player, list_other,
                                _list_per_level_[0], _list_per_level_[1], _list_per_level_[2],
                                _list_bot_level_[0], _list_bot_level_[1], _list_bot_level_[2])
    else:
        return n_games_normal(p0, num_game, per_player, list_other,
                                _list_per_level_[0], _list_per_level_[1], _list_per_level_[2],
                                _list_bot_level_[0], _list_bot_level_[1], _list_bot_level_[2])
    