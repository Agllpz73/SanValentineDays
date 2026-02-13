const messages = [
    "Segura?",
    "Segurisimaaaaa??",
    "Estas completamente segura??",
    "Por favorcitoooo mi amorcitooooo...",
    "Piensalooooo, te conviene!",
    "Si dices que no, me voy a sentir muy triste...",
    "Estare muy tristeeee....",
    "Me voy a sentir muy mal si dices que nooooo...",
    "Ok, esta es la ultima oportunidad para decir que no...",
    "Puedes decir que no, pero recuerda que te amo mucho y quiero pasar el resto de mi vida contigo... ❤️"
];

let messageIndex = 0;

function handleNoClick() {
    const noButton = document.querySelector('.no-button');
    const yesButton = document.querySelector('.yes-button');
    noButton.textContent = messages[messageIndex];
    messageIndex = (messageIndex + 1) % messages.length;
    const currentSize = parseFloat(window.getComputedStyle(yesButton).fontSize);
    yesButton.style.fontSize = `${currentSize * 1.5}px`;
}

function handleYesClick() {
    window.location.href = "yes_page.html";
}