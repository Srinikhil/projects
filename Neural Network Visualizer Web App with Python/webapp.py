import requests
import os
import matplotlib.pyplot as plt
import streamlit as st
import json
import numpy as np

URL = 'http://127.0.0.1:5000/server'

st.title('Neural Network Visualizer')
st.sidebar.markdown('# Input Image')

if st.button('Get random prediction'):
    response = requests.post(URL, data={})
    response = json.loads(response.text)
    preds = response.get('prediction')
    image = response.get('image')
    image = np.reshape(image, (28, 28))
    
    st.sidebar.image(image, width=150)
    
    for layer, p in enumerate(preds):
        print('p.shape:', np.array(p).shape)
        numbers = np.squeeze(np.array(p))
        print('numbers.shape:', numbers.shape)
        print('layer:', layer)
        plt.figure(figsize=(32, 4))
        
        if layer == 2:
            row = 1
            col = 10
        else:
            row = 2
            col = 16
            
        for i, number in enumerate(numbers):
            plt.subplot(row, col, i+1)
            plt.imshow((number * np.ones((8, 8, 3))).astype('float32'), cmap='binary')
            plt.xticks([])
            plt.yticks([])
            if layer == 2:
                plt.xlabel(str(i), fontsize=40)
        plt.subplots_adjust(wspace=0.05, hspace=0.05)
        plt.tight_layout()
        
        st.text('Layer {}'.format(layer+1), )
        st.pyplot()