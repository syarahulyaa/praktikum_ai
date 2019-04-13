# In[18]:load the pre-trained model and predict the math symbol for an arbitrary image;
# the code below could be placed in a separate file

import keras.models
model2 = keras.models.load_model("mathsymbols.model")
print(model2.summary())
