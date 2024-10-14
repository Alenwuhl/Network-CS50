# CS50W Network Project

## Description

This project was created as part of the CS50W course and is intended for educational purposes only. It is not designed for real users or a live production environment. The application mimics the core functionalities of a social media platform like Twitter, allowing users to create posts, follow other users, like posts, and edit their own posts.

## Features

### 1. **User Registration and Login**
   - Users can register for a new account via the registration form.
   - Once registered, users can log in using their credentials.
   - Logged-in users will be able to access all the features of the platform.

### 2. **Create a New Post**
   - After logging in, users can create new text-based posts.
   - Posts will appear on the "All Posts" page and be visible to other users.

### 3. **View All Posts**
   - The "All Posts" page displays a feed of posts from all users.
   - Posts are shown in reverse chronological order (newest first).
   - Pagination is used to display a maximum of 10 posts per page.

### 4. **Profile Pages**
   - Each user has a profile page that displays all their posts.
   - Profile pages show the number of followers and the number of users the profile owner is following.
   - Users can follow and unfollow other users from their profile pages.

### 5. **Following**
   - Logged-in users can follow or unfollow other users.
   - The "Following" page displays a feed of posts from users that the logged-in user is following.
   - Pagination is available on the "Following" page, showing 10 posts per page.

### 6. **Like/Unlike Posts**
   - Users can like or unlike posts by clicking the heart icon next to the post.
   - The like count for each post is updated asynchronously without needing to reload the page.

### 7. **Edit Own Posts**
   - Users can edit their own posts by clicking the floating "Edit" button that appears on posts they have authored.
   - Upon clicking the "Edit" button, the content of the post is replaced with a text area to allow editing.
   - After editing, users can click "Save" to update their post, and the updated content is saved without reloading the page.

### 8. **Pagination**
   - Pagination is implemented on the "All Posts" and "Following" pages.
   - Users can navigate between pages of posts using the "Next" and "Previous" buttons.

## Technologies Used

- **Django**: Python-based web framework used for backend functionality.
- **JavaScript (ES6)**: Used for asynchronous updates (AJAX) and dynamic page behavior.
- **HTML5 & CSS3**: Markup and styling for the frontend.
- **Bootstrap**: Frontend framework used for responsive design and layout.
- **SQLite**: Database used to store user information, posts, likes, and follow relationships.
- **FontAwesome**: For the icons (e.g., heart, pencil) used in the interface.

## Installation and Setup

To set up this project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/network.git
   cd network
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Apply migrations:
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
6. Run the development server:
   ```bash
   python3 manage.py runserver

## Demo

If you don't want to download and run the project, you can watch a demo video that shows how the website works: [YouTube Demo](https://www.youtube.com/watch?v=eUaTYWhH4wo)

