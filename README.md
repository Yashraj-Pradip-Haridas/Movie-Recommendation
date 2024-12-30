
# Movie Recommendation System

This project is a Movie Recommendation System that suggests movies to users based on their preferences.

## Features

- **Movie Dataset**: Contains a collection of movies with relevant metadata.
- **Similarity Calculation**: Computes similarity between movies to provide recommendations.
- **Web Application**: A user-friendly interface built with Flask for users to interact with the recommendation system.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Yashraj-Pradip-Haridas/Movie-Recommendation.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Movie-Recommendation
   ```

3. **Create a Virtual Environment**:
   ```bash
   python -m venv myenv
   ```

4. **Activate the Virtual Environment**:
   - **Windows**:
     ```bash
     myenv\Scripts\activate
     ```
   - **macOS and Linux**:
     ```bash
     source myenv/bin/activate
     ```

5. **Install the Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Ensure the Virtual Environment is Activated**.

2. **Run the Application**:
   ```bash
   python app.py
   ```

3. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:5000/`.

4. **Get Movie Recommendations**:
   - Enter the name of a movie you like.
   - The system will display a list of similar movies you might enjoy.

## File Structure

- **`app.py`**: Main application file that runs the Flask web server.
- **`movies.pkl`**: Serialized file containing the movie dataset.
- **`movies_dict.pkl`**: Serialized file containing a dictionary of movie titles and their indices.
- **`similarity.pkl`**: Serialized file containing the precomputed similarity matrix between movies.
- **`requirements.txt`**: List of Python packages required to run the application.

## Dependencies

Ensure that the following Python packages are installed:

- Streamlit
- pandas
- scikit-learn
- numpy
- pickle

These can be installed using the `requirements.txt` file as shown in the installation steps.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The movie dataset used in this project.
- The developers of the libraries and frameworks utilized.

---

For more information, visit the [GitHub repository](https://github.com/Yashraj-Pradip-Haridas/Movie-Recommendation).
Link for the website [Link](https://yashraj-pradip-haridas-movie-recommendation-app-npe28m.streamlit.app/)
