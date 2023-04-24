document.addEventListener("DOMContentLoaded", () => {
    const bodyTable = document.getElementById("body-table-rows");
    const equipmentTable = document.getElementById("equipment-table-rows");
    const searchButton =  document.getElementById("search-button");

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
        bodySelection = bodyTable.querySelector("tr.selected").dataset.selection;
        equipmentSelection = equipmentTable.querySelector("tr.selected").dataset.selection;

        window.location.href = "/search_results/" + bodySelection + "/" + equipmentSelection;
    });
    
});


function tableSelection(table, row) {
    // You can only select one row at a time

    if (!row) return;

    // If any row is already selected, unselect it
    const selectedRows = table.querySelectorAll("tr.selected");
    selectedRows.forEach((row) => {
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
