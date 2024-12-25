#TODO: Don't add any comma's here as it will be considered as a trailing comma which becomes tuple

# Select Queries
ALL_LEARNING_ENTRIES = "SELECT * FROM learning_entries;"
LEARNING_ENTRY = "SELECT * FROM learning_entries WHERE id = %s;"
ALL_SUBJECTS = "SELECT * FROM subjects;"
 

# Insert Queries
ADD_LEARNING_ENTRIES = "INSERT INTO learning_entries (date, learning) VALUES (%s, %s);"


# Update Queries
UPDATE_LEARNING_ENTRIES = "UPDATE learning_entries SET learning = %s,date = %s WHERE id = %s;"