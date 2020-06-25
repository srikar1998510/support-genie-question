class Agent:
    def __init__(self,ia,av,ro):
        self.ia=ia
        self.av=av
        self.ro=ro

class Issue():
    def agent_issue(self,l,m):
        n_l=[]
        if(m=='all available'):
            for i in l:
                if(i.ia==True):
                    n_l.append(i)
        
        elif(m=='least busy'):
            return [min(l,key=lambda x:x.av[:2])]
        elif(m=='random'):
            issue=input('What type of issues here?').lower().split()
            for i in l:
                for j in i.ro:
                    if j in issue:
                        n_l.append(i)
        return n_l
                
            
        
n=int(input('Enter the no of agents'))
l=[]
for _ in range(n):
    is_available=input(f'will agent{_+1} be available')
    if(is_available=='Yes'.lower()):
        is_available=True
    elif(is_available=='No'.lower()):
        is_available=False
    if(is_available==True):
        available_since=input('enter the time since agent is available(24 hrs format)')
    else:
        available_since=0
    roles=list(map(lambda j:j.lower(),input('enter the roles').split()))
    a=Agent(is_available,available_since,roles)
    l.append(a)
mode=input('Enter the agent selection mode')
p=Issue()
op=[]
for i in p.agent_issue(l,mode):
    op.append({f'Agent {l.index(i)+1}':['Yes' if i.ia else 'No',i.av,i.ro]})
print(op)
    
