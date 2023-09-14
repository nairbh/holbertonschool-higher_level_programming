document.getElementById('toggle_header').onclick = () => {
    let header= document.querySelector('header');
    header.classList.toggle('red');
    header.classList.toggle('green');

};