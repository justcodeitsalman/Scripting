import os 


#base path 
base_path='/extkciarch01/shared/inzone'

#calculate comp base  path
comp_base= {
    base_:'/extkciarch01/',
    base_:'/extkciarch01/',
    base_:'/extkciarch01/',
    base_:'/extkciarch01/',
    base_:'/extkciarch01/'
    base_:'/extkciarch01/',
    base_:'/extkciarch01/'
           
           }
          
rotaion=2

#path to check file for last 2 day's
for base,value in comp_base.items():
    if os.path.exists(value):
            for root_folder, folders, files in os.walk(value):
                while rotaion<=2
                     print(root_folder)
                    for folder in folders:
                        #value_path = os.path.join(root_folder, folder)
                        #file_path=os.path.join(value_path,files)
                        print(folder)
                rotaion=rotaion-1


