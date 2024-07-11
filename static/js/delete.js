const modal = document.querySelectorAll('#modal');
const openModalBtn = document.querySelectorAll('#openModalBtn');
const closeBtn = document.querySelectorAll('.close-btn');
const cancleBtn = document.querySelectorAll('#cancle');
const modalForm = document.querySelectorAll('#modalForm');


openModalBtn.forEach((btn) => {
    btn.addEventListener('click', openModal.bind(this, btn.dataset.modalid));
});
closeBtn.forEach((btn) => {
    btn.addEventListener('click', closeModal.bind(this, btn.dataset.modalid));
})
cancleBtn.forEach((btn) => {
    btn.addEventListener('click', closeModal.bind(this, btn.dataset.modalid));
})


// Function to open modal
function openModal(id) {
    let pk = id;
    let wanted_modal;
    modal.forEach((item) => {
        if (item.dataset.modalid == pk) {
            wanted_modal = item;
            console.log('pooof')
        }
    })
    wanted_modal.style.display = 'block';
}

// Function to close modal
function closeModal(id) {
    let pk = id;
    let wanted_modal;
    modal.forEach((item) => {
        if (item.dataset.modalid == pk) {
            wanted_modal = item;
            console.log('pooof')
        }
    })
    wanted_modal.style.display = 'none';
}

// Function to close modal if outside click

// Function to handle form submission
function submitForm(e) {
    closeModal();
}
