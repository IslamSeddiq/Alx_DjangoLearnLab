# Permissions & Groups Setup

## Custom Permissions (on Book model)
- can_view → View book list
- can_create → Create a new book
- can_edit → Edit an existing book
- can_delete → Delete a book

## Groups
- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins → can_view, can_create, can_edit, can_delete

## Usage
- Permissions are enforced in views with `@permission_required`.
- Users inherit permissions from their assigned group.
- Test by creating users and adding them to groups via the admin site.
