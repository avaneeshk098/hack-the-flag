[...document.getElementsByClassName('table-row')].forEach(element => {
    element.addEventListener('click', e => {
        e.preventDefault();
        window.location = `/${element.dataset.link}`;
    })
})