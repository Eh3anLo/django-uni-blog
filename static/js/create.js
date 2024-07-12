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
        if (tagsInput.value.includes('Tag')) {
            while ((match = regex.exec(tagsInput.value)) !== null) {
                local_tag.push(match[1]);
            }
        } else {
            local_tag = tagsInput.value.split(',')
        }
        // Iterate through all matches
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
    if (tags.length == 1) {
        tagsInput.value += ",";
    }
    if (tags.length > 5) {
        e.preventDefault();
        console.log('hello')
        message('تعداد برچسب های نمیتواند بیشتر از ۵ تا باشد.', 'error');
        return;
    }
    tagsInput.value = tags.join(',');
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

function message(text, state) {
    const msg = $('#successMsg').clone(true);
    $($($(msg).children()).children()[1]).text(text);
    $('#message').append($(msg));
    $(msg).toggleClass(`${state} animate__animated animate__fadeInRight`);
    setTimeout(function () {
        $(msg).toggleClass(`${state} animate__animated animate__fadeInRight`);
        $(msg).toggleClass(`${state} animate__animated animate__fadeOutRight`);
        setTimeout(function () {
            $(msg).toggleClass(`${state} animate__animated animate__fadeOutRight`);
            $(msg).remove();
        }, 1000);
    }, 2100);
}