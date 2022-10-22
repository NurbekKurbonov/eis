const guruh = document.querySelector("#guruh");

guruhiy.addEventListener('click', function handleClick(){
    
      fetch("/addguruh", {
        body: JSON.stringify({ stir: stirVal }),
        method: "POST",
      })
    
  });