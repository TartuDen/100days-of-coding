
import math
# list_of_books=[{"Jane Austen":["Pride and Prejudice","Sense and Sensibility","Emma"]},
#                {"Ernest Hemingway":["The Old Man and the Sea","A Farewell to Arms","For Whom the Bell Tolls"]},
#                {"Toni Morrison":["Song of Solomon","The Bluest Eye","Gabriel García Márquez"]}]

list_of_books=[{"author":"Jane Austen","books":["Pride and Prejudice","Sense and Sensibility","Emma"]},
               {"author":"Ernest Hemingway","books":["The Old Man and the Sea","A Farewell to Arms","For Whom the Bell Tolls"]},
               {"author":"Toni Morrison","books":["Song of Solomon","The Bluest Eye","Gabriel García Márquez"]}]


def processer(arg):
    temp=[]
    for i in arg:
        if len(i):
            temp.append(i)
        elif len(i)==0:
            temp.append(None)
    return(temp)

def searcher(*arg):
    list_search=[]
    list_result=[]

    search_name=''
    search_books=''
    if arg:
        
        list_search=processer(arg)
        number_of_runs=math.factorial(len(list_search))-1
        def run_down():
            
            number_of_runs-=1

        print(list_search)
    else:
        return(list_of_books)
      
        

        


print(searcher("aa"))

