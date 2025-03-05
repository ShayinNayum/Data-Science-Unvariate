class Univariate():

    def quanQual(dataset):

        qual=[]
        quan=[]
        for columnName in dataset.columns:
            print (columnName)
            if (dataset[columnName].dtype=='O'):
                #print("qual")
                qual.append(columnName)
            else:
               # print("quan")
                quan.append(columnName)
        return quan,qual