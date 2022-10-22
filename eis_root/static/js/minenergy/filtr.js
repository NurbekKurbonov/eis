

const Dmanzil = document.getElementById('Dmanzil');
const manzil = document.getElementById('manzil');
const selectmanzil = document.getElementById('selectmanzil');

const DTHST = document.getElementById('DTHST');
const DDBIBT = document.getElementById('DDBIBT');
const Diftum = document.getElementById('Diftum');
    
const THST = document.getElementById('THST');
const DBIBT = document.getElementById('DBIBT');

manzil.addEventListener('click', function handleClick() {
    if (manzil.checked) {
      selectmanzil.style.display = 'block';
      DTHST.style.display = 'none';
      DDBIBT.style.display = 'none';
      Diftum.style.display = 'none';
      guruhiy.disabled=true;
      davomi.style.display='block';

    } else {
      selectmanzil.style.display = 'none';
      DTHST.style.display = 'block';
      DDBIBT.style.display = 'block';
      Diftum.style.display = 'block';
      guruhiy.disabled=false;
      davomi.style.display='none'; 
    }
  });

DBIBT.addEventListener('click', function handleClick() {
    if (DBIBT.checked) {
      Dmanzil.style.display = 'none';
      guruhiy.disabled=true;
      davomi.style.display='block';

      
    } else {
      Dmanzil.style.display = 'block';
      guruhiy.disabled=false;
      davomi.style.display='none'; 
    }
  });

THST.addEventListener('click', function handleClick() {
    if (THST.checked) {
      davomi.style.display='block';
      Dmanzil.style.display = 'none';
      guruhiy.disabled=true;
    } else {
      davomi.style.display='none'; 
      Dmanzil.style.display = 'block';
      guruhiy.disabled=false;
    }
  });


 