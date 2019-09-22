import pandas as pd
# pandas gồm 2 cấu trúc dữ liệu series và data frame
# khởi tạo 1 series pd.series(data,index)
fruits=pd.Series([30,6,'yes','no'],['mango','apple','pineaple','orange'])
#print(fruits)
#data ở cot 2 chỉ số index ở cột 1
#data frame là mảng 2 chiều gồm nhiều series

#tao dictionary
item={'Bob':pd.Series(data = [245, 25, 55],
                           index = ['bike', 'pants', 'watch']),
      'Alice':pd.Series(data = [40, 110, 500, 45],
                             index = ['book', 'glasses', 'bike', 'pants'])}
datafrm=pd.DataFrame(item)
print(datafrm['Bob'])

