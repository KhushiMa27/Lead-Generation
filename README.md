
# Lead Generation System

A comprehensive web application designed to manage and streamline lead generation processes. Developed using **Django** and **Python** with **REST APIs**, this system allows businesses to efficiently capture, organize, and manage leads, boosting productivity and enhancing team collaboration.

## Features

- **Lead Capture and Management**: Effortlessly capture and organize leads with an intuitive user interface.
- **RESTful API Integration**: Provides secure and structured endpoints for data handling and interoperability with other applications.
- **User Authentication**: Supports secure login and user management to protect sensitive lead information.
- **Data Visualization**: Display insights from lead data to improve sales strategies.
- **Responsive Design**: Optimized for use across desktop and mobile devices.

## Technologies Used

- **Backend**: Django, Python, REST APIs
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (can be swapped with other RDBMS)
- **APIs**: Django REST framework for secure and scalable API services

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/KhushiMa27/Lead-Generation.git
   cd Lead-Generation
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

   Access the app at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints

- **/api/leads** - List all leads and create new ones
- **/api/leads/{id}** - Retrieve, update, or delete a specific lead
- **/api/users** - Manage user registration and authentication

## Usage

1. Open the app in your browser.
2. Register or log in to access lead management features.
3. Add new leads, edit existing ones, and track lead status.
4. Use the REST API to integrate with other platforms.

## Contributing

Feel free to submit issues or pull requests to improve this project. Follow these steps for contributions:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions, please reach out to [Khushi Makhija](https://github.com/KhushiMa27).

---



