# Alx_DjangoLearnLab

# Authentication Features
- Register a new account (/register)
- Login (/login)
- Logout (/logout)
- Manage profile (/profile)

## How to Test
1. Register at /register
2. Login at /login
3. Update email in /profile
4. Logout at /logout

### Blog Post Features
- View all posts at /posts/
- View details at /posts/<id>/
- Create posts at /posts/new/ (requires login)
- Edit your own posts at /posts/<id>/edit/
- Delete your own posts at /posts/<id>/delete/

Permissions:
- Anyone can view posts.
- Only logged-in users can create posts.
- Only the author can edit or delete their own posts.
