//РЕДАКТИРОВАНИЕ ПРОФИЛ
const profileEditButton = document.getElementById('profile-edit');
const profileCardsBlock = document.getElementById('profileCards');
const profileEditBlock = document.getElementById('profileEdit');

profileEditButton.addEventListener('click', function() {
    
    profileCardsBlock.style.transition = "opacity 0.5s";
    profileCardsBlock.style.opacity = 0;

   
    profileEditBlock.style.transition = "opacity 0.5s";
    profileEditBlock.style.opacity = 1;
    profileEditBlock.style.display = "block";
});
