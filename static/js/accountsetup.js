// Trigger file input for profile picture
function uploadProfilePicture() {
    document.getElementById('profile-upload').click();
}

// Trigger file input for cover photo
function uploadCoverPhoto() {
    document.getElementById('cover-upload').click();
}

// Handle profile picture file selection and upload
document.getElementById('profile-upload').addEventListener('change', function() {
    var file = this.files[0];
    if (file) {
        uploadImage(file, '/upload/profile-picture');  // Call backend API for profile picture
    }
});

// Handle cover photo file selection and upload
document.getElementById('cover-upload').addEventListener('change', function() {
    var file = this.files[0];
    if (file) {
        uploadImage(file, '/upload/cover-photo');  // Call backend API for cover photo
    }
});

// Function to send image to server using fetch
function uploadImage(file, url) {
    var formData = new FormData();
    formData.append('image', file);

    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Update the image on the page after successful upload
            if (url.includes('profile-picture')) {
                document.getElementById('profile-pic').src = data.newImageUrl;
            } else {
                document.getElementById('cover-pic').src = data.newImageUrl;
            }
        }
    })
    .catch(error => console.error('Error uploading image:', error));
}
