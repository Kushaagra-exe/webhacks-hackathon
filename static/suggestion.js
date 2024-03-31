function updateSelection(dropdownButtonId) {
    var dropdownButton = document.getElementById(dropdownButtonId);
    var checkboxes = document.querySelectorAll(
      "#" + dropdownButtonId + ' + .dropdown-content input[type="checkbox"]'
    );
    var selectedItems = [];
  
    checkboxes.forEach(function (checkbox) {
      if (checkbox.checked) {
        selectedItems.push(checkbox.value);
      }
    });
  
    if (selectedItems.length > 0) {
      dropdownButton.textContent = selectedItems.join(", ");
    } else {
      dropdownButton.textContent = "Select";
    }
  }
  