window.addEventListener("scroll", function() {
  var navbar1 = document.getElementById("navbar1");
  var navbar2 = document.getElementById("navbar2");
  if (window.pageYOffset > 0) {
    navbar1.classList.add("navbar-hidden");
    navbar2.classList.add("navbar-scrolled");
  } else {
    navbar1.classList.remove("navbar-hidden");
    navbar2.classList.remove("navbar-scrolled");
  }
});


function showList() {
  if (document.getElementById('buttonlist_id').innerHTML == '<i class="fa-solid fa-x"></i>'){
    document.getElementById('allinone').style.display = 'none'
    document.getElementById('allinone_2').style.display = 'none'
    document.getElementById('buttonlist_id').innerHTML = '<i class="fa-sharp fa-solid fa-bars"></i>'
    document.getElementById('restofall').classList.remove('d-none')
  }else{
    document.getElementById('buttonlist_id').innerHTML = '<i class="fa-solid fa-x"></i>'
    document.getElementById('allinone').style.display = 'flex'
    document.getElementById('allinone_2').style.display = 'flex'
    document.getElementById('restofall').classList.add('d-none')
  }
}


const nameInput = document.querySelector('.card_order input[name="caro"] + .fs_inner .two_input .uni_input:first-child input');
const surnameInput = document.querySelector('.card_order input[name="caro"] + .fs_inner .two_input .uni_input:last-child input');
const nameSpan = document.querySelector('.card_order input[name="caro"] + .fs_inner .two_input .uni_input:first-child span');
const surnameSpan = document.querySelector('.card_order input[name="caro"] + .fs_inner .two_input .uni_input:last-child span');

nameInput.addEventListener('keyup', function() {
  updateSpanStyle(this.value, nameSpan);
});

surnameInput.addEventListener('keyup', function() {
  updateSpanStyle(this.value, surnameSpan);
});

function updateSpanStyle(value, span) {
  if (value !== '') {
    span.style.transform = 'translateY(-1.5rem) scale(0.8)';
  } else {
    span.style.transform = 'none';
  }
}


function handleInputChange(selectElement, labelId) {
  var label = selectElement.parentElement.querySelector('#' + labelId);
  if (selectElement.value !== '') {
      label.classList.add('move-up');
  } else {
      label.classList.remove('move-up');
  }
}

window.addEventListener('scroll', function() {
  var button = document.getElementById('internetBankButton');
  if (window.scrollY > 0) {
    button.innerHTML = ''; 
  } else {
    button.innerHTML = '<b><i class="fa-sharp fa-solid fa-arrow-right-from-bracket"></i></b>'; 
  }
});