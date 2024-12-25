#Note: Don't add any comma's here as it will be considered as a trailing comma which becomes tuple

# Select Queries
ALL_LEARNING_ENTRIES = "SELECT * FROM learning_entries;"
ALL_SUBJECTS = "SELECT * FROM subjects;"
 

# Insert Queries

ADD_LEARNING_ENTRIES = "INSERT INTO learning_entries (date, learning) VALUES (%s, %s);"
