import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import io


from matplotlib.patches import Rectangle

def table_results(df):
    # Assuming df has columns: 'Adjacency_Matrix', 'Graph_Image_1', 'Graph_Image_2'
    
    # Plotting the images along with the adjacency matrix values
    fig, axs = plt.subplots(len(df), 3, figsize=(15, len(df) * 5))  # 3 columns: adjacency matrix, first image, second image
    axs = axs.ravel()  # Flatten the 2D array of axes to iterate over it

    for i in range(len(df)):
        # Display adjacency matrix as an array
        adjacency_matrix = np.array(df['Adjacency_Matrix'][i])  # Convert to NumPy array
        axs[3*i].axis('off')  # Hide axes for cleaner display
        axs[3*i].text(0.5, 0.5, str(adjacency_matrix), fontsize=12, ha='center', va='center')  # Center text in the subplot
        
        # Set title based on the index
        if i == 0:
            axs[3*i].set_title("Graph Adjacency Matrix")
        else:
            axs[3*i].set_title("Complement Graph Adjacency Matrix")


        # Display first graph image
        axs[3*i+1].imshow(df['Graph_Image_1'][i])  # Image of the first graph
        if i == 0:
            axs[3*i+1].set_title("Graph visualization")
        else:
            axs[3*i+1].set_title("Complement graph Visualisation")

        axs[3*i+1].axis('off')  # Hide axes for cleaner display

        # Display second graph image
        axs[3*i+2].imshow(df['Graph_Image_2'][i])  # Image of the second graph
        if i == 0:
            axs[3*i+2].set_title("Clique identified")
        else :
            axs[3*i+2].set_title("Independent set identified")

        axs[3*i+2].axis('off')  # Hide axes for cleaner display

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()








def table_results_GENERAL(df, matrix_col, image_cols, titles=None, hide_axes=True, figsize=(15, 5)):
    """
    General function to visualize matrices and corresponding images from a DataFrame.

    Parameters:
    - df: pandas DataFrame containing the data to plot
    - matrix_col: column name of the matrix data
    - image_cols: list of column names of image data
    - titles: list of titles for each column, defaults to None
    - hide_axes: whether to hide axes in the plot, defaults to True
    - figsize: size of the figure, defaults to (15, 5)
    """

    n_cols = len(image_cols) + 1  # Number of columns: 1 for matrix + number of image columns
    fig, axs = plt.subplots(len(df), n_cols, figsize=(figsize[0], len(df) * figsize[1]))  # Dynamic subplots
    axs = axs.ravel()  # Flatten the 2D array of axes to iterate over it
    
    # Loop over the rows of the DataFrame
    for i in range(len(df)):
        # Display matrix as text
        matrix = np.array(df[matrix_col][i])  # Convert to NumPy array
        axs[n_cols * i].axis('off') if hide_axes else axs[n_cols * i].axis('on')
        axs[n_cols * i].text(0.5, 0.5, str(matrix), fontsize=12, ha='center', va='center')
        
        # Set title for the matrix column
        if titles and len(titles) > 0:
            axs[n_cols * i].set_title(titles[0])
        
        # Display the image columns
        for j, col in enumerate(image_cols):
            axs[n_cols * i + j + 1].imshow(df[col][i])  # Show image from DataFrame
            axs[n_cols * i + j + 1].axis('off') if hide_axes else axs[n_cols * i + j + 1].axis('on')
            
            # Set title for the image columns
            if titles and len(titles) > j + 1:
                axs[n_cols * i + j + 1].set_title(titles[j + 1])

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()


def tuple_to_image(data_tuple):
    # Create a blank white image
    img = Image.new('RGB', (200, 50), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    # Convert the tuple to a string
    tuple_str = str(data_tuple)

    # Define font size and type (use default font if no specific font available)
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()

    # Add the tuple text onto the image
    d.text((10, 10), tuple_str, fill=(0, 0, 0), font=font)

    # Convert the image to a format that imshow() can use (a numpy array)
    return np.array(img)








