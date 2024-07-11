const modal = document.getElementById('modal');
const openModalBtn = document.getElementById('openModalBtn');
const closeBtn = document.querySelector('.close-btn');
const modalForm = document.getElementById('modalForm');
const imagePreview = document.getElementById('imagePreview');
const imageInput = document.getElementById('id_img');
const selectElement = document.getElementById('id_status');
const tagsInput = document.getElementById('id_tags');
const tagsContainer = document.getElementById('tagsContainer');
const regex = /<Tag:\s([^>]+)>/g;

let tags = [];

document.addEventListener('DOMContentLoaded', domOnLoad)
imageInput.addEventListener('change', updateImagePreview);
openModalBtn.addEventListener('click', openModal);
closeBtn.addEventListener('click', closeModal);
window.addEventListener('click', outsideClick);
modalForm.addEventListener('submit', submitForm);

selectElement.addEventListener('change', changeStatus);
tagsInput.addEventListener('keypress', handleTagsInput);

function domOnLoad() {
    if (tagsInput.value) {
        let match;
        let local_tag = [];
        // Iterate through all matches
        while ((match = regex.exec(tagsInput.value)) !== null) {
            local_tag.push(match[1]);
        }
        local_tag.forEach((tagText) => {
            addTag(tagText);
            tagsInput.value = '';

        })
    }
}
// Function to open modal
function openModal() {
    modal.style.display = 'block';
}

// Function to close modal
function closeModal() {
    modal.style.display = 'none';
}

// Function to close modal if outside click
function outsideClick(e) {
    if (e.target == modal) {
        closeModal();
    }
}

// Function to handle form submission
function submitForm(e) {
    tagsInput.value = tags.join(',');
    if (tags.length == 1){
        tagsInput.value += ",";
    }
    closeModal();
}

function updateImagePreview() {
    const file = imageInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block';
        }
        reader.readAsDataURL(file);
    } else {
        imagePreview.src = '';
        imagePreview.style.display = 'none';
    }
}


function changeStatus() {
    if (this.value === 'منتشر شده') {
        this.classList.add('publish');
        this.classList.remove('draft');
    } else {
        this.classList.add('draft');
        this.classList.remove('publish');
    }
};
// Function to handle tags input
function handleTagsInput(e) {
    if (e.key === ',' || e.key === 'Enter') {
        e.preventDefault();
        const tagText = tagsInput.value.trim().replace(/,$/, '');
        if (tagText) {
            addTag(tagText);
            tagsInput.value = '';
        }
    }
}

// Function to add a tag
function addTag(tagText) {
    if (!tags.includes(tagText)) {
        tags.push(tagText);
        const tagElement = document.createElement('div');
        tagElement.className = 'tag';
        tagElement.innerHTML = `${tagText} <span class="close-tag">&times;</span>`;
        tagsContainer.appendChild(tagElement);

        // Add event listener to the close button
        tagElement.querySelector('.close-tag').addEventListener('click', () => {
            removeTag(tagText);
        });
    }
}

// Function to remove a tag
function removeTag(tagText) {
    tags = tags.filter(tag => tag !== tagText);
    const tagElements = tagsContainer.querySelectorAll('.tag');
    tagElements.forEach(tagElement => {
        if (tagElement.textContent.trim() === tagText + ' ×') {
            tagElement.remove();
        }
    });
}