function toggleNavDropDown() {
    const target = this.event.target;
    if (target.classList.contains('navbar-link')) {
        if (target.classList.contains('is-active')) {
            target.classList.remove('is-active');
            target.removeAttribute('tabindex');
            target.addEventListener('blur', deactivateNavDropDown);
        }
        else {
            target.classList.add('is-active');
            target.setAttribute('tabindex', '0');
        }
    }
    else {
        target.querySelectorAll('.navbar-link').forEach(el => {
            el.classList.remove('is-active');
            el.removeAttribute('tabindex');
        })
    }
}


function deactivateNavDropDown() {
    this.classList.remove('is-active');
    this.removeAttribute('tabindex');
}