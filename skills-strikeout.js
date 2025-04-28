if (document.readyState == 'loading') {
  document.addEventListener('DOMContentLoaded',execute);
  // var skillsHtml = document.getElementById('skillsList');
  // skillsHtml.innerHTML = localStorage.getItem('store1');
}else{
  execute();
}

let isStrike = [false, false, false, false, false, false, false, false, false, false];

function execute() {
  var skillsText = document.getElementsByClassName('skills');
  for(let i = 0; i < skillsText.length; i++){
    let p = skillsText[i].querySelector('p');
    skillsText[i].addEventListener('click',function(){
      // Strike text
      if (isStrike[i] == false) {
        let strikeOut = document.createElement('s');
        strikeOut.innerHTML = skillsText[i].innerHTML;
        p.replaceWith(strikeOut);
      // Save isStrike
        isStrike[i] = true;
        sessionStorage.setItem('store2', isStrike)
      // Save HTML
        // skillsHtml = document.getElementById("skillsList").innerHTML;
        // localStorage.setItem('store1', skillsHtml);
      }
    });
  }
}
