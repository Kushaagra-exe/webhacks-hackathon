let formData = {};

document.addEventListener("DOMContentLoaded", function () {
  const submitBtn = document.getElementById("submitBtn");

  submitBtn.addEventListener("click", async function () {
    
    await updateForm();
    sendData(formData);
  });
});


const sendData = async (formData) =>{
    try {
        const response = await fetch('/suggestor', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(formData)
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        // Handle success response
        console.log('Data sent successfully!');
      } catch (error) {
        // Handle error
        console.error('There was a problem sending the data:', error);
      }
}


async function updateForm() {
    const duration = document.getElementById('duration').value;
    const budget = document.getElementById('budget').value;
    const startingLocation = document.getElementById('curr_location').value;

    const interestsArray = [];
    document.querySelectorAll('#dropdownContent4 input[type=checkbox]:checked').forEach(function(checkbox) {
        interestsArray.push(checkbox.value);
    });
    const interests = interestsArray.join(', ');

    const styleArray = [];
    document.querySelectorAll('#dropdownContent5 input[type=checkbox]:checked').forEach(function(checkbox) {
        styleArray.push(checkbox.value);
    });
    const style = styleArray.join(', ');

    const destinationTypeArray = [];
    document.querySelectorAll('#dropdownContent2 input[type=checkbox]:checked').forEach(function(checkbox) {
        destinationTypeArray.push(checkbox.value);
    });
    const destinationType = destinationTypeArray.join(', ');

    formData = {
        duration: duration,
        budget: budget,
        startingLocation: startingLocation,
        interests: interests,
        style: style,
        destinationType: destinationType
    };

    console.log(formData);

}

