# MałoSAFECycling
## Making cycling safer

MałoSAFECycling is a cutting-edge application designed to make cycling safer by leveraging the power of AI and real-time road safety data. Whether you're commuting or exploring new routes, our app provides cyclists with up-to-date information on road conditions and potential risks. With MałoSAFECycling, you can enjoy your ride with greater peace of mind, knowing you're equipped with intelligent insights to keep you safe on the road.



### Local Installation Guide

Follow the steps below to set up and run the MałoSAFECycling application on your local machine.



### 1. Clone the Repository:
```bash
  git clone https://github.com/Rusiek/HackYeah2024.git
  cd HackYeah2024
```

## Backend Setup

### 2. Set Up a Python Virtual Environment
Move to the backend directory and set up a Python virtual environment. Then, activate the environment:


```bash
  cd backend
  python3 -m venv venv
  python3 -m venv/Scripts/activate
```

### 3. Create a .env File for the Backend
Inside the backend directory, create a .env file with the following content, replacing <HERE_API_KEY> with your own HERE API key:

```batch
  HERE_API_KEY=<your-api-key>
```

### 4. Install Backend Dependencies
Install the required Python packages:
```batch
  pip install -r backend/requirements.txt
```

### 5. Start the Main Application Server
Open a new terminal, navigate to the backend folder, and run the main application server:
```batch
  py ./server/run.py
```

### 6. Open new terminal and start the routing micro-services server
In a new terminal, start the routing microservice server to handle pathfinding:
```batch
  py ./route_risk/find_path.py
```

## Frontend Setup

### 7. Move to the `frontend` directory and install required packages
Navigate to the frontend directory and install the necessary packages using npm:
```batch
  cd frontend
  npm install
```

### 8. Create .env file for frontend with `<VITE_MAP_KEY>` ApiKey for mapbox API:
Inside the frontend directory, create a .env file with your Mapbox API key. Replace <VITE_MAP_KEY> with your own key:
```batch
  VITE_MAP_KEY=<your-api-key>
```

### 9. Run the application in new terminal
In a new terminal, start the frontend application:
```batch
  npm run dev
```

## Access the Web Application
### 10. Access the webapp in the browser using the link provided in the terminal
Once the frontend server starts, a URL will be provided in the terminal output. Open this URL in your web browser to access the MałoSAFECycling application.

>Note: Make sure all the servers are running in separate terminals for the backend and frontend to function correctly.


