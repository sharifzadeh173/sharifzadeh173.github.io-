#MacroF1Score
#you are provided with the ground truth target values y_true and estimated target values y_pred.
#Return the macro F1 score of the given y_pred and y_true.

from sklearn.metrics import f1_score
def macrof1score(y_true,y_pred):
    #your code here
    macro_f1=f1_score(y_true,y_pred,average='macro')
    return macro_f1

#exampl1
y_true=[2,1,2,1,2,1,1,1,2,1,3,1,0,1,3,1,3,2]
y_pred=[0,0,1,1,2,1,2,1,2,1,1,1,1,2,2,2,2,3]
#output:.230392156

print(macrof1score(y_true,y_pred))

#example2
y_true=[1,1,2,1,3,1,0,1,3,1,3,2]
y_pred=[0,0,1,1,1,2,2,2,2,3,3,3] 
print(macrof1score(y_true,y_pred))

#output0.1388888888888888
       