# Soccer Manager

Soccer Manager is a web application for managing players, equipment, and staff of a soccer team. The project is developed using Python, Flask, and MongoDB.

## Features

- Register, edit, list, and remove players
- Register, edit, list, and remove equipment
- Register, edit, list, and remove staff members
- Associate equipment with players

## Technologies Used

- Python 3
- Flask
- MongoDB

## Installation and Setup

To run the application locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/soccer_manager.git
   cd soccer_manager
   ```
2. **Docker run:**
    ```bash
    docker-compose up --build
    ```

## Project Structure
```bash
    soccer_manager/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── models.py
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── index.html
    │   │   ├── add_player.html
    │   │   ├── edit_player.html
    │   │   ├── players.html
    │   │   ├── add_equipment.html
    │   │   ├── edit_equipment.html
    │   │   ├── equipment.html
    │   │   ├── add_staff.html
    │   │   ├── edit_staff.html
    │   │   └── staff.html
    │   └── routes.py
    │   └── config.py
    │
    ├── run.py
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    └── README.md
```

## Class Diagram
- [Miro Class Diagram](https://miro.com/welcomeonboard/VHpPN1hZYjVZWE90eDlpVUREQ0pIdXpWOHQ2TEJsanlLd2F0enJNWjQzQjhnbDh1bDJUNHlJUHFmV3ByUzNMbnwzNDU4NzY0NTQwMTQ1MDUxNzU0fDI=?share_link_id=135897382331)