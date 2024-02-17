class ContactsLocalError(Exception):
    """Base class for ContactsLocal exceptions."""

    def __init__(self, message="ContactsLocal error occurred."):
        self.message = message
        super().__init__(self.message)


class ContactInsertionError(ContactsLocalError):
    """Exception raised for errors related to inserting contacts."""

    def __init__(self, message="Error occurred while inserting contact."):
        super().__init__(message)


class ContactUpdateError(ContactsLocalError):
    """Exception raised for errors related to updating contacts."""

    def __init__(self, message="Error occurred while updating contact."):
        super().__init__(message)


class ContactDeletionError(ContactsLocalError):
    """Exception raised for errors related to deleting contacts."""

    def __init__(self, message="Error occurred while deleting contact."):
        super().__init__(message)


class ContactBatchInsertionError(ContactsLocalError):
    """Exception raised for errors related to batch insertion of contacts."""

    def __init__(self, message="Error occurred while batch inserting contacts."):
        super().__init__(message)


class ContactRetrievalError(ContactsLocalError):
    """Exception raised for errors related to retrieving contacts."""

    def __init__(self, message="Error occurred while retrieving contact."):
        super().__init__(message)


class ContactObjectInsertionError(ContactsLocalError):
    """Exception raised for errors related to inserting contact objects."""

    def __init__(self, message="Error occurred while inserting contact object."):
        super().__init__(message)
