Permissions and Groups
-----------------------
- Groups: Admins, Editors, Viewers
- Custom Permissions on Book model:
    - can_view: Allows viewing book entries
    - can_create: Allows creating book entries
    - can_edit: Allows editing book entries
    - can_delete: Allows deleting book entries

Views are protected using @permission_required with appropriate checks.
