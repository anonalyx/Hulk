fitbase() {
    cd "../src/app/fitbase_data"
    python3 test_Hulk.py -v
}

test_tables() {
    cd "../src/app/models"
    python3 test_makeTables.py -v
}

current_dir=$(pwd)

fitbase
cd "$current_dir"

test_tables
cd "$current_dir"