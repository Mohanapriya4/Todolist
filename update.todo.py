import PySimpleGUI as sg
layout=[
 [sg.Text("Enter the task",font=("Arial",16)),sg.InputText("",font=("Arial",16),size=(50,1),key="task"),sg.Button("Add",font=("Arial",16),key='add_save')],
 [sg.Listbox([],font=("Arial",16),size=(50,10),key = "tasklist"),sg.Button("Edit"),sg.Button("Delete")]
 ]
window=sg.Window("First App",layout)

def add_tasks(values):
    new_task=values['task']
    todolist.append(new_task)
    window.FindElement( 'tasklist').Update(values=todolist)
    window.FindElement( 'task').Update(value=' ')
    window.FindElement('add_save').Update('Add')
    
def delete_tasks(values):
    print(values)
    delete_task= values['tasklist'][0]
    todolist.remove(delete_task)
    window.FindElement( 'tasklist').Update(values=todolist)
    
def edit_tasks(values):
    edit_val=values['tasklist'][0]
    window.FindElement( 'task').Update(value= edit_val)
    window.FindElement('add_save').Update('save')
    todolist.remove(edit_val)
    
todolist=[]
while True:
    event,values=window.read()
    if event == 'add_save':
        add_tasks(values)
    elif event == 'Delete':
        delete_tasks(values)
    elif event == 'Edit':
        edit_tasks(values)
    else:
        break
    
window.close()
