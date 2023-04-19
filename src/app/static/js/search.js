



document.addEventListener("DOMContentLoaded", () => {
    const bodyTable = document.getElementById("body-table-rows");
    const equipmentTable = document.getElementById("equipment-table-rows");
    const searchButton =  document.getElementById("search-button");
    
    //Actual API calls when database is set up
    //bodyData = getData("/api/bodies");
    //equipmentData = getData("/api/equipment");
    bodyData = [{"BodyPart": "Biceps"}, 
                {"BodyPart": "Abdominals"}, 
                {"BodyPart": "Shoulders"}, 
                {"BodyPart": "Back"}, 
                {"BodyPart": "Quads"}];

    equipmentData = [{"Equipment": "None"},
                     {"Equipment": "Dumbbells"},
                     {"Equipment": "Kettle bell"},
                     {"Equipment": "Barbell"},
                     {"Equipment": "Excercise ball"}];

    
    fillTable(bodyTable, "BodyPart", bodyData);
    fillTable(equipmentTable, "Equipment", equipmentData);

    //Event listener for Body Part Table
    bodyTable.addEventListener("click", (event) => {
        const row = event.target.closest("tr");
        tableSelection(bodyTable, row);
        buttonActivation(bodyTable, equipmentTable);
    });

    //Event listener for Equipment Table
    equipmentTable.addEventListener("click", (event) => {
        const row = event.target.closest("tr");
        tableSelection(equipmentTable, row);
        buttonActivation(bodyTable, equipmentTable);
      }); 
    
    //Event listener for Search Button
    searchButton.addEventListener("click", (event) => {
        bodySelection = bodyTable.querySelector("tr.selected").id;
        equipmentSelection = equipmentTable.querySelector("tr.selected").id;

        window.location.href = "/search_results/" + bodySelection + "/" + equipmentSelection;
    });
    
});


function fillTable(table, attribute, data) {
    // data is a JSON
    data.forEach((rowData) => {
        const row = document.createElement("tr");
        row.dataset.selected = false;
        row.id = rowData[attribute];
        Object.values(rowData).forEach((cellData) => {
            const cell = document.createElement("td");
            cell.textContent = cellData;
            row.appendChild(cell);
        });
        table.appendChild(row);
    })
}

async function getData(url) {
    try {
        const response = await fetch(url);
        const rows = await response.json();
        return rows;
    }

    catch (error) {
        console.log('Error fetching data with: ' + url, error);
    }
}


function tableSelection(table, row) {
    // You can only select one row at a time

    if (!row) return;

    // If any row is already selected, unselect it
    const selectedRows = table.querySelectorAll("tr.selected");
    selectedRows.forEach((row) => {
        row.dataset.selected = false;
        row.classList.toggle("selected");
    });
    
    // Select the row
    row.classList.toggle("selected");
}

function buttonActivation(bodyTable, equipmentTable) {
    // If both a body part and equipment are selected, enable the search button

    bodyIsSelected = bodyTable.querySelector("tr.selected");
    equipmentIsSelected = equipmentTable.querySelector("tr.selected");
    if (bodyIsSelected && equipmentIsSelected) {
        document.getElementById("search-button").disabled = false;
    }
}
