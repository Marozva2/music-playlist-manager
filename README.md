# Music Playlist Manager

## Description

The Music Playlist Manager is a Python application designed to help users manage their music playlists efficiently. It allows users to create, update, add songs to playlists, and view the details of songs and playlists. This application is built using Python, Click, alembic, and SQLAlchemy.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use the Music Playlist Manager, follow these installation steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/music-playlist-manager.git
    ```

2. Navigate to the project directory:

    ```bash
    cd music-playlist-manager
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```bash
    python3 `cli.py`
    ```

## Usage

To run the Music Playlist Manager, execute the following command:

```bash
python3 cli.py
```
# Features
- User Management:
    - Create a new user with a first name, last name, email, and contact information.
    - View the list of all users.
- Song Management:
    - Add a new song with details such as name, category, sub-category, price, and date created.
    - View the list of all songs.
- Playlist Management:
    - Create a new playlist for a specific customer, including the order date and total amount.
    - View the list of all playlists.
- Playlist Songs:
    - Add songs to a playlist by specifying the order ID, product ID, and quantity.
    - View the list of all order items.