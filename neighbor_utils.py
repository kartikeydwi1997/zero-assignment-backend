import pandas as pd


def get_pop(zip_val):
    df = pd.read_csv("data/population_data.csv")

    if zip_val not in df['zipcode'].tolist():
        return -1
    
    pop = df[df['zipcode'] == zip_val]['population'].tolist()[0]
    
    if pop == 0:
        return -1
    
    return pop

def get_neighbors(start_zip):
    count_back_front = 0
    padding = 1
    vals = []
    while True:
        pop = get_pop(start_zip+padding)
        if pop != -1:
            count_back_front += 1
            vals.append([start_zip+padding, pop])
        
        pop = get_pop(start_zip-padding)
        if pop != -1:
            count_back_front += 1
            vals.append([start_zip-padding, pop])
            
        if count_back_front >= 5:
            break
            
        padding += 1

    return vals