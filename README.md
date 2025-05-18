

# activate the environment
source /Users/hussamelmaghraby/Data/Projects/SELF/store_hub_project/.venv/bin/activate

# migrate the database
python manage.py makemigrations storehub
python3 manage.py migrate