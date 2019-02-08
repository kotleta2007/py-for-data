# NEED TO TEST DIFFERENT LOSS FUNCTIONS

# Importing dependencies
import numpy as np
import scipy as sp
from lightfm import LightFM

# Constructing a record array from CSV file
r = np.genfromtxt("jester-data-1.csv", delimiter=',', encoding='utf-8')

# Printing array and its dimensions (rows->users, columns->jokes)
#print(r)
#print(r.shape[0], r.shape[1])

# Converting array to sparse matrix
data = sp.sparse.coo_matrix(r)

# Training the model
model = LightFM(loss='warp')
model.fit(data, epochs=10, num_threads=2)

def sample_recommendation(model, data, user_ids):
    n_users, n_items = data.shape
    
    for user_id in user_ids:
        known_positives = data.tocsr()[user_id].indices
        scores = model.predict(user_id, np.arange(n_items))
        top_items = np.argsort(-scores)
        
        print("User %s" % user_id)
        print("     Known positives:")
        
        for x in known_positives[:3]:
            print("     %s" % x)
            
        print("")
        print("     Recommended:")
        
        for x in top_items[:3]:
            print("     %s" % x)
            
        print("")
        
sample_recommendation(model, data, [3, 25, 450])
