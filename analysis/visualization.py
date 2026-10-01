import matplotlib.pyplot as plt 
def visualization(x_value, y_value, x_name, y_name, title, folder): 

    plt.bar( x_value, y_value )
    plt.xlabel(x_name)
    plt.ylabel(y_name)

    plt.title(title)
    title = title.lower().replace(' ', "_")

    plt.savefig(f"./images/{folder}/{title}.png", dpi=300, bbox_inches="tight")
    plt.close()