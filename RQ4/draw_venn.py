
import matplotlib.pyplot as plt
import venn
import pandas as pd



def get_set(method_name):
    # 读取 Excel 文件中的特定工作表
    file_path = "baselines.xlsx"  
    sheet_name = "FL"         
    column_name =method_name       

    column_names = ['RewardRepair', 'DEAR', 'Tare', 'TBar', 'GT-Repair']
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    df = df.dropna(subset=[column_name])
    column_data = df[column_name]  

    index = column_names.index(column_name)

    column_data = df.iloc[:,index]    
    data_list = column_data.tolist()
    
    return data_list


if __name__ == '__main__':
    baseline = ['RewardRepair', 'DEAR', 'Tare', 'TBar', 'GT-Repair']
    sets = []
    for method in baseline:
        fixed_list = get_set(method)
        sets.append(set(fixed_list))
        print(f"{method}: {fixed_list}")

    labels = venn.get_labels(sets,)
    fig, ax = venn.venn5(labels, names=baseline)
    fig.savefig('venn5.png', bbox_inches='tight')
    plt.close()
