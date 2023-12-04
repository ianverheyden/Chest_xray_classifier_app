document.addEventListener('DOMContentLoaded', function() {
    // Add click event listeners to images for prediction
    var xrayImages = document.querySelectorAll('.xray-image');
    xrayImages.forEach(function(img) {
        img.addEventListener('click', function() {
            predict(this.src);
        });
    });
});

function predict(imageSrc) {
    // Extract the image filename from the imageSrc
    let filename = imageSrc.split('/').pop();
    
    // Make a POST request to the server for prediction
    fetch('/predict', {
        method: 'POST',
        body: JSON.stringify({ image_name: filename }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Handle the prediction result
        // You may want to display the result to the user
        console.log('Prediction result:', data);
    })
    .catch(error => {
        console.error('Error making prediction:', error);
    });
}

function refreshImages() {
    // Make a GET request to the server to get new image URLs
    fetch('/refresh-images')
    .then(response => response.json())
    .then(data => {
        var xrayImages = document.querySelectorAll('.xray-image');
        xrayImages.forEach(function(img, index) {
            // Update the src of each image with the new image URLs provided by the server
            if (data[index]) { // Check if the image URL exists
                img.src = data[index];
            }
        });
    })
    .catch(error => {
        console.error('Error refreshing images:', error);
    });
}

