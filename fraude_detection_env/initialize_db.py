from database import engine
import models

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)
print("Database initialized!")
