var submit = document.getElementById("addbutton");

submit.onclick = function(e){
  // prevent form from sending when clicking on submit button
  e.preventDefault();

  var newtodo = document.getElementById("entryfield");
  var value = newtodo.value; 
  encoded_value = value.replace(" ", "+");
  encoded_value = encodeURIComponent(encoded_value);
  var name = encodeURIComponent("content");
  var pair = name + "=" + encoded_value;
  console.log(pair);
  
  var csrf_token= document.getElementById("csrf-token").content;
  console.log(csrf_token);

  // Send data with Ajax in order to create an new todo task
  var request = new XMLHttpRequest();
  var url = "/addtodo";
  request.open("POST", url);
  request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  request.setRequestHeader("X-CSRFToken", csrf_token);

  request.onreadystatechange = function(){
    if (request.readyState == 4 && request.status === 200){
      console.log(request.responseText);
      // add a new task in the list
      var li = document.createElement("li");
      var p = document.createElement("p");
      li.appendChild(p);
      li.className = "todo";
      p.textContent = value;
      p.className = "todotext";
      var todolist = document.getElementById("ul-todos");
      todolist.appendChild(li);
      // clean the input field
      newtodo.value = '';
    }
      
  }
  request.send(pair);
};
