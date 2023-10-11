from turtle import *
import math
import matplotlib.pyplot as plt

def place_points_around_center(num_vertices, radius):
    """
    Place points evenly around the center of the screen.
    
    Args:
        num_vertices (int): Number of vertices (points) to be placed.
        radius (float): Distance from the center to the points.
    
    Returns:
        list of tuples: List of (x, y) coordinates of the placed points.
    """
    if num_vertices <= 2:
        raise ValueError("Number of vertices should be greater than 2")
    
    # Calculate the angle between each vertex
    angle_increment = 2 * math.pi / num_vertices

    # Initialize the list to store the coordinates of the points
    points = []

    for i in range(num_vertices):
        # Calculate the angle for this vertex
        angle = i * angle_increment

        # Calculate the (x, y) coordinates using polar to Cartesian conversion
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        # Add the coordinates to the list
        points.append((x, y))

    return points



def place_vertices(num):
    # center point where vertices will be drawn around
    setheading(90)
    center = (0,0)
    # angle for each separate vertice
    angle_btw = 360 / num
    for i in range(0,num):
        penup()
        forward(100)
        pendown()
        dot(10)
        penup()
        goto(0,0)
        right(angle_btw)





def main():
    # Set the number of vertices and radius
    num_vertices = 47
    radius = 50

    # Calculate the points
    points = place_points_around_center(num_vertices, radius)

    # Extract x and y coordinates from the list of points
    x_coordinates, y_coordinates = zip(*points)

    # Create a scatter plot
    plt.scatter(x_coordinates, y_coordinates, color='blue', s=50)

    # Set axis limits and labels
    plt.xlim(-radius -10, radius + 10)
    plt.ylim(-radius - 10, radius + 10)
    plt.xlabel('X')
    plt.ylabel('Y')

    # Display the plot
    plt.title('Points Around Center')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()