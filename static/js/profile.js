const imagePreview = document.getElementById('imagePreview');
const imageInput = document.getElementById('id_img');
imageInput.addEventListener('change', updateImagePreview);

function updateImagePreview() {
    const file = imageInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            imagePreview.src = e.target.result;
        }
        reader.readAsDataURL(file);
    } else {
        imagePreview.src = '';
    }
}