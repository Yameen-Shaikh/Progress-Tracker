#TODO: Add this in notes Don't add any comma's here as it will be considered as a trailing comma which becomes tuple

# Select Queries
ALL_LEARNING_ENTRIES = "SELECT * FROM learning_entries;"
LEARNING_ENTRY = "SELECT * FROM learning_entries WHERE id = %s;"
ALL_SUBJECTS = "SELECT * FROM subjects;"
SUBJECT = "SELECT * FROM subjects WHERE id = %s;"


# Insert Queries
INSERT_LEARNING_ENTRY = "INSERT INTO learning_entries (date, learning) VALUES (%s, %s);"
INSERT_SUBJECT = "INSERT INTO subjects (name, optional, description) VALUES (%s, %s, %s)"


# Update Queries
UPDATE_LEARNING_ENTRY = "UPDATE learning_entries SET date = %s, learning = %s WHERE id = %s;"
UPDATE_SUBJECT = "UPDATE subjects SET name = %s, optional = %s, description = %s WHERE id = %s;"


# Delete Query
ALL_DELETE_LEARNING_ENTRIES = "DELETE FROM learning_entries;"
ALL_DELETE_SUBJECTS = "DELETE FROM subjects;"
DELETE_LEARNING_ENTRY = "DELETE FROM learning_entries WHERE id = %s;"
DELETE_SUBJECT = "DELETE FROM subjects WHERE id = %s;"