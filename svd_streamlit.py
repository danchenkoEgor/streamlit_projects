import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import streamlit as st 

uploaded_image = st.file_uploader("Choose a file")

image_choose = plt.imread(uploaded_image)

if len(image_choose.shape) == 3:
    st.header("Choose channel you want to work with:")
    red = st.checkbox('Red')
    green = st.checkbox('Green')
    blue = st.checkbox('Blue')
    if red:
        image = image_choose[:, :, 0]
    if green:
        image = image_choose[:, :, 1]
    if blue:
        image = image_choose[:, :, 2]

if len(image_choose.shape) == 2:
    image = plt.imread(uploaded_image)



u, sing_values, v = np.linalg.svd(image)
sigma = np.zeros((image.shape[0], image.shape[1]))
np.fill_diagonal(sigma, sing_values)

k = st.slider(f'Select the number of features you want to leave (of {len(sing_values)} total)', min_value = 10, 
               max_value = int(len(sing_values) / 4), value = int(len(sing_values) / 8), step = 10)

sigma_cut = sigma[:k, :k]
u_cut = u[:, :k]
v_cut = v[:k, :]

corrupted_image = u_cut@sigma_cut@v_cut

fig, ax = plt.subplots(1, 2, figsize=(130, 80))
ax[0].imshow(corrupted_image)
ax[1].imshow(image)

st.pyplot(fig)


#st.write(f'Number of bytes saved: {(u_cut.nbytes + sigma_cut.nbytes + v_cut.nbytes)} of total {image.nbytes}')