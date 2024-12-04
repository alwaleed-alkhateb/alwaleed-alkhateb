#add mation 
#mark task as compliate 
#show mission
#quit project

message="""
1-add mission
2-mark as compliate
3-show mission
4-quit """  
print(message)
tasks=[]
def add_mission():
    task=input('enter the tasks: ')

    task_info={"task":task,"compliate":False}    
    tasks.append(task_info)
    print(tasks)
    
    
def mark_compliate():
    incompliate=[]
    for task in tasks:
        if task["compliate"]==False:
            incompliate.append(task)
            
        
        for i , taks in enumerate(incompliate):
            print(f'{i+1} - {task["task"]}')
    task_num=int(input('enter the task num: '))
    incompliate[task_num-1]["compliate"]=True

def show_mission():
    if not tasks:
        print('no tasks to view')

        return
    else:
        print(tasks) 

def quit_project():
    print('Quit project is done')
    
while True:
    user_choies=int(input('enter your choies'))
    
    if user_choies==1:
        add_mission()
    
    elif user_choies==2:
        mark_compliate()
        print(tasks)
    
    elif user_choies==3:
        show_mission()
    
    elif user_choies==4:
        quit_project()

        break