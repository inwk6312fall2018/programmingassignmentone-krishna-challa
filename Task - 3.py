
filein=open('running-config.cfg')
global=[]
management=[]
for line in filein:                     
  line=line.strip()
  line=line.split()
  if(line[0]=='access-list' and line[1]=='global_access'):
    global.append(line)          
  if(line[0]=='access-list' and line[1]=='fw management_access_in'):
    management.append(line)
print(global)
print(management)
