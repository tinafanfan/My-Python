def plot_two_lines(x1, y1, x2, y2, lagend1, legend2):

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(20, 4))

    # Plot the line
    ax.plot(x1, y1, color = '#1f77b4') # blue
    ax.plot(x2, y2, color = '#ff7f0e') # orange

    # Set labels and title
    plt.title('NYISO forecast')
    ax.legend([lagend1, legend2])
    ax.set(xlabel=None, ylabel='value', title=str(''))

    # Rotate x-axis tick labels for better visibility
    plt.xticks(rotation=45)
    # Display the plot   

    # fig.savefig('.png'.format(x))
    fig.show()
