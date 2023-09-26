# Project Summary

## Project Name: TRAVEL TOGHETER!

### Vehicle and Person Distribution

### Overview

The Vehicle and Person Distribution project is a Python-based program designed to efficiently distribute people into vehicles based on various criteria such as vehicle capacity, geographic location, and ownership. The project aims to optimize the allocation of individuals to vehicles to minimize the number of vehicles used while ensuring that each person's needs are met.

### Features

1. **Method 1 - Capacity Optimization:** This method groups people without vehicles with people who have vehicles, utilizing the least number of vehicles possible. If there is remaining space in vehicles and there are still people with vehicles, additional individuals with vehicles will be assigned to vehicles until capacity is reached.

2. **Method 2 - Geographic Proximity:** Method 2 groups people by geographic location and assigns them to vehicles based on proximity. Each vehicle includes its owner and other individuals who are geographically close to the owner.

3. **Visualization on OpenStreetMap:** The program includes a feature to display the distribution of people on OpenStreetMap with person icons, facilitating visualization of the allocation.

4. **Random Generation of People:** The program generates a random set of people located in Mendoza, Argentina, within a circular area with a 10km radius. Each person is assigned a random name, location (latitude and longitude), and a vehicle with specified capacity and bicycle capacity (50% probability of having a vehicle).

5. **Data Export and Import:** The program allows data to be saved to a Python file and imported for future use.

6. **Initial State Display:** The program displays the initial state, showing which person has which vehicle.

7. **Equitable Distribution:** Ensures equitable distribution of people across vehicles by optimizing the use of vehicle capacity.

8. **Customizable Color Coding:** Supports customizable color coding for individuals in the OpenStreetMap visualization, distinguishing vehicle owners from passengers.

### Usage

To use the program, follow these steps:

1. Run the program to generate random people in Mendoza, Argentina, with vehicles and locations.
2. Choose between Method 1 or Method 2 for optimizing person-vehicle distribution.
3. Visualize the distribution on OpenStreetMap.
4. Export data for future use if needed.

### Dependencies

The project depends on the following libraries:

- Python
- Folium (for OpenStreetMap visualization)

### Contribution

Contributions to the project are welcome! Feel free to fork the repository, make changes, and submit pull requests.

### License

This project is open-source and available under the MIT License.

For more details and usage instructions, please refer to the project's documentation.

